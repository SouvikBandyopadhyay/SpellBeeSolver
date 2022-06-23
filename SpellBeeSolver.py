fi=open("SpellBeeInputfile.txt", "r")
fr= list(fi.read().split())
fr.sort(key=len)
inp=input().upper()
main=inp[0]
a=set([x for x in inp])

for i in fr:
    i=i.upper()
    if len(i)<4:
        continue
    else:
        word=set([x for x in i])
        if word-a:
            continue
        else:
            if main in word:
                print(i)
