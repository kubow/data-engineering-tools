from dagster import Definitions
from dagster_dbt import DbtCliResource
from dagster_duckdb import DuckDBResource
from .assets import dbt_demo_dbt_assets, customer_dataset
from .project import dbt_demo_project
from .schedules import schedules
from pathlib import Path

defs = Definitions(
    assets=[dbt_demo_dbt_assets, customer_dataset],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dbt_demo_project, profiles_dir=str(Path("~/.dbt").expanduser())),
        "duckdb": DuckDBResource(
            database=str(Path("~/dev.duckdb").expanduser()),
        )
    }
)
