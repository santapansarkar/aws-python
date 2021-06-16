import json

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

def json_navigate():
    with open('example_package.json','r') as json_file:
        contents = json.load(json_file)
        #json_string = json.loads(contents)
        #first_key = json_string['dependencies']
        #code_name = json_string['name']
        #nested_dict = json_string['scripts']['test']
        #lic_details = json_string['license']
        #return nested_dict,lic_details,first_key,code_name
        #return contents['name']
        return contents['scripts']['test']



if __name__=="__main__":
    json_input = json.loads(json_string)
    json_output = json.dumps(json_input, indent=2)
    #print(json_output)
    #output = json_navigate()
    kwargs = json_navigate()
    print(kwargs)