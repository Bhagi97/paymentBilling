from app.models import SalesReportBase, SalesReport
from datetime import datetime
from blocks.helper import findrate

def manage(meta, pro):
    my_dict = {}
    if meta['customer']=='':
        meta['customer'] = None
    my_dict['customer'] = meta['customer']
    my_dict['date'] = datetime.now()
    my_dict['franchise_code'] = meta['franchise'].id
    my_dict['bill_type'] = 'Pharmacy'
    my_dict['bill_id'] = meta['bill_id']
    sales_report_base= SalesReportBase(**my_dict)
    sales_report_base.save()
    total = 0
    for product in pro:
        my_dict = {'sales_base':sales_report_base}
        try:
            my_dict['item_name'] = product['product'].item_name
            my_dict['sale_rate'] = float(product['product'].MRP)
        except:
            my_dict['item_name'] = product['product'].name
            my_dict['sale_rate'] = float(findrate(product['product'].rates,meta['franchise'].id))
            sales_report_base.bill_type = 'Invoice'
        total += my_dict['sale_rate']
        if len(product['discount'])>0:
            if product['discount'][0].discount_type=='%':
                my_dict['sale_rate']-=(product['discount'][0].value/100)*(my_dict['sale_rate'])
            else:
                my_dict['sale_rate']-=product['discount'][0].value
            my_dict['sale_rate'] = round(my_dict['sale_rate'])
        my_dict['quantity'] = product['quantity']
        sales_report = SalesReport(**my_dict)
        sales_report.save()

    if meta['discount_type']!='':
        sale_rate = round(total*(meta['discount_value']/100)) if meta['discount_type']=='%' else int(round(meta['discount_value']))
        my_dict = {'sales_base': sales_report_base}
        my_dict['item_name'] = 'Discount'
        my_dict['sale_rate'] = -(sale_rate)
        my_dict['quantity'] = 1
        sales_report = SalesReport(**my_dict)
        sales_report.save()

    return sales_report_base.id


def homanage(meta, pro):
    my_dict = {}
    my_dict['customer'] = None
    my_dict['date'] = datetime.now()
    my_dict['franchise_code'] = 0
    my_dict['bill_type'] = 'Pharmacy'
    sales_report_base= SalesReportBase(**my_dict)
    sales_report_base.save()
    for product in pro:
        my_dict = {'sales_base':sales_report_base}
        my_dict['item_name'] = product['product'].item_name
        my_dict['sale_rate'] = float(product['product'].MRP)
        my_dict['quantity'] = int(product['quantity'])
        sales_report = SalesReport(**my_dict)
        sales_report.save()
        sales_report_base.save()
    return sales_report_base.id