numList = ["","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]
powOfTenList = ["","สิบ","ร้อย","พัน","หมื่น","แสน"]


num = int(input("Enter number :"))
powOfTen = 0
word = ""
while(num):
    digit = num % 10

    if powOfTen == 6:
        word = "ล้าน" + word
        powOfTen = 0
    
    if digit == 1 and powOfTen == 0 and num//10:
        word = "เอ็ด" + word
    elif digit == 2 and powOfTen == 1:
        word = "ยี่สิบ"+word
    elif digit == 1 and powOfTen == 1:
        word = "สิบ"+word
    elif digit:
        word = numList[digit] + powOfTenList[powOfTen] + word

    num = num // 10
    powOfTen += 1

print(word)