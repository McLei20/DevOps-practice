# DevOps-practice
A script that checks whether a list of websites is up and writes a report

## Setup
```powershell 
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
## Linux Setup
```powershell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Note for Ubuntu
```powershell
sudo apt install python3-venv
```

## Usage
Put the URLs to check in urls.json, then run `python request.py`.
