SHELL := /bin/bash

PYTHON ?= python3.14
DAGSTER_PYTHON ?= python3.14
VENV_ROOT ?= .venv
REQ_ROOT ?= requirements

DBT_PY := $(VENV_ROOT)/dbt/bin/python
DBT_BIN := $(VENV_ROOT)/dbt/bin/dbt
DLT_PY := $(VENV_ROOT)/dlt/bin/python
PREFECT_PY := $(VENV_ROOT)/prefect/bin/python
AIRFLOW_PY := $(VENV_ROOT)/airflow/bin/python
DAGSTER_PY := $(VENV_ROOT)/dagster/bin/python

.PHONY: help lock-all install-all dbt dlt prefect prefect-server airflow dagster \
        venv-dbt venv-dlt venv-prefect venv-airflow venv-dagster clean-venvs

help:
	@echo "Usage: make [PYTHON=python3.14] <scenario>"
	@echo ""
	@echo "Scenarios: dbt, dlt, prefect, prefect-server, airflow, dagster"
	@echo "Prepare only: venv-dbt, venv-dlt, venv-prefect, venv-airflow, venv-dagster"
	@echo "Regenerate locks: lock-all"
	@echo "Dagster uses DAGSTER_PYTHON=$(DAGSTER_PYTHON)"

define PREPARE_ENV
	$(2) -m venv --clear $(VENV_ROOT)/$(1)
	$(VENV_ROOT)/$(1)/bin/python -m pip install --upgrade pip pip-tools
	$(VENV_ROOT)/$(1)/bin/pip-compile --upgrade --strip-extras \
		--output-file=$(REQ_ROOT)/$(1).txt $(REQ_ROOT)/$(1).in
	$(VENV_ROOT)/$(1)/bin/pip install --requirement=$(REQ_ROOT)/$(1).txt
endef

venv-dbt:
	$(call PREPARE_ENV,dbt,$(PYTHON))

venv-dlt:
	$(call PREPARE_ENV,dlt,$(PYTHON))

venv-prefect:
	$(call PREPARE_ENV,prefect,$(PYTHON))

venv-airflow:
	$(call PREPARE_ENV,airflow,$(PYTHON))

venv-dagster:
	$(call PREPARE_ENV,dagster,$(DAGSTER_PYTHON))

lock-all:
	@for scenario in dbt dlt prefect airflow dagster; do \
		$(PYTHON) -m piptools compile --upgrade --strip-extras \
			--output-file=$(REQ_ROOT)/$$scenario.txt $(REQ_ROOT)/$$scenario.in || exit $$?; \
	done

install-all: venv-dbt venv-dlt venv-prefect venv-airflow venv-dagster

dbt: venv-dbt
	$(DBT_BIN) build --project-dir dbt_demo

dlt: venv-dlt
	$(DLT_PY) dlt_demo/load_csv.py

prefect: venv-prefect
	$(PREFECT_PY) prefect_demo/flow.py

prefect-server: venv-prefect
	$(VENV_ROOT)/prefect/bin/prefect server start

airflow: venv-airflow
	AIRFLOW_HOME=$(CURDIR)/.airflow \
	AIRFLOW__CORE__DAGS_FOLDER=$(CURDIR)/airflow_demo/dags \
	$(AIRFLOW_PY) -m airflow standalone

dagster: venv-dbt venv-dagster
	cd dagster_demo && $(DAGSTER_PY) -m dagster dev

clean-venvs:
	rm -rf $(VENV_ROOT)
