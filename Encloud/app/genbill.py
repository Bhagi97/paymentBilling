from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import textwrap
import datetime

from blocks.helper import findrate
import pdb



def numToWords(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen', \
             'Seventeen','Eighteen','Nineteen']
    tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy', \
            'Eighty','Ninety']
    thousands = ['','Thousand','Million','Billion','Trillion','Quadrillion', \
                 'Quintillion','Sextillion','Septillion','Octillion', \
                 'Nonillion','Decillion','Undecillion','Duodecillion', \
                 'Tredecillion','Quattuordecillion','Sexdecillion', \
                 'Septendecillion','Octodecillion','Novemdecillion', \
                 'Vigintillion']
    words = []
    if num==0: words.append('Zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)/3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('Hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words


def generatepdf(meta, pro):
    if meta['company_flag']:
        img = Image.open("/var/www/html/static/bill/templates/billpc.jpg")
    else:
        img = Image.open("/var/www/html/static/bill/templates/billp.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 16)
    headerfont = ImageFont.truetype("FreeSans.ttf", 19)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 21)

    #BILL VARIABLES
    total_amt = 0
    total_amt_tax = 0
    total_cgst = 0
    total_sgst = 0


    #HEADER
    margin = 75
    offset = 100
    draw.text((margin, offset), "Club Ayurveda Pvt Ltd", font=headerfont, fill="#000000")
    offset+=30
    draw.text((margin, offset), meta['franchise'].franchise_name, font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].address, font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].district+', '+meta['franchise'].state, font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].country, font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), "Drug License No: "+meta['franchise'].druglicenseno, font=headerfont, fill="#000000")


    #BILL DETAILS
    margin=200
    offset=352
    draw.text((margin, offset), str(meta['bill_id']),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), datetime.datetime.today().strftime("%d %B, %Y"),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), meta.get('doctor',''),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), meta['franchise'].state,font=font, fill="#000000")
    margin+=410
    draw.text((margin, offset), "2  4",font=font, fill="#000000")

    #CUSTOMER DETAILS
    margin=860
    offset=352
    # pdb.set_trace()
    if meta['customer']==None:
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 24
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 24
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 24
        if meta['company_flag']:
            draw.text((margin, offset), meta['company_name'], font=font, fill="#000000")
            offset += 25
    else:
        draw.text((margin, offset), meta['customer'].name, font=font, fill="#000000")
        offset+=24
        draw.text((margin, offset), meta['customer'].customer_code, font=font, fill="#000000")
        offset+=24
        if meta['company_flag']:
            draw.text((margin, offset), meta['customer'].address, font=font, fill="#000000")
            offset += 25
            draw.text((margin, offset), meta['company_name'], font=font, fill="#000000")
            offset += 25
        else:
            for line in textwrap.wrap(meta['customer'].address, width=40):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 25

        offset += 24

    #PRODUCTS
    margin = 50
    offset = 575
    for i in range(0,len(pro)):
        margin = 50
        draw.text((margin, offset), str(i+1),font=font, fill="#000000")
        margin+=75
        draw.text((margin, offset), pro[i]['product'].item_name,font=font, fill="#000000")
        margin+=350
        draw.text((margin, offset), pro[i]['stock'].hsn_code,font=font, fill="#000000")
        margin+=175
        try:
            draw.text((margin, offset), pro[i]['stock'].batch_no,font=font, fill="#000000")
        except:
            draw.text((margin, offset), "|   N/A   |",font=font, fill="#000000")
        margin+=150
        try:
            draw.text((margin, offset), datetime.datetime.strftime(pro[i]['stock'].expiry_date,"%d/%m/%Y"),font=font, fill="#000000")
        except:
            draw.text((margin, offset), "|   N/A   |",font=font, fill="#000000")
        margin+=125
        draw.text((margin, offset), str(pro[i]['quantity']),font=font, fill="#000000")
        margin+=60
        draw.text((margin, offset), str(pro[i]['product'].MRP),font=font, fill="#000000")
        margin+=70
        total=pro[i]['product'].MRP*int(pro[i]['quantity'])
        total_amt += total
        tax = int(pro[i]['quantity'])*(pro[i]['stock'].MRP - pro[i]['product'].MRP)
        total_cgst += tax*(pro[i]['stock'].tax_CGST/(pro[i]['stock'].tax_CGST+pro[i]['stock'].tax_SGST))
        total_sgst += tax*(pro[i]['stock'].tax_SGST/(pro[i]['stock'].tax_CGST+pro[i]['stock'].tax_SGST))
        total_amt_tax += tax
        rate_string = str(total)
        if len(pro[i]['discount'])>0:
            if pro[i]['discount'][0].discount_type=='%':
                total_amt-=(pro[i]['discount'][0].value/100)*(total)
                total-=(pro[i]['discount'][0].value/100)*(total)
                perc = pro[i]['discount'][0].value
            else:
                total_amt-=pro[i]['discount'][0].value
                total-=pro[i]['discount'][0].value
                perc = int(round((pro[i]['discount'][0].value/(pro[i]['product'].MRP)*100)))
            total = round(total)
            total_amt = round(total)
            rate_string = str(total)
            rate_string_d = ' (' + str(perc) + '% off)'

        draw.text((margin, offset), str(tax) ,font=font, fill="#000000")
        margin+=80
        draw.text((margin, offset), rate_string , font=font, fill="#000000")
        if len(pro[i]['discount']) > 0:
            margin-=17
            offset+=20
            draw.text((margin, offset), rate_string_d, font=font, fill="#000000")
        offset += 40

    # BILL SUMMARY
    offset = 1495
    margin -= 30
    draw.text((margin, offset), str(total_amt + total_amt_tax), font=boldfont, fill="#000000")

    margin += 30
    offset += 62
    total_amt_tax = int(round(total_amt_tax))
    total_amt = int(round(total_amt))
    draw.text((margin, offset), str(total_amt),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_cgst),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_sgst),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "-",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_cgst+total_sgst),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_amt+total_amt_tax),font=font, fill="#000000")

    # BILL SUMMARY IN WORDS
    offset = 1600
    margin=185
    draw.text((margin, offset), "Rs. "+numToWords(total_amt+total_amt_tax),font=font, fill="#000000")


    img.save('/var/www/html/media/bill/' + meta['filename'] + '.jpg')
    img.save('/var/www/html/media/bill/' + meta['filename'] + '.pdf', "PDF", resolution=100.0)
    return total_amt + total_amt_tax


