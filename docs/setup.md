# Setup Guide

## Requirements
- Python 3.8+
- Flask
- Apache2 with mod_wsgi

## Installation
```bash
sudo apt update
sudo apt install apache2 libapache2-mod-wsgi-py3 python3-pip
pip install -r requirements.txt
```

## Troubleshooting
- If Apache shows 404, ensure WSGI path is correct
- Check `error.log` in `/var/log/apache2`
