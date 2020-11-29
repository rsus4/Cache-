import math

print("           COMPUTER ORGANIZATION                                      ")
print("          END SEMESTER ASSIGNMENT                  ")



def read(address1,cache3,bits_in_B,bits_in_set,loop):
	l1=len(address1)
	extra_tag_length=int(l1-bits_in_B-bits_in_set)
	i2=32-l1
	flag1=False
	tag2=""
	for i in range(i2):
		tag2+="0"
	finaladdress=tag2+address1
	tag2+=address1[:extra_tag_length]
	offset=finaladdress[int(32-bits_in_B):]
	off=binaryToDecimal(offset)
	setNum=finaladdress[int(32-bits_in_B-bits_in_set):int(32-bits_in_B)]
	for i in range(0,len(cache3),loop):
		if(binaryToDecimal(setNum)==binaryToDecimal(cache3[i].set_no)):
			for j in range(i,i+loop):
				if(cache3[j].address==tag2):
					print("Value = " + str(cache3[j].arrOfBlock[off]))
					flag1=True
	if(flag1==False):
		print("Read Miss :(")
	print()

def write(address1,data1,cache3,bits_in_B,bits_in_set,loop,list1,listindex):
	l1=len(address1)
	extra_tag_length=int(l1-bits_in_B-bits_in_set)
	i2=32-l1
	tag2=""
	for i in range(i2):
		tag2+="0"
	finaladdress=tag2+address1
	tag2+=address1[:extra_tag_length]
	offset=finaladdress[int(32-bits_in_B):]
	off=binaryToDecimal(offset)
	setNum=finaladdress[int(32-bits_in_B-bits_in_set):int(32-bits_in_B)]
	for i in range(0,len(cache3),loop):
		if(binaryToDecimal(setNum)==binaryToDecimal(cache3[i].set_no)):
			if(tag2 in list1[binaryToDecimal(setNum)]):
				# i.arrOfBlock[off]=data1
				index=binaryToDecimal(setNum)*loop + list1[binaryToDecimal(setNum)].index(tag2)#cache line to which the data is to be written
				cache3[index].arrOfBlock[off]=data1
				cache3[index].address=tag2
			else:
				if(len(list1[binaryToDecimal(setNum)])!=loop):
					list1[binaryToDecimal(setNum)].append(tag2)
					listindex[binaryToDecimal(setNum)]+=1
					index=binaryToDecimal(setNum)*loop + list1[binaryToDecimal(setNum)].index(tag2)
					for rishi in range(len(cache3[index].arrOfBlock)):
						cache3[index].arrOfBlock[rishi]=0
					cache3[index].arrOfBlock[off]=data1
					cache3[index].address=tag2
				else:
					if(listindex[binaryToDecimal(setNum)]==loop):
						listindex[binaryToDecimal(setNum)]=0
					list1[binaryToDecimal(setNum)].pop(0)
					list1[binaryToDecimal(setNum)].append(tag2)
					index=binaryToDecimal(setNum)*loop + listindex[binaryToDecimal(setNum)]
					for rishi in range(len(cache3[index].arrOfBlock)):
						cache3[index].arrOfBlock[rishi]=0
					cache3[index].arrOfBlock[off]=data1
					cache3[index].address=tag2
					listindex[binaryToDecimal(setNum)]+=1
	for i in cache3:
		print("Adress Of Block : " + i.address)
		print("Index : " + decimalToBinary(i.Cline))
		for k in range(len(i.arrOfBlock)):
			print("offset value = " + decimalToBinary(k)+" , value = " +str(i.arrOfBlock[k]))

	print()

print("Enter the size of your cache: ")
S  =int(input())
print("Enter the number of cache lines: ")
Cl =int(input())
print("Enter the block size: ")
B  =int(input())
print("Enter the number of sets: ")
n  =int(input())

def decimalToBinary(n):  
    return bin(n).replace("0b", "") 

def binaryToDecimal(n): 
    return int(n,2) 

class setCache:
	def __init__(self,set_no,Cline,address,arrOfBlock):
		self.set_no=set_no
		self.Cline=Cline
		self.address=address
		self.arrOfBlock=arrOfBlock
bits_in_B=math.log(B,2)
bits_in_set=math.log(n,2)
Adr_bits=int(32-bits_in_B-bits_in_set)
cache3=[]
list1=[]
listindex=[]
for i in range(n):
	list1.append([])
	listindex.append(0)

for i in range(Cl):
	b1=[]
	adr=""
	for j in range(B):
		b1.append(decimalToBinary(0))
	for j in range(Adr_bits):
		adr+="0"
	set_number=int(i/n)
	set_num=decimalToBinary(set_number)
	b=setCache(set_num,i,adr,b1)
	cache3.append(b)


# for i in cache3:
# 	print(i.set_no,end=" ")
# 	print(i.Cline,end=" ")
# 	print(i.arrOfBlock,end=" ")
# 	print(i.address)

	
T=100 
for j in range(T):
	print("1> Read, 2> Write, 3> Exit")
	Op=int(input())
	if(Op==1):
		print("Enter address: ")
		address=input()
		read(address,cache3,bits_in_B,bits_in_set,int(Cl/n))
	if(Op==2):
		print("Enter address: ")
		address1=input()
		print("Enter data: ")
		data1=int(input())
		write(address1,data1,cache3,bits_in_B,bits_in_set,int(Cl/n),list1,listindex)
	if(Op==3):
		print()
		print("CO END-SEM PROJECT")
		print("  Rishit Gupta")
		print("    2019091  ")
		print("   Thank You ")
		break
