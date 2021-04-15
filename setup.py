from os import path
from setuptools import find_packages, setup


run_requirements = [
    "loguru==0.5.3",
    "pydantic==1.8.1",
    "celery==5.0.5",
    "urllib3==1.26.4",
    "gunicorn==20.1.0",
    "fastapi==0.63.0",
    "uvicorn[standard]==0.13.4",
    "pytest==6.2.1",
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="publicacao_numeros",
    version="0.1.0",
    author="Kevin de Santana Araujo",
    author_email="kevin_santana.araujo@hotmail.com",
    packages=find_packages(exclude=["docs", "tests"]),
    url="https://github.com/kevinsantana/desafio-tecnico-byne",
    description="O projeto tem como objetivo dispobilizar uma API que consome um"
                " serviço periódico",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=run_requirements,
    python_requires=">=3.8",
)