import assignment0
import argparse
import os
import urllib.parse
import pypdf
from pypdf import PdfReader

#from assignment0.assignment0 import createdb, drop, extractincidents, fetchincidents, populatedb, status

# Main function to orchestrate the process
def main(url):
    # Download data
    incident_data = assignment0.fetchincidents(url)

    # Extract data
    incidents = assignment0.extractincidents(incident_data)

    # Create new database

    db = assignment0.createdb()

    # Insert data
    assignment0.populatedb(db, incidents)

    # Print incident counts
    assignment0.status(db)

    assignment0.drop(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="Incident summary URL.")
    args = parser.parse_args()

    if args.incidents:
        main(args.incidents)
