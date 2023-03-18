import os
import json
import openai
import time
#sends request to openai api
def apiCall(mode,title,attributeNum,heading):
    
    openai.api_key = os.environ["yuh"]

    mode0="As a skilled JSON writer,  your task is to create a JSON file that is both informative and engaging on the topic given to you. The JSON file should be optimized for search engine efficiency, using keywords and phrases that are relevant to the topic.\nTo accomplish this, you will need to incorporate research and data into the file to support the contents. Each section should be broken down into clear headings to make it easier for readers to navigate.\nThe JSON file should adhere to the following structure:\n{\n    \"(x)\": {\n        \"title\": \"(x)\",\n        \"author\": \"leave blank\",\n        \"content\": [\n            {\n                \"heading\": \"(x)\",\n                \"text\": \"leave blank\"\n            }\n        ]\n    }\n}\nYour task is to replace the \"(x)\" values with an appropriate name based on the topic provided, and generate a specific number of content attributes.\nMake sure that you do not change any value that is equal to \"leave blank\".\nEnsure the title and headings are descriptive and add purpose to the JSON file.\nAlso, ensure that the final \"content\" attribute is titled \"Conclusion\".\nTopic:"+ str(title)+" \nAttributes: "+str(attributeNum)+"}"
    mode1="You are hired to write a subheading for a website. The topic and sub-heading title are provided. Write engaging, informative, and well-written content that is relevant to the website's topic, tailored to the audience's language, tone, and style. Use research and data to support your writing. Ensure that the content fits the website's broader narrative, and keep it interesting by including anecdotes or a compelling narrative. Don't restate the sub-heading title at the start of your response. Write at least 250 words. Ensure that the introduction is minimized. Your goal is to make the sub-heading interesting and encourage readers to explore more of the website's content.\nTopic: "+title+" Subheading: "+heading
    mode2 = "Only responding with the answer and without punctuation, find the most important noun in the following phrase: "+title
    Request_msgs=[
    {"role":"user","content":mode0},
    {"role":"user","content":mode1},
    {"role":"user","content":mode2}
    ]
    start_time = time.perf_counter()
    response = openai.ChatCompletion.create(
    
      model="gpt-3.5-turbo",
      messages=[
      #  
        Request_msgs[mode]
      ],
        
    )
    end_time = time.perf_counter()
    if mode==1:
      print(heading+f" created in {end_time-start_time:0.4f} seconds")
    elif mode==0:
      print(title+f" layout created in {end_time-start_time:0.4f} seconds")
    elif mode==2:
      print("image keyword about "+title+f" created in {end_time-start_time:0.4f} seconds")
    return response
def openAIObjecttoDict(input):
    buffer =json.loads(str(input['choices'][0]['message']))
    return buffer
def getWebsiteJson(topic,attributes):
  print("Website creation for "+topic+" initialized")
  start_time = time.perf_counter()
  result = apiCall(0,topic,attributes,"")

  #start of bad code
  content_msg=  openAIObjecttoDict(result)["content"]

  with open("gpt_output.json","w") as f:

     f.write(content_msg)

  with open('gpt_output.json') as json_file:
      gpt_data= json.loads(json_file.read())
      json_file.close()
  print(gpt_data.keys())
  #end of bad code
  gpt_data=json.loads(openAIObjecttoDict(result)["content"])
  counter = 0
  for objects in gpt_data:
      json_title = gpt_data[objects]["title"]
      counter+=1
      for i in range(len(gpt_data[objects]["content"])):
          subheading = gpt_data[objects]["content"][i]["heading"]
          request = apiCall(1,json_title,0,subheading)
          gpt_data[objects]["content"][i]["text"]=openAIObjecttoDict( request)["content"]
      with open("content.json","w") as f:

          f.write(json.dumps(gpt_data))
  print(str(counter)+" attributes")
  end_time = time.perf_counter()
  print("Website about "+topic +f" created in {end_time-start_time:0.4f} seconds")


