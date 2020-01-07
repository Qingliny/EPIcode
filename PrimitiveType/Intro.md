# Integer
Python has unbounded integers- The maximun integer is a function of available memory.
constant: sys.maxsize

float("inf")
float('-inf')

# Bitwise operator 
and & :  ```6&4 -> 110 & 100 -> 100 -> 4  ```.  
or  | :  ```1|2 -> 01 | 10 -> 11 -> 3  ```.   
右移 >> ：```8 >> 2 -> 1000 >> 2 -> 0010 -> 2			#相当于除4  ```.    
	``` -16 >> 2 -> -10000 >> 2 -> -100 -> -4		```.   
左移 << : ``` 1 << 2 -> 1 << 2 -> 100 -> 4				#相当于乘4```.    
no  ~ :  ``` ~0 -> -1  -> ~x = -x-1  有符号的二进制数按位取反，x的补码 ```.    
xor ^ :  ```2 ^ 3 -> 10 ^ 11 -> 01 -> 1	  ```.    

**x & (x-1) == x with its lowest set bit erased**.   
**x & ～(x-1) == isolate the lowest bit that is 1 in x**.   
_use to lower the time complexity_.   
x = 11010   
res = 11000    

# numeric type
abs(-34.5)  
math.ceil(2.17)  
math.floor(3.14)   
min(x, -4)   
max(3.14, y)   
pow(2.71, 3.14) 2.71^3.14
math.sqrt(225)

# interconvert   
str()
float()

# random
random.randrange(28). -> generate an integer in 28.   
random.randint(8,16). -> generate an integer  
random.random(). -> generate float
random.choice(A). -> A is a list or any sequence
random.shuffle(A). -> 
```python
number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]  
random.shuffle(number_list)  
print("List after first shuffle  : ", number_list) 
```
# 4.1 Parity
##### parity of a binary word is 1 if the number of 1s in the word is odd, otherwise, it is 0   
parity of 1001100 is 1, 10001110 is 0.   

# 4.2 swap bits
Use **BitMask** and **XOR** to flip the value.   
x XOR 1:    
if x == 0: x^1 = 1;    
if x == 1: x^1 = 0;    











