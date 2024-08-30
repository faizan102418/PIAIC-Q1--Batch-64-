number = [1,2,3,4,5,6]

def square_num(x:list[int]):
    square = []
    for num in x:
        square.append(num*num) 
    return square     
        
print(square_num(number)) 
  