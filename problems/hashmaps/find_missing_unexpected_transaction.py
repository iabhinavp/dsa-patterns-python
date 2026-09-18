def find_missing_unexpected_transaction(expected: list[str], processed: list[str]) -> dict[str, list[str]]:
    missing = []
    unexpected = []

    transaction_frequency = {}
    processed_frequency = {}

    for trax in expected:
        transaction_frequency[trax] = transaction_frequency.get(trax, 0) + 1

    for trax in processed:
        processed_frequency[trax] = processed_frequency.get(trax, 0) + 1

    for trax in processed:
        if transaction_frequency.get(trax, 0) > 0:
            transaction_frequency[trax] -= 1
        else:
            unexpected.append(trax)

    for trax in expected:
        if processed_frequency.get(trax, 0) > 0:
            processed_frequency[trax] -= 1
        else:
            missing.append(trax)
  
    return {
        "missing": missing,
        "unexpected": unexpected
    }
   
    



print(
    find_missing_unexpected_transaction(
        expected=["txn_1", "txn_1", "txn_2", "txn_3"],
        processed=["txn_1", "txn_2", "txn_2", "txn_4"],
    )
)

print(find_missing_unexpected_transaction([], []))

print(
    find_missing_unexpected_transaction(
        expected=["txn_1", "txn_1", "txn_2"],
        processed=["txn_1", "txn_2", "txn_2"],
    )
)


