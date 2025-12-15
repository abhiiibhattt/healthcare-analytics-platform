-- 1. Appointment completion vs no-show rate
SELECT
    status,
    COUNT(*) AS count
FROM appointments
GROUP BY status;

-- 2. Average test turnaround time by test type
SELECT
    test_type,
    ROUND(AVG(turnaround_time_hours), 2) AS avg_turnaround_hours
FROM tests
GROUP BY test_type;

-- 3. Revenue by department
SELECT
    a.department,
    SUM(b.amount) AS total_revenue
FROM billing b
JOIN appointments a
    ON b.patient_id = a.patient_id
GROUP BY a.department
ORDER BY total_revenue DESC;

-- 4. Pending vs paid bills
SELECT
    payment_status,
    COUNT(*) AS count
FROM billing
GROUP BY payment_status;

-- 5. Patient volume by city
SELECT
    city,
    COUNT(*) AS patient_count
FROM patients
GROUP BY city
ORDER BY patient_count DESC;

-- 6. High turnaround tests (potential bottlenecks)
SELECT
    test_type,
    turnaround_time_hours
FROM tests
WHERE turnaround_time_hours > 24
ORDER BY turnaround_time_hours DESC;
