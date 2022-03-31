import string
"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generateParenthesis(n: int):
  output = []
  
  def generate(left,right,stack,parstring):
    if left == right == 0:
      output.append(parstring)
    if left > 0:
      generate(left-1,right,stack+1,parstring+"(") 
    if right > 0 and stack > 0:
      generate(left,right-1,stack-1,parstring+")")
  generate(n,n,0,"")
  return output 

"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""
def isPalindrome(input):
    if input == '':
        return True
    solution = input.replace(' ', '')
    solution = solution.lower()
    solution = solution.translate(str.maketrans('','', string.punctuation))
    if solution == solution[::-1]:
        return True
    else:
        return False
