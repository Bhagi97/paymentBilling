from __future__ import unicode_literals
from app.Mailing.draft import *
from django.core.mail import send_mail
from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    class Meta:
        permissions = (
            ("itemwise_discount", "Can set discount - Granularity:Item"),
            ("categorywise_discount", "Can set discount - Granularity:Category"),
            ("price_discount", "Can set price wise discount"),
            ("percentage_discount", "Can set percentage wise discount"),
            ("viewdoctor", "Can view doctor details"),
            ("viewpatient", "Can view patient details"),
            ("prescribe", "Can prescribe medicine"),
            ("bill", "Bill"),
            ("receipt", "Receipt"),
            ("receiptreport", "Receipt Report"),
            ("adduser", "Can add user"),
            ("modifyuser", "Can modify user"),
            ("vendor", "Is a vendor"),
            ("ho", "Is a Main Office Member"),
            ("prescriptionreport", "Can see Prescription Report")
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=50)
    regid = models.CharField(max_length=30, default='0')
    organisation = models.CharField(max_length=100)
    franchise_code = models.IntegerField(default=0)
    phoneno = models.CharField(max_length=15)

    def __str__(self):
        return self.name


def unique_rand():
    while True:
        code = User.objects.make_random_password(length=6).upper()
        if not Customer.objects.filter(customer_code=code).exists():
            return code


class Customer(models.Model):
    name=models.CharField(max_length=30)
    phoneno=models.CharField(max_length=15)
    phoneno_sec=models.CharField(max_length=15)
    emailid=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    gstno=models.CharField(max_length=30)
    company_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    dob=models.DateTimeField()
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    customer_code=models.CharField(max_length=10, unique=True)
    franchise_code = models.IntegerField()

    def __str__(self):
        return self.name + '-' + self.customer_code


