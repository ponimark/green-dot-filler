@echo off
echo Cleaning old processes...
taskkill /F /IM "streamlit.exe" >nul 2>&1
taskkill /F /IM "python.exe" >nul 2>&1
cls
echo Starting Expense Tracker...
python -m streamlit run expense_tracker_app.py --server.port=8502
pause 