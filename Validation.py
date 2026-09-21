def validate(df):
    assert df.isnull().sum().sum() == 0, "Dataframe still contains null values"
    assert df["patient_id"].notnull().all(), "Patient ID contains null values"
    assert df["waiting_minutes"].ge(0).all(), "Waiting time cannot be negative"
    assert df["risk_flag"].isin(["Low", "Medium", "High"]).all(), "Invalid risk flag"
    assert df["age"].ge(0).all(), "Age cannot be negative"

    print("Validation Passed")
