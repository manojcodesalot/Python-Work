st = "hello python"
# __add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__len__
# ', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
#  'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
# 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
#  'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# #  'title', 'translate', 'upper', 'zfill']
# print(dir(st))


# #16-07-2022

# #'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
# # 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# #  'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# #   'isupper', 'rindex', 'rfind', 'upper', 'lower', 'ljust', 'rjust',]
# print(st)
# st1 = st.capitalize()
# print(st1)
# st2 = st1.casefold()
# print(st2)
print(st1.casefold.__doc__)
# y = st.find("o")
# print(y)
# q = st.index("o")
# print(q)
# print("someone".isspace())
# print("ABC".isupper())
# print("makicharan".rindex("c"))
# st4 = st.upper()
# print(st4)
# st5 = st.lower()
# print(st5)
# print(st.removeprefix("hello"))
# print(st.removesuffix("Wolrd"))
# print(st.startswith("hello"))
# print(st.endswith("Wolrd"))
#print(st.swapcase())
#print(st.zfill(85))
# print(st.title())
mac = "a b c d e f g"
print(mac.split())
l1 = "a e d r t"
l2 = "1 2 3 4 5"
m = str.maketrans(l1,l2)




