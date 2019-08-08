#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    if length < 2:
        return None
    
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    for i, weight in enumerate(weights):
        value = hash_table_retrieve(ht, limit - weight)
        if value != None:
            if value > i:
                return (value, i)
            return (i, value)



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
