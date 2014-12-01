import mechanize

br = mechanize.Browser()
url = "http://toolsfordatascience.wordpress.com/"

r = br.open(url)
html = r.read()

# Show the source
print(html)
print("\n")
# or for the last page we opened
#print br.response().read()

# Show the title
print("Title: {}\n".format(br.title()))
