# from pprint import pprint
# a=[letter for letter in range(1,11)]
# #print(a)
# b=[letter for letter in range(11,21)]
# #print(b)
# c=[letter for letter in range(21,31)]
# #print(c)
# d={"a":a,"b":b,"c":c}
# pprint(d)

# from pprint import pprint

# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# pprint(d)
# print(d["b"][2])

#d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# for key,value in d.items():
#     if key=="a":
#         print(key," has value ",value)
#     elif key=="b":
#         print(key," has value ",value)
#     else:
#          print(key," has value ",value)

# import string
# import string
# for letter in string.ascii_lowercase:
# print(letter)

# def accelerate(v1,v2,t1,t2):
# a=(v2-v1)/(t2-t1)
# return a
# def string():
#     str=input("Sring name")
#     strsplit=str.split(" ")
#     length=strsplit.__len__()
#     return length
# print(string())
# import re
# def string():
#     with open("words2.txt","r") as myfile:
#         string=myfile.read()
#         strsplit=re.split(",| ",string)
#         length=len(strsplit)
#         return length
# print(string())

# import math
# print(math.pow(2,3))
# import string
# with open("words3.txt","w") as myfile:
#     for alphabets in string.ascii_uppercase:
#         myfile.write(alphabets+"\n")

# a = [1, 2, 3]
# b = (4, 5, 6)
# c=list(b)
# print(c)
# for num1,num2 in zip(a,b):
#     print(num1+num2)
# import string
# with open("word4.txt","w") as myfile:
#     for letter1,letter2 in zip(string.ascii_lowercase[0::2],string.ascii_letters[1::2]):
#         myfile.write(letter1+letter2+"\n")


# import string
# letters = string.ascii_lowercase + " "

# slice1 = letters[0::3]
# slice2 = letters[1::3]
# slice3 = letters[2::3]
# with open("word5.txt","w") as myfile:
#     for letter1,letter2,letter3 in zip(string.ascii_lowercase[0::3],string.ascii_letters[1::3],string.ascii_letters[2::3]):
#         myfile.write(letter1+letter2+letter3+"\n")

# import string,os
# os.makedirs("letters")
# for letter in string.ascii_lowercase:
#     with open("letters/"+letter+".txt","w") as file:
#         file.write(letter+"\n")

# import glob
# letters=[]
# check="python"
# name=glob.glob("letters/*.txt")
# for file in name:
#     with open(file,"r") as myfile:
#         letter=myfile.read().strip("\n")
#     if letter in check:
#         letters.append(letter)

# print(letters)

# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" % firstname, secondname)

# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smith"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}
# d["employees"].append(dict(firstName="Albert",lastName="Bert"))

# print(d)
# import json
# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smith"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}
# with open("company1.json","w") as m:
#     json.dump(d,m,indent=4)

# import json
# from pprint import pprint
# with open("company1.json","r") as m:
#     data=json.load(m)
#     pprint(data)

# import json

# with open("company1.json","r+") as myfile:
#     d=json.loads(myfile.read())
#     d["employees"].append(dict(firstName="Albert",lastName="Bert"))
#     myfile.seek(0)
#     json.dump(d,myfile,indent=4)
#     myfile.truncate()

# a = [1, 2, 3]
# for b,c in enumerate(a):
#     print("item ",c," has index ",b)

# while True:
#     print("Hello")

# import time
# while True:
#     print('Hello World!')
#     time.sleep(2)

# import time
# i=0
# while True:
#     i=i+1
#     print( 'Hello World!')
#     time.sleep(i)

# import time
# for i in range(0,5):
#     if i<=3:
#         print("Hello")
#         time.sleep(i)
#     else:
#         print("End of Loop")
#         break

# import time
# i=0
# while True:
#     print("Hello")
#     i=i+1
#     if i>3:
#         print("End of Loop")
#         break
#     time.sleep(i)

# while True:
#     print("Hello")
#     if 2>1:
#         pass
#     print("Hi")

# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# name=input("Enter word")
# if name in d.keys():
#     print(d[name])

# from os import name


# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# name=input(" Enter word ")
# if name in d.keys():
#     print(d[name])
# else:
#     print("The word doesnot exists!")

# import requests
# response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
# text = response.text
# print(text)


# import requests
# response=requests.get("http://www.pythonhow.com/data/universe.txt")
# text=response.text
# count=text.count("a")
# print(count)

# import webbrowser
# string=input(" Please enter the word you want to search ")
# webbrowser.open(string)

# import webbrowser

# url = 'https://pythonexamples.org'
# chrome_path="C:\\Users\\anjali bajaj\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe %s"
# webbrowser.get(chrome_path).open(url)

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5


long_time()
