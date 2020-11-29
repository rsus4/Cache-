import math

def read(adr,cache2,list1,tag2,offset):
	flag1=False
	for i in cache2:
		if(i.add==tag2):
			print("value = " + str(i.aOfBlock[binaryToDecimal(offset)]))
			flag1=True
	if(flag1==False):
		print("Read Miss")

def write(Catchline,data,cache2,offset,tag,zero_or_not):
	for j in cache2:
		# print("HI")
		# print(j.CLine,Catchline)
		if(binaryToDecimal(j.CLine)==Catchline):
			if(zero_or_not):
				for del2 in range(len(j.aOfBlock)):
					j.aOfBlock[del2]=0
			j.aOfBlock[offset]=data
			j.add=tag
	for j in cache2:
		print("Adress Of Block : " + j.add)
		print("Index :ds " + j.CLine)
		for k in range(len(j.aOfBlock)):
			print("offset value = " + decimalToBinary(k)+" , value = " +str(j.aOfBlock[k]))





def decimalToBinary(n):  
    return bin(n).replace("0b", "") 

def binaryToDecimal(n): 
    return int(n,2) 

class block_ass:
	def __init__(self,CLine,aOfBlock,add):
		self.CLine=CLine
		self.aOfBlock=aOfBlock	
		self.add=add	

print("Enter the size of your cache: ")
S  =int(input())
print("Enter the number of cache lines: ")
Cl =int(input())
print("Enter the block size: ")
B  =int(input())
bits_in_Cl=int(math.log(Cl,2))
bits_in_B=int(math.log(B,2))
Adr_bits= 32 - bits_in_B
cache2=[]
list1=[]
i1=0
for i in range(Cl):
	b1=[]
	adr=""
	for j in range(B):
		b1.append(decimalToBinary(0))
	for j in range(int(Adr_bits)):
		adr+="0"
	b=block_ass(decimalToBinary(i),b1,adr)
	cache2.append(b)
# for i in cache2:
# 	print(i.CLine,end=" ")
# 	print(i.aOfBlock,end=" ")
# 	print(i.add)


zero_or_not=False
T=100
flag=False
for j in range(T):
	print("1> Read, 2> Write, 3> Exit")
	Op=int(input())
	if(Op==1):
		print("Enter address: ")
		address=input()
		length1=len(address)
		# print(address)
		b_no=address[:-bits_in_B]
		# print(b_no)
		length2=len(b_no)
		offset=address[-bits_in_B:]
		length3=len(offset)
		ini=32-length1
		# print(ini)
		tag2=""
		for i in range(ini):
			tag2+="0"
		tag2=tag2+b_no
		# print(tag2)
		read(address,cache2,list1,tag2,offset)
	if(Op==2):
		print("Enter address: ")
		address1=input()
		length1=len(address1)
		print("Enter data: ")
		data=int(input())
		b_no=address1[:-bits_in_B]
		# length2=len(b_no)
		offset=address1[-bits_in_B:]
		# length3=len(offset)
		ini=32-length1
		# print(ini)
		tag2=""
		for i in range(ini):
			tag2+="0"
		tag2=tag2+b_no
		# print(tag2)
		# print(len(tag2))
		off=binaryToDecimal(offset)
		if(b_no in list1):
			zero_or_not=False
			print("Write hit!")
			write(list1.index(b_no),data,cache2,off,tag2,zero_or_not)
		else:
			print("Write miss :(")
			zero_or_not=True
			i1=i1+1
			# print(i1)
			if(i1!=Cl+1):
				list1.append(b_no)
				# print(list1)
				if(flag==False):
					write(i1-1,data,cache2,off,tag2,zero_or_not)
				else:
					write(i1,data,cache2,off,tag2,zero_or_not)
			else:
				# print("HIII")
				list1.pop(0)
				list1.append(b_no)
				i1=0
				flag=True
				write(i1,data,cache2,off,tag2,zero_or_not)
	if(Op==3):
		print("Rishit Gupta")
		print("   2019091  ")
		print("  ThankYou! ")
		break
