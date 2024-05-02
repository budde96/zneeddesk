# Zneeddesk (WIP)
Zneeddesk is a Zendesk ticket exporter written in Flask using zenpy, psycopg(postgres), dotenv and gunicorn. Security is not a factor at the moment since this is meant to be run internally and this should never be run as a public facing service. Output format is JSON.
### Instructions
1. git clone git@github.com:budde96/zneeddesk.git
2. cd zneeddesk/
3. python -m venv ./venv
4. pip install -r requirements.txt
5. gunicorn --config gunicorn_config.py zneeddesk:app
6. Open http://ip_to_host:8080 in your browser
