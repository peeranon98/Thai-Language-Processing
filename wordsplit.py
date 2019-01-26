from collections import Counter
#raw = open('in.txt')
#text = raw.read()
dictionary = open('TWC_Dict.txt')
dics = dictionary.read()
dic = dics.split()
#print(f"Dictionary : {dic}")
def wordsplit(text):
    out = []
    words = text.split()
    #print(f"Here is variable words {words}\n")
    for word in words:
        if word in dic:
            #print(f"Word {word} is found\n")
            out.append(word) 
        else : 
            
            search = True
            preout = []
            check = word
            found = False
            while check!="":
                if found :
                    check = word
                #print(f"Here is variable check {check}")
                if check not in dic :
                    #print(f"{check} is not in dict")
                    check = check[0:-1]
                    found = False
                    continue
                elif check in dic :
                    #print(f"{check} in dic\n")
                    preout.append(check)
                    start = word.find(check)
                    word = word[start+len(check):]
                    #print(f"Start+len {start+len(check)}")
                    found = True
                    pass
                elif check == "":
                    #print(f"End checking for line {word}\n")
                    break

                
                #print(f"Here {preout}")

            t = 0
            while preout != []:
                #print(f"rem is {rem}")
                rem = preout[t]
                start = word.find(rem)
                end = start + len(rem)
                word = word[0:start]+word[end:]
                #print(word)
                out.append(rem)
                preout.remove(rem)
                #t +=1
            if word != "" :
                out.append(word)

    #print(f"From input: '{text}'")
    return out
if __name__ == '__main__':
    text = input("Input text : ")
    splited = wordsplit(text)
    print(splited)
