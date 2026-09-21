-- Query 2: Funcionários por Região e Localização
SELECT 
    e.employee_id,
    e.first_name,
    e.last_name,
    e.salary,
    d.department_name,
    l.city,
    l.state_province,
    c.country_name,
    r.region_name
FROM hr.employees e
LEFT JOIN hr.departments d ON e.department_id = d.department_id
LEFT JOIN hr.locations l ON d.location_id = l.location_id
LEFT JOIN hr.countries c ON l.country_id = c.country_id
LEFT JOIN hr.regions r ON c.region_id = r.region_id
WHERE r.region_name IS NOT NULL;
