string = input('enter a number - ')
num = {'1':0,
       '2':0,
       '3':0,
       '4':0,
       '5':0,
       '6':0,
       '7':0,
       '8':0,
       '9':0,
       }
for i in string:
    if i in num:
        num[i]+=1

panagram = True
for x in num.values():
    if x == 0:
        panagram = False

if panagram:
    print('Entered number is a panagram')

else:
    print('Entered number is not a panagram')
