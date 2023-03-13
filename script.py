import os
from jinja2 import Template
import json
import random

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
				<li><a href="#">About</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
			
		    </nav>
	    </header>
        <main>
        <p>By: {{author}}</p>
        {{body}}
        </main>
        <footer></footer>
    </body>
</html>
"""
    body_template="""
    <article>
        <h2>{{heading}}</h2>
        <p>{{text}}</p>
    </article>
    """


    #set up everything else
    with open('names.json') as json_file:
        names= json.load(json_file)

    author=names["first_names"][random.randrange(40)]+" "+names["last_names"][random.randrange(40)]

    #input file
    data = inputJson
    #pretty sure its a dict not json
    strbuilder=""
    bodyT= Template(body_template)

    #loop through every heading
    #print(data)
    for i in data["content"]:

        strbuilder+=bodyT.render(i)+"\n"
    data['body']=strbuilder



    outputFile = Template(html_template)

    def createFileName(input_json,ext):
        fileName  = input_json["title"]
        fileName=fileName.replace(" ","")
        fileName = ''.join([i for i in fileName if i.isalnum()])
        fileName="./website/"+fileName+ext
        print(fileName)

        return fileName

    #write to file
    output_directory=createFileName(data,".html")
    print(output_directory)
    with open(output_directory, "w") as output:
        output.write(outputFile.render(data))
        output.close()
    with open("website_list.txt","a") as output:
        output.write(output_directory)
        output.write("\n")
        output.close()

