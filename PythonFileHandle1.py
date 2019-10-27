file = open('location',"r")
print("ID" , '\t' ,"Name",'\t' ,"SM", '\t' ,"MM",'\t' ,"SoM",'\t',"TOTAL")
print("------------------------------------------")
for line in file:
    x = line.strip().split(',')
    if len(x) == 5:
        print(x[0], '\t', x[1], '\t', x[2], '\t', x[3], '\t', x[4], '\t', int(x[2]) + int(x[3]) + int(x[4]))
        #fileout = open('location',"a")
        #fileout.write(ft)





# (x[1],'\t',x[2],'\t',x[3],'\t' ,x[4], '\t', int(x[2],10)+ int(x[3],10)+ int(x[4],10))