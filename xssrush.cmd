@echo off
if exist "C:\Users\logir\Projects\vault-memory\.venv\Scripts\python.exe" (
    "C:\Users\logir\Projects\vault-memory\.venv\Scripts\python.exe" "%~dp0integrations\XSSRush\xssr.py" %*
) else (
    python "%~dp0integrations\XSSRush\xssr.py" %*
)
