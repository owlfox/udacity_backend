#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import logging
import webapp2
from valid import *
form="""
<form method="post">
    Whas is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value=""%(month)s"">
    </label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>

    <br>
    <div style="color: red"> %(error)s</div>
    <br>
<input type="submit"></input>
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def writeform(self, error="", year="", day="", month=""):
        self.response.write(form % {"error":error, "month":month, "year":year, "day":day})

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
        self.writeform()

    def post(self):
        user_month  = self.request.get('month')
        user_day    = self.request.get('day')
        user_year   = self.request.get('year')
        month = valid_month(user_month)
        day = valid_month(user_day)
        year = valid_month(user_year)

        if not (day and month and year):
            self.writeform("Hey wtf are you entering!!(badass server)")
            self.response.write(user_day)
            self.response.write(user_month)
            self.response.write(user_year)
        else:
            self.response.writeform("Thanks, that might be a good day to born.")



class TestHandler(webapp2.RequestHandler):
    def post(self):
        # q = self.request.get("q")
        # self.response.write(q)
        # this returns plain text
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)
