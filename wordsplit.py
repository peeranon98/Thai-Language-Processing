from collections import Counter
#raw = open('in.txt')
#text = raw.read()
dictionary = open('dict.txt')
dics = dictionary.read()
dic = dics.split()
print(f"Dictionary : {dic}")
def wordsplit(text):
    out = []
    words = text.split()
    #print(f"Here is variable words {words}\n")
    for word in words:
        if word in dic:
            #print(f"Word {word} is found\n")
            out.append(word) 
        else : 
            check = word
            search = True
            preout = []
            while search:
                #print(f"Here is variable check {check}")
                if check in dic :
                    #print(f"{check} in dic\n")
                    preout.append(check)
                    start = word.find(check)
                    check = word[start+len(check):]
                    continue
                elif check == "":
                    #print(f"End checking for line {word}\n")
                    break
                else :
                    #print(f"{check} is not in dict")
                    check = check[0:-1]
                    continue
            for rem in preout :
                start = word.find(rem)
                end = start + len(rem)
                word = word[0:start]+word[end:]
                out.append(rem)
                preout.remove(rem)
            out.append(word)
    #print(f"From input: '{text}'")
    return out
if __name__ == '__main__':
    text = input("Input text : ")
    splited = wordsplit(text)
    print(splited)