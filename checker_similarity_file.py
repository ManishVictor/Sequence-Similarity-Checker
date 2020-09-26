f1=open("input1.txt","r")#single line fasta input required
f2=open("input2.txt.fasta","r")#single line fasta input required
for line1 in f1:
    for line2 in f2:
        if line1==line2:
            print("SAME\n")
        else:
            print(line1 + line2)
        break
f1.close()
f2.close()