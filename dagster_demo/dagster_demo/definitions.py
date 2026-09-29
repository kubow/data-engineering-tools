from dagster import Definitions
from dagster_duckdb import DuckDBResource
from .assets import dbt_demo_dbt_assets, customer_dataset
from .schedules import schedules
from pathlib import Path

defs = Definitions(
    assets=[dbt_demo_dbt_assets, customer_dataset],
    schedules=schedules,
    resources={
        "duckdb": DuckDBResource(
            database=str(Path("~/dev.duckdb").expanduser()),
        )
    }
)
