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


form = """
<form method="post">
	What is your birthday?
	<br>
	<label>
		Month
		<input type="text" name="month">
	</label>
	<label>
		Day
		<input type="text" name="day">
	</label>
	<label>
		Year
		<input type="text" name="year">
	</label>
	<br><br>
	<input type="submit">
</form>
"""



months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
			'August', 'September', 'Octaober', 'November', 'December']


def valid_day(day):
	if(day and day.isdigit()):
		day = int(day)
	if(day < 32 and day >0):
		return day


def valid_month(month):
	if(month):
		month = month.capitalize()
	if(month in months):
		return month



def valid_year(year):
	if(year and year.isdigit()):
		year = int(year)
	if(year < 2020 and year >1880):
		return year


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
    	user_day = valid_day(self.request.get('day'))
    	user_month = valid_month(self.request.get('month'))
    	user_year = valid_year(self.request.get('year'))

    	if not(user_day and user_month and user_year):
    	 	self.response.out.write(form)
    	else:
    		self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
