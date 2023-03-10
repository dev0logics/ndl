import os

os.system('title BitLogics')
docs_path = os.path.expanduser('~/Documents')
bitlogics_path = os.path.join(docs_path, 'bitlogics')

# crea la cartella 'bitlogics' se non esiste già
if not os.path.exists(bitlogics_path):
    print('\x1b[36;49;1mBitLogics Launcher/n')
    print('\x1b[31;49;1m[error] Program files not found, run setup to install or repair files!\n')
    input('\u001b[0mPress enter to exit.')
else:
    # avvia il server in background
    server_path = os.path.join(bitlogics_path, 'server.py')
    os.system(f'start /B python "{server_path}"')

    # avvia il client in una nuova finestra di terminale
    client_path = os.path.join(bitlogics_path, 'client.py')
    os.system(f'start /B python "{client_path}"')
