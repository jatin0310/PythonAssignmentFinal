# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included)
        
def number_divisible_by7_not_by_5():
	list_nums = []
	for i in range(2000, 3201):
		if i%7 == 0 and i%5!=0:
			list_nums.append(i)
	
	print("Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 both included")
	print(list_nums ,"\n")


number_divisible_by7_not_by_5()

# 2. get the occurence of all vowels and consonent from the large given string.
def count_occurence_vowel_constonants(str1):
	vowels = ['a', 'e', 'i', 'o', 'u']
	constonent = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	vow=""
	const=""
	for x in str1:
		if x in vowels:
			vow += x
		elif x in constonent:
			const += x
	print("Get the occurence of all vowels and consonent from the large given string")
	print("No of vowels in ",str1," are ",len(vow))
	print("vowels=",vow)
	print("No of consonent in ",str1," are ",len(const))
	print("constonent",const)
	

count_occurence_vowel_constonants("abcdefdckejhvcf")    

print("\n")

# 3. convert a number into binary and binary to number.
print("Conversion of number into binary and binary into number")
def decimal_to_binarynum(n):
	if n>=1:
		decimal_to_binarynum(n//2)
	print(n % 2,end = '')	
	
decimal_to_binarynum(8) 

def binarynum_to_decimal(bnum):
    return int(bnum,2)

a=binarynum_to_decimal('1000')        
print("\nDecimal Number:",a)


#Reverse the list by using negative index and apply logic also.
print("Reverse the list by using negative index and apply logic also.")
def rev_list_negative_index(list_int):
	print("Original list:",list_int)
	newlist=list_int[::-1]
	print("Reversed List:",newlist," using index")
	
list_int_num=[1,2,3,4,5]    
rev_list_negative_index(list_int_num)

def rev_list_using_logic(list1):
	revlist=[]
	for i in range(len(list1)-1,-1,-1):
		revlist.append(list1[i])
	print("Reverse list:",revlist," using logic")
	

list2=[1,2,3,4,5]
rev_list_using_logic(list2)	


# 5. participants_list = [
#     ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
#     ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
#     ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
#     ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
#     ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
#     ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
#     ]
# print("daily_participants---------")
# daily_participants(participants_list) # ['Desmond', 'Krish', 'Sam']
# print("one_time_participants---------")
# one_time_participants(participants_list)# ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
# print("first_day_only_participants----------------")
# first_day_only_participants(participants_list) #  ['John', 'Joan']

def check_the_participations():
	def daily_participants(dict, part_list):
		daily_participation = []
		for participant, participation in dict.items():
			if participation == len(part_list):
				daily_participation.append(participant)
		
		return daily_participation

	def one_time_participants(dict, part_list):
		one_time_participation = []
		for participant, participation in dict.items():
			if participation == 1:
				one_time_participation.append(participant)

		return one_time_participation

	def first_day_only_participants(dict, part_list):
		first_day_participants = []
		for i in part_list[0]:
			if i in dict and dict[i] == 1:
				first_day_participants.append(i)
		
		return first_day_participants


	participants_list = [['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ], ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'], ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'], ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'], ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'], ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']]

	dict_for_participants_count = {}#Giving the count to each participant
	for i in participants_list:
		for j in i:
			if j not in dict_for_participants_count:
				dict_for_participants_count[j] = 1
			else:
				dict_for_participants_count[j] += 1
				

	print(" Play around with the list and printing the following : ")
	print("Daily Participants---------------------------\n", daily_participants(dict_for_participants_count, participants_list))
	print("One time Participants------------------------\n", one_time_participants(dict_for_participants_count, participants_list))
	print("Only First day Participants------------------\n", first_day_only_participants(dict_for_participants_count, participants_list))
	print()

check_the_participations()

# 6. Create a list by picking an odd-index items from the first list and even index items from the second return third list.
def merge_odd_even_index_list():
	
	list1 = [0,2,4,6,8,10] 
	list2 = [1,3,5,7,9,11,13,15]
	list3 = []
	n = min(len(list1), len(list2)) #calculate minimum length of list from list1 and list2

	for i in range(n):
		if i%2 == 0: list3.append(list2[i])
		else: list3.append(list1[i])
	
	if n == len(list1): list3 += list2[n+1:]
	else: list3 += list1[n+1:]
	
	print(list3)

print("Printing an odd-index items from the first list and even index items from the second return third list.")	
merge_odd_even_index_list()    


