#1

# def real_len(text):
#     spec_symb = "\n, \f, \r, \t, \v"
#     length = ""
#     for i in text:
#         if not i in spec_symb:
#             length += i
#     print(len(length))
# real_len("Alex\nKdfe23\t\f\v.\r")

#2

# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]


# def find_articles(key, letter_case=False):
#     new_list = []
#     for i in articles_dict:
#         for k, v in i.items():
#             if letter_case:
#                 a = str(v).find(key)
#                 if a != -1:
#                     new_list.append(i)
#                     print(new_list)
#             else:
#                 v2 = str(v).lower()
#                 key2 = key.lower()
#                 a = str(v2).find(key2)
#                 if a >= 0:
#                     new_list.append(i)
#                     print(new_list)
#     return new_list

#3

# import re
# def sanitize_phone_number(phone) -> str:
#     find = re.findall('\d+', phone)
#     numbers = "".join(find)
#     print(numbers)
# sanitize_phone_number("+ 38(050)123-32-34") 

#4

# import re
# def is_check_name(fullname, first_name):
#     n = re.findall({first_name}, fullname)   
#     if n in fullname:
#         return True
#     else:
#         return False    

#5

# import re
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         # .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):
#     numbers_cantries = {"UA": [], "JP": [], "TW": [], "SG": []}
#     for i in list_phones:
#         i = sanitize_phone_number(i)
#         jp = i.find("+81", 0, 4)
#         if jp != -1:
#             numbers_cantries["JP"].append(i)
#         sg = i.find("+65", 0, 4)
#         if sg != -1:
#             numbers_cantries["SG"].append(i)
#         tw = i.find("+886", 0, 4)
#         if tw != -1:
#             numbers_cantries["TW"].append(i)
#         ua = i.find("+38", 0, 4)
#         if ua != -1:
#             numbers_cantries["UA"].append(i)
#         for l in numbers_cantries:
#             print(l)
            
# get_phone_numbers_for_countries([" +81(050)123-32-34", "     +650503451234",
#     "+886(050)8889900","+38050-111-22-22","38050 111 22 11   "])  

#6

# import re
# def is_spam_words(text, spam_words, space_around=False):
#     for i in spam_words:
#         if space_around:
#             result = re.findall(rf"\w+{i}\w+", text)
#         else:
#             result = re.findall(i, text, re.I)
#     if result:
#         print("True")
#     else:
#         print("False")
#     return(print(is_spam_words))    
# is_spam_words("Ты хорош, но выглядишь как лох", "лох", space_around=False)

#7

# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
# TRANS = {}
# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()
# def translate(name):
#     transtaled = name.translate(TRANS)
#     print(transtaled)
# translate("абвг")

# 8

# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
# def formatted_grades(students):
#     el = []
#     c = 1
#     for k, v in students.items():
#         el.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(c, k, v, grades[v]))
#         c += 1
#     return el

# for el in formatted_grades(students):
#     print(el)

#9

# el = []
# head = "|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')
# el.append(head)
# for i in range(16):    
#     # h = '{0:x}'.format(i)
#     # b = '{0:b}'.format(i)
#     s = "|{:^10}|{:^10}|{:^10}|".format("{0:d}".format(i), "{0:x}".format(i), "{0:b}".format(i))
#     el.append(s)
# print(el)

#10




      
    
    
    
        
  
        
        
            

    
        
        
        
            
        
        
            
        
        
            
        
        
            
        
            
    
                

        
        
    
    
        
    
        
        
        
            
        
        
            
        
        
            
        
        
            
        
            
    