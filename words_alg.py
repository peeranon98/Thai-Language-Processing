# V2
from collections import Counter
raw = open('in.txt') # Get input string
text = raw.read()
words = text.split() # Get phrases from split input with space
dictionary = open('dict.txt')
dics = dictionary.read()
dic = dics.split()
print(f"Dictionary : {dic}")
out = []
rem = []
print(f"Here is variable words {words}\n")
for word in words:
    if word in dic: # check if the phrase with dictionary
        print(f"Word {word} is found\n")
        out.append(word) # if it's in dictionary keep it in the list
    else : 
        check = word # check phrase start with full phrase
        #preout = [] 
        #search = True
        while True:
            #check += word[i]
            print(f"Here is variable check {check}")
            if check in dic :
                print(f"{check} in dic\n")
                out.append(check) # if word from phrase is in dictionary keep it in the list
                start = word.find(check)
                check = word[start+len(check):] # move first letter of checking word to after the last letter of previos found word
                continue
            elif check == "": # no more letter in phrase
                print(f"End checking for line {word}\n")
                break
            else :
                print(f"{check} is not in dict")
                check = check[0:-1] # shorten the check word one by one from the last character
                continue
print(f"From input: '{text}'")
output = dict(Counter(out))
print(f"We have {output}")
