# screening-test

### 1. password_generator.py
the program generates a password of length 8 which
have a minimum number and one minimum upper
case character.

### 2. get rolling sum total of sales using window function
query : SELECT distinct date, SUM(sales) OVER (PARTITION by date) as Sales FROM table1;

### 3. create a view that only shows the most updated transactions for each id
query : CREATE VIEW vw_transaction AS 
SELECT a.id,a.insert_time,a.tx_amount,a.tx_type,a.status FROM trx a
INNER JOIN (
	SELECT MAX (insert_time) insert_time, id FROM trx GROUP BY id
) b ON a.id = b.id AND a.insert_time = b.insert_time

### 4. json_to_csv.py
create automation that converts JSON file into 3 categories CSV 
