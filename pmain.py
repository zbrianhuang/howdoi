
import json
import time
from pweb_template import createHtmlFile
from pchatapi import getWebsiteJson
#pseudo_main lol
def pmain(attributeNum,topics_list):
    total_start_time = time.perf_counter()
    with open("topics.json") as f:
        topicDict = json.loads(f.read())
    total_topic_count = len(topicDict["Topics"])
    failure_count = 0
    for i in range(total_topic_count):
        
        print("Generating Topic #"+str(i+1)+" out of " +str(total_topic_count)+" topics.")
        current_topic = topicDict["Topics"][i]["title"]
        try:
            start_time = time.perf_counter()
            #topicList=["How to create intricate wire-wrapped bonsai trees"]
            #attributesList=[attributeNum]
            getWebsiteJson(current_topic,attributeNum)
            json_data=""
            with open('content.json') as json_file:
                json_data = json_file.read()
                content= json.loads(json_data)
                json_file.close()


            for objects in content:

                createHtmlFile(content[objects])

            with open("log.txt", 'a') as f:
                f.write(json.dumps(content))
                f.write("\n")
                f.close()
            with open('content.json', 'w') as f:
                print("data in 'content.json' successfully deleted")
                f.write("{}")

            end_time=time.perf_counter()
            print(f"Completed in {end_time-start_time:0.4f} seconds")
        except:
            print("Failed to create "+current_topic+". Moving on...")
            failure_count+=1
    total_end_time=time.perf_counter()
    print("\n\n\nFailures:"+str(failure_count))
    print(str(total_topic_count-failure_count)+"/"+str(total_topic_count)+" pages with "+str(attributeNum)+f" attributes completed in {total_end_time-total_start_time:0.4f} seconds")
    
