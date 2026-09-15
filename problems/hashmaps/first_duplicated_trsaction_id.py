def first_repeated_transaction_id(transaction_ids: list[str]) -> str | None:
    seen = set()

    for transaction in transaction_ids:
        if transaction in seen:
            return transaction

        seen.add(transaction)

    return None

print(first_repeated_transaction_id(["txn_1", "txn_2", "txn_1"]))
print(first_repeated_transaction_id(["txn_1", "txn_2", "txn_3", "txn_2", "txn_1"]))
print(first_repeated_transaction_id(["txn_1", "txn_2", "txn_3"]))