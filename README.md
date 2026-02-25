# Graded Assignment: Python Lab Sheet

The repository contains the solution for the *Graded Assignment: Python Lab Sheet* in the *Databases and Cloud* module.

The structure of the repository: 
- `main.py` - The file contains Python code for a CLI application that implements a flight management system allowing users to add flights, view flights by various criteria, update flight information, assign pilots to flights, and view pilot schedules.
- `schema.sql` - The file contains the SQLite database schema defining the table structures with constraints and primary/foreign key relationships.
- `test_queries.sql` - A collection of SQL queries used to verify that the flight management database has been created and populated correctly with data.
- `flight_management.db` - The Flight Management System database. The file is created after the first run of the `main.py` file.
- `README.md` - Project documentation providing setup instructions, how to launch the application, required VS Code extensions, and an overview of the repository structure.

The CLI application can be tested via GitHub Codespaces. Install the following extensions in VS Code:
- `Python` (by Microsoft).
- `SQLite` (by alexcvzz).
- `SQLite Viewer` (by Florian Klampfer).

To launch the application, run the following commands: 
- `cd /workspaces/GradedAssignmentPythonLabSheet` - Navigates to the root folder of the reposity.
- `python main.py` - Launches the CLI application.

The executed `python main.py` will create the `flight_management.db` database and populate it with the mock data. The SQL queries in the `test_queries.sql` file can be use to verify that the database has been created and populated with the mock data. 

Once the application has launched, the user will be presented with a CLI-menu and prompted to select one of the options.

