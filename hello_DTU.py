import mechanize

br = mechanize.Browser()
base_url = "http://toolsfordatascience.wordpress.com/"

r = br.open(base_url)
html = r.read()

# Show the source
print(html)
print("\n")
# or for the last page we opened
#print br.response().read()

# Show the title
print("Title: {}\n".format(br.title()))
