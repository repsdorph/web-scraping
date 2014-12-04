#!/usr/bin/python2.7
__author__ = 'repsdorph'
"""This is a test script to show mechanize for academic purpos, don't use

Don't be a spamer, and respect the robots.txt unless you have a really good reason not to!
"""

import mechanize

import cookielib



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

# Open some site, let's pick a random one, the first that pops in mind:
r = br.open('http://google.com')
html = r.read()

# Select the first (index zero) form
# You need to select a form this way, before you are able to chose a form based on keyword
br.select_form(nr=0)

# Let's search
br.form['q'] = 'DTU'
br.submit()
# print br.response().read()

# Looking at some results in link format
for l in br.links(url_regex='dtu'):
    print(l.text)

    # Click on the next-link

    # Read the next side

req = br.click_link(text='2')
br.open(req)

for l in br.links(url_regex='dtu'):
    print(l.text)
