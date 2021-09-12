
def data_types():    
    some_string = 'Hello Python for AWS'
    some_integer=10
    some_float=10.5
    some_list=['Hello','From','Python','For','AWS']
    some_dictionary={'Language':'Python','Platform':'AWS'}
    some_tuple =('Hello','From','Python','For','AWS')
    print (f'This is Santapan and \t I would like to say \n{some_string}')
    print (some_integer)
    print (some_float)
    print (some_list)
    print (some_dictionary)
    print (some_tuple)


def dict_usage():
    first_dict = {'name':'websrv','env':'dev','compiler':'hugo','language':'markdown'}
    print(first_dict["name"])
    print(f'\tName of the server is {first_dict["name"]} \n\t The website is built using {first_dict["compiler"]}')
    print(f"\tWe will modify our static website and will add dynamic part")
    first_dict["DynamicCompiler"] = "PythonFlask"
    print(first_dict)
    print(f'\tNow we added dynamic website and we built it using {first_dict["DynamicCompiler"]}')
    print('let us delete the static part')
    del first_dict['compiler']
    print(f'current dictionary obejcts are {first_dict}')
    people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

    print(type(people))
    print ('accessing nested dictionary of people\n**********\n************') 
    print(f'age of {people[3]["name"]} is {people[3]["age"]}')
    print("\n***************\nlet's find out who is youngest" )
    for rec in people:
        print(people[1]['age'])


def list_usage():
    first_list = ['webserver','rating server','billing server','license server','database server']
    print(f'Printing list {first_list}')    
    print(f'printing last element of list {first_list[-1]}')
    first_list.append("data proxy server")
    print(f'adding new element into the  list {first_list}')
    first_list.insert(0,'online modules')
    print (f'Final new list is --> {first_list}')
    print(f'\n\t ****************\n\t')
    print(f'\n\t ****************\n\t')
    print('deleteing lemenet from list now.....')
    first_list.remove('online modules')
    print(f'new first list looks like -->\n\t{first_list}')
    data_srv = first_list.pop()
    print(f'fetched data server name from list {data_srv}')
    next_list = [{'server':'web'},{'runtime':'hugo'},{'language':'markdown'}]
    print (next_list) 
    print('accessing next list data\n\t *****************\n\t ')
    print(f'Webserver runtime is {next_list[1]["runtime"]}')
    print(f'Static webpages are wriiiten in {next_list[-1]["language"]} language')




if __name__ == '__main__':
    dict_usage() 
    #list_usage()