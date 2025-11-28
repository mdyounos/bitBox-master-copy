fhand = open('bitBox.txt')
count=0
for line in fhand:
    count+=1
    if(count>10):
        break
    print(line)