def ibillpdf(meta, pro):
    if meta['company_flag']:
        img = Image.open("/var/www/html/static/bill/templates/invoicec.jpg") if meta['discount_type'] == '' else Image.open("/var/www/html/static/bill/templates/invoicecd.jpg")
    else:
        img = Image.open("/var/www/html/static/bill/templates/invoice.jpg") if meta['discount_type'] == '' else Image.open("/var/www/html/static/bill/templates/invoiced.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 16)
    headerfont = ImageFont.truetype("FreeSans.ttf", 20)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 21)

    #BILL VARIABLES
    total_amt = 0
    total_amt_tax = 0
    total_cgst = 0
    total_sgst = 0

    # HEADER
    margin = 75
    offset = 100
    draw.text((margin, offset), "Club Ayurveda Pvt Ltd", font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].franchise_name, font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].address, font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].district + ', ' + meta['franchise'].state, font=headerfont,
              fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].country, font=headerfont, fill="#000000")

    #BILL DETAILS
    margin=200
    offset=350
    draw.text((margin, offset), str(meta['bill_id']),font=font, fill="#000000")
    offset+=25
    draw.text((margin, offset), datetime.datetime.today().strftime("%d %B, %Y"),font=font, fill="#000000")
    offset+=25
    draw.text((margin, offset), meta.get('doctor',''),font=font, fill="#000000")
    offset+=25
    draw.text((margin, offset), "Kerala",font=font, fill="#000000")
    margin+=420
    draw.text((margin, offset), "2  4",font=font, fill="#000000")

    #CUSTOMER DETAILS
    margin=870
    offset=350
    if meta['customer'] == None:
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 25
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 25
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 25
    else:
        draw.text((margin, offset), meta['customer'].name, font=font, fill="#000000")
        offset+=25
        draw.text((margin, offset), meta['customer'].customer_code, font=font, fill="#000000")
        offset+=25
        if meta['company_flag']:
            draw.text((margin, offset), meta['customer'].address, font=font, fill="#000000")
            offset += 25
            draw.text((margin, offset), meta['customer'].company_name, font=font, fill="#000000")
            offset += 25
        else:
            for line in textwrap.wrap(meta['customer'].address, width=40):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 25


    #PRODUCTS
    offset = 580

    for i in range(0,len(pro)):
        margin = 75
        draw.text((margin, offset), str(i+1),font=font, fill="#000000")
        margin+=80
        offset_counter = 0
        try:
            for line in textwrap.wrap(pro[i]['product'].name, width=35):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset_counter += 1
                offset += 25
        except:
            for line in textwrap.wrap(pro[i]['product'].item_name, width=35):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset_counter += 1
                offset += 25
        offset -= offset_counter*25
        margin+=300
        # try:
        #     for line in textwrap.wrap(pro[i]['product'].description, width=40):
        #         draw.text((margin, offset), line, font=font, fill="#000000")
        #         offset += 25
        #
        # except:
        draw.text((margin, offset), "    -   ",font=font, fill="#000000")
        margin+=220
        draw.text((margin, offset), str("1"),font=font, fill="#000000")


        if pro[i]['rate']<0:
            pro[i]['rate'] = total = float(findrate(pro[i]['product'].rates,meta['franchise'].id))
        else:
            pro[i]['rate'] = total = float(pro[i]['rate'])
        total_cgst += total*pro[i]['product'].tax_CGST/100
        total_sgst += total*pro[i]['product'].tax_SGST/100
        total_tax = total*(pro[i]['product'].tax_CGST+pro[i]['product'].tax_SGST)/100
        total_amt += total
        total_amt_tax += total_tax
        pro[i]['rate'] = total+total_tax

        rate_string = str(pro[i]['rate'])
        rate_string_d = "  -  "
        if len(pro[i]['discount']) > 0:
            if pro[i]['discount'][0].discount_type == '%':
                total_amt -= (pro[i]['discount'][0].value / 100) * (total)
                total -= (pro[i]['discount'][0].value / 100) * (total)
                perc = pro[i]['discount'][0].value
            else:
                total_amt -= pro[i]['discount'][0].value
                total -= pro[i]['discount'][0].value
                perc = int(round((pro[i]['discount'][0].value / (total) * 100)))
            total=round(total)
            total_amt=round(total_amt)
            rate_string = str(total + total_tax)
            rate_string_d = str(perc) + '% off'

        margin += 110
        draw.text((margin, offset), str(total_tax), font=font,fill="#000000")
        margin+=80
        draw.text((margin, offset), str(pro[i]['rate']), font=font, fill="#000000")
        margin += 120
        draw.text((margin, offset), rate_string_d, font=font, fill="#000000")
        margin += 110
        draw.text((margin, offset), rate_string, font=font, fill="#000000")
        offset += offset_counter*25
        offset += 40

    # BILL SUMMARY
    # -- CHECK DISCOUNT
    total_discount = 0
    if meta['discount_type'] != '':
        total_discount = int(round((total_amt + total_amt_tax)*(meta['discount_value']/100))) if meta['discount_type']=='%' else int(round(meta['discount_value']))

    offset = 1093
    margin -= 20
    draw.text((margin, offset), str(total_amt + total_amt_tax - total_discount), font=boldfont, fill="#000000")

    margin += 20
    offset = 1155
    total_amt_tax = int(round(total_amt_tax))
    total_amt = int(round(total_amt))
    draw.text((margin, offset), str(total_amt),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_cgst),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_sgst),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "-",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_cgst+total_sgst),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), str(total_amt+total_amt_tax),font=font, fill="#000000")
    if total_discount!= 0:
        offset += 20
        draw.text((margin, offset), str(total_discount), font=font, fill="#000000")
        offset += 20
        draw.text((margin, offset), str(total_amt + total_amt_tax - total_discount), font=font, fill="#000000")

    # BILL SUMMARY IN WORDS
    offset = 1200
    margin=170
    draw.text((margin, offset), "Rs. "+numToWords(total_amt+total_amt_tax-total_discount),font=font, fill="#000000")

    #BANK DETAILS
    margin=280
    offset = 1300
    if meta['franchise'].bankaccountno:
        draw.text((margin, offset), meta['franchise'].bankaccountno,font=font, fill="#000000")
    offset+=30
    if meta['franchise'].ifsccode:
        draw.text((margin, offset), meta['franchise'].ifsccode,font=font, fill="#000000")

    img.save('/var/www/html/media/bill/'+meta['filename']+'.jpg')
    img.save('/var/www/html/media/bill/'+meta['filename']+'.pdf', "PDF", resolution=100.0)
    return total_amt + total_amt_tax - total_discount


