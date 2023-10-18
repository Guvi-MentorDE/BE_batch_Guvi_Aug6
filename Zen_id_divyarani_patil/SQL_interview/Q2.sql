
CREATE TABLE IF NOT EXISTS employee(
    employee_id int,
    team_id int,
    primary key (employee_id)
);

insert INTO employee VALUES(1,8),(2,8),(3,8),(4,7),(5,9),(6,9);

SELECT employee_id, COUNT(team_id) OVER (PARTITION BY team_id) team_size
FROM Employee