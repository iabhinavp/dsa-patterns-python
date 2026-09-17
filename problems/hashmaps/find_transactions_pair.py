def find_transaction_pair(transactions: list[dict], target: int) -> tuple[str, str] | None:
    transaction_by_amount={}

    for transaction in transactions:
        amount = transaction["amount"]
        difference_amount = target - amount

        if difference_amount in transaction_by_amount:
            return (
                transaction_by_amount[difference_amount],
                transaction["id"]
            )
        transaction_by_amount[amount] = transaction["id"]

    return None


print(
    find_transaction_pair(
        [
            {"id": "txn_1", "amount": 40},
            {"id": "txn_2", "amount": 20},
            {"id": "txn_3", "amount": 60},
        ],
        100,
    )
)
# Expected: ("txn_1", "txn_3")


print(
    find_transaction_pair(
        [
            {"id": "txn_1", "amount": 25},
            {"id": "txn_2", "amount": 25},
        ],
        50,
    )
)
# Expected: ("txn_1", "txn_2")
# It must use two different transactions.


print(
    find_transaction_pair(
        [
            {"id": "txn_1", "amount": 10},
            {"id": "txn_2", "amount": 20},
        ],
        100,
    )
)
# Expected: None


print(find_transaction_pair([], 100))
# Expected: None


print(
    find_transaction_pair(
        [{"id": "txn_1", "amount": 50}],
        100,
    )
)
# Expected: None
# A transaction cannot be paired with itself.