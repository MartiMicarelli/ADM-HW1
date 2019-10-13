# Introduction -> Say "Hello, World!" With Python
print("Hello, World!")

# Introduction -> Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        else:
            if n<=20:
                print("Weird")
            else:
                print("Not Weird")


# Introduction -> Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Introduction -> Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Introduction -> Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

# Introduction -> Write a function
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap

year = int(input())
print(is_leap(year))

# Introduction -> Print function
if __name__ == '__main__':
    n = int(input())
    x=range(1,n+1)
    for i in x:
        print(i, end='')

# Basic Data Types -> List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    A = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)        if i+j+k!=n ]
    print(A)

# Basic Data Types -> Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s=set(arr)
    s.remove(max(s))
    print(max(s))

# Basic Data Types -> Nested Lists
if __name__ == '__main__':
    l=[]
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        s.append(score)
    s=set(s)
    s.remove(min(s))
    m=min(s)
    names=[]
    for [name,score] in l:
        if score==m:
            names.append(name)
    names.sort()
    for i in names:
        print(i)

# Basic Data Types -> Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s=0
    n=0
    for score in student_marks[query_name]:
        s+=score
        n=n+1
    print("{0:.2f}".format(s/n))

# Basic Data Types -> Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))

# Basic Data Types -> Lists
if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(N):
        inputs=input().split()
        if inputs[0]=="insert":
            L.insert(int(inputs[1]), int(inputs[2]))
        elif inputs[0]=="print":
            print(L)
        elif inputs[0]=="remove":
            L.remove(int(inputs[1]))
        elif inputs[0]=="append":
            L.append(int(inputs[1]))
        elif inputs[0]=="sort":
            L.sort()
        elif inputs[0]=="pop":
            L.pop()
        elif inputs[0]=="reverse":
            L.reverse()

# Strings -> sWAP cASE
def swap_case(s):
    newstring=''
    for i in s:
        if i.islower():
            newstring+=i.upper()
        else:
             newstring+=i.lower()
    return newstring

# Strings -> String split and join
def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

# Strings -> What's Your Name?
def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." %(a,b))

# Strings -> Mutations
def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string

# Strings -> Find a string
def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)):
        index=string.find(sub_string, i, i+len(sub_string))
        if index!= -1:
            count+=1
    return count

# Strings -> String Validators
if __name__ == '__main__':
    s = input()
    x=False
    for i in range(0, len(s)):
        if(s[i]).isalnum():
            x=True
            break
    print(x)
    x=False
    for i in range(0, len(s)):
        if(s[i]).isalpha():
            x=True
            break
    print(x)
    x=False
    for i in range(0, len(s)):
        if(s[i]).isdigit():
            x=True
            break
    print(x)
    x=False
    for i in range(0, len(s)):
        if(s[i]).islower():
            x=True
            break
    print(x)
    x=False
    for i in range(0, len(s)):
        if(s[i]).isupper():
            x=True
            break
    print(x)

# Strings -> Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Strings -> Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

# Strings -> Designer Door Mat
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(''.join(['.|.'] * i).center(M, '-'))
print("WELCOME".center(M, '-'))
for i in range(N-2, -1, -2):
    print(''.join(['.|.'] * i).center(M, '-'))

# Strings -> String formatting
def print_formatted(number):
    l=len(str(bin(number))[2:])
    for i in range(1, number+1):
        print(str(i).rjust(l), oct(i)[2:].rjust(l), hex(i)[2:].upper().rjust(l),
bin(i)[2:].rjust(l))

# Strings -> Alphabet Rangoli
import string
def print_rangoli(size):
    n=size-1
    s='-'
    for i in range(n, 0, -1):
        l=['-']*(2 * size - 1)
        for j in range(size - i):
            l[n-j]= l[n+j]=string.ascii_lowercase[j+i]
        print(s.join(l))

    for i in range(0, size):
        l=['-']*(2*size-1)
        for j in range(0,size-i):
            l[n-j]=l[n+j]=string.ascii_lowercase[j + i]
        print(s.join(l))

# Strings -> Capitalize!
def solve(s):
    l=s.split(' ')
    m=[]
    for i in l:
        m.append(i.capitalize())
    s=' '. join(m)
    return s

