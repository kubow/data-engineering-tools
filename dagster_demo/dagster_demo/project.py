from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DBT_PROJECT_DIR = REPO_ROOT / "dbt_demo"
DBT_EXECUTABLE = REPO_ROOT / ".venv" / "dbt" / "bin" / "dbt"
