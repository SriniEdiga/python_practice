str1 = "Exa"
str2 = "Thought"


str = str1+" / "+str2

print(str1+str2)                             #Concatination of String
print(str)


#predefined methods in String

print(str.upper())                           #Converts to uppercase
print(str.lower())                           #Converts to lowercase

print(len(str))                              #Gives the length of the Srting

print(str.split("/",-1))
print(str.split("/")[0])
print(str.split("/",)[-1])                   #splits based on index and sring given

strex = "    Exa      Thought   "
print(strex.strip())                         #neglate the spaces around the string

print(str.replace("Thought","Docs"))         #replace the particular string

ex = "My name is Srinivas N, and this is My name"
ex1 = str1+str2

print(ex.capitalize())                     #Convert first letter into capital
print(ex1.center(20,"*"))                  #gives the String in center with filling the extra place with provided string 

print(ex.count("My",7,40))                 #count how many times particular string is repeated
print(ex.find("Srinivas"))                 #use to find the index position of gibven string
print(ex.endswith("name"))                 #check weather the string is ending with given string

#index()                  #Gives the index position of particual string
#isalnum()                #check weather the string is alphanumeric
#isalpha                  #check weather the si=tring is alphabetic
#isdecimal()              #check the given strig is decimal
#isdigit                  #check the given string is numbers
#isidentifier             #check given string is idnetifier rules
#islower                  #check weather the string is lower 
#isnumeric                #check string is numeric


s = "Srinivas"
output = s[::-1]
print(output)


