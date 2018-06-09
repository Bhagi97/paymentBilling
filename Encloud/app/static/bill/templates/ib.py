from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import textwrap
import datetime
import pdb

class wrapper:
    def __init__(self,item_name,MRP,tax_CGST,tax_SGST):
        self.MRP=MRP
        self.tax_CGST=tax_CGST
        self.tax_SGST=tax_SGST
        self.item_name=item_name


def draw_underlined_text(draw, pos, text, font, **options):    
    twidth, theight = draw.textsize(text, font=font)
    lx, ly = pos[0], pos[1] + theight
    draw.text(pos, text, font=font, **options)
    draw.line((lx, ly, lx + twidth, ly), **options)
    draw.line((lx, ly+1, lx + twidth, ly+1), **options)


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


def generatepdf():
    img = Image.open("InvoiceBill.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 18)
    
    #BILL VARIABLES
    total_amt = 0
    total_amt_tax = 0
    total_cgst = 0
    total_sgst = 0


    #BILL DETAILS
    margin=200
    offset=350
    draw.text((margin, offset), "1",font=font, fill="#000000")
    offset+=25
    draw.text((margin, offset), "2/2/2019",font=font, fill="#000000")
    offset+=25
    draw.text((margin, offset), "-",font=font, fill="#000000")
    offset+=25
    draw.text((margin, offset), "Kerala",font=font, fill="#000000")
    margin+=420
    draw.text((margin, offset), "2  4",font=font, fill="#000000")

    #CUSTOMER DETAILS
    margin=870
    offset=350
    draw.text((margin, offset), " - ", font=font, fill="#000000")
    offset += 25
    draw.text((margin, offset), " - ", font=font, fill="#000000")
    offset += 25
    draw.text((margin, offset), " - ", font=font, fill="#000000")
    offset += 25
    
    #PRODUCTS
    margin = 75
    offset = 580

    margin=75
    draw.text((margin, offset), str(1),font=font, fill="#000000")
    margin+=80
    draw.text((margin, offset), "Package 1", font=font, fill="#000000")
    margin+=300
    draw.text((margin, offset), "My description", font=font, fill="#000000")
    margin+=220
    draw.text((margin, offset), str(235),font=font, fill="#000000")
    margin+=110    
    '''
    total=pro[i]['product'].MRP*int(pro[i]['quantity'])
    total_amt += total
    total_cgst += total*pro[i]['product'].tax_CGST/100
    total_sgst += total*pro[i]['product'].tax_SGST/100
    total_tax=total*(pro[i]['product'].tax_CGST+pro[i]['product'].tax_SGST)/100
    total_amt_tax += total_tax
    '''
    draw.text((margin, offset), str(18) ,font=font, fill="#000000")
    margin+=80
    draw.text((margin, offset), str(235+0.18*235), font=font, fill="#000000")
    margin+=110
    draw.text((margin, offset), str(0), font=font, fill="#000000")
    margin+=70
    draw.text((margin, offset), str(235+0.18*235), font=font, fill="#000000")
    offset += 80

   
    #BILL SUMMARY
    offset = 1095
    margin = 1100
    draw.text((margin, offset), "1456",font=font, fill="#000000")
    

    offset = 1153
    margin = 1100
    '''
    total_amt_tax = int(round(total_amt_tax))
    total_amt = int(round(total_amt))
    '''
    draw.text((margin, offset), "1234",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "123",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "123",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "-",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "246",font=font, fill="#000000")
    offset+=24
    draw.text((margin, offset), "1456",font=font, fill="#000000")

    # BILL SUMMARY IN WORDS
    offset = 700
    margin=170
    draw.text((margin, offset), "Rs. "+numToWords(1456),font=font, fill="#000000")

    #BANK DETAILS
    margin=280
    offset = 1300
    draw.text((margin, offset), "7A2B 6R45 HJ9L JKIO",font=font, fill="#000000")
    offset+=30
    draw.text((margin, offset), "2A5TY78IO-310",font=font, fill="#000000")

    img.save('qwerty.jpg')


def genpre():
    img = Image.open("Prescription.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 41)
    headerfont = ImageFont.truetype("FreeSans.ttf", 52)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 41)
    # MEDICINES
    margin = 200
    offset = 1000
    diag = "dsdf sdf sd fds f dsf ds fds f ds f  sdf dsf ds  fds f gh ghjgfhjg d h r fb hf hg f dg df g fsd g  adf g a f g f g s fd g f d g f ds g fsdh a  h f h  sf g h fda hg fd h  fg hngf n gfnj gdh gf h gfh fd g  ag fad g fd ghfdg fd g fa dg  af g f  a  ag  f gh fd h   fgh   h  hf a hb af bhfdb fad  h f dh ad h fad h afd  h fda h fd  h afd h fd h  h fd hf bfd b  fd bh g nh gf n gn hg n  nh rf,hmreu bvd ve vklsd vkla v sce..cewpv ewrvmevodsmv dskv edv ed vuds vds"
    report="g  af g f  a  ag  f gh fd h   fgh   h  hf a hb af bhfdb fad  h f dh ad h fad h afd  h fda h fd  h afd h fd h  h fd hf bfd b  fd bh g nh gf n gn hg "
    draw_underlined_text(draw, (margin, offset), "Diagnosis", boldfont, fill=0)
    offset += 80
    for line in textwrap.wrap(diag, width=130):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset += 56
    offset += 70
    draw_underlined_text(draw, (margin, offset), "Report", boldfont, fill=0)
    offset += 80
    for line in textwrap.wrap(report, width=130):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset += 56
    offset += 70
    draw_underlined_text(draw, (margin, offset), "Medication", boldfont, fill=0)
    offset += 80
    for line in textwrap.wrap(diag, width=130):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset += 56
    offset += 70
    draw_underlined_text(draw, (margin, offset), "Diet Advice", boldfont, fill=0)
    offset += 80
    for line in textwrap.wrap(report, width=130):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset += 56
    offset += 70
    draw_underlined_text(draw, (margin, offset), "Follow up date", boldfont, fill=0)
    offset += 80
    draw.text((margin, offset), "2/2/2018", font=font, fill="#000000")
    offset += 125

    
    draw_underlined_text(draw, (margin, offset), "Medicine/Treatment Prescribed", boldfont, fill=0)
    offset += 120

    

    
    margin = 200
    draw.text((margin, offset), "Sl No", font=font, fill="#000000")
    margin += 150
    draw.text((margin, offset), "Medicine/Treatment Name", font=font, fill="#000000")
    margin += 1000
    draw.text((margin, offset), "Quantity", font=font, fill="#000000")
    margin += 400
    draw.text((margin, offset), "Dosage", font=font, fill="#000000")
    offset += 126

    pro = [["Arishtam fds fds f ds fsd f sd fds f dhb fdbh fd gh sfdg agsd gda sg",'1','Twice fd h sfdh fd hsfd hfsd h, fsdh fd,sm h,mfsd h,m dfh,m fsd'],["Chavana",'1','Once']]
    for i in range(0, len(pro)):
        margin = 200
        draw.text((margin, offset), str(i+1), font=font, fill="#000000")
        margin += 150
        try:
            reset_offset=0
            for line in textwrap.wrap(pro[i][0], width=40):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 56
                reset_offset+=56
            offset-=reset_offset
        except AttributeError:
            reset_offset = 0
            for line in textwrap.wrap(pro[i][0], width=40):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 56
                reset_offset+=56
            offset-=reset_offset
        margin += 1000
        draw.text((margin, offset), str(1), font=font, fill="#000000")
        margin += 400
        for line in textwrap.wrap(pro[i][2], width=30):
            draw.text((margin, offset), line, font=font, fill="#000000")
            offset += 56
        offset += 70

    # END OF MEDICINES

    img.save('q.jpg')


def gencover():
    img = Image.open("cover.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 41)
    headerfont = ImageFont.truetype("FreeSans.ttf", 52)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 41)

    margin,offset = 250, 800
    draw.text((margin, offset), "Name: Dennis Peter George", font=font, fill="#000000")
    offset += 80
    draw.text((margin, offset), "Age: 21", font=font, fill="#000000")
    offset += 80
    draw.text((margin, offset), "Patient ID: KLER10", font=font, fill="#000000")
    offset += 80
    draw.text((margin, offset), "Gender: Male", font=font, fill="#000000")
    offset += 80
    draw.text((margin, offset), "Date Range: 02/02/2017-01/03.2018", font=font, fill="#000000")
    
    img.save('q.jpg')

def main():
     gencover()

main()
