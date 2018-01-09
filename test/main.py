from source.DatabaseHandler import DatabaseHandler

db = DatabaseHandler("database.db")
db.open()
db.set_used_table("Food")
db.insert("Food", ["0", "'ham'", "0", "1", "2", "3", "4", "5", "6"], db.get_table_name("Food"))
db.insert("Food", ["1", "'honey'", "0", "1", "2", "3", "4", "5", "6"], db.get_table_name("Food"))
db.commit()
db.release_used_table("Food")
db.set_used_table("Users")
db.select("Food", ["ID", "name", "energy"], [(""'ID'"", "<", "5")])
db.insert("Users", ["0", "'test'", "'guy'", "1", "2", "3", "4", "5"], db.get_table_name("Users"))
db.insert("Users", ["1", "'test'", "'guy2'", "1", "2", "3", "4", "5"], db.get_table_name("Users"))
db.update("Food", [(db.get_table_name("Food")[0], "1")], [(db.get_table_name("Food")[1], "=", "'honey'")])
db.delete("Food", [(db.get_table_name("Food")[1], "!=", "'honey'")])
db.select("Food", ["ID", "name", "energy"], [(""'ID'"", "<", "5")])
db.commit()
db.release_used_table("Users")
db.close()