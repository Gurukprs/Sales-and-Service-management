This repository contains 2 applications and their source code.
Once made necessary changes (host,user,database,password) in the code u can run the programme.
For the user to access the database remotely, you will have to replace the host of user file with the target system's ip address, and also make sure both the systems are in the same network. 
Then make sure to create a new inbound rule in firewall allowing access to the port '3306' (or any other in which you host the databaes, 3306 is set default)
**Before Running:**

prerequsite: 
            -> MySQL
            -> Python
            
Pip connections to be made before running:
            -> pip install mysql-connector-python
            -> pip install SQLAlchemy
            -> pip install pandas
            -> pip install PyMySQL
            -> pip install auto-py-to-exe (if you want to make an .exe application)

Steps to be followed to make an .exe file:
            -> once completed the script type "cmd" in the directory path bar on the top of explorer
            -> then run this "pyinstaller --onefile --windowed script_name.py" #be sure to replace the script_name with your script name
            -> then u can find the programme inside a folder that will be automatically generated and named "dist" in the same directory
