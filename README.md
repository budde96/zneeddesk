# Zneeddesk (WIP)
### Instructions
1. cd zneeddesk/
2. python python -m venv ./venv
3. pip install -r requirements.txt
4. gunicorn --config gunicorn_config.py zneeddesk:app
