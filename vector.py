
vector1 = [4,1,6,1,2,8,1,6]
vector2 = []
x = 5
for i in vector1:
    if i in range(-1,3):
        vector2.append(i)
print(vector2)
while vector2.count(5)<4:
    vector2.append(x) 
print(vector2)