'''
TODO
-create tags for related things
-space paragraphs out
-try except everything.
-update names json, reduce total names while maintaining a healthy gender ratio
-improve image search so that images are more relavant to the article content/title
-SEO optmization: more internal links, more coherent titles
-fix formatting so that there are no replacement characters in html -i think something something utf 8 not iso-~~~~
3-20-23 MOSTLY DONE -make text section a little less redundant ( stop restating topic), make it more relatvant with past info) 
'''
import json
import time
import openai
import os

def main(numAttribute,fileLoc):
    print(time.time())
    path = fileLoc+"rewrite/topics.json"
    with open(path) as f:
        topicDict = json.loads(f.read())
    total_topic_count = len(topicDict["Topics"])
    failure_count = 0

    #loop through each topic from topics.json
    for i in range(total_topic_count):
        current_topic = topicDict["Topics"][i]["title"]
        print("INFO: Generating Topic "+str(i+1)+"/" +str(total_topic_count)+": "+current_topic)
        start_time = time.perf_counter()
        getWebsiteJson(current_topic,numAttribute)
        end_time=time.perf_counter()
        print("INFO: "+current_topic+f" completed in {end_time-start_time:0.4f} seconds")
        '''try:
            start_time = time.perf_counter()
            getWebsiteJson(current_topic,numAttribute)
            end_time=time.perf_counter()
            print("INFO: "+current_topic+f" completed in {end_time-start_time:0.4f} seconds")
        except:
            print("WARNING: Failed to create "+current_topic+". Moving on...")
            failure_count+=1'''
def getWebsiteJson(topic,attributes):
    print("INFO: Webspage content creation for "+topic+" initialized")
    
    
    #get the json layout
    start_time = time.perf_counter()

    requestMsg="As a skilled JSON writer,  your task is to create a JSON file that is both informative and engaging on the topic given to you. The JSON file should be optimized for search engine efficiency, using keywords and phrases that are relevant to the topic. To accomplish this, you will need to incorporate research and data into the file to support the contents. Each section should be broken down into clear headings to make it easier for readers to navigate.\nThe JSON file should adhere to the following structure:\n{\"(x)\": {\"title\": \"(x)\",\"author\": \"leave blank\",\"content\": [{\"heading\":\"(x)\",\"text\": \"leave blank\"}]}}\nYour task is to replace the '(x)' values with an appropriate name based on the topic provided, and generate a specific number of content attributes. Make sure that you do not change any value that is equal to 'leave blank'. Ensure the title and headings are descriptive and add purpose to the JSON file. Make sure the 'text' is left blank. Do not include anything other than the json file. Also, ensure that the final 'content' attribute is titled 'Conclusion'. Topic:"+ str(topic)+". Attributes:"+ str(attributes)
    jsonFrame = json.loads(apiCall({"role":"user","content":requestMsg}))
    
    

    #start filling in the empty text
    requestMsg="You are hired to write a subheading for a website. The topic and sub-heading title, and previous sub-heading titles are provided. Write engaging, informative, and well-written content that is relevant to the website's topic, tailored to the audience's language, tone, and style. Use research and data to support your writing. Attempt to write so that the content fits the website's broader narrative, and keep it interesting by including anecdotes or a compelling narrative. Don't restate the sub-heading title at the start of your response no matter what. Ensure that the introduction is minimized. Ensure the response is of an appropriate length.  Do not add the word 'subheading' at the start of the response. Your goal is to make the sub-heading interesting and encourage readers to explore more of the website's content.\n"
    previousTitles= []
    jsonFrameTitle=jsonFrame[list(jsonFrame.keys())[0]]
    for i in range(len(jsonFrameTitle["content"])):
        tstart_time = time.perf_counter()
        currentheading = jsonFrameTitle["content"][i]
        headingTitle = currentheading["heading"]
        requestMsg+="Topic: "+topic+". Subheading: "+headingTitle
        currentheading["text"]=apiCall({"role":"user","content":requestMsg})
        previousTitles.append(currentheading["heading"])
        tend_time = time.perf_counter()
        print(f"INFO: Api response received in {tend_time-tstart_time:0.4f} seconds")
    end_time = time.perf_counter()
    print("INFO: Webpage: '"+topic +f"' content created in {end_time-start_time:0.4f} seconds")
    return jsonFrame
    
def apiCall(input):
    
    openai.api_key = os.environ["yuh"]
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [input]
    )
    end_time = time.perf_counter()   
    print("INFO: Api response received")
    
    return vars(response)['_previous']['choices'][0]['message']['content'] #dict version instead of OpenAIObject
main(5,"C:/Users/zbria/Desktop/howdoi/")