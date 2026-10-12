l meaning without conversion.
Use this sample transactions table:
transaction_id	currency	transaction_type	amount
txn_1	GBP	credit	100.00
txn_2	GBP	debit	30.00
txn_3	GBP	credit	50.00
txn_4	USD	debit	20.00
txn_5	USD	debit	10.00
txn_6	EUR	credit	40.00


Write a query that returns one row per currency with:
- transaction_count
- credit_total
- debit_total
- net_amount, defined here as credits minus debits
Expected result:
currency	transaction_count	credit_total	debit_total	net_amount
EUR	1	40.00	0.00	40.00
GBP	3	150.00	30.00	120.00
USD	2	0.00	30.00	-30.00


with currency_total as (
    select currency, count(*) as transaction_count,
    sum(
        case
            when transaction_type = 'credit' then amount
            else 0 END
    ) as credit_total.
    sum(
        case 
        when transaction_type = 'debit' then amount
        else 0 END
    ) as debit_total
    from transactions group by currency
)

select cuurency, transaction_count, credit_total, debit_total, (credit_total - debit_total) as net_amount
from currency_total order by currency
