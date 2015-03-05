#coding=utf-8

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

form_html="""
<form>
<h2>Add a food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

hidden_html="""<input type="hidden" name="food" value="%s">"""

items_html="""<li>%s</li>"""
shopping_list_html="""
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class MainHandler(webapp2.RequestHandler):
	def write_form(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def get(self):
		output_hidden = ""
		output_form = form_html

		items = self.request.get_all("food")  #获取所有food
		if items:
			output_items = ""
			for item in items:
				output_hidden += hidden_html %item 		#生成hidden
				output_items += items_html %item
			output_shopping_list = shopping_list_html %output_items		#生成shopping list
			output_form += output_shopping_list 	#追加shopping list

		output_form = output_form %output_hidden	#追加hidden
		self.write_form(output_form)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
