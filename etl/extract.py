import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("../data/raw")

def load_csv(filename):
    return pd.read_csv(RAW_DATA_PATH / filename)

if __name__ == "__main__":
    patients = load_csv("patients.csv")
    appointments = load_csv("appointments.csv")
    tests = load_csv("tests.csv")
    billing = load_csv("billing.csv")

    print("Patients:", patients.shape)
    print("Appointments:", appointments.shape)
    print("Tests:", tests.shape)
    print("Billing:", billing.shape)
