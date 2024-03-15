JIRA Automation with Flask and Requests
This project demonstrates how to automate tasks in JIRA using Flask and the Requests library in Python.
Description
The project consists of a Flask web application that allows users to create JIRA issues programmatically. It utilizes the JIRA REST API to interact with JIRA.
Features
• Create JIRA issues with custom parameters such as project key, issue type, summary, and description.
• Intuitive Flask web interface for easy interaction.

Installation
1. Clone the repository:
git clone https://github.com/EneeyaSenthil/GitHub_Jira_Integration
2. Install dependencies:
pip install flask
3. Set up a JIRA API token:
• Obtain your JIRA API token from the Atlassian website.

Usage
1. Navigate to the project directory.
2. Run the Flask application:

python file_name.py
3. Access the web interface by opening a browser and navigating to `http://localhost:5000/createjira`.