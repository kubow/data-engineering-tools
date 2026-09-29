# dlt_demo/load_csv.py
import dlt
from dlt.sources.filesystem import filesystem, read_csv

p = dlt.pipeline(
    pipeline_name="csv2duckdb",
    destination="duckdb",
    dataset_name="raw",
    # by default creates a duckdb file in .dlt; you can pass duckdb_path=... in destination_kwargs
)
csv_files = filesystem(bucket_url=".", file_glob="*.csv") | read_csv()
info = p.run(csv_files)
print(info)
