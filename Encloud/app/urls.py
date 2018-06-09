from django.conf.urls import url 
from app import views

urlpatterns = [
                # Matches any html file - to be used for gentella   
                # Avoid using your .html in your resources. Or create a separate django app.

                # -- Franchise management --
                url(r'^.*addfranchise.html', views.addfranchise, name='addfranchise'),
                url(r'^.*ajax/checkfranchisename/', views.checkfranchisename, name='checkfranchisename'),
                url(r'^.*ajax/suspendfranchise/', views.suspendfranchise, name='suspendfranchise'),
                url(r'^.*viewfranchise.html', views.viewfranchise, name='viewfranchise'),
                url(r'^.*editfranchise.html', views.editfranchise, name='editfranchise'),
                # -- END --

                # -- HO/Admin Panel --

                # User Management
                    url(r'^.*adduser.html', views.adduser, name='adduser'),
                    url(r'^.*edituser.html', views.edituser, name='edituser'),
                    url(r'^.*ajax/checkusername/', views.checkusername, name='checkusername'),
                    url(r'^.*viewusers.html', views.viewusers, name='viewusers'),
                    url(r'^.*loginhistory.html', views.loginhistory, name='loginhistory'),
                    url(r'^.*ajax/suspenduser/', views.suspenduser, name='suspenduser'),
                    url(r'^.*ajax/checkregid/', views.checkregid, name='checkregid'),

                # Inventory Management
                    url(r'^.*categoryentry.html', views.categoryentry, name='categoryentry'),
                    url(r'^.*ajax/getcategories/',views.getcategories, name='getcategories'),
                    url(r'^.*productentry.html', views.productentry, name='productentry'),
                    url(r'^.*ajax/getproducts/',views.getproducts, name='getproducts'),
                    url(r'^.*ajax/deleteproduct/',views.deleteproduct, name='deleteproduct'),
                    url(r'^.*packageentry.html', views.packageentry, name='packageentry'),
                    url(r'^.*ajax/deletepackage/',views.deletepackage, name='deletepackage'),
                    url(r'^.*togglepackages.html', views.togglepackages, name='togglepackages'),
                    url(r'^.*ajax/getpackages/',views.getpackages, name='getpackages'),
                    url(r'^.*serviceentry.html', views.serviceentry, name='serviceentry'),
                    url(r'^.*ajax/deleteservice/',views.deleteservice, name='deleteservice'),
                    url(r'^.*toggleservices.html', views.toggleservices, name='toggleservices'),
                    url(r'^.*ajax/getservices/',views.getservices, name='getservices'),
                    url(r'^.*treatmententry.html', views.treatmententry, name='treatmententry'),
                    url(r'^.*ajax/deletetreatmentmaster/',views.deletetreatmentmaster, name='deletetreatmentmaster'),
                    url(r'^.*mytreatments.html', views.mytreatments, name='mytreatments'),
                    url(r'^.*ajax/deletetreatment/',views.deletetreatment, name='deletetreatment'),
                    url(r'^.*ajax/gettreatments/', views.gettreatments, name='gettreatments'),
                    url(r'^.*ajax/gettreatmentmaster/', views.gettreatmentmaster, name='gettreatmentmaster'),
                    url(r'^.*discountentry.html', views.discountentry, name='discountentry'),
                    url(r'^.*ajax/getdiscounts/', views.getdiscounts, name='getdiscounts'),
                    url(r'^.*ajax/getitems/', views.getitems, name='getitems'),
                    url(r'^.*addstock.html', views.addstock, name='addstock'),
                    url(r'^.*stockreturn.html', views.stocktransfer, name='stocktransfer'),
                    url(r'^.*ajax/getstockdetails/',views.getstockdetails, name='getstockdetails'),
                    url(r'^.*ajax/resolvetransferrequest/',views.resolvetransferrequest, name='resolvetransferrequest'),
                    url(r'^.*ajax/get_base_product/', views.get_base_product, name='get_base_product'),
                    # url(r'^.*ajax/getskulist/', views.getskulist, name='getskulist'),
                    # url(r'^.*ajax/deletesku/', views.deletesku, name='deletesku'),
                    # url(r'^.*skuentry.html', views.skuentry, name='skuentry'),
                # -- END --

                # -- General --
                url(r'^.*ajax/getstates/',views.getstates, name='getstates'),
                url(r'^.*ajax/getdistricts/',views.getdistricts, name='getdistricts'),
                url(r'^.*ajax/search_id/',views.search_id, name='search_id'),
                url(r'^.*resetpassword.html', views.resetpassword, name='resetpassword'),
                url(r'^.*editprofile.html', views.editprofile, name='editprofile'),
                url(r'^.*ajax/checkstock/', views.checkstock, name='checkstock'),
                url(r'^.*ajax/get_stock_item/', views.get_stock_item, name='get_stock_item'),
                url(r'^.*ajax/customerfranchiseeverification/', views.customerFranchiseeVerification, name='customerFranchiseeVerification'),
                # --END --

                # -- Reports --
                url(r'^.*enquiry_report.html',views.enquiry_report, name='enquiry_report'),
                url(r'^.*report_.*.html', views.reports, name='reports'),
                url(r'^.*ajax/getreport/',views.getreport, name='getreport'),
                url(r'^.*export_report.*.html', views.export_report, name='exportreports'),
                url(r'^.*ajax/get_bill/',views.get_bill, name='get_bill'),
                url(r'^.*ajax/printreport/',views.printreport, name='printreport'),
                url(r'^.*ajax/deletebill/',views.deletebill, name='deletebill'),
                # -- END --

                # -- LOGIN MODULE --
                url(r'^.*ajax/mailpassword/', views.mailpassword, name='mailpassword'),
                url(r'.*login.html$', views.login_request, name='login_request'),
                url(r'.*lostpassword.html$', views.lostpassword, name='lostpassword'),
                url(r'^.*logout.html',views.logout_request, name='logout_request'),
                # -- END --

                # -- Reception --
                url(r'^.*registerpatient.html',views.registerpatient, name='registerpatient'),
                url(r'^.*reception.html.*',views.recepetion, name='recepetion'),
                url(r'^.*medicalreports.html',views.medicalreports, name='medicalreports'),
                url(r'^.*enquiry.html.*', views.enquiry, name='enquiry'),
                url(r'^.*ajax/changeenquirystatus/', views.changeenquirystatus, name='changeenquirystatus'),
                url(r'^.*ajax/clearenquiry/', views.clearenquiry, name='clearenquiry'),
                # -- END --

                # -- Billing --
                url(r'^.*newbill.html',views.newbill, name='newbill'),
                url(r'^.*receipt.html',views.receipt, name='receipt'),
                url(r'^.*invoicebill.html',views.invoicebill, name='invoicebill'),
                url(r'^.*ajax/getreceipts/',views.getreceipts, name='getreceipts'),
                url(r'^.*prescriptionreport.html',views.prescriptionreport, name='prescriptionreport'),
                url(r'^.*ajax/savebill/',views.savebill, name='savebill'),
                url(r'^.*ajax/getsavedbill/',views.getsavedbill, name='getsavedbill'),
                url(r'^.*ajax/get_products/',views.get_products, name='get_products'),
                url(r'^.*ajax/getHOproducts/',views.getHOproducts, name='getHOproducts'),
                url(r'^.*ajax/printbill/',views.printbill, name='printbill'),
                url(r'^.*ajax/print_hobill/',views.print_hobill, name='print_hobill'),
                url(r'^.*ajax/printinvoice/',views.printinvoice, name='printinvoice'),
                # -- END --

                # -- Doctor --
                url(r'^.*pending_patients.html',views.pending_patients, name='pending_patients'),
                url(r'^.*upload.html',views.upload_scans, name='upload_scans'),
                url(r'^.*prescriptionsmade.html', views.prescriptions_made, name='prescriptions_made'),
                url(r'^.*editprescription.html', views.edit_prescription, name='edit_prescription'),
                url(r'^.*pendingprescription.html$', views.pending_prescription, name='pending_prescription'),
                url(r'^.*pendingprescriptionview.html', views.get_pending_prescription, name='get_pending_prescription'),
                url(r'^.*ajax/printprescription/',views.printprescription, name='printprescription'),
                url(r'^.*ajax/getscans/',views.getscans, name='getscans'),
                url(r'^.*ajax/delscan/',views.delscan, name='delscan'),
                # -- END --

                # -- Distributor --
                url(r'^.*implementation.html',views.implementation, name='implementation'),
                url(r'^.*inspection.html',views.inspection, name='inspection'),
                # -- END --

                url(r'^.*viewpatients.html',views.viewpatients, name='viewpatients'),
                url(r'^.*doctor_details.html',views.doctor_details, name='doctor_details'),
                url(r'^.*prescription_new.html',views.prescription, name='prescription'),
                url(r'^.*ajax/getlist/', views.getlist, name='getlist'),
                url(r'^.*ajax/printpatientreport/', views.patientreport, name='patientreport'),
                url(r'^.*patient_details.html',views.patient_details, name='patient_details'),

                # The home page
                url(r'^.*index.html',views.index, name='index'),
                url(r'^.*quicknav.html',views.index, name='index'),
                url(r'^$', views.index, name='index'),

                # 404
                # url(r'.*', views.err_404, name='404'),

              ]