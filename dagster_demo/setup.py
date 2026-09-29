from setuptools import find_packages, setup

setup(
    name="dagster_demo",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "dagster_demo": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)
