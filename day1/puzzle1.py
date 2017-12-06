file=open("data/input_data.txt")
line = file.read()
if line[0] == line[len(line)-1]:
    sum = int(line[0])
else:
    sum = 0
for i in range(len(line)-1):
    if line[i] == line[i+1]:
        sum = sum + int(line[i])
print(sum)