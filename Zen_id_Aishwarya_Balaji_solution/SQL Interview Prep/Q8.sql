-- Write a SQL query to find all numbers that appear at least three times consecutively.

-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+

-- Solution:

CREATE TABLE repetition(id INT, num INT);

INSERT INTO repetition VALUES(1, 1);
INSERT INTO repetition VALUES(2, 1);
INSERT INTO repetition VALUES(3, 1);
INSERT INTO repetition VALUES(4, 2);
INSERT INTO repetition VALUES(5, 1);
INSERT INTO repetition VALUES(6, 2);
INSERT INTO repetition VALUES(7, 2);

SELECT * FROM repetition;

WITH RowNumbered AS 
(
    SELECT res.num, COUNT(res.next_num) AS count_next_num 
    FROM
    (
        SELECT id, num, 
        ROW_NUMBER() OVER (PARTITION BY num ORDER BY id asc) AS row_num,
        LEAD(num) OVER (ORDER BY num) AS next_num
        FROM repetition
    ) res 
    GROUP BY res.next_num, res.num 
    HAVING COUNT(res.next_num) >= 3
)

SELECT num 
FROM RowNumbered;