# Modern Data Engineering Solutions Overview
## Project Init

```shell
python -m venv venv
source venv/bin/activate
pip install pip-tools
pip-compile --upgrade --strip-extras requirements.in  # generate latest requirements.txt
pip install -r requirements.txt  # install dependencies
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
