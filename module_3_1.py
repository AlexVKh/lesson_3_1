def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple = ()
    tuple += len(string), string.upper(), string.lower()
    return tuple

def is_contains(string, list_to_search):
    count_calls()
    i = 0
    is_contains = False
    while i < len(list_to_search):
        if str(list_to_search[i]).lower() == string.lower():
            is_contains = True
            break
        i += 1
    return is_contains

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
