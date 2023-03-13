import json
from script import createHtmlFile
def main():
    json_data=""
    with open('content.json') as json_file:
        json_data = json_file.read()
        content= json.loads(json_data)
        json_file.close()
    
    counter = 0
    print(content["Sprinting"].keys())
    for objects in content:
        
        createHtmlFile(content[objects])
        counter+=1
    with open("log.txt", 'a') as f:
        f.write(json.dumps(content))
        f.write("\n")
        f.close()
    with open('content.json', 'w'):
        print("uhoh")
        #f.write()


main()