# mysql-unexpected-shutdown-fix
📂 Project Overview
This repository, mysql-unexpected-shutdown-fix , contains a Python script designed to automate the process of fixing the "MySQL shutdown unexpectedly" error in XAMPP. The script cleans up the MySQL data directory (C:\xampp\mysql\data) and restores it from a backup, ensuring MySQL starts correctly.

⚠️ Problem Description
When MySQL shuts down unexpectedly, it often results in errors like the one shown below:

![xampp erreur](https://github.com/user-attachments/assets/85743883-ecb9-43dd-b572-012da375f45b)

This script helps resolve such issues by:


Deleting specific folders (phpmyadmin, performance_schema, mysql, test) from the data directory.
Removing all files except ibdata1 to ensure a clean slate.
Restoring the database files from a backup directory (C:\xampp\mysql\backup).
🛠️ Requirements
Python : Ensure Python is installed on your system. You can download it from python.org .
XAMPP : The script assumes you are using XAMPP with MySQL installed.
Backup Directory : A valid backup of the MySQL data directory must exist at C:\xampp\mysql\backup.
📋 Installation and Setup
Clone the Repository :

git clone https://github.com/houssemm/mysql-unexpected-shutdown-fix.git

Navigate to the Project Directory :

cd mysql-unexpected-shutdown-fix

Ensure Permissions :
Make sure you have administrative privileges to modify the C:\xampp\mysql\data directory.
If prompted, allow the script to access and modify files.
Run the Script :

python restore_mysql_data.py

🌟 How the Script Works
The script performs the following steps:

Delete Specific Folders :
Removes the following folders from C:\xampp\mysql\data:
phpmyadmin
performance_schema
mysql
test
Clean Up Files :
Deletes all files in C:\xampp\mysql\data except for ibdata1.
Restore Backup :
Copies all files and folders from C:\xampp\mysql\backup to C:\xampp\mysql\data, excluding ibdata1 if it exists in the backup.
Restart MySQL :
After running the script, restart the MySQL service in the XAMPP Control Panel to apply the changes.

🚨 Important Notes
Backup Validation :
Ensure that the backup directory (C:\xampp\mysql\backup) contains a valid and recent backup of your MySQL data.
If the backup is incomplete or corrupted, the script may not restore your database correctly.
Permissions :
Running the script requires administrative privileges. If you encounter permission errors, run your terminal or IDE as an administrator.
MySQL Service :
After running the script, manually restart the MySQL service in the XAMPP Control Panel to ensure it starts correctly.

🤝 Contributing
If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Contributions are welcome!

👩‍💻 Contact
For questions or support, reach out to:

Email: houssemm.labidi@gmail.com
GitHub: @housssemm


🏆 Credits
This script was created to simplify the process of recovering MySQL databases in XAMPP environments. Thank you for using it!

Final Steps After Running the Script
Restart MySQL :
Open the XAMPP Control Panel.
Click the Start button next to the MySQL service.
Verify Operation :
Check if MySQL starts successfully without any errors.
Access phpMyAdmin or your database client to ensure all databases are restored correctly.
Monitor Logs :
If MySQL still fails to start, review the logs in the XAMPP Control Panel or the Windows Event Viewer for additional clues.
