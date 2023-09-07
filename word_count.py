def countoccurrences(store, value):
    try:
        store[value] = store[value] + 1
    except KeyError as e:
        store[value] = 1
    return


def count_word(str):
    store = {}
    list  =str.split(' ')
    for data in list:
        countoccurrences(store, data)
    for k, v in store.items():
        print( k,v )
count_word("olly olly in come olly");