import wikipedia as wp

wp.set_lang("en")
query = "Atos"
print(wp.search(query, results = 5))

page_object = wp.page(query)

print(wp.summary(query))
 
# # # printing html of page_object
# print(page_object.html)

# # # printing title
# print(page_object.original_title)
 
# # printing links on that page object
# print(page_object.links[0:10])