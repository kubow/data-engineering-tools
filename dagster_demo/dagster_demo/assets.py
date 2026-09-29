import pandas as pd
import subprocess
from dagster_duckdb import DuckDBResource

from dagster import AssetExecutionContext, asset

from .project import DBT_EXECUTABLE, DBT_PROJECT_DIR
from pathlib import Path

@asset
def customer_dataset(duckdb: DuckDBResource):
    dataset = Path(__file__).joinpath("..", "..", "..", "customer_profile_dataset.csv").resolve()
    # "../../customer_profile_dataset.csv"
    customer_df = pd.read_csv(dataset)
    target_table = "customer_dagster"
    with duckdb.get_connection() as conn:
        conn.execute(f"CREATE TABLE {target_table} AS SELECT * FROM customer_df")


@asset
def dbt_demo_dbt_assets(context: AssetExecutionContext):
    """Run the dbt project using its independent Python environment."""
    subprocess.run(
        [str(DBT_EXECUTABLE), "build", "--project-dir", str(DBT_PROJECT_DIR)],
        cwd=DBT_PROJECT_DIR,
        check=True,
    )
