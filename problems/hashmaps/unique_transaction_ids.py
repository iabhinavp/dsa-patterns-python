def unique_transaction_ids(transactions: list[str]) -> list[str]:
    seen_once_frequency = {}
    final_result = []
    for transaction in transactions:
        if transaction in seen_once_frequency:
          seen_once_frequency[transaction] = seen_once_frequency[transaction] + 1
        else:
          seen_once_frequency[transaction] = 1

    for id in transactions:
       if seen_once_frequency[id] == 1:
          final_result.append(id)   

    return final_result


print(
    unique_transaction_ids(
        ["txn_1", "txn_2", "txn_1", "txn_3", "txn_4", "txn_3"]
    )
)
# Expected: ["txn_2", "txn_4"]

print(unique_transaction_ids([]))
# Expected: []

print(unique_transaction_ids(["txn_1", "txn_2"]))
# Expected: ["txn_1", "txn_2"]

print(unique_transaction_ids(["txn_1", "txn_1", "txn_1"]))
# Expected: []