# Zneeddesk (WIP)
### Instructions
1. git clone git@github.com:budde96/zneeddesk.git
2. cd zneeddesk/
3. python python -m venv ./venv
4. pip install -r requirements.txt
5. gunicorn --config gunicorn_config.py zneeddesk:app
