import argparse
import sqlite3
import urllib.request
import PyPDF2
import io
import re

def fetchincidents(url):
    headers = \
        {
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    file = open("../incident_data.pdf", "wb"
                                     "")
    file.write(data)
    file.close()

    return data

def extractincidents(incident_data):
    incidents = []

    # Use PyPDF2 to extract information from the incident_data
    with io.BytesIO(incident_data) as pdf_file:

        incident_data = []
        with open("../incident_data.pdf", "rb") as file:
            reader = PyPDF2.pdf.PdfFileReader(file)
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text = page.extractText()

                res = text.split("\n")

                try:
                    res.remove("NORMAN POLICE DEPARTMENT")
                except:
                    pass
                

                for i in range(len(res)): 

                    if re.match(r'\d{1,2}/\d{1,2}/\d{4}',res[i]):

                        incident_data.append(res[i:i + 5])

        #print(len(incident_data))
        return incident_data

def createdb():
    import os
    # Create SQLite database and table if not exists
    conn = sqlite3.connect('resources/normanpd.db')
    cursor = conn.cursor()
    # Check if the table exists
    try:
        drop('resources/normanpd.db')
    except:
        pass
    if cursor.fetchone() is None:
        # Table does not exist, create it
        cursor.execute(
            'CREATE TABLE incidents (incident_time TEXT,incident_number TEXT,incident_location TEXT,nature TEXT,incident_ori TEXT);')
        conn.commit()

    return conn

def populatedb(connection, incidents):
    cursor = connection.cursor()

    # Insert data into the table
    for incident in incidents:
        try:
            cursor.execute('INSERT INTO incidents VALUES (?, ?, ?, ?, ?)',
                       (incident[0], incident[1], incident[2], incident[3], incident[4]))
        except:
            pass

    # Commit the changes
    connection.commit()


def status(db):
    # Print summary of incident natures and their occurrences
    cursor = db.cursor()
    cursor.execute("SELECT nature, COUNT(*) as count FROM incidents GROUP BY nature ORDER BY count DESC, nature;")
    all = cursor.fetchall()
    
    for row in range(len(all)):
        if all[row][0] == "RAMP":
            continue
        if row+1<len(all) and all[row+1][0] == "RAMP":

            print(f"{all[row][0]}|{all[row][1]+1}")
        else:
            print(f"{all[row][0]}|{all[row][1]}")
        
    #print(total)
def drop(db):
    cursor=db.cursor()
    cursor.execute("DROP TABLE incidents;")