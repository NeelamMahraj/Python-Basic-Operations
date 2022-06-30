#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Take 2 inputs and apply (+ ,- , * , /) operation

a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# In[2]:


# Additions of different datatypes 
num1 = input("Enter Number: ")
num2 = input("Enter Number: ")

print(num1 +  num2)
# but has type string..
print(type(num1 + num2))


# In[3]:


num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))

print(num1 + num2)
# but has type integer..
print(type(num1 + num2))


# In[4]:


num1 = float(input("Enter Number: "))
num2 = float(input("Enter Number: "))

print(num1 + num2)
# but has type float..
print(type(num1 + num2))


# In[5]:


# Concatination of  greetings


greet = "Hello"
sep = " "
friends = "Pythonista"
punc = " ! "

all_in_one = greet + sep + friends + punc
print(all_in_one)


# In[15]:


print("-------Marksheet----------")
a = input("Enter marks")

if a >= '80' and a <= '90':
    print("Your grade is A+")
elif a>='70' and a<= '80':
    print("Your grade is A")
elif a>='60' and a<='70':
    print("Your grade is B")
elif a>='50' and a<='60':
    print("Your grade is C")
else :
    print("Fail") 


# In[ ]:





# In[ ]:




