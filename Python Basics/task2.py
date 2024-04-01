''' A palindrome is a string which is same read forward or backwards.
For example: &quot;dad&quot; is the same in forward or reverse direction. Another example is
&quot;aibohphobia&quot; which literally means, an irritable fear of palindromes.
Write a function in python that receives a string and returns True if that string is a
palindrome and False otherwise. Remember that difference between upper and lower case
characters are ignored during this determination.'''


palString = None

palString = input("Enter the string: ")

notpalString = palString[::-1]
if(notpalString==palString):
    print("it is pal")
else:
    print("it is not pal")