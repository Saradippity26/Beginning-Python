"""
Learn about dictionaries
"""
from pprint import pprint as pp # pretty print

def main():
    """
    Test function
    :return: 
    """
    urls = {
        "google": "www.google.com",
        "yahoo": "www.yahoo.com",
        "twitter": "www.twitter",
        "WSU": "weber.edu"}
    # dictionary {} of url's : order not accounted for in dic, members accessed by key not order
    print(urls, type(urls)) # -> {'google': 'www.google.com', 'WSU': 'weber.edu',...'} <class 'dict'>
    # access by key
    print(urls["WSU"]) # -> weber.edu

    # Build dict with dict() constructor
    names_age = [('Alice', 32), ('Mario', 23), ('Hugo', 21)] # Tuples, needs a unique key or doubles could override
    d = dict(names_age)
    print(d) # -> {'Alice': 32, 'Hugo': 21, 'Mario': 23}

    # Another method
    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta') # also builds a dict.
    print(phonetic) # -> {'c': 'charlie', 'b': 'bravo', 'd': 'delta', 'a': 'alpha'}

    # How to copy a dict: copy()
    e = phonetic.copy() # will make a shallow copy phonetic dict, reference will point to same object until edited
    print(e) # -> {'c': 'charlie', 'd': 'delta', 'a': 'alpha', 'b': 'bravo'}

    # How to update a dict: using update() method
    stocks = {'GOOG':891, 'APPL':416, 'IBM':194} # used when you need to update multiple lines at a time
    print(stocks) # -> {'GOOG': 891, 'IBM': 194, 'APPL': 416}
    stocks.update({'GOOG':999, 'YHOO':2}) # if key exists will update, if not will added
    print(stocks) # -> {'GOOG': 999, 'IBM': 194, 'YHOO': 2, 'APPL': 416}

    # Iteration: default is by key
    for key in stocks:
        print("{k} => {v}".format(k=key, v=stocks[key])) # -> GOOG => 999\n IBM => 194...

    # Iterate by values
    for val in stocks.values():
        print("val = ", val) # -> val =  416\n val =  2...

    # Iteration with both key and value items
    for items in stocks.items():
        print(items) # -> ('APPL', 416)\n ('YHOO', 2)....

    for key, val in stocks.items():
        print(key, val) # -> APPL 416 \n YHOO 2 ...

    # Test for membership via key
    print('GOOG' in stocks) # -> True
    print('WINDOWS' not in stocks) # -> True

    # Deleting: use the del keyword
    print(stocks) # -> {'YHOO': 2, 'APPL': 416, 'IBM': 194, 'GOOG': 999}
    del stocks['YHOO']
    print(stocks) # -> {'APPL': 416, 'IBM': 194, 'GOOG': 999}

    # Mutability of dict
    isotopes = { # dictionary of lists
        'H': [1, 2, 3],
        'He': [3, 4],
        'Li': [6, 7],
        'Be': [7, 9, 10],
        'B': [10, 11],
        'C': [11, 12, 13, 14]
    }
    print(isotopes) # -> {'He': [3, 4], 'Be': [7, 9, 10], 'Li': [6, 7], 'B': [10, 11], 'H': [1, 2, 3]....
    # keys are unique object may change
    isotopes['H'] += [4, 5, 6, 7] # =+ lets add a few more
    print(isotopes)
    # -> {'Li': [6, 7], 'C': [11, 12, 13, 14], 'He': [3, 4], 'Be': [7, 9, 10], 'B': [10, 11], 'H': [1, 2, 3, 4, 5, ...
    isotopes['N'] = [13, 14, 15] # if key exists it is updated if not it is appended(added)
    pp(isotopes) # print using pp pretty print
    # -> {'Li': [6, 7], 'He': [3, 4], 'Be': [7, 9, 10], 'N': [13, 14, 15], 'B': [10, 11], 'C': [11, 12, 13, 14],
    # 'H': [1, 2, 3, 4, 5, 6, 7]} ( using print(isotopes))
    """ printing with pp: pp(isotopes)
    {'B': [10, 11],
     'Be': [7, 9, 10],
     'C': [11, 12, 13, 14],
     'H': [1, 2, 3, 4, 5, 6, 7],
     'He': [3, 4],
     'Li': [6, 7],
     'N': [13, 14, 15]}
    """



if __name__ == '__main__':
    main()
    exit(0)