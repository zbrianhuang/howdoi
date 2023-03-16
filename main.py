import json
import time
from script import createHtmlFile
from chatapi import getWebsiteJson
def main():
    start_time = time.perf_counter()
    topicList=["Car myths debunked"]
    attributesList=[8]
    getWebsiteJson(topicList[0],attributesList[0])
    json_data=""
    with open('content.json') as json_file:
        json_data = json_file.read()
        content= json.loads(json_data)
        json_file.close()
    
    counter = 0
    for objects in content:
        
        createHtmlFile(content[objects])
        counter+=1
    with open("log.txt", 'a') as f:
        f.write(json.dumps(content))
        f.write("\n")
        f.close()
    with open('content.json', 'w') as f:
        print("data in 'content.json' successfully deleted")
        f.write("{}")

    end_time=time.perf_counter()
    print(f"Completed in {end_time-start_time:0.4f} seconds")
main()