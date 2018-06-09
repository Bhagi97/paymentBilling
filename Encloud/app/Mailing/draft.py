from email.mime.multipart import MIMEMultipart
def My_HTML_Mail(name,username,role,password,franchise):
    if role=='Admin' and franchise != 'Main Office':
        html = """\
<!DOCTYPE html>
<html>
  <head>
    <style>
      #outer{
          margin-left: 100px;
          margin-right: 100px;
        }
      @media only screen and (max-width: 720px) {
        #outer{
          margin-left: 20px;
          margin-right: 20px;
        }
      }
      @media only screen and (max-width: 480px) {
        #outer{
          margin-left: 0px;
          margin-right: 0px;
        }
      }
    </style>
  </head>
  <body>
    <div class="main">
      <div id="outer" style="background-color: #f3f3f3;">
        <h2 style="text-align: center; padding: 20px; background: #228B22; /* for browsers that do not support gradients */     background: -webkit-linear-gradient(left top, #228B22,  #ADFF2F); /* for safari 5.1 to 6.0 */     background: -o-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for opera 11.1 to 12.0 */   background: -moz-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for firefox 3.6 to 15 */     background: linear-gradient(to bottom right, #228B22,  #ADFF2F);"><img src="http://clubayurveda.com/images/logo.png" alt="Clubayurveda logo" width="423" height="86" /></h2>
        <div id="contents" style="padding-left: 20px; padding-right: 20px;">
          <h2 style="text-align: center;">Welcome to Club Ayurveda</h2>
          <p>Hi %(name)s,</p>
          We proudly welcome you as a franchisee of <span style="font-weight:bold;">Club Ayurveda</span> for giving a better health services to our society.<br/>
          Please find your user details given below. Login to the <span style="color: #008000;"><a href="http://app.clubayurveda.com" target="_blank" style="color: #008000;">Club Ayurveda Application</a></span> with the credentials given below to activate your account. It is recommended to change your password after your first login. Please keep your password confidential to avoid any misuse.<br/>
          <p><b>User Credentials<br /></b></p>
          <ul>
            <li>Username : %(username)s</li>
            <li>Password : %(password)s</li>
            <li>Role : %(role)s</li>
          </ul><br/>
          You can authorize additional users (ie employees of your institution) by using "Add user" option in the home page and can provide them with separate user id and password if required. <br/>
          Assuring you of our best services at all times.
          <p>Yours sincerely, <br /> Customer Service Team <br /> Club Ayurveda Pvt. Ltd.</p>
          <p><span style="font-size: 10pt;"><em>Note: The information in this e-mail is confidential and may be legally privileged. It is intended solely for the addressee. Access to this e-mail by anyone else is unauthorized. If you are not the intended recipient, kindly discard this e-mail. Any disclosure, copying, distribution or any action taken or omitted to be taken in reliance on it, is prohibited and may be unlawful.<br /></em></span></p>
          <p><br/></p>
        </div>
      </div>
      <div style="text-align: center;">
        <p><img style="margin-right:30px;" src="http://app.clubayurveda.com/static/images/logo_encloud.png" alt="EnCloud" width="169" height="33" />           <img src="http://www.endogreen.com/images/logo.png" alt="Endogreen logo" width="138" height="40" /></p>
      </div>
    </div>
  </body>
</html>        
        """% dict(name=name, username=username, password=password, role=role, franchise=franchise)
    else:
        if franchise=='Main Office':
            in_between = ""
        else:
            in_between = ", a Club Ayurveda Franchisee"
        html = """\
<!DOCTYPE html>
<html>
  <head>
    <style>
      #outer{
          margin-left: 100px;
          margin-right: 100px;
        }
      @media only screen and (max-width: 720px) {
        #outer{
          margin-left: 20px;
          margin-right: 20px;
        }
      }
      @media only screen and (max-width: 480px) {
        #outer{
          margin-left: 0px;
          margin-right: 0px;
        }
      }
    </style>
  </head>
  <body>
    <div class="main">
      <div id="outer" style="background-color: #f3f3f3;">
        <h2 style="text-align: center; padding: 20px; background: #228B22; /* for browsers that do not support gradients */     background: -webkit-linear-gradient(left top, #228B22,  #ADFF2F); /* for safari 5.1 to 6.0 */     background: -o-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for opera 11.1 to 12.0 */   background: -moz-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for firefox 3.6 to 15 */     background: linear-gradient(to bottom right, #228B22,  #ADFF2F);"><img src="http://clubayurveda.com/images/logo.png" alt="Clubayurveda logo" width="423" height="86" /></h2>
        <div id="contents" style="padding-left: 20px; padding-right: 20px;">
          <h2 style="text-align: center;">Welcome to Club Ayurveda</h2>
          <p>Hi %(name)s,</p>
          We welcome you as the member of <span style="font-weight:bold;">Club Ayurveda</span> for giving a better health services to our customers.
          You have been invited to join %(franchise)s"""% dict(name=name, franchise=franchise)+in_between+""". Please find your user details given below. Login to the <span style="color: #008000;"><a href="http://app.clubayurveda.com" target="_blank" style="color: #008000;">Club Ayurveda Application</a></span> with the credentials given below to activate your account. It is recommended to change your password after your first login. Please keep your password confidential to avoid any misuse.<br/>
          <p><b>User Credentials<br /></b></p>
          <ul>
            <li>Username : %(username)s</li>
            <li>Password : %(password)s</li>
            <li>Role : %(role)s</li>
          </ul><br/>
          Assuring you of our best services at all times.
          <p>Yours sincerely, <br /> Customer Service Team <br /> Club Ayurveda Pvt. Ltd.</p>
          <p><span style="font-size: 10pt;"><em>Note: The information in this e-mail is confidential and may be legally privileged. It is intended solely for the addressee. Access to this e-mail by anyone else is unauthorized. If you are not the intended recipient, kindly discard this e-mail. Any disclosure, copying, distribution or any action taken or omitted to be taken in reliance on it, is prohibited and may be unlawful.<br /></em></span></p>
          <p><br/></p>
        </div>
      </div>
      <div style="text-align: center;">
        <p><img style="margin-right:30px;" src="http://app.clubayurveda.com/static/images/logo_encloud.png" alt="EnCloud" width="169" height="33" />           <img src="http://www.endogreen.com/images/logo.png" alt="Endogreen logo" width="138" height="40" /></p>
      </div>
    </div>
  </body>
</html>
    """% dict(username=username,password=password,role=role)
    return html


