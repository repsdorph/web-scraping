#!/usr/bin/python2.7
__author__ = 'repsdorph'
"""This is a test script to show mechanize for academic purpos, don't use

Don't be a spamer, and respect the robots.txt unless you have a really good reason not to!
"""

import mechanize

import cookielib
import passwords


# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)  # Ignore what robots.txt says

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
# br.set_debug_http(True)
# br.set_debug_redirects(True)
# br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

base_url = ""
login_url = 'http://portalen.dtu.dk'
br.open(login_url)

# Show the available forms
# for f in br.forms():
# print(f)

#br.add_password(login_url, 's100322', passwords.dtu())
br.select_form(nr=0)
br['ctl00$ContentPlaceHolder1$Textbox_Username'] = 's100322'
br['ctl00$ContentPlaceHolder1$TextBox_Password'] = passwords.dtu()
br.submit()
#print("Loged in?")

# We want to find the link to forward us to the real site
# Looking at some results in link format
#for l in br.links():
#    print(l.text)

# We find a link named "here", who is to the real side with a login-token
req = br.click_link(text='here')
br.open(req)

# Again, we want to find the link to the kantine, and use a regex to sort the links.
# Looking at some results in link format
#for l in br.links(url_regex='Kantine'):
#    print(l)
#print("-------------")
#print(br.title())
#print(br.response().info())

# We find a link named "here", who is to the real side with a login-token
req = br.click_link(text='Kantinen')
br.open(req)

html = br.response().read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html)
table = soup.find('table', {'class': 'cantine'})
tds = table.findAll('td')

tds = [a.text.strip() for a in tds if len(a.text.strip()) > 3]
#print("Date: {}".format(tds.pop()))
for i in range(0, len(tds), 2):
    try:
        print("{d} - {p}\n".format(d=tds[i].encode('utf-8'), p=tds[i + 1].encode('utf-8')))
        print("---")
    except:
        pass