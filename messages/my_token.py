from os.path import isfile, abspath, dirname

TOKEN = ""
SERVER_ID = ""
token_file = dirname(abspath(__file__)) + "/token"
id_file = dirname(abspath(__file__)) + "/server_id"
print(token_file)

if(isfile(token_file)):
  with open(token_file) as file:
    TOKEN = file.read()

if(isfile(id_file)):
  with open(id_file) as file:
    SERVER_ID = file.read()

