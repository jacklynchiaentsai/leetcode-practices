from functools import cmp_to_key
from collections import deque
"""
custom compare + dictionary + set
time: O(nlogn)
-> going through past transactions is under constant constraint of 60
space: O(n)
"""
class Transaction:
    def __init__(self, transaction_str):
        transaction_list = transaction_str.split(',')
        self.name = transaction_list[0]
        self.time = int(transaction_list[1])
        self.amount = int(transaction_list[2])
        self.city = transaction_list[3]

def compare(trans_str1, trans_str2):
        
        transaction1 = Transaction(trans_str1)
        transaction2 = Transaction(trans_str2)
        if transaction1.time < transaction2.time:
            return -1
        elif transaction1.time == transaction2.time:
            return 0
        else:
            return 1

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions.sort(key = cmp_to_key(compare))
        past_dict = {}
        invalid_set = set()
        seen_transactions = set()
        invalid_list = []
        # print(transactions)
        for i, transaction_str in enumerate(transactions):
            
            # check for duplicate transactions
            if transaction_str in seen_transactions:
                invalid_list.append(transaction_str)
                invalid_set.add(transaction_str)
                continue
            
            seen_transactions.add(transaction_str)

            cur_transaction = Transaction(transaction_str)
            
            if cur_transaction.amount > 1000:
                invalid_set.add(transaction_str)

            if cur_transaction.name not in past_dict:
                past_dict[cur_transaction.name] = collections.deque([])
            else:
                while len(past_dict[cur_transaction.name]) > 0:
                    earliest = past_dict[cur_transaction.name][0]
                    past_time, past_city, past_i = earliest

                    if cur_transaction.time - past_time > 60:
                        past_dict[cur_transaction.name].popleft()
                    else:
                        break

                iscurInvalid = False
                for past_transaction in past_dict[cur_transaction.name]:
                    past_time, past_city, past_i = past_transaction
                    if cur_transaction.time - past_time <= 60 and past_city != cur_transaction.city: 
                        invalid_set.add(transactions[past_i])
                        iscurInvalid = True
                
                if iscurInvalid:
                    invalid_set.add(transaction_str)

            past_dict[cur_transaction.name].append((cur_transaction.time, cur_transaction.city, i))

        # print(invalid_list)
        # print(invalid_set)
        invalid_list += list(invalid_set)
        return invalid_list

"""
custom sort transactions by time
past_dict = {name: deque[(time, city, i), (time, city, i)]}

for transaction_str in transactions:
    # parse values
    if name in past_dict:
        # eliminate past transactions > 60
        iscurInvalid = False
        for past_transaction in past_dict[name]:
            if within 60 min in different city:
                append to invalid_set
                iscurInvalid = True
        
        iscurInvalid -> append current to invalid_set
        else -> do amount check

convert invalid_set -> list       
"""
