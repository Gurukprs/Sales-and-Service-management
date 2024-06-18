This repository contains 2 applications and their source code.

1.Once made necessary changes (host,user,database,password) in the code u can run the programme.

2.For the user to access the database remotely, you will have to replace the host of user file with the target system's ip address, and also make sure both the systems are in the same network. 

3.Then make sure to create a new inbound rule in firewall allowing access to the port '3306' (or any other in which you host the databaes, 3306 is set default)

⚠️ **Before Running:** ⚠️

make sure to create the db using _Database build.sql_

**Prerequsite** 

1. MySQL
2. Python
            
**Pip connections to be made before running**

1. pip install mysql-connector-python
2. pip install SQLAlchemy
3. pip install pandas
4. pip install PyMySQL
5. pip install auto-py-to-exe (if you want to make an .exe application)

**Steps to be followed to make an .exe file:**

1. once completed the script type "cmd" in the directory path bar on the top of explorer
2. then run this "pyinstaller --onefile --windowed script_name.py" #be sure to replace the script_name with your script name
3. then you can find the programme inside a folder that will be automatically generated and named "dist" in the same directory
