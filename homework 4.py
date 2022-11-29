# 1

# def amount_payment(payment):
#     sum = 0
#     for value in payment:
#         if value > 0:
#             sum = sum + value
#     print(sum)
# amount_payment([1, -3, 4])    

#2

# def prepare_data(data):
#     data.remove(max(data))
#     data.remove(min(data))
#     data.sort(data)
#     return(data)

#3

# def format_ingredients(items):
#     if len(items) < 2:
#         str_items = f"{' '.join(items[:])}"
#         print(items)
#     else:    
#         print(len(items))
#         items.insert(-1, "and")
#         and_plus = items[-3:]
#         new_str = " ".join(and_plus)
#         items.pop(-1)
#         items.pop(-1)
#         items.pop(-1)
#         new_str2 = ", ".join(items)
#         print(f"{new_str2}, {new_str}")
# format_ingredients(["2 eggs"])

#4

# def get_grade(key):
#     grades = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
#     if key in grades:
#         print(grades.get(key))
#     else:
#         print("None") 
        
        
# def get_description(key):
#     description = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
#     if key in description:
#         print(description.get(key))
#     else:
#         print("None")
        
# get_grade(input())
# get_description(input())   

#5

# def lookup_key(data, value):
#     result = []
#     for k, v in data.items():
#         if v == value:
#             result.append(k)
#     return result   

#6

# def split_list(grade):
#     if len(grade) == 0:
#         return [], []
        
#     elif len(grade) == 1:
#         first.append(grade)
#         return grade, [] 
#     else:
#         middle = sum(grade) / len(grade)
#         for i in grade:
#             if i <= middle:
#                 first.append(i)
#             else:
#                 second.append(i)
#         return first, second 

#7

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }
# def calculate_distance(coordinates):
#     result = 0
#     spusok = []
#     for i in range(0, len(coordinates)-1):
#             if coordinates[i] > coordinates[i + 1]:
#                 spusok.append(((coordinates[i+1], coordinates[i])))
#             else:
#                 spusok.append(((coordinates[i], coordinates[i + 1])))    
#     for coord in spusok:
#         result += points.get(coord)
#     return result            
            
#8

# def game(terra, power):
#     energy = power
#     for i in terra:
#         for num in i:
#             if num <= energy:
#                 energy += num
#             else:
#                 break
#     return energy
            
#9
 
# def is_valid_pin_codes(pin_codes):
#     flag = False
#     if len(pin_codes) == len(set(pin_codes)):
#         for i in pin_codes:
#             if i and len(i) == 4 and isinstance(i, str) and i.isnumeric():
#                 flag = True
#             else:
#                 flag = False
#     return flag

#10

# from random import randint
# def get_random_password():
#     password = ""
#     i = 0
#     while i <= 7:
#         random_num = randint(40, 126)
#         password += chr(random_num)
#         i += 1
#     return password

#11

# def is_valid_password(password):
#     symb = "abcdefghijklmnopqrstuvwxyz"
#     cap_symb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     cyfr = "0123456789"
#     lenght = None
#     symbol = None
#     cap_symbol = None
#     nomer = None
#     if len(password) == 8:
#         lenght = True
#     for chr in password:
#         if chr in symb:
#             symbol = True
#     for cap in password:
#         if cap in cap_symb:        
#             cap_symbol = True
#     for num in password:
#         if num in cyfr:
#             nomer = True
#     if lenght == True and symbol == True and cap_symbol == True and nomer == True:
#         return True      
#     else:
#         return False

#12
    
# from random import randint


# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result


# def is_valid_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False


# def get_password():
#     flag = True   
#     while flag:
#         password = get_random_password()
#         valid = is_valid_password(password)
#         if valid == True:                
#             flag = False
#             return password
#         else:
#             get_password() in range(100)

#13

# from pathlib import Path
# def parse_folder(path):
#     files = []
#     folders = []
#     for i in path.iterdir():
#         if i.is_dir():
#             folders.append(i.name)
#         elif i.is_file():
#             files.append(i.name)
#     return files, folders
        
#14

# import sys
# def parse_args():
#     result = ""
#     list = []
#     for arg in sys.argv[1::]:
#         list.append(arg) 
#         result = " ".join(list)
#     return result
            
        
        
            
    
    
    
    
    
    
    
        
        
        
    
    
    
    
    
    
        
            
        
            
        
            
    
        
    

       
     
      
        
        
        
              
            
        
    
        
        
         

