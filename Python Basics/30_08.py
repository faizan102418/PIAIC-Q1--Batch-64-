# number = [1,2,3,4,5,6]

# def square_num(x:list[int]):
#     square = []
#     for num in x:
#         square.append(num*num) 
#     return square     
        
# print(square_num(number)) 
  
  
numbers = [1,2,3,4,5]

square = list(map(lambda x : x * x ,numbers))
print(square) 

# squared_num = list(map(lambda x: x * x , numbers))
# print(squared_num)

x = range(6)

# print(x[1],x[2],x[0],x[3],x[4],x[5])

# for n in x:
#     print(n)
    
    
# for n in range(6):
#     print(n)    

for x in range(2,6,2):
    print(x)