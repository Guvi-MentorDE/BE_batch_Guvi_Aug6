-- Table: UserActivity

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | username      | varchar |
-- | activity      | varchar |
-- | startDate     | Date    |
-- | endDate       | Date    |
-- +---------------+---------+
-- This table does not contain primary key.
-- This table contain information about the activity performed of each user in a period of time.
-- A person with username performed a activity from startDate to endDate.

-- Write an SQL query to show the second most recent activity of each user.

-- If the user only has one activity, return that one. 

-- A user can't perform more than one activity at the same time. Return the result table in any order.

-- The query result format is in the following example:

-- UserActivity table:
-- +------------+--------------+-------------+-------------+
-- | username   | activity     | startDate   | endDate     |
-- +------------+--------------+-------------+-------------+
-- | Alice      | Travel       | 2020-02-12  | 2020-02-20  |
-- | Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
-- | Alice      | Travel       | 2020-02-24  | 2020-02-28  |
-- | Bob        | Travel       | 2020-02-11  | 2020-02-18  |
-- +------------+--------------+-------------+-------------+

-- Result table:
-- +------------+--------------+-------------+-------------+
-- | username   | activity     | startDate   | endDate     |
-- +------------+--------------+-------------+-------------+
-- | Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
-- | Bob        | Travel       | 2020-02-11  | 2020-02-18  |
-- +------------+--------------+-------------+-------------+

-- The most recent activity of Alice is Travel from 2020-02-24 to 2020-02-28, before that she was dancing from 2020-02-21 to 2020-02-23.
-- Bob only has one record, we just take that one.

--Solution

CREATE TABLE user_activity(username VARCHAR(50), activity VARCHAR(50), startDate DATE, endDate DATE);


INSERT INTO user_activity VALUES ('Alice', 'Travel', '2020-02-12', '2020-02-20');
INSERT INTO user_activity VALUES ('Alice', 'Dancing', '2020-02-21', '2020-02-23');
INSERT INTO user_activity VALUES ('Alice', 'Travel', '2020-02-24', '2020-02-28');
INSERT INTO user_activity VALUES ('Bob', 'Travel', '2020-02-11', '2020-02-18');

SELECT * FROM user_activity;

WITH active_user AS
(
    SELECT *, COALESCE(LAG(rank_on_activity, 1) OVER(ORDER BY rank_on_activity DESC), 0) AS lead_pro 
    FROM 
    (
        SELECT *, DENSE_RANK() OVER (PARTITION BY username ORDER BY startDate ASC) AS rank_on_activity  
        FROM user_activity
    ) densed
)

SELECT username, activity, startDate, endDate 
FROM active_user
WHERE lead_pro in (SELECT MAX(lead_pro) FROM active_user GROUP BY username);