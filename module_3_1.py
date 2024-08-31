calls = 0
def count_calls():
    global calls
    calls = calls+1
def string_info(string):
         count_calls()
         t = (len(string), string.upper(), string.lower())
         return t
def is_contains(string, list_to_search):
    count_calls()
    n = string.upper()
    uppercase_list = [s.upper() for s in list_to_search]
    if n in uppercase_list:
        return True
    else:
        return False














#     print(new_list_to_search)
#     if string in new_list_to_search:
#          return True
#     else:
#          False
#
print(string_info('Capibara'))
print(string_info('Армагеддон'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling',  'cyclik']))
print(calls)

















    




























