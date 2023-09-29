-- Table Accounts:

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | name          | varchar |
-- +---------------+---------+
-- the id is the primary key for this table.
-- This table contains the account id and the user name of each account.
 

-- Table Logins:

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | login_date    | date    |
-- +---------------+---------+
-- There is no primary key for this table, it may contain duplicates.
-- This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.
 

-- Write an SQL query to find the id and the name of active users.

-- Active users are those who logged in to their accounts for 5 or more consecutive days.

-- Return the result table ordered by the id.

-- The query result format is in the following example:

-- Accounts table:
-- +----+----------+
-- | id | name     |
-- +----+----------+
-- | 1  | Winston  |
-- | 7  | Jonathan |
-- +----+----------+

-- Logins table:
-- +----+------------+
-- | id | login_date |
-- +----+------------+
-- | 7  | 2020-05-30 |
-- | 1  | 2020-05-30 |
-- | 7  | 2020-05-31 |
-- | 7  | 2020-06-01 |
-- | 7  | 2020-06-02 |
-- | 7  | 2020-06-02 |
-- | 7  | 2020-06-03 |
-- | 1  | 2020-06-07 |
-- | 7  | 2020-06-10 |
-- +----+------------+

-- Result table:
-- +----+----------+
-- | id | name     |
-- +----+----------+
-- | 7  | Jonathan |
-- +----+----------+
-- User Winston with id = 1 logged in 2 times only in 2 different days, so, Winston is not an active user.
-- User Jonathan with id = 7 logged in 7 times in 6 different days, five of them were consecutive days, so, Jonathan is an active user.

-- Solution:

CREATE TABLE accounts(id INT, name NVARCHAR(100), CONSTRAINT PK PRIMARY KEY(id));

CREATE TABLE logins(id INT, login_date DATE);

INSERT INTO accounts VALUES(1, 'Winston');
INSERT INTO accounts VALUES(7, 'Jonathan');

INSERT INTO logins VALUES(7, '2020-05-30');
INSERT INTO logins VALUES(1, '2020-05-30');
INSERT INTO logins VALUES(7, '2020-05-31');
INSERT INTO logins VALUES(7, '2020-06-01');
INSERT INTO logins VALUES(7, '2020-06-02');
INSERT INTO logins VALUES(7, '2020-06-02');
INSERT INTO logins VALUES(7, '2020-06-03');
INSERT INTO logins VALUES(1, '2020-06-07');
INSERT INTO logins VALUES(7, '2020-06-10');

SELECT * FROM accounts;

SELECT * FROM logins;

-- Only using active days

SELECT DISTINCT val.id, val.name 
FROM 
(
    SELECT accounts.id, name, ROW_NUMBER() OVER(PARTITION BY logins.id ORDER BY logins.login_date) as active_days 
    FROM accounts 
    INNER JOIN logins ON logins.id = accounts.id
) val 
WHERE val.active_days>=5;

-- 5 or more consecutive days

--Solution 1: 
SELECT final.id, final.name FROM
(SELECT gets.id, gets.name, COUNT(gets.Prev_Days) OVER(PARTITION BY gets.Prev_Days, gets.id) AS count_val, gets.Prev_Days FROM
(SELECT val.id, val.name, val.login_date, DATE_SUB(val.login_date, INTERVAL val.active_days DAY) AS Prev_Days FROM
(SELECT accounts.id, name, logins.login_date, ROW_NUMBER() OVER(PARTITION BY logins.id ORDER BY logins.login_date) as active_days 
FROM accounts 
INNER JOIN logins ON logins.id = accounts.id)
val)
gets)
final GROUP BY final.id HAVING SUM(count_val)>=5;


WITH final AS
(
    SELECT gets.id, gets.name, COUNT(gets.Prev_Days) OVER(PARTITION BY gets.Prev_Days, gets.id) AS count_val, gets.Prev_Days FROM
        (
            SELECT val.id, val.name, val.login_date, DATE_SUB(val.login_date, INTERVAL val.active_days DAY) AS Prev_Days FROM
                (
                    SELECT accounts.id, name, logins.login_date, ROW_NUMBER() OVER(PARTITION BY logins.id ORDER BY logins.login_date) as active_days 
                    FROM accounts 
                    INNER JOIN logins ON logins.id = accounts.id
                )
            val
        )
    gets
)

SELECT final.id, final.name FROM final GROUP BY final.id HAVING SUM(count_val)>=5;