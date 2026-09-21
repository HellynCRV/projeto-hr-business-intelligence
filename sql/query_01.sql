-- Query 1: Como os salários estão distribuídos entre os departamentos e cargos

-- Etapa inicial: apenas funcionários e seus IDs de departamento
-- SELECT
--     e.EMPLOYEE_ID,
--     e.FIRST_NAME,
--     e.LAST_NAME,
--     e.SALARY,
--     e.JOB_ID,
--     e.DEPARTMENT_ID
-- FROM HR.EMPLOYEES e;

-- Etapa intermediária: adicionando nome do departamento
-- SELECT
--     e.EMPLOYEE_ID,
--     e.FIRST_NAME,
--     e.LAST_NAME,
--     e.SALARY,
--     e.JOB_ID,
--     e.DEPARTMENT_ID,
--     d.DEPARTMENT_NAME
-- FROM HR.EMPLOYEES e
-- LEFT JOIN HR.DEPARTMENTS d
--     ON e.DEPARTMENT_ID = d.DEPARTMENT_ID;

-- Etapa intermediária: adicionando nome do cargo
-- SELECT
--     e.EMPLOYEE_ID,
--     e.FIRST_NAME,
--     e.LAST_NAME,
--     e.SALARY,
--     d.DEPARTMENT_NAME,
--     j.JOB_TITLE
-- FROM HR.EMPLOYEES e
-- LEFT JOIN HR.DEPARTMENTS d
--     ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
-- LEFT JOIN HR.JOBS j
--     ON e.JOB_ID = j.JOB_ID;

-- Resultado final da Query 1 (executável):
SELECT
    e.EMPLOYEE_ID,
    e.FIRST_NAME,
    e.LAST_NAME,
    e.SALARY,
    d.DEPARTMENT_NAME,
    j.JOB_TITLE
FROM HR.EMPLOYEES e
LEFT JOIN HR.DEPARTMENTS d
    ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN HR.JOBS j
    ON e.JOB_ID = j.JOB_ID
WHERE e.SALARY > 0;