def managestock(pro):
    success, flag = 1, 1
    status = []
    for i in range(0, len(pro)):
        if pro[i]['stock']=='N.A.':
            status.append('N.A.')
        elif pro[i]['stock']=="":
            status.append('No stock entry')
            success, flag = 0,0
        else:
            pro[i]['stock'].stock_quantity = pro[i]['stock'].stock_quantity - int(pro[i]['quantity'])
            if pro[i]['stock'].stock_quantity<0:
                status.append('Insufficient stock')
                success, flag = 0, 0
            else:
                status.append('Positive')
    if success:
        for i in range(0, len(pro)):
            if status[i]=='Positive':
                pro[i]['stock'].save()
    return success, status


def implementationreport(meta):
    img = Image.open("/var/www/html/static/bill/templates/implementation.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 25)

    # LEFT DETAILS
    margin = 300
    offset = 444
    draw.text((margin, offset), meta['franchise'].franchise_name, font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), str(meta['franchise'].id), font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].admin.name, font=font, fill="#000000")

    # RIGHT DETAILS
    margin = 980
    offset = 444
    draw.text((margin, offset), datetime.datetime.today().strftime("%d/%m/%Y"), font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['row'].vendor.name, font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['row'].vendor.user.username, font=font, fill="#000000")

    # CENTRAL DETAILS
    mymap = {True:'Complete', False:'Pending'}
    margin = 650
    offset = 752
    draw.text((margin, offset), meta['row'].date_mou.strftime("%d/%m/%Y"), font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), mymap[meta['row'].painting], font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), mymap[meta['row'].electrification], font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), mymap[meta['row'].signboard], font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), mymap[meta['row'].installation_of_required_equipment], font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset),  meta['row'].inaugration_date.strftime("%d/%m/%Y"), font=font, fill="#000000")
    offset += 60

    # Additional comments
    margin = 125
    offset = 1400
    for line in textwrap.wrap(meta['row'].comments, width=80):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset += 30

    img.save('/var/www/html/media/bill/'+meta['filename']+'.pdf', "PDF", resolution=100.0)


