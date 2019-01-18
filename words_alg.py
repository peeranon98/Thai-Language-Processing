# Version1 shortest word first
from collections import Counter
raw = open('in.txt') # get input from text file
text = raw.read()
words = text.split() # separate textfile with space and assign to list
dictionary = open('dict.txt') # read mock-up dictionary ** Further update needs for full Thai dictionary **
dics = dictionary.read()
dic = dics.split()
print(f"Dictionary : {dic}")
out = []
rem = []
print(f"Here is variable words {words}\n")
for word in words:
    if word in dic: # choose phrase to compare with dictionary
        print(f"Word {word} is found\n")
        out.append(word) # if phrase in dictionary add it to out put
        #words.remove(word)
        #print(f"Here is variable words {words}\n")
    else : 
        check = "" # for comparing word to dictionary start with empty string
        for i in range (len(word)):
            check += word[i] # expand the word one character at a time
            print(f"Here is variable check {check}")
            if check in dic : # if the word is in dict add it to output
                print(f"{check} in dic\n")
                out.append(check) 
                start = word.find(check)
                word = word[start:] # change the phrase to continue searching
                check = ""
                continue
            else :
                continue

print(f"From input: '{text}'")
output = dict(Counter(out))
print(f"We have {output}")
