from sqlalchemy import create_engine
from Config import DB_CONFIG

def load(df, table_name="patient_care_analytics"):
    conn_str = (
        f"mysql+mysqlconnector://"
        f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
    )

    engine = create_engine(conn_str)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into '{table_name}' table")
