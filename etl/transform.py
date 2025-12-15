import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("../data/raw")
PROCESSED_DATA_PATH = Path("../data/processed")

def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

def main():
    patients = pd.read_csv(RAW_DATA_PATH / "patients.csv")
    appointments = pd.read_csv(RAW_DATA_PATH / "appointments.csv")
    tests = pd.read_csv(RAW_DATA_PATH / "tests.csv")
    billing = pd.read_csv(RAW_DATA_PATH / "billing.csv")

    # Standardize columns
    patients = clean_columns(patients)
    appointments = clean_columns(appointments)
    tests = clean_columns(tests)
    billing = clean_columns(billing)

    # Drop duplicates
    patients.drop_duplicates(inplace=True)
    appointments.drop_duplicates(inplace=True)
    tests.drop_duplicates(inplace=True)
    billing.drop_duplicates(inplace=True)

    # Convert dates
    appointments["appointment_date"] = pd.to_datetime(appointments["appointment_date"])
    tests["test_date"] = pd.to_datetime(tests["test_date"])

    # Validate patient_id relationships
    valid_patients = set(patients["patient_id"])

    appointments = appointments[appointments["patient_id"].isin(valid_patients)]
    tests = tests[tests["patient_id"].isin(valid_patients)]
    billing = billing[billing["patient_id"].isin(valid_patients)]

    # Save cleaned data
    PROCESSED_DATA_PATH.mkdir(exist_ok=True)

    patients.to_csv(PROCESSED_DATA_PATH / "patients_clean.csv", index=False)
    appointments.to_csv(PROCESSED_DATA_PATH / "appointments_clean.csv", index=False)
    tests.to_csv(PROCESSED_DATA_PATH / "tests_clean.csv", index=False)
    billing.to_csv(PROCESSED_DATA_PATH / "billing_clean.csv", index=False)

    print("Data cleaning and transformation completed successfully.")

if __name__ == "__main__":
    main()
