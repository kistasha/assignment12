# importing requests
import requests

# performing a get request to retrieve the contents
r = requests.get("https://gsom.spbu.ru/en/")
# converting content to string
content = r.content.decode('utf-8')
# counting all .png occurences on the webpage and printing the result out
png_count = content.count('.png')
print()
print(f'Number of png images found on the page: {png_count}')
print()

# looking for the first occurence of .png
first_png = content.find('.png')

# using method rfind() to search for the opening quote " backward (before the png part of the url)
# it will be searching for it in the range from 0 to find_png
link_start = content.rfind('"',0,first_png)
link_start += 1 # just skipping the quote in the url

# now, looking for the position of the closing " at the end of the url
link_end = content.find('"',first_png) 

# now, we can combine it all in one url 
# slicing the string between link_start and link_end to get the url
url = content[link_start:link_end]
# adding the given address to the beginning of the link
url = "https://gsom.spbu.ru" + url

print(f"First png URL: {url}")
print()

# time to steal it... 
# just saved it the exact same way we did in class
image= requests.get(url)
with open('/home/jovyan/Homework12/gsom.png','wb') as f:
    f.write(image.content)

print("You've successfully stolen some of GSOM's intellectual property:)")
print()