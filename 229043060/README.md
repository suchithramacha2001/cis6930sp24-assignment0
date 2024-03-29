# Cis6930sp24 - Assignment 0 - Normanpd Project

## Project Description
The project aims to streamline the process of accessing and analyzing incident data reported by the Norman, Oklahoma police department. Through the development of a Python application, the project automates the extraction of valuable information from PDF reports, including date/time, incident numbers, locations, nature of incidents, and incident ORIs. By leveraging Python libraries such as urllib and PyPDF2, the application fetches incident reports from the department's website and parses them to extract relevant data.

Upon downloading the PDF file containing incident summaries, the application systematically extracts incident data, ensuring accuracy and efficiency in the process. This extracted data is then stored in a SQLite database, facilitating easy access and retrieval for further analysis. The database schema is designed to accommodate various fields such as incident time, number, location, nature, and ORI, providing a comprehensive repository of incident information.

One of the key functionalities of the application is the generation of insightful summaries of incident counts, sorted by the nature of incidents. By querying the SQLite database, the application computes the frequency of each unique nature of the incident and presents the results in a structured format. This allows stakeholders, including law enforcement agencies and policymakers, to gain valuable insights into crime patterns and trends within the Norman community.

The project prioritizes usability and effectiveness, ensuring that users can seamlessly interact with the application to access and analyze incident data. Through rigorous testing using the pytest framework, the application's functionality and reliability are validated, guaranteeing accurate results and robust performance. Overall, the project serves as a valuable tool for enhancing public safety efforts by providing actionable insights derived from comprehensive incident data analysis.

## how To Run
Pipenv Run Python Assignment0/main.py --incidents <url>


## Functions

# fetch incident url
The `fetchincidents` function downloads incident data from a specified URL in PDF format. It constructs a request with headers to simulate a web browser's user-agent, ensuring access to the resource. Using `urllib.request.urlopen()`, it retrieves the PDF data from the URL and writes it to a file in binary write mode. Utilizing a context manager (`with` statement), it ensures proper file closure after writing. The function returns the file path where the PDF is saved, facilitating further processing. Error handling is implemented with a `try` and `except` block, providing informative messages and returning `None` upon encountering exceptions, thus ensuring robustness.

# Extract Fields 
The `extractincidents` function processes raw PDF data to extract incident information. Utilizing PyPDF2, it reads through each page, splitting text by newline characters. It removes header/footer content like "NORMAN POLICE DEPARTMENT". By identifying date patterns, it captures relevant incident details, including date/time, incident number, location, nature, and incident ORI. Extracted data is organized into lists of incidents, each containing five elements. Error handling is implemented to gracefully handle cases where header/footer information is not present. Overall, the function efficiently parses PDF text to generate structured incident data ready for further analysis or database insertion.

# Create Database 
The `createdb` function establishes a connection to a SQLite database located at 'resources/normanpd.db' and defines a table structure for storing incident data. It checks for the existence of the 'incidents' table within the database and creates it if it doesn't already exist. The table schema includes columns for incident time, number, location, nature, and ORI, all of which are of type TEXT. Error handling is implemented to handle potential exceptions during table creation, ensuring smooth execution. Upon completion, the function returns the database connection object, facilitating subsequent operations such as data insertion and querying. Overall, `createdb` sets up the necessary database infrastructure for storing incident information effectively.

# Insert Into Database 
The `populatedb` function facilitates the insertion of incident data into a SQLite database table. It utilizes the provided database connection to create a cursor object, enabling SQL query execution. By iterating over the incidents list, it attempts to insert each incident into the 'incidents' table using an SQL INSERT statement. Robust error handling ensures graceful handling of exceptions that may arise during insertion, such as duplicate entries. Upon completing the insertion process, changes are committed to the database, ensuring data permanence. Overall, `populatedb` streamlines the process of populating the database with incident data, ensuring database integrity and reliability.

# Print Status 
The `status` function generates a summary of incident natures and their occurrences from a SQLite database. It first executes an SQL query to retrieve the distinct incident natures and their corresponding counts, ordering them by count in descending order and alphabetically by nature. The function then iterates over the fetched rows, printing each nature along with its count. Overall, `status` provides a succinct overview of the distribution of incident types, aiding in data analysis and understanding.



## Tests
## How To Run Tests
Pipenv Run Python -m Pytest

# Test Download Pdf 
Verifies That The Download_pdf Function Correctly Downloads And Saves A Pdf File.

# Test Extract Fields 
Validates The Extract_fields Function's Ability To Extract Fields From A Given Line Of Text.

# Test Insert Into Database
Checks That The Insert_into_database Function Properly Inserts Data Into The Sqlite Database.

# Test Status
Verifies That The Status Function Correctly Prints The Count Of Each Incident Nature Stored 
In The Database.

### Note
In The Test_download_pdf Method, We Mock Requests.get And Open To Avoid Actual Network Requests 
And File Operations. Then, We Assert That The Functions Are Called Correctly.

In The Other Test Methods, We Mock Sqlite3.connect And Cursor To Avoid Actual Database Operations. 
We Also Mock Sys.stdout To Capture The Output Of The Status Function.#   2 2 9 0 4 3 0 6 0  
 