# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# Mat size must be N x M . ( N is an odd natural number, and M is 3 times N .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

n = int(input())
m = int(input())
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
print('WELCOME'.center(m,'-'))
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))