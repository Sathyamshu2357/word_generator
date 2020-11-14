letterfiles = [  'letter2.txt', 'letter3.txt', 'letter4.txt', 'letter5.txt', 'letter6.txt', 'letter7.txt', 'letter8.txt', 'letter9.txt', 'letter10.txt', 'letter11.txt', 'letter12.txt' ]
for letfile in letterfiles:
    filee = open(letfile,"r")
    data = filee.readlines()
    filee.close()
    alphaorder = { "a":'',"b":'',"c":'',"d":'',"e":'',"f":'',"g":'',"h":'',"i":'',"j":'',"k":'',"l":'',"m":'',
                    "n":'',"o":'',"p":'',"q":'',"r":'',"s":'',"t":'',"u":'',"v":'',"w":'',"x":'',"y":'',"z":'',"\n":'' }
    for each in data:
        alphaorder[each[0]] += each[:-1] + " "
    filee = open(letfile,"w")
    for each in alphaorder.values():
        filee.write(each)
        filee.write("\n")
    filee.close()
print("\nSuccessfully sorted for the better search ...! ")