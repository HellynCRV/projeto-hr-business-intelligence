-- Query 3 (extra): Funcionários por Cargo e Faixa Salarial
SELECT 
    j.job_title,
    CASE 
        WHEN e.salary <= 3000 THEN 'Até 3k'
        WHEN e.salary BETWEEN 3001 AND 6000 THEN '3k - 6k'
        WHEN e.salary BETWEEN 6001 AND 10000 THEN '6k - 10k'
        ELSE 'Acima de 10k'
    END AS faixa_salarial,
    COUNT(*) AS total_funcionarios
FROM HR.EMPLOYEES e
JOIN HR.JOBS j ON e.job_id = j.job_id
GROUP BY j.job_title, faixa_salarial
ORDER BY j.job_title, faixa_salarial;