class Country(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    district_code = models.CharField(max_length=8)
    counter = models.BigIntegerField(default=0)

    @classmethod
    def get_patientID(cls, country, state, district):
        with transaction.atomic():
            meta = (
                cls.objects
                    .select_for_update()
                    .get(country=country, state=state, district=district)
            )
            meta.counter += 1
            meta.save()
        code = state.split('(')[1].split(')')[0]
        code += (meta.district_code+str(meta.counter))
        return code


class Franchise(models.Model):
    franchise_name = models.CharField(max_length=100, unique=True)
    franchise_type = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    bankaccountno = models.CharField(max_length=50)
    bankname = models.CharField(max_length=50)
    ifsccode = models.CharField(max_length=20)
    gstno = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    owner = models.CharField(max_length=60)
    ownercontact = models.CharField(max_length=10)
    druglicenseno =  models.CharField(max_length=20)
    vendor = models.ForeignKey(Profile, related_name='vendormap')
    remarks = models.CharField(max_length=300, null=True)
    permbs1 = models.BooleanField()
    permbs2 = models.BooleanField()
    currency = models.CharField(max_length=10)
    permb3 = models.BooleanField()
    permb4 = models.BooleanField()
    permb5 = models.BooleanField()
    active = models.BooleanField(default=True)
    admin = models.ForeignKey(Profile, related_name='adminmap', null=True)
    sales_today = models.FloatField(default=0)
    customers_today = models.FloatField(default=0)
    new_customers = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        obj = TimestampDB.objects.get(table_name='Franchise')
        obj.timestamp = datetime.now()
        obj.save()
        super(Franchise, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ' - ' + self.franchise_name


class Category(models.Model):
    class Meta:
        unique_together = (('category_name', 'franchise_code'),)
    category_name = models.CharField(max_length=30)
    category_code = models.CharField(max_length=20)
    category_description = models.CharField(max_length=200, null=True)
    franchise_code = models.IntegerField(default=0)


class Product(models.Model):
    class Meta:
        unique_together = (('item_name', 'franchise_code'),)
    item_name = models.CharField(max_length=50)
    MRP = models.FloatField()
    category = models.CharField(max_length=30)
    remarks = models.CharField(max_length=200)
    franchise_code = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name.encode('ascii','ignore') + '-' + str(self.id)


class HOProduct(models.Model):
    item_name = models.CharField(max_length=50)
    MRP = models.FloatField()
    stock = models.IntegerField(default=0)
    tax_CGST = models.FloatField(default=0)
    tax_SGST = models.FloatField(default=0)


class Service(models.Model):
    name = models.CharField(max_length=100)
    service_code = models.CharField(max_length=20, unique=True)
    rates = models.CharField(max_length=30)
    body_part = models.CharField(max_length=30,null=True)
    tax_CGST = models.FloatField(default=0)
    tax_SGST = models.FloatField(default=0)
    remarks = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=500,null=True)
    image = models.ImageField(null=True)
    duration = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        obj = TimestampDB.objects.get(table_name='Service')
        obj.timestamp = datetime.now()
        obj.save()
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.name.encode('ascii','ignore')


class ServiceMask(models.Model):
    mask = mask = models.CharField(max_length=500)
    franchise_code = models.IntegerField()

    def save(self, *args, **kwargs):
        obj = TimestampDB.objects.get(table_name='ServiceMask')
        obj.timestamp = datetime.now()
        obj.save()
        super(ServiceMask, self).save(*args, **kwargs)


class Package(models.Model):
    name = models.CharField(max_length=80, unique=True)
    package_code = models.CharField(max_length=20, unique=True)
    rates = models.CharField(max_length=30)
    body_part = models.CharField(max_length=30,null=True)
    tax_CGST = models.FloatField(default=0)
    tax_SGST = models.FloatField(default=0)
    remarks = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(null=True)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.name.encode('ascii','ignore')

    def save(self, *args, **kwargs):
        obj = TimestampDB.objects.get(table_name='Package')
        obj.timestamp = datetime.now()
        obj.save()
        super(Package, self).save(*args, **kwargs)


class PackageMask(models.Model):
    mask = models.CharField(max_length=500)
    franchise_code = models.IntegerField()

    def save(self, *args, **kwargs):
        obj = TimestampDB.objects.get(table_name='PackageMask')
        obj.timestamp = datetime.now()
        obj.save()
        super(PackageMask, self).save(*args, **kwargs)


class TreatmentMaster(models.Model):
    name = models.CharField(max_length=100,unique=True)
    remarks = models.CharField(max_length=200)
    duration = models.FloatField()

    def __str__(self):
        return self.name


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()
    tax_CGST = models.FloatField(null=True)
    tax_SGST = models.FloatField(null=True)
    franchise_code = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + str(self.franchise_code)


class Discount(models.Model):
    pid = models.ForeignKey(Package,default=None,null=True)
    proid = models.ForeignKey(Product,default=None,null=True)
    sid = models.ForeignKey(Service,default=None,null=True)
    tid = models.ForeignKey(Treatment,default=None,null=True)
    subject = models.CharField(max_length=25)
    discount_type = models.CharField(max_length=10)
    value = models.FloatField()
    franchise_code = models.IntegerField(default=0)
    franchise_name = models.CharField(max_length=40, default='Main Office')

    def save(self, *args, **kwargs):
        obj = TimestampDB.objects.get(table_name='Discount')
        obj.timestamp = datetime.now()
        obj.save()
        super(Discount, self).save(*args, **kwargs)


class Stock(models.Model):
    item_name = models.CharField(max_length=30)
    stock_quantity = models.IntegerField()
    franchise_code = models.IntegerField()
    batch_no = models.CharField(max_length=20)
    vendor = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    gst_no = models.CharField(max_length=30)
    expiry_date = models.DateField()
    hsn_code = models.CharField(max_length=30)
    tax_CGST = models.FloatField(default=0)
    tax_SGST = models.FloatField(default=0)
    purchase_rate = models.FloatField()
    MRP = models.FloatField()
    pid = models.IntegerField()



class StockTransfer(models.Model):
    item_name = models.CharField(max_length=30)
    stock_amount = models.CharField(max_length=20)
    franchise_name = models.CharField(max_length=30)
    discount = models.IntegerField(null=True)
    expiry_date = models.DateField()
    franchise_code = models.IntegerField()


class SavedBill(models.Model):
    customer_code = models.CharField(max_length=10)
    franchise_code = models.IntegerField()
    doctor = models.CharField(max_length=50)
    productlist = models.CharField(max_length=200)
    ratelist = models.CharField(max_length=200)
    durationlist = models.CharField(max_length=200)


class SKUList(models.Model):
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    franchise_code = models.IntegerField(default=0)


class SalesReportBase(models.Model):
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, null=True, blank=True, default=None)
    bill_type = models.CharField(max_length=30)
    bill_id = models.CharField(max_length=20)
    franchise_code = models.IntegerField()

    def __str__(self):
        return str(self.profile.bill_id)


class SalesReport(models.Model):
    sales_base = models.ForeignKey(SalesReportBase)
    item_name = models.CharField(max_length=80)
    quantity = models.IntegerField()
    sale_rate = models.FloatField()


class AuditReport(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=30)
    bill = models.CharField(max_length=30)
    no = models.IntegerField()
    no_items = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=30)
    franchise_code = models.IntegerField()

class PendingPrescription(models.Model):
    customer_code = models.CharField(max_length=6)
    customer_name = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=30)
    franchise_code = models.IntegerField()
    consultation_fees = models.IntegerField(default=0)


class PendingTreatment(models.Model):
    customer_code = models.CharField(max_length=6)
    customer_name = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=30)
    franchise_code = models.IntegerField()
    consultation_fees = models.IntegerField(default=0)


class Prescription(models.Model):
    pending_prescription = models.ForeignKey(PendingPrescription, null=True, default=None)
    pending_treatment = models.ForeignKey(PendingTreatment, null=True, default=None)


class Appointment(models.Model):
    customer_code = models.CharField(max_length=6,unique=True)
    customer_name = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=50)
    request = models.CharField(max_length=100)
    franchise = models.ForeignKey(Franchise, null=True, default=None)
    receptionist_name = models.CharField(max_length=30)
    start_time = models.DateTimeField()


