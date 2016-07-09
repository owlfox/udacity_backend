# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from utility import *
form = """
<html>
<head>
    <title>Unit 2 Rot 13</title>
 </head>
<h1> Enter some text to ROT13:</h1>
<form method="post">
    <textarea style="height: 100px; width: 400px;" name="text">%(text)s</textarea>
    <br>
    <input type="submit">
</form>
</html>
"""
signupform = """
<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">%(err_uname)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">%(err_pw)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">%(err_pwvfy)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">%(err_email)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""
signup_err = {
"pwvfyerr": "Your passwords didn't match.",
"emailnotvalid": "That's not a valid email.",
"namenotvalid": "That's not a valid username.",
"pwnotvalid": "That's not a valid password.",
}
welcome_html = """
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Signup</title>
  </head>

  <body>
    <h2>Welcome, %s!</h2>
  </body>
</html>
"""
class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.write(welcome_html % username)

class MainPage(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.write(form % {"text": escape_html(text)})
    def get(self):
        self.write_form()
    def post(self):
        text = self.request.get("text")
        rotted = rot13(text)
        self.write_form(rotted)

class UserSignup(webapp2.RequestHandler):
    def write_form(self, username="", password="" ,email="",err_uname="",err_pw="",err_pwvfy="",err_email=""):
        self.response.write(signupform % {"username":username, "password":password, "email":email,
        "err_uname":err_uname,"err_pw":err_pw,"err_pwvfy":err_pwvfy,"err_email":err_email,})
    def get(self):
        self.write_form()
    def post(self):
        err_uname, err_pw, err_pwvfy, err_email = "", "", "", ""
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        isValid = True
        if valid_username(username) is None:
            isValid = False
            err_uname = signup_err.get("namenotvalid")
        if valid_pw(password) is None:
            isValid = False
            err_pw = signup_err.get("pwnotvalid")
        if password != verify:
            isValid = False
            err_pwvfy = signup_err.get("pwvfyerr")

        # email is optional, not empty string, then we check
        if email != "" and valid_email(email) is None:
            isValid = False
            err_email = signup_err.get("emailnotvalid")
        if isValid is False:
            self.write_form(escape_html(username), escape_html(password), escape_html(email), escape_html(err_uname), escape_html(err_pw), escape_html(err_pwvfy), escape_html(err_email))
        else:
            self.redirect("/welcome?username=%(username)s" % {'username':escape_html(username)})

app = webapp2.WSGIApplication([
    ('/', MainPage),('/signup', UserSignup),('/welcome', Welcome)
], debug=True)
