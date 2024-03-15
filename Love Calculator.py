# 3. Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
count = 0
check1 = 'true'
check2 = 'love'
truefinal = []
for name in check1:
    for i in name1:
        if name == i:
            count += 1
    for l in name2:
        if name == l:
            count += 1
if count:
    truefinal.append(count)

count2 = 0
lovefinal = []
for name in check2:
    for i in name1:
        if name == i:
            count2 += 1
    for l in name2:
        if name == l:
            count2 += 1
if count2:
    lovefinal.append(count2)

finaltrue = truefinal.pop()
finallove = lovefinal.pop()

final = str(finaltrue) + '' + str(finallove)
final = int(final)

if final < 10 or final > 90:
    print(f'Your score is {final}, you go together like coke and mentos.')
elif final >= 40 and final <= 50:
    print(f'Your score is {final}, you are alright together.')
else:
    print(f'Your score is {final}.')