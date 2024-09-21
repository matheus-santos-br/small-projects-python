
from PyDictionary import PyDictionary 
  
dict = PyDictionary() 

while True:
    word = input("Enter your word: ")

    if(word == ""):
        break

    meaning = dict.meaning(word) 
    print(meaning) 

#print(dictionary.meaning(word))

##def main():
##    word_dic = {
##        "hi": "Way of greeting",
##        "eyes" : "Organ for seeing",
##        "Earth" : "Planet in space"
##    }
##
##    while(True):
##
##        word = input("Enter a word: ")
##
##        if(word == ""):
##            break
##        if word in word_dic:
##            print(F"{word}: {word_dic[word]}")
##        
##main()

    