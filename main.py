import soundex as sd
import wordsplit as ws

if __name__ == '__main__':
	text = input("Input text : ")
	print()
	splited = ws.wordsplit(text)
	#print(splited)
	for i in splited :
		print (f"soundex for {i} is {sd.soundex(i)}\n")