SELECT server_id, AVG(cpu_usage) AS avg_cpu
FROM server_metrics
GROUP BY server_id
HAVING avg_cpu < 20;
