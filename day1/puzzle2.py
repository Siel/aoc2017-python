file=open("data/input_data.txt")
line = file.read()
sum = 0
line2 = line + line
for i in range(len(line)):
    print("comparando: "+line[i]+", con: "+line2[i+int(len(line)/2)])
    if line[i] == line2[i+int(len(line)/2)]:
        sum = sum + int(line[i])
print(sum)