# airflow_demo/dags/dbt_build.py
from __future__ import annotations
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from pathlib import Path
import sys, shlex

REPO_ROOT = Path(__file__).resolve().parents[2]
DBT_PROJECT_DIR = REPO_ROOT / "dbt_demo"

# Absolute path to the dbt binary inside THIS venv (the one running Airflow)
DBT_BIN = Path(sys.executable).with_name("dbt")
DBT = shlex.quote(str(DBT_BIN))
PROJ = shlex.quote(str(DBT_PROJECT_DIR))

with DAG(
    dag_id="dbt_demo_build",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dbt", "duckdb", "demo"],
) as dag:
    version = BashOperator(
        task_id="dbt_version",
        bash_command=f"{DBT} --version",
    )

    # Only run deps if packages.yml exists (otherwise skip gracefully)
    deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"cd {PROJ} && [ -f packages.yml ] && {DBT} deps || echo 'No packages.yml, skipping deps'",
    )

    seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"cd {PROJ} && {DBT} seed",
    )

    build = BashOperator(
        task_id="dbt_build",
        bash_command=f"cd {PROJ} && {DBT} build",
    )

    version >> deps >> seed >> build