def My_HTML_Mail_reset(name,username,password):
    html = """\
<!DOCTYPE html>
<html>
  <head>
    <style>
      #outer{
          margin-left: 100px;
          margin-right: 100px;
        }
      @media only screen and (max-width: 720px) {
        #outer{
          margin-left: 20px;
          margin-right: 20px;
        }
      }
      @media only screen and (max-width: 480px) {
        #outer{
          margin-left: 0px;
          margin-right: 0px;
        }
      }
    </style>
  </head>
  <body>
    <div class="main">
      <div id="outer" style="background-color: #f3f3f3;">
        <h2 style="text-align: center; padding: 20px; background: #228B22; /* for browsers that do not support gradients */     background: -webkit-linear-gradient(left top, #228B22,  #ADFF2F); /* for safari 5.1 to 6.0 */     background: -o-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for opera 11.1 to 12.0 */   background: -moz-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for firefox 3.6 to 15 */     background: linear-gradient(to bottom right, #228B22,  #ADFF2F);"><img src="http://clubayurveda.com/images/logo.png" alt="Clubayurveda logo" width="423" height="86" /></h2>
        <div id="contents" style="padding-left: 20px; padding-right: 20px;">
          <h2 style="text-align: center;">Welcome to Club Ayurveda</h2>
          <p>Hi %(name)s,</p>
          Your user credentials have been reset. Please find your new password below. Login to the <span style="color: #008000;"><a href="http://app.clubayurveda.com" target="_blank" style="color: #008000;">Club Ayurveda Application</a></span><br />
          <p><b>User Credentials<br /></b></p>
          <ul>
            <li>Username : %(username)s</li>
            <li>Password : %(password)s</li>
          </ul>
          <br />
          <p><span style="font-size: 10pt;"><em>Note: The information in this e-mail is confidential and may be legally privileged. It is intended solely for the addressee. Access to this e-mail by anyone else is unauthorized. If you are not the intended recipient, kindly discard this e-mail. Any disclosure, copying, distribution or any action taken or omitted to be taken in reliance on it, is prohibited and may be unlawful.<br /></em></span></p>
          <p><br/></p>
        </div>
      </div>
      <div style="text-align: center;">
        <p><img style="margin-right:30px;" src="http://app.clubayurveda.com/static/images/logo_encloud.png" alt="EnCloud" width="169" height="33" />           <img src="http://www.endogreen.com/images/logo.png" alt="Endogreen logo" width="138" height="40" /></p>
      </div>
    </div>
  </body>
</html>
    """% dict(name=name,username=username,password=password)
    return html


