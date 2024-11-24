USE covid_db;

SELECT departamento_nom, COUNT(*) AS case_count
FROM covid_data
GROUP BY departamento_nom
ORDER BY case_count DESC
LIMIT 20;