from itertools import permutations, combinations 
lets = input("\nEnter the letters to be scrambled [3 - 12 letters]: ")
if(len(lets)>12 or len(lets)<3):
    print("\nSorry...Limits crossed . Terminating the program..! Try other by Re-executing")
    exit()
combis = []
for i in range(2,len(lets)+1):
    combis.append(list(''.join(x) for x in combinations(lets,i)))
permus = []
for every in combis:
    just = [] 
    for each in every:
        just = just + list(''.join(x) for x in permutations(each))
    permus.append(just)

letterfiles = [  'letter2.txt', 'letter3.txt', 'letter4.txt', 'letter5.txt', 'letter6.txt', 'letter7.txt', 'letter8.txt', 'letter9.txt', 'letter10.txt', 'letter11.txt', 'letter12.txt' ]

print()
idx = 0
for everylist in permus:
    filee = open(letterfiles[idx],"r")
    data = filee.readlines()
    temp = []
    for eachword in everylist:
        if (eachword in data[(ord(eachword[0])-97)]) and (eachword not in temp):
            temp.append(eachword)
    print(*temp,end="\n\n")
    idx += 1