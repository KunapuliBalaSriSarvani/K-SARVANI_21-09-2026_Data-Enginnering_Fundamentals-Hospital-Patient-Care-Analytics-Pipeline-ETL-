CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- The ETL pipeline creates/replaces the patient_care_analytics table.
-- After running pipeline.py, verify the loaded data:

SELECT COUNT(*) AS total_patients
FROM patient_care_analytics;

SELECT
    department,
    ROUND(AVG(waiting_minutes), 2) AS avg_waiting_minutes,
    COUNT(*) AS patient_count
FROM patient_care_analytics
GROUP BY department;

SELECT
    risk_flag,
    COUNT(*) AS patient_count
FROM patient_care_analytics
GROUP BY risk_flag;

SELECT
    patient_id,
    patient_name,
    department,
    waiting_minutes,
    risk_flag
FROM patient_care_analytics
ORDER BY risk_points DESC, waiting_minutes DESC;
