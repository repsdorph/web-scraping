import mechanize

br = mechanize.Browser() # Make our browser-object
base_url = "http://toolsfordatascience.wordpress.com/"

br.open(base_url)

# Show the html
print(br.response().read())
print("\n")

# Show the title
print("Title: {}\n".format(br.title()))
