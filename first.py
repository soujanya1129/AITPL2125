#palindrome or not
def ispalindrome(x):
    return x == x[:: -1]
x = 'amma'
x1= ispalindrome(x)
if x1:
    print('is a palindrome')
else:
    print('not a palindrome')

