from typing import Counter


a_file = open("/Users/Lenovo/Desktop/ListMaker/sample.txt", "r",encoding="utf8")

result = ''

result = result + '{ '
count = 0
result = result + str(count) + ' : ' + '['
list_of_lists = []
for line in a_file:
  if line == '\n':  
      result = result + ']' + ', '
      count+=1
      result = result + str(count) + ' : ' + '['
  else:
    stripped_line = line.strip()
    line_list = stripped_line
    result = result + '\'' + line_list  + '\'' + ', '
    

a_file.close()
result = result + ']'
result = result + '} '

print(result)
