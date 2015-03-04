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
import cgi
import re


#----------- ROT13 START--------------
formRot13 = """
	<form method="post">
		<textarea name="text" rows="10" cols="60">%(rotWords)s</textarea>
		<br>
		<input type="submit" value="submit">
	</form>
"""


def escape_html(s):
	return cgi.escape(s, quote = True) #使用html转义，如：'<abc>'将转换成'&lt;abc&gt'


class Rot13(webapp2.RequestHandler):
	def write_form_rot13(self, rotWords=""):
		self.response.out.write(formRot13 
			%{"rotWords":escape_html(rotWords)})

	def get(self):
		self.write_form_rot13()
	def post(self):
		rotWords = self.request.get('text').encode("rot13")
		self.write_form_rot13(rotWords)
#------------  ROT13 END-----------------------





# SIGNUP START >>>>>>>>>>>>>>>>>>>>>>
formSignup = """
	<h2>Signup</h2>
	<form method="post">
		<table>
			<tr>
				<td>Username</td>
				<td>
					<input type="text" name="username" value="%(username)s">
				</td>
				<td>
					<label style="color:red">%(unvalidUsername)s</lable>
				</td>
			</tr>			
			<tr>
				<td>Password</td>
				<td>
					<input type="password" name="password">
				</td>
				<td>
					<label style="color:red">%(unvalidPassword)s</lable>
				</td>
			</tr>			
			<tr>
				<td>Verify Password</td>
				<td>
					<input type="password" name="verify">
				</td>				
				<td>
					<label style="color:red">%(unmatchedPassword)s</lable>
				</td>
			</tr>			
			<tr>
				<td>Email(optional)</td>
				<td>
					<input type="text" name="email" value="%(email)s">
				</td>				
				<td>
					<label style="color:red">%(unvalidEmail)s</lable>
				</td>
			</tr>
		</table>
		<input type="submit">
	</form>
"""




class Signup(webapp2.RequestHandler):
	def write_form_signup(self,username="", email="", 
		unvalidUsername="", unvalidPassword = "", 
		unmatchedPassword="", unvalidEmail=""):
		self.response.out.write(formSignup %{
			"username":escape_html(username),
			"email":escape_html(email),
			"unvalidUsername":escape_html(unvalidUsername),
			"unvalidPassword":escape_html(unvalidPassword),
			"unmatchedPassword":escape_html(unmatchedPassword),
			"unvalidEmail":escape_html(unvalidEmail)})

	def get(self):
		self.write_form_signup()
	def post(self):
		username=self.request.get('username')
		password=self.request.get('password')
		verifyPassword=self.request.get('verify')
		email=self.request.get('email')

		strUnvalidUsername = ""
		strUnvalidPassword = ""
		strUnmatchedPassword =""
		strUnvalidEmail =""		

		isAllRight = True

		if(not re.compile("^[a-zA-Z0-9_-]{3,20}$").match(username)):
			strUnvalidUsername = "That's not a valid username"
			isAllRight = False

		if(not re.compile("^.{3,20}$").match(password)):
			strUnvalidPassword = "That's not a valid password"
			isAllRight = False
		elif(not password == verifyPassword):
			strUnmatchedPassword = "Your password didn't match" 
			isAllRight = False

		if(not (re.compile("^[\S]+@[\S]+\.[\S]+$").match(email)
			or ''==email)):
			strUnvalidEmail = "That's not a valid email"
			isAllRight = False

		if(isAllRight):
			self.redirect("/welcome?username="+username)
		else:
			self.write_form_signup(username, email, 
				strUnvalidUsername, 
				strUnvalidPassword, strUnmatchedPassword,
				strUnvalidEmail)

class Welcome(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(
			"welcome, %s" %escape_html(self.request.get('username')))
# SIGNUP END <<<<<<<<<<<<<<<<<<<<<


class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(
			"This is Problem Set 2 on Udacity.<br><br>" 
			+ "Pages on <b>'/rot13'</b> and <b>'/signup'</b><br><br>"
			+ "Maked by qzh")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rot13', Rot13),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
