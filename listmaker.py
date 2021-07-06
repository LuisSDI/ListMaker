

a_file = open("/Users/Lenovo/Desktop/ListMaker/sample.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line
  list_of_lists.append(line_list)

a_file.close()

print(list_of_lists)