class Implementation(models.Model):
    franchise_code = models.IntegerField()
    date = models.DateField(default=datetime.today)
    date_mou = models.DateField()
    vendor = models.ForeignKey(Profile)
    painting = models.BooleanField()
    electrification = models.BooleanField()
    signboard = models.BooleanField()
    installation_of_required_equipment = models.BooleanField()
    inaugration_date = models.DateField()
    comments = models.CharField(max_length=100)


class Inspection(models.Model):
    franchise_code = models.IntegerField()
    date = models.DateField(default=datetime.today)
    vendor = models.ForeignKey(Profile)
    v1 = models.CharField(max_length=10)
    v2 = models.CharField(max_length=10)
    v3 = models.CharField(max_length=10)
    v4 = models.CharField(max_length=10)
    v5 = models.CharField(max_length=10)
    v6 = models.CharField(max_length=10)
    v7 = models.CharField(max_length=10)
    staff_behaviour = models.CharField(max_length=10)
    comments = models.CharField(max_length=100)


class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    type = models.CharField(max_length=10, null=True) #Brahmi,Tulsi,Arayaal
    sid = models.IntegerField(null=True, default=None)
    s = models.ForeignKey(Service, null=True, default=None)
    pid = models.IntegerField(null=True, default=None)
    p = models.ForeignKey(Package, null=True, default=None)
    trid = models.IntegerField(null=True, default=None)
    t = models.ForeignKey(TreatmentMaster, null=True, default=None)
    tid = models.CharField(max_length=10) #Service,Package,Treatment
    requested_time = models.DateTimeField(default=None, null=True)
    franchise_code = models.IntegerField(null=True)
    status = models.CharField(max_length=15, default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    confirmed_time = models.DateTimeField(null=True, default=None)
    lastchanged = models.DateTimeField(default=None, null=True)
    cleared = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.sid:
            self.s = Service.objects.get(id=self.sid)
            self.tid = "Service"
        if self.pid:
            self.p = Package.objects.get(id=self.pid)
            self.tid = "Package"
        if self.trid:
            self.t = TreatmentMaster.objects.get(id=self.trid)
            self.tid = "Treatment"
        obj = TimestampDB.objects.get(table_name='Enquiry')
        obj.timestamp = datetime.now()
        if self.id==None:
            my_kwargs = {'fail_silently': True, 'html_message': My_HTML_Mail_enquiry_reply(self.name),
                      'recipient_list': [self.email], 'from_email': 'care@clubayurveda.com', 'message': '',
                      'subject': 'Club Ayurveda: Appointment Request'}
            send_mail(**my_kwargs)
        obj.save()
        super(Enquiry, self).save(*args, **kwargs)


class TimestampDB(models.Model):
    table_name = models.CharField(max_length=50)
    timestamp = models.DateTimeField()


class Scan(models.Model):
    patient = models.ForeignKey(Customer)
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='scans')
    timestamp = models.DateTimeField(auto_now_add=True)


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pic = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


class LoginHistoryManager(models.Manager):
    def get_queryset(self):
        qset = super(LoginHistoryManager, self).get_queryset().order_by('-timestamp')
        for i in range(0,len(qset)):
            my_code = qset[i].ref.profile.franchise_code
            if my_code==0:
                qset[i].organisation = "Main Office"
            else:
                qset[i].organisation = Franchise.objects.get(id=qset[i].ref.profile.franchise_code).franchise_name
        return qset

class LoginHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile)

    objects = models.Manager()

    def __str__(self):
        return str(self.profile.franchise_code) + ' - ' + self.profile.name



class LoginTimestamps(models.Model):
    ref = models.ForeignKey(LoginHistory)
    timestamp = models.DateTimeField(auto_now_add=True)

    manager = LoginHistoryManager()


class Receipt(models.Model):
    receipt_id = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    franchise = models.ForeignKey(Franchise, default=None,null=True)
    customer = models.ForeignKey(Customer, default=None,null=True)
    cashier = models.ForeignKey(Profile, default=None,null=True)
    method = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    details = models.CharField(max_length=100)
    amount = models.FloatField(max_length=20)
    bill = models.ForeignKey(SalesReportBase, null=True, default=None)


class IDGenerator(models.Model):
    name = models.CharField(max_length=20)
    franchise_code = models.IntegerField()
    counter = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.franchise_code)+' - '+self.name

    @classmethod
    def get_id(cls,name,fc):
        with transaction.atomic():
            meta = (
                cls.objects
                .select_for_update()
                .get(name=name,franchise_code=fc)
            )
            meta.counter+=1
            meta.save()
        return str(fc)+"/"+datetime.now().strftime("%Y")+"/"+str(meta.counter)


class StockReturn(models.Model):
    item_name = models.CharField(max_length=50)
    stock_identifier = models.IntegerField()
    stock_quantity_returned = models.IntegerField()
    reason = models.CharField(max_length=200)
    franchise_code = models.IntegerField()
    franchise_name = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)