# Strings -> The Minion Game
def minion_game(string):
    s_score=0
    k_score=0
    l=['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in l:
            k_score+=len(string)-i
        else:
            s_score+=len(string)-i
    if s_score > k_score:
        print("Stuart", s_score)
    elif k_score>s_score:
        print("Kevin", k_score)
    else:
        print("Draw")

# Strings -> Merge the Tools!
def merge_the_tools(string, k):
    l=[string[i:i+k] for i in range(0, len(string), k)]
    for i in l:
        m=[]
        u=[]
        for w in i:
            if w not in m:
                m.append(w)
                u.append(w)
        u_p=''.join(u)
        print(u_p)

# Sets -> Introduction to Sets
def average(array):
    # your code goes here
    s=set(array)
    n=len(s)
    sum=0
    for i in s:
        sum+=i
    return sum/n

# Sets -> Symmetric Difference
m=int(input())
m_set=set(input().split(' '))

n=int(input())
n_set=set(input().split(' '))

d=(m_set.difference(n_set)).union(n_set.difference(m_set))
for i in sorted(d, key=int):
    print(i)

# Sets -> Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c=input().split(' ')
    if c[0]=="pop":
        if len(s)!=0:
            s.pop()
    elif c[0]=="remove" and int(c[1]) in s:
        s.remove(int(c[1]))
    elif c[0]=="discard":
        s.discard(int(c[1]))
sum=0
for j in s:
    sum+=j
print(sum)

# Sets -> No Idea!
n,m=map(int,input().split(' '))
ar=map(int,input().split(' '))
A=map(int, input().split(' '))
B=map(int,input().split(' '))
like=set(A)
dislike=set(B)
happiness=0
for i in ar:
    if i in like:
        happiness+=1
    elif i in dislike:
        happiness-=1
print(happiness)

# Sets -> Set.add()
n=int(input())
l=[]
for i in range(n):
    l.append(input())
s=set(l)
print(len(s))

# Sets -> Set.union() Operation
n=int(input())
eng_set=set(input().split(' '))
b=int(input())
fr_set=set(input().split(' '))
print(len(eng_set.union(fr_set)))

# Sets -> Set.intersection() Operation
n=int(input())
eng_set=set(input().split(' '))
b=int(input())
fr_set=set(input().split(' '))
print(len(eng_set.intersection(fr_set)))

# Sets -> Set.difference() Operation
n=int(input())
eng_set=set(input().split(' '))
b=int(input())
fr_set=set(input().split(' '))
print(len(eng_set.difference(fr_set)))

# Sets -> Set.symmetric_difference() Operation
n=int(input())
eng_set=set(input().split(' '))
b=int(input())
fr_set=set(input().split(' '))
print(len(eng_set.symmetric_difference(fr_set)))

# Sets -> Set Mutations
l,A=int(input()),set(input().split())
N=int(input())
for i in range(N):
    op, s=input().split(), input().split()
    if op[0]=='intersection_update':
        A.intersection_update(s)
    elif op[0]=='difference_update':
        A.difference_update(s)
    elif op[0]=='symmetric_difference_update':
        A.symmetric_difference_update(s)
    elif op[0]=='update':
        A.update(s)
print(sum(map(int,A)))

# Sets -> The Captain's Room
k=int(input())
s1=set()
s2=set()
l=input().split()
for n in l:
    if n not in s1:
        s1.add(n)
    else:
        s2.add(n)

s1.difference_update(s2)
print(s1.pop())

# Sets -> Check Subset
t=int(input())
for _ in range(t):
    n_A=int(input())
    A=input().split()
    n_B = int(input())
    B = input().split()
    bool=True
    for j in A:
        if j not in B:
            bool=False
    print(bool)

# Sets -> Check Strict Subset
A=input().split()
n=int(input())
bool=True
for _ in range(n):
    s=input().split()
    for i in s:
        if i not in A:
            bool=False
    if len(A)<=len(s):
        bool=False
print(bool)

# Collections -> collections.Counter()
import collections
x=int(input())
sizes=collections.Counter(map(int,input().split()))
n_c=int(input())
sum=0
for _ in range(n_c):
    (size, p) = map(int, input().split())
    if sizes[size]>0:
        sizes[size]-=1
        sum+=p
print(sum)

# Collections -> DefaultDict Tutorial
from collections import defaultdict
n,m=map(int,input().split(' '))
A=[]
B=[]
for _ in range(n):
    A.append(input())
for _ in range(m):
    B.append(input())
d=defaultdict(list)
index=0
for k in A:
    d[k].append(index+1)
    index+=1
for z in B:
    if z in d:
        print(' '.join(map(str,d[z])))
    else:
        print(-1)

# Collections -> Collections.namedtuple()
from collections import namedtuple
N=int(input())
x=input().split()
Student=namedtuple('Student', x)
sum=0
for _ in range(N):
    i=input().split()
    s=Student(*i)
    sum+=int(s.MARKS)
print('{:.2f}'.format(sum/N))






