

dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
grid = [[' ',1,2,3,4,5,6,7,8,9,10],['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J']]
for i in range(1,11):
    for x in range(11):
        grid[i].append('~')
        

for i in range(11):
    for x in range(11):
        print(grid[i][x]," " , end='')  
    print("\n")
    

#print(grid)
#co = input("Enter coordinates here: ")
#tmp = co.split(',')
#print(tmp)
#print(dic[tmp[0]] , (int(tmp[1])))
#print(grid)


#def overlap(a):
    if a != '~':
        return "overlap"
    
def shoot():
    if shot == True:
        a = "x"
        