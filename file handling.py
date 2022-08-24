
file_name = "source.txt"
f = open(file_name,"r")
char = f.read()
words = char.split()

number_of_characters = len(char)


print('Number of characters in text file :', number_of_characters)
print('Number of words in text file :', len(words))

count = 0
# read_data = f.read()
words = set(char.split())
for word in words:
    count += 1
    
print('Total Unique Words:', count)


f.close()
# print("done")

# f = open(file_name)
# x = f.read()
# print(x)
# f.close
# print("done")

# x = f.readline()
# print(x)

# f = open(file_name,"a")
# f.write("I am HULK")
# f.close()

# file_name = "manoj.txt"
# f = open(file_name,"w")
# print(f.read())
# f.close()

#bianry file
# 
# f = open(file_name,"wb")
# f.writelines([s1,s2,s3,s4])
# f.close()

 