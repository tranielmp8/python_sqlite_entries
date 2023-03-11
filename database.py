# DATABASE 
import sqlite3

connection = sqlite3.connect('C: location of where you saved sqlite data')
# connection.row_factory = sqlite3.Row

def create_table():
  with connection:
    connection.execute("CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
  with connection: # (?,?); , (data, data) helps prevent SQL Injection attacks
    connection.execute("INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date))
  # with connection: #SQL INJECTION ATTACKS CAN OCCUR LIKE THIS
  #   connection.execute(f"INSERT INTO entries VALUES ('{entry_content}', '{entry_date}');")

def get_entries():
  cursor = connection.execute("SELECT * FROM entries;")
  return cursor
  # return cursor.fetchall() # get all results and put them in a list, but we can just use cursor since it iterates over all anyway
  
  # LONG WAY TO DO CURSOR BELOW:
  # cursor = connection.cursor()
  # cursor.execute("SELECTION * FROM entries;")