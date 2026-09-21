import pandas as pd

def extract():
    patients = pd.read_csv("patients.csv")
    appointments = pd.read_csv("appointments.csv")
    labs = pd.read_csv("labs.csv")
    vitals = pd.read_csv("vitals.csv")
    consultations = pd.read_csv("consultations.csv")

    print(f"Patients: {len(patients)} rows")
    print(f"Appointments: {len(appointments)} rows")
    print(f"Labs: {len(labs)} rows")
    print(f"Vitals: {len(vitals)} rows")
    print(f"Consultations: {len(consultations)} rows")

    return patients, appointments, labs, vitals, consultations
