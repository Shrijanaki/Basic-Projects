# -*- coding: utf-8 -*-
"""Password.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14qvnOXq64Kp2Sn1EMPr8M0NynmbPozg-
"""

import random 

length = 12
  
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z']
  
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*'] 
  


  

digits = random.choice(num) 
uppercase = random.choice(upper) 
lowercase = random.choice(lower) 
symbol = random.choice(symbols)

together = digits + uppercase + lowercase + symbol 

password = ''
password = password.join(random.choice(together)for i in range(1, length))
print("The password:",password)