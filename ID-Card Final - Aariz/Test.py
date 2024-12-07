# import pickle
# stu={}
# def create():
#  f1=open('student1.dat','wb')
#  ans='y'
#  while (ans=='y'):
#  rno=int(input("Enter roll number:"))
#  name=input("Enter name:")
#  marks=float(input("Enter marks:"))
#  stu['Rollno']=rno
#  stu['Name']=name
#  stu['Marks']=marks
#  pickle.dump(stu,f1)
#  ans=input("Would you like to enter one more
# record?(y/n)....")
#  f1.close()
# def search():
#  found=False
#  f2=open('student1.dat','rb')
#  key=int(input("Enter the roll number to be searched:"))
#  try:
#  print("Searching in file student...")
#  while True:
#  stu=pickle.load(f2)
#  if( stu['Rollno']== key):
#  print(stu)
#  found=True
#  except EOFError:
#  f2.close()
#  if found==False:
#  print("No such records found in the file")
#  else:
#  print("Search successful")


s = input('Enter String: ')
rev = reversed(s)
if list(s) == list(rev):
 print('The String is Palindrome')
else:
 print('The String is not a Palindrome')
