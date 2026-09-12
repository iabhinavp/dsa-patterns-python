def has_dups_transaction_ids(transactions):
    ids = set()
    for id in transactions:
        if id in ids:
            return True
        ids.add(id)
    return False    


print(has_dups_transaction_ids(["trans1", "trans2", "trans3"]))
print(has_dups_transaction_ids(["trans1", "trans1", "trans3"]))