'''Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38'''

Ans:
birth_year = int(input())
current_year = int(input())
full_birth_year = 1900 + birth_year if birth_year >= 50 else 2000 + birth_year
full_current_year = 1900 + current_year if current_year >= 50 else 2000 + current_year
age = full_current_year - full_birth_year
print(age)