def inspectionreport(meta):
    img = Image.open("/var/www/html/static/bill/templates/inspection.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 25)

    # LEFT DETAILS
    margin=300
    offset=425
    draw.text((margin, offset), meta['franchise'].franchise_name, font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), str(meta['franchise'].id), font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['franchise'].owner, font=font, fill="#000000")

    # RIGHT DETAILS
    margin = 980
    offset = 425
    draw.text((margin, offset), datetime.datetime.today().strftime("%d/%m/%Y"), font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['row'].vendor.name, font=font, fill="#000000")
    offset += 30
    draw.text((margin, offset), meta['row'].vendor.user.username, font=font, fill="#000000")

    # CENTRAL DETAILS
    margin = 950
    offset = 733
    draw.text((margin, offset), meta['row'].v1, font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), meta['row'].v2, font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), meta['row'].v3, font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), meta['row'].v4, font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), meta['row'].v5, font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), meta['row'].v6, font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), meta['row'].v7, font=font, fill="#000000")
    offset += 60
    draw.text((margin, offset), meta['row'].staff_behaviour, font=font, fill="#000000")
    offset += 60

    # Additional comments
    margin = 125
    offset = 1400
    for line in textwrap.wrap(meta['row'].comments, width=80):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset += 30

    img.save('/var/www/html/media/bill/'+meta['filename']+'.pdf', "PDF", resolution=100.0)


