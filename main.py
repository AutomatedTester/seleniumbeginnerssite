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


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import os
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):

  def get(self):
    template_values = { }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

class Chapter1Handler(webapp.RequestHandler):

  def get(self):
    template_values = { }

    path = os.path.join(os.path.dirname(__file__), 'chapter1.html')
    self.response.out.write(template.render(path, template_values))

class Chapter2Handler(webapp.RequestHandler):

  def get(self):
    from datetime import datetime
    now = datetime.now()
    template_values = {'now':str(now) }

    path = os.path.join(os.path.dirname(__file__), 'chapter2.html')
    self.response.out.write(template.render(path, template_values))
    
class WindowPopupHandler(webapp.RequestHandler):

  def get(self):
    template_values = { }

    path = os.path.join(os.path.dirname(__file__), 'windowpopup.html')
    self.response.out.write(template.render(path, template_values))

class LoadAjaxHandler(webapp.RequestHandler):

  def get(self):
    self.response.out.write("""
        <p>The following text has been loaded from another page on this site. It has been loaded in
        an asynchronous fashion so that we can work through the AJAX section of this chapter</p>
    """)

class Chapter3Handler(webapp.RequestHandler):

  def get(self,name=None):
    import random
    from datetime import datetime
    words = ['pool','cool','fool','mool']
    template_values = {}
    if name:
      template_values = {'name':name, 'word':words[random.randrange(4)],"date":datetime.now()}
    else:
      template_values = {'word':words[random.randrange(4)],"date":datetime.now()}

    path = os.path.join(os.path.dirname(__file__), 'chapter3.html')
    self.response.out.write(template.render(path, template_values))

class Chapter4Handler(webapp.RequestHandler):

  def get(self):
    template_values = { }

    path = os.path.join(os.path.dirname(__file__), 'chapter4.html')
    self.response.out.write(template.render(path, template_values))   
    
class Chapter8Handler(webapp.RequestHandler):

  def get(self):
    template_values = { }

    path = os.path.join(os.path.dirname(__file__), 'chapter8.html')
    self.response.out.write(template.render(path, template_values)) 

class MultiSelect(webapp.RequestHandler):

  def get(self):
    template_values = { }

    path = os.path.join(os.path.dirname(__file__), 'multi-select.html')
    self.response.out.write(template.render(path, template_values)) 

def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/chapter1', Chapter1Handler),
                                        ('/windowpopup\.html', WindowPopupHandler),
                                        ('/loadajax', LoadAjaxHandler),
                                        ('/chapter2', Chapter2Handler),
                                        ('/chapter3/?(.*)', Chapter3Handler),
                                        ('/chapter4', Chapter4Handler),
                                        ('/chapter8', Chapter8Handler),
                                       ('/multi-select.html', MultiSelect)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
