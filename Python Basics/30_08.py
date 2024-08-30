# number = [1,2,3,4,5,6]

# def square_num(x:list[int]):
#     square = []
#     for num in x:
#         square.append(num*num) 
#     return square     
        
# print(square_num(number)) 
  
  
numbers = [1,2,3,4,5]

square = map(lambda x : x * x ,numbers)
print(type(square))  

# squared_num = list(map(lambda x: x * x , numbers))
# print(squared_num)