def hogeneratepdf(meta, pro):
    img = Image.open("/var/www/html/static/bill/templates/billho.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 16)
    headerfont = ImageFont.truetype("FreeSans.ttf", 20)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 21)

    #BILL VARIABLES
    total_amt = 0
    total_amt_tax = 0
    total_cgst = 0
    total_sgst = 0


    #HEADER
    margin = 75
    offset = 100
    draw.text((margin, offset), "Club Ayurveda Pvt Ltd", font=headerfont, fill="#000000")
    offset+=30
    draw.text((margin, offset), "Customer Care No: +91 8710 009 955", font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), "Call: +91 483 2979955, +91 8710 009 944", font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), "E Mail: care@clubayurveda.com", font=headerfont, fill="#000000")
    offset += 30
    draw.text((margin, offset), "Web: clubayurveda.com", font=headerfont, fill="#000000")


    #BILL DETAILS
    margin=200
    offset=352
    draw.text((margin, offset), str(meta['bill_id']),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), datetime.datetime.today().strftime("%d %B, %Y"),font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "-",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "-",font=font, fill="#000000")
    margin+=410
    draw.text((margin, offset), " ",font=font, fill="#000000")

    #CUSTOMER DETAILS
    margin=860
    offset=352
    f = meta.get('franchise',None)
    if f != None:
        draw.text((margin, offset), meta['franchise'].franchise_name, font=font, fill="#000000")
        offset += 24
        draw.text((margin, offset), str(meta['franchise'].id)+' (Franchise Code)', font=font, fill="#000000")
        offset += 24
        draw.text((margin, offset), '-', font=font, fill="#000000")
        offset += 24
    else:
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 24
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 24
        draw.text((margin, offset), " - ", font=font, fill="#000000")
        offset += 24


    #PRODUCTS
    margin = 50
    offset = 575
    for i in range(0,len(pro)):
        margin = 50
        draw.text((margin, offset), str(i+1),font=font, fill="#000000")
        margin+=75
        draw.text((margin, offset), pro[i]['product'].item_name,font=font, fill="#000000")
        margin+=350
        draw.text((margin, offset), "    -    ",font=font, fill="#000000")
        margin+=175
        draw.text((margin, offset), "|   N/A   |",font=font, fill="#000000")
        margin+=150
        draw.text((margin, offset), "|   N/A   |",font=font, fill="#000000")
        margin+=125
        draw.text((margin, offset), str(pro[i]['quantity']),font=font, fill="#000000")
        margin+=60
        draw.text((margin, offset), str(pro[i]['product'].MRP),font=font, fill="#000000")
        margin+=70
        total=pro[i]['product'].MRP*int(pro[i]['quantity'])
        total_amt += total
        total_cgst += total*pro[i]['product'].tax_CGST/100
        total_sgst += total*pro[i]['product'].tax_SGST/100
        total_tax=total*(pro[i]['product'].tax_CGST+pro[i]['product'].tax_SGST)/100
        total_amt_tax += total_tax
        rate_string = str(total+total_sgst+total_cgst)

        draw.text((margin, offset), str(total_cgst+total_sgst) ,font=font, fill="#000000")
        margin+=80
        draw.text((margin, offset), rate_string , font=font, fill="#000000")
        offset += 40

    # BILL SUMMARY
    offset = 1495
    margin -= 30
    draw.text((margin, offset), str(total_amt + total_amt_tax), font=boldfont, fill="#000000")

    margin += 30
    offset += 62
    total_amt_tax = int(round(total_amt_tax))
    total_amt = int(round(total_amt))
    draw.text((margin, offset), str(total_amt), font=font, fill="#000000")
    offset += 24
    draw.text((margin, offset), str(total_cgst), font=font, fill="#000000")
    offset += 24
    draw.text((margin, offset), str(total_sgst), font=font, fill="#000000")
    offset += 24
    draw.text((margin, offset), "-", font=font, fill="#000000")
    offset += 24
    draw.text((margin, offset), str(total_cgst + total_sgst), font=font, fill="#000000")
    offset += 24
    draw.text((margin, offset), str(total_amt + total_amt_tax), font=font, fill="#000000")

    # BILL SUMMARY IN WORDS
    offset = 1600
    margin = 185
    draw.text((margin, offset), "Rs. " + numToWords(total_amt + total_amt_tax), font=font, fill="#000000")

    draw.text((margin, offset), "    -    ",font=font, fill="#000000")
    img.save('/var/www/html/media/bill/' + meta['filename'] + '.jpg')
    img.save('/var/www/html/media/bill/' + meta['filename'] + '.pdf', "PDF", resolution=100.0)
    return total_amt + total_amt_tax


