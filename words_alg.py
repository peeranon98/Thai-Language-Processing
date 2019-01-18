# PSEUDO CODE
from collections import Counter
raw = open('in.txt') # สตริงยาวๆ
text = raw.read()
words = text.split() # แยกมาเป็น list ด้วย space
dictionary = open('dict.txt')
dics = dictionary.read()
dic = dics.split()
print(f"Dictionary : {dic}")
out = []
rem = []
print(f"Here is variable words {words}\n")
for word in words:
    if word in dic: # คำที่แยกมาจาก space ทั้งคำ เป็น คำใน dict
        print(f"Word {word} is found\n")
        out.append(word) #เอาใส่คำตอบสุดท้าย
        #words.remove(word) # ลบออกจาก list คำที่ต้องเช็ค ไว้ดูคำที่ไม่เหลือใน dict หลังรันครบ ?
        #print(f"Here is variable words {words}\n")
    else : 
        check = "" # สตริงเช็ค ขยายเรื่อยๆ
        preout = [] # ไว้เก็บคำที่เจอใน line ยาวๆ
        for i in range (len(word)):
            check += word[i] # เช็คเพิ่มทีละตัวอักษร
            print(f"Here is variable check {check}")
            if check in dic :
                print(f"{check} in dic\n")
                out.append(check) # ถ้ามีตรง เก็บใส่ list
                start = word.find(check)
                word = word[start:]
                check = ""
                continue
            else :
                continue

# ส่วนเหลือ 
print(f"From input: '{text}'")
# ที่เจอ
output = dict(Counter(out))
print(f"We have {output}") # คำตอบจะออกมาใน Data structure Dictionaty จย้าาาาา