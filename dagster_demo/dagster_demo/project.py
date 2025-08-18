from pathlib import Path

from dagster_dbt import DbtProject

dbt_demo_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt_demo").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)