import os
import json
import urllib
import requests
import random
import time
from urllib.request import urlopen


def bingSearch(keyword):
    print("Searching Bing with keyword: "+keyword)
    start_time = time.perf_counter()
    try:
        numResults = 5
        bing_apikey = os.environ["eee"]
        search_url = "https://api.bing.microsoft.com/v7.0/images/search"
        header = {"Ocp-Apim-Subscription-Key":bing_apikey}
        params = {
            "q":keyword.strip("\n"),
            "count":numResults,
            "license":"ShareCommercially"
            }
        response= requests.get(search_url,headers = header,params=params)
        img_dict = json.loads(response.text)
        #print(json.dumps(img_dict))
        finalImg= img_dict["value"][random.randint(0,numResults-1)]
        url = finalImg["contentUrl"]
        img_path = "images/"+finalImg["imageId"]+(url[-4:]).lower()
        pypath = "website/"+img_path #bc its outside the websites folder
        with open(pypath, 'wb') as handler:
            img = requests.get(url)
            handler.write(img.content)
        output_data = {
            "name": img_path,
            "height":finalImg["height"],
            "width":finalImg["width"]
        }
    except:
        print("No Image found. Defaulting to Logo")

        #bascially useless you should just return name
        output_data = {
            "name":"images/how-do-i-logo.png",
            "height":1500,
            "width":2000

        }
    end_time = time.perf_counter()
    print(f"Image retrieved in  {end_time-start_time:0.4f} seconds")
    return output_data
    
#p much deprecated
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
        img_path = "images/"+api_result["hits"][0]["user"][:1]+str(api_result["hits"][0]["id"]*api_result["hits"][0]["user_id"])+(url[-4:]).lower()
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
