from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import datetime
import pdb


def draw_underlined_text(draw, pos, text, font, **options):
    twidth, theight = draw.textsize(text, font=font)
    lx, ly = pos[0], pos[1] + theight
    draw.text(pos, text, font=font, **options)
    draw.line((lx, ly, lx + twidth, ly), **options)
    draw.line((lx, ly+1, lx + twidth, ly+1), **options)


def generatepdf(pro,meta):
    img = Image.open("/var/www/html/static/bill/templates/Prescription.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 41)
    headerfont = ImageFont.truetype("FreeSans.ttf", 52)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 41)

    # HEADER
    margin = 180
    offset = 160
    draw.text((margin, offset), "Club Ayurveda Pvt Ltd", font=headerfont, fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].franchise_name, font=headerfont, fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].address, font=headerfont, fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].district + ', ' + meta['franchise'].state, font=headerfont,
              fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].country, font=headerfont, fill="#000000")

    # Bill DETAILS
    margin = 580
    offset = 670
    draw.text((margin, offset), meta['customer'].name, font=font, fill="#000000")
    offset += 56
    counter = 0
    for line in textwrap.wrap(meta['customer'].address, width=40):
        if counter==2:
            break
        draw.text((margin, offset), line, font=font, fill="#000000")
        counter+=1
        offset += 56
    if counter==1:
        offset+=56
    draw.text((margin, offset), meta['prescription']['doctor'], font=font, fill="#000000")
    offset += 56
    # --#
    margin += 1320
    offset = 670
    draw.text((margin, offset), meta['customer'].customer_code, font=font, fill="#000000")
    offset += 56
    draw.text((margin, offset), meta.get('date',datetime.datetime.today().strftime("%d %B, %Y")), font=font, fill="#000000")
    offset += 56
    draw.text((margin, offset), str(meta['prescription']['prescription_id']), font=font, fill="#000000")
    offset += 56
    # END OF HEADER

    margin = 200
    offset = 1000
    draw_underlined_text(draw, (margin, offset), "Diagnosis", boldfont, fill=0)
    offset += 80
    for line in textwrap.wrap(meta['prescription']['diagnosis'], width=120):
        draw.text((margin, offset), line, font=font, fill="#000000")
        offset += 56
    offset += 70

    if meta['prescription'].get('procedure','')!='':
        draw_underlined_text(draw, (margin, offset), "Clinical examination", boldfont, fill=0)
        offset += 80
        for line in textwrap.wrap(meta['prescription']['procedure'], width=120):
            draw.text((margin, offset), line, font=font, fill="#000000")
            offset += 56
        offset += 70

    if meta['prescription'].get('treatmentsuggested','') != '':
        draw_underlined_text(draw, (margin, offset), "Treatments Suggested", boldfont, fill=0)
        offset += 80
        for line in textwrap.wrap(meta['prescription'].get('treatmentsuggested',''), width=120):
            draw.text((margin, offset), line, font=font, fill="#000000")
            offset += 56
        offset += 70

    draw_underlined_text(draw, (margin, offset), "Medicine/Treatment Prescribed", boldfont, fill=0)
    offset += 120

    # MEDICINES

    margin = 200
    draw.text((margin, offset), "Sl No", font=font, fill="#000000")
    margin += 150
    draw.text((margin, offset), "Medicine/Treatment Name", font=font, fill="#000000")
    margin += 1000
    draw.text((margin, offset), "Quantity", font=font, fill="#000000")
    margin += 400
    draw.text((margin, offset), "Dosage/Suggestions", font=font, fill="#000000")
    offset += 126

    for i in range(0, len(pro)):
        margin = 200
        draw.text((margin, offset), str(i + 1), font=font, fill="#000000")
        margin += 150
        reset_offset, reset_offset_2 = 0,0
        try:
            for line in textwrap.wrap(pro[i]['product'].item_name, width=25):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 56
                reset_offset += 56
            offset -= reset_offset
        except AttributeError:
            reset_offset = 0
            for line in textwrap.wrap(pro[i]['product'].name, width=25):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 56
                reset_offset += 56
            offset -= reset_offset
        margin += 1000
        draw.text((margin, offset), str(pro[i]['quantity']), font=font, fill="#000000")
        margin += 400
        if pro[i]['dosage'] != '':
            for line in textwrap.wrap(pro[i]['dosage'], width=30):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 56
                reset_offset_2 += 56
            offset -= reset_offset_2
        offset += reset_offset if reset_offset > reset_offset_2 else reset_offset_2
        offset += 70
    offset+=50
    margin=200
    # END OF MEDICINES

    if meta['prescription'].get('advice','') != '':
        draw_underlined_text(draw, (margin, offset), "Advice on Discharge", boldfont, fill=0)
        offset += 80
        for line in textwrap.wrap(meta['prescription'].get('advice',''), width=120):
            draw.text((margin, offset), line, font=font, fill="#000000")
            offset += 56
        offset += 70

    if meta['prescription'].get('medications', '') != '':
        draw_underlined_text(draw, (margin, offset), "Medications", boldfont, fill=0)
        offset += 80
        for line in textwrap.wrap(meta['prescription']['medications'], width=120):
            draw.text((margin, offset), line, font=font, fill="#000000")
            offset += 56
        offset += 70

    if meta['prescription'].get('dietadvice', '') != '':
        draw_underlined_text(draw, (margin, offset), "Diet Advice", boldfont, fill=0)
        offset += 80
        for line in textwrap.wrap(meta['prescription']['dietadvice'], width=120):
            draw.text((margin, offset), line, font=font, fill="#000000")
            offset += 56
        offset += 70

    if meta['prescription'].get('followupdate', '') != '':
        draw_underlined_text(draw, (margin, offset), "Follow up date", boldfont, fill=0)
        offset += 80
        draw.text((margin, offset), meta['prescription'].get('followupdate', ''), font=font, fill="#000000")
        offset += 125


    img.save('/var/www/html/media/bill/'+meta['filename']+'.jpg')
    img.save('/var/www/html/media/bill/'+meta['filename']+'.pdf', "PDF", resolution=100.0)