def My_HTML_Mail_patient(name,customer_code):
    html = """\
    <!DOCTYPE html>
<html>
  <head>
    <style>
      #outer{
        margin-left: 100px;
        margin-right: 100px;
      }
      @media only screen and (max-width: 720px) {
        #outer{
          margin-left: 20px;
          margin-right: 20px;
        }
      }
      @media only screen and (max-width: 480px) {
        #outer{
          margin-left: 0px;
          margin-right: 0px;
        }
      }
    </style>
  </head>
  <body>
    <div class="main">
      <div id="outer" style="background-color: #f3f3f3;">
        <h2 style="text-align: center; padding: 20px; background: #228B22; /* for browsers that do not support gradients */     background: -webkit-linear-gradient(left top, #228B22,  #ADFF2F); /* for safari 5.1 to 6.0 */     background: -o-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for opera 11.1 to 12.0 */   background: -moz-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for firefox 3.6 to 15 */     background: linear-gradient(to bottom right, #228B22,  #ADFF2F);"><img src="http://clubayurveda.com/images/logo.png" alt="Clubayurveda logo" width="423" height="86" /></h2>
        <div id="contents" style="padding-left: 20px; padding-right: 20px;">
          <h2 style="text-align: center;">Welcome to Club Ayurveda</h2>
          <p>Dear %(name)s,</p>
          Club Ayurveda welcomes you for giving better health services. Your customer code is <b>%(code)s</b> For the optimum effectiveness of an Ayurvedic Sukhachikitsa treatment one should prepare their body by controlling their life style at least for a period of one week before commencement of treatment. A vegetarian diet is preferable for at least two weeks prior to the commencement of the treatments. Similarly, the doctor's advice on diet and lifestyle shall be followed for the prescribed period even after treatment also.
          <p><b>Things to Remember:<br /></b></p>
          <ul>
            <li>While undergoing treatments, avoid exposure to cold, wind, hot, sun, dust, smoke, fog etc.</li>
            <li>Women cannot have a full body massage treatment at the time of their mensuration.</li>
            <li>Avoid physical or mental stress during the course of treatment.</li>
            <li>Bring all your previous medical reports (if any) while consulting doctor.</li>
            <li>Liquor is strictly prohibited during the treatment period.</li>
            <li>Any laboratory tests or specialist consultation if needed will cost extra.</li>
          </ul>
          <br /> Assuring you of our best services at all times.
          <p>Yours sincerely, <br /> Customer Service Team <br /> Club Ayurveda Pvt. Ltd.</p>
          <p><span style="font-size: 10pt;"><em>Note: The information in this e-mail is confidential and may be legally privileged. It is intended solely for the addressee. Access to this e-mail by anyone else is unauthorized. If you are not the intended recipient, kindly discard this e-mail. Any disclosure, copying, distribution or any action taken or omitted to be taken in reliance on it, is prohibited and may be unlawful.<br /></em></span></p>
          <p></p>
        </div>
      </div>
      <div style="text-align: center;">
        <p><img style="margin-right: 30px;" src="http://app.clubayurveda.com/static/images/logo_encloud.png" alt="EnCloud" width="169" height="33" /> <img src="http://www.endogreen.com/images/logo.png" alt="Endogreen logo" width="138" height="40" /></p>
      </div>
    </div>
  </body>
</html>
    """% dict(name=name,code=customer_code)

    return html


