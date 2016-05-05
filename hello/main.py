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
import webapp2
form="""
<form action="http://www.google.com/search">
<!--By default, the form submit to itself if we're not setting action -->
<input name="q"></input>
<input type="submit"></input>
<!-- q=better+filght+search if we type in "better flight search"-->
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