def generatecover(meta):
    img = Image.open("/var/www/html/static/bill/templates/cover.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 60)
    headerfont = ImageFont.truetype("FreeSans.ttf", 70)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 60)

    margin, offset = 500, 1600
    draw.text((margin, offset), "Name: "+meta['customer'].name, font=font, fill="#000000")
    offset += 150
    draw.text((margin, offset), "Patient ID: "+meta['customer'].customer_code, font=font, fill="#000000")
    offset += 150
    draw.text((margin, offset), "DOB: "+datetime.datetime.strftime(meta['customer'].dob,"%d/%m/%Y"), font=font, fill="#000000")
    offset += 150
    draw.text((margin, offset), "Gender: "+meta['customer'].gender, font=font, fill="#000000")
    offset += 150
    draw.text((margin, offset), "Date Range: "+meta['range'], font=font, fill="#000000")

    img.save('/var/www/html/media/bill/'+meta['filename']+'.jpg')
    img.save('/var/www/html/media/bill/'+meta['filename']+'.pdf', "PDF", resolution=100.0)


def generateprescription(meta,dl):
    img = Image.open("/var/www/html/static/bill/templates/Prescription.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 41)
    headerfont = ImageFont.truetype("FreeSans.ttf", 52)
    boldfont = ImageFont.truetype("FreeSansBold.ttf", 41)

    # HEADER
    margin = 180
    offset = 160
    draw.text((margin, offset), "Club Ayurveda Pvt Ltd", font=headerfont, fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].franchise_name, font=headerfont, fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].address, font=headerfont, fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].district + ', ' + meta['franchise'].state, font=headerfont,
              fill="#000000")
    offset += 65
    draw.text((margin, offset), meta['franchise'].country, font=headerfont, fill="#000000")

    # Bill DETAILS
    margin = 580
    offset = 670
    draw.text((margin, offset), meta['customer'].name, font=font, fill="#000000")
    offset += 56
    counter = 0
    for line in textwrap.wrap(meta['customer'].address, width=40):
        if counter==2:
            break
        draw.text((margin, offset), line, font=font, fill="#000000")
        counter+=1
        offset += 56
    if counter==1:
        offset+=56
    draw.text((margin, offset), meta['doctor'], font=font, fill="#000000")
    offset += 56
    # --#
    margin += 1320
    offset = 670
    draw.text((margin, offset), meta['customer'].customer_code, font=font, fill="#000000")
    offset += 56
    draw.text((margin, offset), meta.get('date',datetime.datetime.today().strftime("%d %B, %Y")), font=font, fill="#000000")
    offset += 56
    draw.text((margin, offset), str(meta.get('prescription_id','-')), font=font, fill="#000000")
    offset += 56
    # END OF HEADER

    margin = 200
    offset = 1000

    draw_underlined_text(draw, (margin, offset), "Medicine/Treatment Prescribed", boldfont, fill=0)
    offset += 120

    # MEDICINES

    draw.text((margin, offset), "Sl No", font=font, fill="#000000")
    margin += 150
    draw.text((margin, offset), "Medicine/Treatment Name", font=font, fill="#000000")
    margin += 1000
    draw.text((margin, offset), "Quantity", font=font, fill="#000000")
    margin += 400
    draw.text((margin, offset), "Dosage/Suggestions", font=font, fill="#000000")
    offset += 126

    for i,(key,value) in enumerate(meta['prescription'].items()):
        margin = 200
        draw.text((margin, offset), str(i + 1), font=font, fill="#000000")
        margin += 150
        reset_offset, reset_offset_2 = 0, 0
        for line in textwrap.wrap(value[1], width=25):
            draw.text((margin, offset), line, font=font, fill="#000000")
            offset += 56
            reset_offset += 56
        offset -= reset_offset

        margin += 1000
        draw.text((margin, offset), str(value[2]), font=font, fill="#000000")
        margin += 400
        if dl[i] != '':
            for line in textwrap.wrap(dl[i], width=30):
                draw.text((margin, offset), line, font=font, fill="#000000")
                offset += 56
                reset_offset_2 += 56
            offset -= reset_offset_2
        offset += reset_offset if reset_offset > reset_offset_2 else reset_offset_2
        offset += 70

    offset+=50
    margin=200
    # END OF MEDICINES

    if meta.get('followupdate','')!='':
        offset += 70
        draw_underlined_text(draw, (margin, offset), "Follow up date", boldfont, fill=0)
        offset += 80
        draw.text((margin, offset), meta.get('followupdate',''), font=font, fill="#000000")
        offset += 125


    img.save('/var/www/html/media/bill/'+meta['filename']+'.jpg')
    img.save('/var/www/html/media/bill/'+meta['filename']+'.pdf', "PDF", resolution=100.0)
