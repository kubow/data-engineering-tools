import pandas as pd
from dagster_duckdb import DuckDBResource

from dagster import AssetExecutionContext, asset
from dagster_dbt import DbtCliResource, dbt_assets

from .project import dbt_demo_project
from pathlib import Path

@asset
def customer_dataset(duckdb: DuckDBResource):
    dataset = Path(__file__).joinpath("..", "..", "..", "customer_profile_dataset.csv").resolve()
    # "../../customer_profile_dataset.csv"
    customer_df = pd.read_csv(dataset)
    target_table = "customer_dagster"
    with duckdb.get_connection() as conn:
        conn.execute(f"CREATE TABLE {target_table} AS SELECT * FROM customer_df")


@dbt_assets(manifest=dbt_demo_project.manifest_path)
def dbt_demo_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
