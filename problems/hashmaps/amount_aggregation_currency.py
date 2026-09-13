def total_amount_by_currency(transactions: list[dict]) -> dict:
    totals_by_currency = {}

    for transaction in transactions:
        currency = transaction["currency"]

        if currency in totals_by_currency:
            totals_by_currency[currency] = (
                totals_by_currency[currency] + transaction["amount"]
            )
        else:
            totals_by_currency[currency] = transaction["amount"]

    return totals_by_currency


transactions = [
    {"amount": 10, "currency": "GBP"},
    {"amount": 15, "currency": "USD"},
    {"amount": 5, "currency": "GBP"},
]

print(total_amount_by_currency(transactions=transactions))