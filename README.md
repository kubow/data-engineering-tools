# Modern Data Engineering Solutions Overview
## Project Init

```shell
The scenarios use separate virtual environments because Airflow and recent
Prefect releases require incompatible SQLAlchemy major versions. The old
combined `requirements.in`/`requirements.txt` files are kept for comparison;
new scenario-specific inputs live under `requirements/`.

```shell
make dbt       # creates .venv/dbt and runs dbt
make dlt       # creates .venv/dlt and runs dlt
make prefect   # creates .venv/prefect and runs the Prefect flow
make airflow   # creates .venv/airflow and starts Airflow
make dagster   # creates .venv/dagster and starts Dagster
```

Dagster uses its own Python 3.14 environment. Its dbt build asset invokes the
separate `.venv/dbt` environment because the `dagster-dbt` integration family
does not currently provide a compatible Python 3.14 release. The other
scenarios can also use Python 3.14. `make lock-all` regenerates
the five scenario lockfiles without installing them.
```

1. Ensure you have duckDB source defined in `dbt_demo` profiles
2. Check that `~/dev.duckdb` exists (otherwise you need [`./duckdb`](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct))

Corresponding handling shown high-level, more detail under specific folders

## dbt demo ()

- Copy CSV files from root into seeds folder

```shell
cd dbt_demo
dbt debug
dbt build
```

## Dagster demo ()

- [Installing Dagster](https://docs.dagster.io/getting-started/installation)


```shell
python -m pip install --upgrade pip  # latest pip
# pip install -e ".[dev]"  # not needed
cd dagster_demo
dagster dev
```

## Airflow demo ()

```shell
make airflow
```


## [Prefect](https://www.prefect.io/) demo ()

```shell
make prefect
# or, for the local Prefect UI/API:
make prefect-server
```


## [dlt](https://dlthub.com/) demo ()

```shell
python dlt_demo/load_csv.py
```
