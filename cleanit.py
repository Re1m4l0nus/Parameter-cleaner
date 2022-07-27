print("Parameter Cleaner")
print("Author: Rei Malonus")
print("Telegram: https://t.me/ReiMalonus")
print("")
print("")

filename = input("Enter Website List (text file): ")
fw= open("domain_list.txt","w")
fr1= open(filename, "r")
num= sum(1 for line in fr1)
fr1.close()
fr= open(filename, "r")
i=0
for i in range(num):
	line= fr.readline()
	index1=""
	if line.find(".") == -1:
		continue
	elif line[line.index(".")-1]=="w" and  line.index(".")<19:
		index1=line.index(".")+1
	else:
		index1=line.index("/")+2
	line1 = line[index1:len(line)]
	index2 = line1.index("/")
	line2= line1[0:index2]
	fw.write(line2+"\n")
	print(line2)
	i= i+1
