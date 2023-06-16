
# a = 10
# b = "Hello"

# print(type(a),id(a),a,sep='\t')
# print(type(b),id(b),b,sep='\t')

# # define a function
# def foo_function(x=0,y=0):
#     pass        # no op

# # calling a python function
# foo_function()


# def add_two(x,y):
#     return x+y

# # call the function with two arguments
# print(add_two(5,4))


# #creating a class
# class class_foo:
#     pass

# Classx = class_foo()


# from os import environ
# from os import name

# def is_windows():

#     if name == 'nt':
#         from dotenv import load_dotenv 
#         load_dotenv()

# def get_env_var(env_var):
#     return environ[env_var]

# is_windows()

# #do something with a different variable since my env doesn't define $AUTHOR
# if "LOGNAME" in environ:
#     print(get_env_var("LOGNAME"))


# python while loop

# counter = 0
# while counter < 5:
#     print(f'Count is {counter}')
#     counter+=1


# counter=0
# while True:
#     print(f'Counter is:\t{counter}')
#     # requires an exit condition or the loop will not end
#     # ctrl-c to stop
#     if counter == 10: break
#     counter+=1


# #for loop

# for each in range(1,5):
#     print(f'{each}')



# #for loop with iterable
# from os import environ
# counter = 1
# for each in environ:
#     #walks over the system environment variable
#     print(f'{each}')
#     counter+=1
# print(f'{counter} variables exist.')


# if False:       # initial conditional
#     print('I’m True')
# elif True:      # after True test a conditional
#     print("I'm Another Test")
# else:
#     print("I'm False")



# Python if statements

# if False:
#     print('I"m True')
# else:
#     print('False branch of initial conditional test')


# a=1
# b=2
# if a==b:
#     print("Values are equal")
# else:
#     print("Values are not equal")


# fruit = ['apples','Bananas','cherries']
# print(fruit)
# #append
# fruit.append('plums')
# print(fruit,"append")

# #insert
# fruit.insert(0,'blueberries')
# print(fruit,"insert")

# #delete an item
# del fruit[0]
# print(fruit,'delete')

# #remove and remove last values
# v=fruit.pop()
# print(fruit,'pop last item')


# fruit = ['apples','Bananas','cherries']
# print(fruit)

# #modify
# fruit[1] = 'kiwi'
# print(fruit,"modified")


# # list comprehension
# numbers = [each*each for each in range(10)]
# print(numbers)


# #dictionaries
# cars ={"red":"toyota","blue":"honda","white":"ford","green":"tesla"}
# for key, value in cars.items():
#     print("Key",key,"Value",value,sep='\t')



# # adding a key-value pair
# cars ={"red":"toyota","blue":"honda","white":"ford","green":"tesla"}
# cars['orange'] = 'chevy'

# for key, value in cars.items():
#     print("Key",key,"Value",value,sep='\t')


# # delete a pair from the dictionary
# cars ={"red":"toyota","blue":"honda","white":"ford","green":"tesla"}
# cars['orange'] = 'chevy'
# #delete
# del cars['red']
# for key, value in cars.items():
#     print("Key",key,"Value",value,sep='\t')



# # delete a pair from the dictionary
# cars ={"red":"toyota","blue":"honda","white":"ford","green":"tesla"}
# cars['orange'] = 'chevy'
# #delete
# del cars['red']
# #modify
# cars['blue'] = 'acura'
# for key, value in cars.items():
#     print("Key",key,"Value",value,sep='\t')


#JSON data
import json

#functions
def write_json_file(FILENAME,DATA):
    with open(FILENAME,"w") as json_data:
        json.dump(DATA,json_data)
    print("{} file written".format(FILENAME))
    print("*"*40)
    return

def read_json_file(FILENAME):
    with open(FILENAME,"r") as json_data:
        data = json.load(json_data)
        print("{} file read",format(FILENAME))
        print("*"*40)
        return data

def display_json_data(JSON_DATA):
    INDENT=4
    print(F'{json.dumps(JSON_DATA,indent=INDENT)}')

#create a JSON structure

data = {}
data['person'] =[]
data['person'].append({'name':'Jarod','address':'1 san jose', 'phone':["555-555-5555 x100","555-555-5555 p"]})
data['person'].append({'name':'Jacob','address':'2 san jose', 'phone':["555-555-5555 x101","555-555-5554 p"]})
data['person'].append({'name':'Sally','address':'1 modesto', 'phone':["555-555-5553 x101","555-555-5553"]})

#json data can be string dump
display_json_data(data)

# serialize to a file
FileName ="json_example.json"
write_json_file(FileName,data)

#deserialize the json file
FileName ="json_example.json"
json_file=read_json_file(FileName)

#print(json_file)
display_json_data(json_file)


for person in json_file["person"]:
    if person["name"] == "Sally":
        print("Found:",person["name"],sep="\t")
        print(person["address"])
        print(person["phone"])
