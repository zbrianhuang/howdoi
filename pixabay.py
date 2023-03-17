import os
import json
import urllib
import requests
from urllib.request import urlopen
def getImg(keyword):
    print("Searching for Image")
    api_key = os.environ["ay"]
    url = "https://pixabay.com/api/?key="+api_key+"&q="+urllib.parse.quote(keyword)
    print(url)
    try:
        with urlopen(url) as response:
            unparsed = response.read()
        api_result = json.loads(unparsed)
        print(api_result["hits"][0])
        url=api_result["hits"][0]["largeImageURL"]
        img_path = "images/"+api_result["hits"][0]["user"][:1]+str(api_result["hits"][0]["id"]*api_result["hits"][0]["user_id"])+url[-4:]
        pypath = "website/"+img_path #bc its outside the websites folder
        with open(pypath, 'wb') as handler:
            img = requests.get(url)
            handler.write(img.content)
        output_data = {
            "name":img_path,
            "height":api_result["hits"][0]["imageHeight"],
            "width":api_result["hits"][0]["imageWidth"]
        }
        print("Image found and written to "+img_path)
    except:
        print("No Image found. Defaulting to Logo")

        #bascially useless you should just return name
        output_data = {
            "name":"images/how-do-i-logo.png",
            "height":1500,
            "width":2000

        }
    return output_data
#print(getImg("Automotive"))