__author__ = "tbsexton"
"""
This parses the .html file containing your jupyter-nbconvert
reveal presentation to allow img html tags after nbconvert.

Note that this will search for anything matching '&lt; img(.*)&gt;' in the
index.html slides file
"""

import re

pattern = re.compile("&lt;img(.*)&gt;")
# pattern = re.compile("<img(.*)>")  # for bugfix
with open('index.html', "r") as htmlfile:
    htmltext = htmlfile.read()


imgs = re.findall(pattern, htmltext)
# try len(imgs)>0:
for i in imgs:
    htmltext=re.sub("&lt;img"+i+"&gt;",  "<img"+i+">", htmltext)
    # htmltext.replace("&lt;img"+i+"&gt;", "<img"+i+">")
    print "&lt;img"+i+"&gt;"+" [[replaced with]] "+"<img"+i+">"

imgs = re.findall(pattern, htmltext)
print "there are now ", len(imgs), "incorrect img tags!"

with open('index.html', "w+") as f:
    f.write(htmltext)
