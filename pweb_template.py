import os
from jinja2 import Template
import json
import random
from pixabay import getImg
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

        image_loc = getImg(str(imgDict["content"])[5:])["name"]
    else:
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


tempjson={
        "title": "All You Need to Know About the Horseshoes Game",
        "author": "leave blank",
        "content": [
            {
                "heading": "Introduction to Horseshoes",
                "text": "Horseshoes is a classic lawn game that has been enjoyed by millions of people around the world. This game involves tossing horseshoes towards a metal stake, with the aim of getting it as close as possible to the stake. The game is simple, yet challenging, and can be enjoyed by people of all ages and skill levels."
            },
            {
                "heading": "The History of Horseshoes",
                "text": "The history of horseshoes can be traced back to ancient Greece, where it was believed to have been played by soldiers. It is said to have been brought to the United States during the 19th century, where it gained widespread popularity. Today, the game is played in backyards, parks, and even professional leagues around the world."
            },
            {
                "heading": "How to Play Horseshoes",
                "text": "To play horseshoes, you need two metal stakes and four horseshoes. The stakes should be placed 40 feet apart. Players then take turns tossing horseshoes towards the opposite stake, with the aim of getting them as close as possible. Points are awarded depending on how close the horseshoe is to the stake."
            },
            {
                "heading": "Horseshoes Strategy",
                "text": "To be successful at horseshoes, players need to develop a solid strategy. This includes things like choosing the right horseshoe, aiming for specific parts of the stake, and adjusting for wind and other environmental factors. The best way to develop a winning strategy is through practice and experience."
            },
            {
                "heading": "Horseshoes Equipment",
                "text": "To play horseshoes, you need several pieces of equipment. This includes horseshoes, metal stakes, and a throwing area. Horseshoes are made from various materials, including steel, aluminum, and plastic. It is important to choose the right horseshoe for your skill level and playing style."
            },
            {
                "heading": "Horseshoes Rules and Variations",
                "text": "There are several variations of horseshoes, each with their own set of rules. Some popular variations include classic horseshoes, quoits, and ring toss. It is important to familiarize yourself with the rules of the specific variation you are playing before beginning a game."
            },
            {
                "heading": "Conclusion",
                "text": "Horseshoes is a fun and challenging game that can be enjoyed by players of all ages and skill levels. Whether you are playing at a backyard BBQ or in a professional league, horseshoes is sure to provide hours of entertainment. So why not give it a try and see for yourself how much fun it can be?"
            }
        ]
    }