def homanagestock(meta, pro):
    flag = 1
    status = []
    for i in range(0, len(pro)):
        pro[i]['product'].stock = pro[i]['product'].stock - int(pro[i]['quantity'])
        if pro[i]['product'].stock<0:
            status.append('Insufficient stock')
            flag=0
        else:
            status.append('Positive')
        if flag==1:
            pro[i]['product'].save()
    return flag, status


def generatereceipt(meta, filename):
    img = Image.open("/var/www/html/static/bill/templates/receipt-a5.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 50)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 50)

    margin = (img.size[0] - draw.textsize(meta.franchise.address,font)[0])/2
    offset = 280
    draw.text((margin, offset), meta.franchise.address, font=font, fill="#000000")
    margin = 200
    offset = 600
    draw.text((margin, offset), "Receipt No: "+str(meta.receipt_id), font=font, fill="#000000")
    margin+=1700
    draw.text((margin, offset), "Date: "+datetime.datetime.today().strftime("%d/%m/%Y"), font=font, fill="#000000")

    offset+=200
    margin=200
    if meta.amount>=0:
        s = "        Received `INR "+ str(meta.amount) +"` (in words: "+ numToWords(meta.amount) +") from "+ meta.customer.name + " (" + meta.customer.customer_code + ") towards " + meta.franchise.franchise_name +", " + meta.franchise.district
    else:
        s = "        Balance refunded to " + meta.customer.name + " (" + meta.customer.customer_code + ") of `INR " + str(-meta.amount) + "` (in words: " + numToWords(-meta.amount) + ") by " + meta.franchise.franchise_name + ", " + meta.franchise.district
    flag=0
    for line in textwrap.wrap(s, width=90):
        margin = 200
        if '`' not in line:
            draw.text((margin, offset), line, font=font, fill="#000000")
        else:
            lines = line.split('`')
            for i in range(0,len(lines)):
                if(i%2==flag):
                    draw.text((margin, offset), lines[i], font=font, fill="#000000")
                    margin+=draw.textsize(lines[i],font)[0]+10
                else:
                    draw.text((margin, offset), lines[i], font=boldfont, fill="#000000")
                    margin+=draw.textsize(lines[i],boldfont)[0]+10
            flag=i%2
        offset += 90

    margin = 1000
    offset+=110
    draw.text((margin, offset), "Payment Summary", font=boldfont, fill="#000000")
    margin = 200
    offset+=150
    draw.text((margin, offset), "Remarks: "+meta.method, font=font, fill="#000000")
    rightmargin = 2050 - draw.textsize("Approved by: "+ meta.cashier.name ,font)[0]
    draw.text((margin+rightmargin, offset), "Approved by: "+ meta.cashier.name, font=font, fill="#000000")
    offset+=100
    offset_mark = offset
    details = meta.details.replace("|","\n")
    for line in details.split("\n"):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset+=80
    draw.text((margin+rightmargin, offset_mark), "Signature:", font=font, fill="#000000")
    offset+=100
    img.save('/var/www/html/media/bill/' + filename + '.jpg')