def My_HTML_Mail_enquiry_reply(name):
    html = """\
    <!DOCTYPE html>
<html>
  <head>
    <style>
      #outer{
          margin-left: 100px;
          margin-right: 100px;
        }
      @media only screen and (max-width: 720px) {
        #outer{
          margin-left: 20px;
          margin-right: 20px;
        }
      }
      @media only screen and (max-width: 480px) {
        #outer{
          margin-left: 0px;
          margin-right: 0px;
        }
      }
    </style>
  </head>
  <body>
    <div class="main">
      <div id="outer" style="background-color: #f3f3f3;">
        <h2 style="text-align: center; padding: 20px; background: #228B22; /* for browsers that do not support gradients */     background: -webkit-linear-gradient(left top, #228B22,  #ADFF2F); /* for safari 5.1 to 6.0 */     background: -o-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for opera 11.1 to 12.0 */   background: -moz-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for firefox 3.6 to 15 */     background: linear-gradient(to bottom right, #228B22,  #ADFF2F);"><img src="http://clubayurveda.com/images/logo.png" alt="Clubayurveda logo" width="423" height="86" /></h2>
        <div id="contents" style="padding-left: 20px; padding-right: 20px;">
          <h2 style="text-align: center;">Welcome to Club Ayurveda</h2>
          <p>Dear %(name)s,</p>
          Thanks for selecting Club Ayurveda for giving you a better health services. Our team will get back to you after verifying the availability of accommodation in the selected Centre on the chosen date/time.
          <br/>
          Assuring you of our best services at all times.
          <p>Yours sincerely, <br /> Customer Service Team <br /> Club Ayurveda Pvt. Ltd.</p>
          <p><br/></p>
        </div>
      </div>
    </div>
  </body>
</html>
    """% dict(name=name)

    return html


def My_HTML_Mail_enquiry_confirmation(name,time):
    html = """\
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          #outer{
              margin-left: 100px;
              margin-right: 100px;
            }
          @media only screen and (max-width: 720px) {
            #outer{
              margin-left: 20px;
              margin-right: 20px;
            }
          }
          @media only screen and (max-width: 480px) {
            #outer{
              margin-left: 0px;
              margin-right: 0px;
            }
          }
        </style>
      </head>
      <body>
        <div class="main">
          <div id="outer" style="background-color: #f3f3f3;">
            <h2 style="text-align: center; padding: 20px; background: #228B22; /* for browsers that do not support gradients */     background: -webkit-linear-gradient(left top, #228B22,  #ADFF2F); /* for safari 5.1 to 6.0 */     background: -o-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for opera 11.1 to 12.0 */   background: -moz-linear-gradient(bottom right, #228B22,  #ADFF2F); /* for firefox 3.6 to 15 */     background: linear-gradient(to bottom right, #228B22,  #ADFF2F);"><img src="http://clubayurveda.com/images/logo.png" alt="Clubayurveda logo" width="423" height="86" /></h2>
            <div id="contents" style="padding-left: 20px; padding-right: 20px;">
              <h2 style="text-align: center;">Welcome to Club Ayurveda</h2>
              <p>Dear %(name)s,</p>
              Thanks for selecting Club Ayurveda for giving you a better health services. Your appointment is confirmed for <b>%(time)s</b> in the selected Centre.
              <br/>
              <br/>
              Assuring you of our best services at all times.
              <p>Yours sincerely, <br /> Customer Service Team <br /> Club Ayurveda Pvt. Ltd.</p>
              <p><br/></p>
            </div>
          </div>
        </div>
      </body>
    </html>
    """% dict(name=name,time=time)

    return html