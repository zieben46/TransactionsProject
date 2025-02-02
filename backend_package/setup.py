from setuptools import setup, find_packages

setup(
    name="streamlit_crud_backend2",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "streamlit",
        "sqlalchemy",
    ],
    include_package_data=True,
    description="Backend package for the Streamlit CRUD app",
)
