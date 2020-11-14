with open("dictwords.txt","r") as f:
    data = f.readlines()

    l2 = open("letter2.txt","w")
    l3 = open("letter3.txt","w")
    l4 = open("letter4.txt","w")
    l5 = open("letter5.txt","w")
    l6 = open("letter6.txt","w")
    l7 = open("letter7.txt","w")
    l8 = open("letter8.txt","w")
    l9 = open("letter9.txt","w")
    l10 = open("letter10.txt","w")
    l11 = open("letter11.txt","w")
    l12 = open("letter12.txt","w")
    just = open("noneed.txt","w")

    d = { "3":l2,"4":l3,"5":l4,"6":l5,"7":l6,"8":l7,"9":l8,"10":l9,"11":l10,"12":l11,"13":l12 }

    for each in data:
        ids = str(len(each))
        if ids not in d:
            just.write(each)
        else:
            d[ids].write(each)
print("\nSegregated successfully as per the length of the word ...! ")