# 7. Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list by using list comprehension 

# dict ={"key1":1234, "k2":"ram"}

# list= [1234,"ram"]

def check_key_value_from_list():
	dict = { "key1": 1234, "k2": "ram" }
	lists = [1234,"ram","Hey",6789,"Batch"]
	print("dict:",dict)
	print("lists:",lists)

	for value, key in dict.items():
		[lists.remove(i) for i in lists if i==key ]

	print("List after checking:", lists)


print("\n Iterate a given list and check if a given element exists as a keys value in a dictionary. If not, delete it from the list by using list comprehension ")
check_key_value_from_list()

# 8. Access the nested key ‘salary’ from the following JSON
# sampleJson = """{ 
#    "company1":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    },
#    "company2":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    },
#     
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# emp-id     emp-name -- salary

def json_read_nesting():
	import json

	json_file_for_nested = """
	{ 
		"company1":{ 
			"employee":{ 
				"name":"Emma",
				"payble":{ 
					"salary":"7000",
					"bonus":"800"
				}
			}
		},
		
		"company2":{
			"employee":{ 
				"name":"Luna",
				"payble":{ 
					"salary":"7000",
					"bonus":"1900"
				}
			}
		},
		
		"company3":{ 
			"employee":{ 
				"name":"Ronny",
				"payble":{ 
					"salary":"4000",
					"bonus":"300"
				}
			}
		}
	}
	"""
	json_file_for_nested = json.loads(json_file_for_nested)
	print("Emp-Name      |       Salary")
	print("____________________________\n")
	for i in json_file_for_nested:
		
		emp_name = json_file_for_nested[i]['employee']['name']
		emp_salary = json_file_for_nested[i]['employee']['payble']['salary']
		

		print("EmpName:{}      EmpSalary:{}".format(emp_name,emp_salary))

print()

json_read_nesting()


# 9. Create class OOPS and implement all oops concept in that.
class School():
	'''This class is for the companies details  '''
	def __init__(self) -> None:
		pass

	def about_school(self):
		print("Hello everyone I am from STCS")
	

class School_department(School):

	def academics(self):
		d_id = "Aca"
		print("This is Academics department:", d_id)
	
	def sports(self):
		d_id = "Sports"
		print("This is Sports department:", d_id)


class School_emp(School_department):
	
	def __init__(self, emp_id, emp_name, emp_department):
		self.emp_id = emp_id
		self.emp_name = emp_name
		self.emp_department = self.academics()
		self.emp_salary = 0

	def set_salary(self, salary):
		self.emp_salary = salary
	
	def get_emp_name(self):
		return self.emp_name
	
	def get_emp_salary(self):
		return self.emp_salary
		

print()
print("Class and OOPS concept")
a12 = School_emp(12, 'Jatin', 'Academics')
a12.set_salary("80000")
print("\nSchool deatils:")
print(a12.about_school())
print("\nEmployee Name: ", a12.emp_name, "\nHis employee id", a12.emp_id)
print("\n")


# 10. Create a class BANK and with two function simple interest and compound interest. 
#  U need to create instance for pnb, icici and hdfc banks with corresponding input.
print()
print("Create a class BANK and with two function simple interest and compound interest.U need to create instance for pnb, icici and hdfc banks with corresponding input.")
import math
class Bank():
    def __init__(self,a,rate,time,d):
        self.a=a
        self.rate=rate
        self.time =time
        self.d=d
    
    def simple(self):
        s_interest=(self.a*self.rate*self.time)/100
        print("printing the simple interest: ", s_interest)
        
    def compound(self):
        b=1+(self.rate/self.d)
        e=self.d*self.time
        f=math.pow(b,e)
        c_interest=self.a*f
        print("Printing compound interest: ", c_interest)
        
Bank_name= input("Enter The Bank Name (HDFC/ICICI/PNB): " )
a= int(input("enter the Amount you have submitted: "))
time= int(input("enter the time in years:  "))
d= int(input("enter number of times interest is compounded per year: "))

    
if(Bank_name=="ICICI"):

    ICIC=Bank(a,2,time,d)
    ICIC.simple()
    ICIC.compound()
    
    
if(Bank_name=="HDFC"):
    Hdfc=Bank(a,2,time,d)
    Hdfc.simple()
    Hdfc.compound()

if(Bank_name=="PNB"):
    PNB=Bank(a,2,time,d)
    PNB.simple()
    PNB.compound()
