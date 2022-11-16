# dict

import json
person_string = '{"name":"Ali","languages":["python","c#"]}'
person_dict = {"name":"ali","languages":["python","c#"]}

# open("person.json","x")

# json string to dict

# result = json.loads(person_string)      # json.loads()  string veriyi dict type'ine cevirir

#result = result["name"]

#result = result["languages"][0]

# with open("person.json") as f :         # json.load()   dosyanin icinden bilgileri okur ve ekrana yazdirir
#     data = json.load(f)
#     print(data["name"])


# dict to json string


#
# result = json.dumps(person_dict)           #  json.dumps() dict veriyi json string veriye cevirir


# with open("person.json","w") as file:
#     file.write("")

# with open("person.json","w") as file:        #  json.dump() dict bir veriyi json dosyasinin icine w modu ile yazdik
#     json.dump(person_dict,file)                    #    once atilacak dict veri yazilir sonra file



# person_dict = json.loads(person_string)
# result = json.dumps(person_dict,indent=4,sort_keys=True)         #  okunabilirligi artirmak icin kullanilir
# print(person_dict)
# print(result)









