DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS billing;

CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    city TEXT
);

CREATE TABLE appointments (
    appointment_id TEXT PRIMARY KEY,
    patient_id TEXT,
    department TEXT,
    appointment_date DATE,
    status TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE tests (
    test_id TEXT PRIMARY KEY,
    patient_id TEXT,
    test_type TEXT,
    test_date DATE,
    turnaround_time_hours INTEGER,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE billing (
    bill_id TEXT PRIMARY KEY,
    patient_id TEXT,
    test_id TEXT,
    amount REAL,
    payment_status TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (test_id) REFERENCES tests(test_id)
);
