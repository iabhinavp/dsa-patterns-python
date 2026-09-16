def group_transaction_ids_by_status(transactions: list[dict]) -> dict[str, list[str]]:
    groupby_status = {}

    for transaction in transactions:
        transaction_status = transaction["status"]
        transaction_id = transaction["id"]
        
        if transaction_status not in groupby_status:
            groupby_status[transaction_status] = []
        
        groupby_status[transaction_status].append(transaction_id)

    return groupby_status

transactions = [
    {"id": "txn_1", "status": "accepted"},
    {"id": "txn_2", "status": "failed"},
    {"id": "txn_3", "status": "accepted"},
]

print(group_transaction_ids_by_status(transactions))