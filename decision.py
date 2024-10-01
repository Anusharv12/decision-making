# decision-making
'''Decision Making
1)Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
Sample Input:
6
8
Sample Output:
6 less than 8'''

Ans:
x = int(input())
y = int(input())
if x == y:
  print(f"{x} and {y} are equal")
elif x > y:
  print(f"{x} greater than {y}")
else:
  print(f"{x} less than {y}")

'''
2)Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel'''
Ans:
a=input()
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print('Vowel')
elif(a>'a' and 'a'<a):
    print("Consonant")
else:
    print("Not an alphabet")

'''3)The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored  
  Grade 
100
S
90 - 99
A
80 - 89
B
70 - 79
C
60 - 69
D
50 - 59
E
<50
F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C'''
Ans:
marks = int(input())
if marks > 100 or marks < 0:
  print("Invalid Input")
if marks == 100:
  grade = "S"
elif 90 <= marks < 100:
  grade = "A"
elif 80 <= marks < 90:
  grade = "B"
elif 70 <= marks < 80:
  grade = "C"
elif 60 <= marks < 70:
  grade = "D"
elif 50 <= marks < 60:
  grade = "E"
else:
  grade = "F"
print(grade)

'''
4) A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00'''

Ans:
cost_per_dozen = float(input())
selling_price_per_banana = float(input())
total_selling_price = selling_price_per_banana * 12
profit_or_loss = total_selling_price - cost_per_dozen
if profit_or_loss > 0:
  print(f"Profit : Rs.{profit_or_loss:.2f}")
elif profit_or_loss < 0:
  print(f"Loss : Rs.{abs(profit_or_loss):.2f}")
else:
  print("No Profit No Loss")





