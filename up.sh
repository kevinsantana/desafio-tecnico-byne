#!/bin/bash
gunicorn --bind=0.0.0.0:5000 --workers=3 --worker-class=uvicorn.workers.UvicornWorker --timeout=174000 --reload publicacao_numeros:app