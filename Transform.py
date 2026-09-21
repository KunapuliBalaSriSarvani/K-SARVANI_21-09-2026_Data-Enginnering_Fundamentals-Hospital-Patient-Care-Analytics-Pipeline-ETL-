import pandas as pd

def transform(patients, appointments, labs, vitals, consultations):
    # Convert times to datetime so waiting time can be calculated
    appointments["scheduled_dt"] = pd.to_datetime(
        appointments["appointment_date"] + " " + appointments["scheduled_time"]
    )
    appointments["consultation_dt"] = pd.to_datetime(
        appointments["appointment_date"] + " " + appointments["consultation_time"]
    )

    appointments["waiting_minutes"] = (
        appointments["consultation_dt"] - appointments["scheduled_dt"]
    ).dt.total_seconds() / 60

    # Merge the operational and clinical sources by patient_id
    df = patients.merge(
        appointments[["appointment_id", "patient_id", "department", "status", "waiting_minutes"]],
        on="patient_id",
        how="left"
    )

    df = df.merge(
        labs[["patient_id", "test_name", "result_value", "unit", "lab_status"]],
        on="patient_id",
        how="left"
    )

    df = df.merge(
        vitals[["patient_id", "systolic_bp", "diastolic_bp", "heart_rate", "spo2"]],
        on="patient_id",
        how="left"
    )

    df = df.merge(
        consultations[["patient_id", "notes", "doctor_name"]],
        on="patient_id",
        how="left"
    )

    # Simple analytics flag for the classroom demo.
    # This is NOT a clinical diagnosis or medical decision tool.
    df["risk_points"] = 0
    df.loc[df["age"] >= 65, "risk_points"] += 1
    df.loc[df["systolic_bp"] >= 140, "risk_points"] += 1
    df.loc[df["spo2"] < 94, "risk_points"] += 1
    df.loc[df["lab_status"] == "Low", "risk_points"] += 1
    df.loc[df["waiting_minutes"] >= 60, "risk_points"] += 1

    df["risk_flag"] = df["risk_points"].apply(
        lambda x: "High" if x >= 3 else ("Medium" if x == 2 else "Low")
    )

    df["waiting_category"] = df["waiting_minutes"].apply(
        lambda x: "Long" if x >= 60 else ("Moderate" if x >= 30 else "Short")
    )

    # Keep a clean analytical table
    df.drop(columns=["registration_date"], inplace=True)

    print(f"Transformed Shape: {df.shape}")
    return df
