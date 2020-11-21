string=input()
new_string=""
count=0
for i in string:
    if i in new_string:
        continue
    else:
        count+=1
print(count)
