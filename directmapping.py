import math

print("           COMPUTER ORGANIZATION                                      ")
print("          END SEMESTER ASSIGNMENT                  ")


def read(address1,bits_in_B,bits_in_Cl,cache):
	l1=len(address1)
	extra_tag_length=int(l1-bits_in_B-bits_in_Cl)
	i2=32-l1
	tag=""
	for i in range(i2):
		tag+="0"
	finaladress=tag+address1
	tag+=address1[:extra_tag_length]
	# offset=finaladress[30:32]
	offset=finaladress[int(32-bits_in_B):]
	off=binaryToDecimal(offset)
	# index=finaladress[28:30]
	index=finaladress[int(32-bits_in_B-bits_in_Cl):int(32-bits_in_B)]
	for i in cache:
		if(binaryToDecimal(i.CacheLine)==binaryToDecimal(index)):
			if(tag==i.address):
				print("value = " + str(i.arrOfBlock[off]))
			else:
				print("Read Miss, value=0")

def write(address1,data1,bits_in_B,bits_in_Cl,cache,B):
	l1=len(address1)
	extra_tag_length=int(l1-bits_in_B-bits_in_Cl)
	i2=32-l1
	tag=""
	for i in range(i2):
		tag+="0"
	finaladress=tag+address1
	tag+=address1[:extra_tag_length]
	# offset=finaladress[30:32]
	offset=finaladress[int(32-bits_in_B):]
	off=binaryToDecimal(offset)
	# index=finaladress[28:30]
	index=finaladress[int(32-bits_in_B-bits_in_Cl):int(32-bits_in_B)]
	for i in cache:
		if(binaryToDecimal(i.CacheLine)==binaryToDecimal(index)):
			if(tag==i.address):
				print("WRITE HIT!")
				i.arrOfBlock[off]=data1
			else:
				print("WRITE MISS :(")
				for del1 in range(B):
					i.arrOfBlock[del1]=0
				i.address=tag
				i.arrOfBlock[off]=data1
	for i in cache:
		print("Adress Of Block : " + i.address)
		print("Index : " + i.CacheLine)
		for k in range(len(i.arrOfBlock)):
			print("offset value = " + decimalToBinary(k)+" , value = " +str(i.arrOfBlock[k]))



print("Enter the size of your cache: ")
S  =int(input())
print("Enter the number of cache lines: ")
Cl =int(input())
print("Enter the block size: ")
B  =int(input())
bits_in_Cl=math.log(Cl,2)
bits_in_B=math.log(B,2)
Adr_bits= 32- bits_in_Cl - bits_in_B
def decimalToBinary(n):  
    return bin(n).replace("0b", "") 

def binaryToDecimal(n): 
    return int(n,2) 

class block:
	def __init__(self,CacheLine,arrOfBlock,address):
		self.CacheLine=CacheLine
		self.arrOfBlock=arrOfBlock	
		self.address=address			
cache=[]
for i in range(Cl):
	b1=[]
	adr=""
	for j in range(B):
		b1.append(decimalToBinary(0))
	for j in range(int(Adr_bits)):
		adr+="0"
	b=block(decimalToBinary(i),b1,adr)
	cache.append(b)
# for i in cache:
# 	print(i.CacheLine,end=" ")
# 	print(i.arrOfBlock,end=" ")
# 	print(i.address)

T=100
for j in range(T):
	print("1> Read, 2> Write, 3> Exit")
	Op=int(input())
	if(Op==1):
		print("Enter address: ")
		address=input()
		read(address,bits_in_B,bits_in_Cl,cache)
	if(Op==2):
		print("Enter address: ")
		address1=input()
		print("Enter data: ")
		data1=int(input())
		write(address1,data1,bits_in_B,bits_in_Cl,cache,B)
	if(Op==3):
		print("Rishit  Gupta")
		print("   2019091  ")
		print("  Thank You ")
		break																	