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
from currency_total 
where transaction_count > 1
and (credit_total - debit_total) > 100
order by currency



===============================================================================================


transaction_id	currency	amount
txn_1	GBP	100
txn_2	GBP	NULL
txn_3	GBP	30
txn_4	USD	NULL
txn_5	USD	NULL


The rules are:
- COUNT(*) counts every row.
- COUNT(amount) counts rows with a non-null amount.
- SUM(amount) adds non-null amounts.
- AVG(amount) averages non-null amounts.
- When a group contains only null amounts, SUM and AVG return NULL.

select cuurency, count(*) as row_count, 

======================================================

SELECT
    c.currency,
    COUNT(t.transaction_id)
        FILTER (WHERE t.transaction_type = 'credit') AS credit_count,
    COALESCE(
        SUM(t.amount) FILTER (WHERE t.transaction_type = 'credit'),
        0
    ) AS credit_total
FROM currencies AS c
LEFT JOIN transactions AS t
    ON t.currency = c.currency
GROUP BY c.currency
ORDER BY c.currency;



==================================================

Use these sample tables:
currencies: GBP, USD, EUR, JPY
transaction_id	currency	transaction_type	amount
txn_1	GBP	credit	100
txn_2	GBP	debit	30
txn_3	USD	debit	20


Write a query returning every supported currency, with its credit count and credit total:
currency	credit_count	credit_total
EUR	0	0
GBP	1	100
JPY	0	0
USD	0	0

select t.cuurency, count(t.transaction_id) filter (where t.transaction_type = 'credit') as credit_count,
COALESCE(sum(t.amount) filter (where t.transaction_type = 'credit') as credit_total, 0)
from currencies c left join 
transactions t on c.currency = t.cuurency
group by currency
order by currency 

====================================

Our requirement is:
Return the most recently created transaction for each currency present in transactions.

Assume these transactions were created on the same day:
transaction_id	currency	amount	created_at
txn_1	GBP	100	09:00
txn_2	GBP	30	10:00
txn_3	USD	200	09:30
txn_4	USD	50	11:00


with ranked_transactions (
    select transaction_id, currency, amount, created_at,
    row_number() over ( partition by currency order by created_at desc, transaction_id desc)
    as rn
    from transactions
)
select transaction_id, cuurency, amount, created_at from ranked_transactions where rn =1 order by currency

========================================================================

Running total -

select transaction_id, currency, amount, created_at,
sum(amount) over (partition by currency order by created_at asc, transaction_id asc
                    rows between unbounded preceding and current row) as running_total
from transactions order by currency, transaction_id, created_at


===================================================

Previous amount -

| Transaction | Currency | Amount | Previous Amount |
| --- | --- | ---: | ---: |
| txn_1 | GBP | 100 | NULL |
| txn_2 | GBP | 30 | 100 |
| txn_3 | GBP | 50 | 30 |
| txn_4 | USD | 20 | NULL |

WITH transaction_history AS (
    SELECT
        transaction_id,
        currency,
        amount,
        created_at,
        LAG(amount) OVER (
            PARTITION BY currency
            ORDER BY created_at ASC, transaction_id ASC
        ) AS previous_amount
    FROM transactions
)
SELECT
    transaction_id,
    currency,
    amount,
    created_at,
    previous_amount,
    amount - previous_amount AS amount_change
FROM transaction_history
ORDER BY currency, created_at DESC, transaction_id DESC;