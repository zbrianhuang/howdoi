import os
from jinja2 import Template
import json
import random
from pixabay import getImg,bingSearch
from pchatapi import apiCall,openAIObjecttoDict
def createHtmlFile(inputJson):
    #define templates
    html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>{{title}}</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
        <header>
		<nav>
			<ul>
				<li><a href="../index.html">Home</a></li>
				<li><a href="../about.html">About</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
			
		    </nav>
	    </header>
        <main>
        <img src="{{img}}">
        <h1>{{title}}</h1>
        <p>By: {{author}}</p>
        {{body}}
        </main>
        <footer>
		<p>All Rights Reserved. &copy; 2023 How Do I. </p>
	</footer>
    </body>
</html>
"""
    body_template="""
    <article id="{{heading}}">
        <h2>{{heading}}</h2>
        <p>{{text}}</p>
    </article>
    """


    #set up everything else
    with open('names.json') as json_file:
        names= json.load(json_file)

    author=names["first_names"][random.randrange(49)]#+" "+names["last_names"][random.randrange(40)]

    #input file
    data = inputJson
    #pretty sure its a dict not json
    strbuilder=""
    bodyT= Template(body_template)

    #loop through every heading
    #print(data)
    for i in data["content"]:

        strbuilder+=bodyT.render(i)+"\n"


    #retrive img data
    imgDict = openAIObjecttoDict( apiCall(2,data['title'],"",""))
    print("test"+json.dumps(imgDict))
    if str(imgDict["content"])[:5] == "genre:":
        try:
            image_loc = bingSearch(str(imgDict["content"])[5:])["name"]          
            
        except:
            image_loc = getImg(str(imgDict["content"])[5:])["name"]
    else:
        try:
            image_loc = bingSearch(str(imgDict["content"]))["name"]
            
        except:
            image_loc = getImg(str(imgDict["content"]))["name"]

    #put everything together
    data['body']=strbuilder
    data['author']=author
    data['img']=image_loc


    outputFile = Template(html_template)

    def createFileName(input_json,ext):
        fileName  = input_json["title"]
        fileName=fileName.replace(" ","")
        fileName = ''.join([i for i in fileName if i.isalnum()])
        fileName="./website/"+fileName+ext

        return fileName

    #write to file
    output_directory=createFileName(data,".html")
    with open(output_directory, "w") as output:
        output.write(outputFile.render(data))
        output.close()
    with open("website_list.txt","a") as output:
        output.write(output_directory)
        output.write("\n")
        output.close()
    with open("website_titles.txt","a") as output:
        output.write(data["title"])
        output.write("\n")
        output.close()
    print("'"+data["title"] +"' successfully created")

