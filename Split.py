file =open('location',"r")
for line in file:
    x=line.split(",")
    print(x[1],'\t',x[2],'\t',x[3],'\t' ,x[4], '\t', int(x[2],10)+ int(x[3],10)+ int(x[4],10))
