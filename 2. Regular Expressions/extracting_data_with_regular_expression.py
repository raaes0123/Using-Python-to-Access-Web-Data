# Find all numbers in a text and sum them
import re
file_name = open('regex_sum_107499.txt','r')
str = file_name.read()
num_list = [int(s) for s in re.findall(r'\d+',str)]
print(sum(num_list))
