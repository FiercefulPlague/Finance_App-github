  <h1>Finance Tracker (Flask)</h1>
A simple local finance tracking application built with Python (Flask) and SQL.
This project is intended for learning purposes and personal use.

It allows users to add income and expenses and store them in a local database.

## Features
- Add income and expense records
- Store data in a local SQL database
- Simple HTML interface
- Flask backend
- Beginner-friendly structure and comments
- No personal data included
- Technologies Used
- Python
- Flask
- MySQL
 -HTML
## Project Structure
finance-app/ <br>
│ ├── app.py # Flask backend logic <br>
├── start.bat # Windows startup script <br>
├── README.md # Project documentation <br>
│ ├── database/ <br>
│ └── App Database.sql # Database structure <br>
│ ├── templates/ <br>
│ └── index.html # Main HTML page <br>

## Installation & Setup
1️ Clone the repository
git clone https://github.com/FiercefulPlague/Personal_finance_web.git cd Personal_finance_web

2️ Install dependencies <br>
-- pip install flask --

3️ Set up the database
Open your MySQL
Run the following file: Database.sql <br>
4️ Run the application <br>
Option A: Using Python <br> 
-- python app.py --

Option B: Windows users Double-click: start.bat

5️ Open in your browser
http://127.0.0.1:5000

## Notes
- The application runs locally only
- No authentication is implemented
- All data is stored on your local machine
- debug=True is enabled for development
- Example values are placeholders only
- No personal or financial data is included
## Intended Use
- Learning Flask fundamentals
- Understanding frontend–backend communication
- Working with SQL databases in Python
- Beginner-friendly portfolio projects
- Experimenting and extending functionality
## License
This project is open-source and free to use for learning and personal projects.
