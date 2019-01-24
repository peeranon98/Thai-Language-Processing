# var def
vowel = ['ๅ','ุ','ู','ึ','ๆ','ไ','ำ','ะ','ั','ํ','ี','๊','ฯ','โ','็','้','เ','า','.','ฺ','ิ','์','ื','?','ใ']
g1 = "กขคฆ"
g2 = "ง"
g3 = "จฉฌชซศษสฎดฏตฐฑฒถทธ"
g4 = "ญย"
g5 = "ณนรลฬ"
g6 = "บปผพภฝฟ"
g7 = "ม"
g8 = "ว"
g0 = "ฅฃฮอฦฤห"
score = {g0:"0",g1:"1",g2:"2",g3:"3",g4:"4",g5:"5",g6:"6",g7:"7",g8:"8"}
def soundex(word):
    # soundexing
    sd = []
    # 1 keep first letter
    sd.append(word[0])
    for letter in word[1:] :
        # 2 replace vowel with 0
        if letter in vowel :
            sd.append('0')
        elif letter in g0 :
            sd.append(score[g0])
        # 3 score other letter
        elif letter in g1 :
            sd.append(score[g1])
        elif letter in g2 :
            sd.append(score[g2])
        elif letter in g3 :
            sd.append(score[g3])
        elif letter in g4 :
            sd.append(score[g4])
        elif letter in g5 :
            sd.append(score[g5])
        elif letter in g6 :
            sd.append(score[g6])
        elif letter in g7 :
            sd.append(score[g7])
        elif letter in g8 :
            sd.append(score[g8])
        else :
            print(f"Error with {letter}")
    print(f"SD after scoring is {sd}")
    # 4 check next
    #for i in range(len(sd)):
    i = 0
    while i < len(sd):
        try :
            #print(f"{sd[i]} = {sd[i+1]}")
            if sd[i] == sd[i+1] :
                #print(f"pop {sd.pop(i+1)}")
                sd.pop(i+1)
                #print(f"SD after poping is {sd}")
                i-=1
            i += 1
        except IndexError:
            break
        #except :
        #    print("something happended")
    # 5 remove 0
    while True:
        try:
            sd.remove("0")
        except:
            break
    # 6 add 0 if len < 4
    while len(sd) < 4:
        sd.append("0")
    # 7 get first to fourth for more than 4
    if(len(sd) > 4):
        sd = sd[0:4]
    # return sounddex
    soundd = ""
    for s in sd :
        soundd += s
    return soundd

if __name__ == '__main__':
    inp = input("Enter word : ")
    inpu = inp.split()
    print(f"Soundexing for {inp}\n")
    for i in inpu :
        print (f"soundex for {i} is {soundex(i)}\n")


