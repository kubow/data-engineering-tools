# prefect_demo/flow.py
from prefect import flow, task
from pathlib import Path
import subprocess, sys

@task
def dbt_build():
    repo = Path(__file__).resolve().parents[1]
    dbt = Path(sys.executable).with_name("dbt")
    subprocess.run([str(dbt), "build"], cwd=repo/"dbt_demo", check=True)

@flow
def demo():
    dbt_build()

if __name__ == "__main__":
    demo()
