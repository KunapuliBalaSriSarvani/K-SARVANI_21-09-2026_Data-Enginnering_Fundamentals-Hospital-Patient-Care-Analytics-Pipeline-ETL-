from extract import extract
from Transform import transform
from Validation import validate
from Load import load

def run_pipeline():
    # 1. Extract data from hospital source systems
    patients, appointments, labs, vitals, consultations = extract()

    # 2. Transform and integrate the data
    clean = transform(
        patients,
        appointments,
        labs,
        vitals,
        consultations
    )

    # 3. Validate the transformed data
    validate(clean)

    # 4. Load the final analytical dataset into MySQL
    load(clean, table_name="patient_care_analytics")

if __name__ == "__main__":
    run_pipeline()
