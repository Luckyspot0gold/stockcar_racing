python -c "import os; from glob import glob; \
print('CRITICAL FILES MISSING!' if not glob('src/**/*.py', recursive=True) else 'STRUCTURE INTACT'); \
os.system('pip freeze | grep -e pygame -e pandas -e ccxt')"
