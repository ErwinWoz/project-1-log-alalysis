# Logs Analysis Project

## Overview
User is required to write a script that uses SQL queries that would fetch information from a database.
User will run the script from the command line. It will not take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.
Urer is required to use single query to answer each question.
### Questions:
1. **What are the most popular three articles of all time?**
	Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
	Example:
	```bash
	Princess Shellfish Marries Prince Handsome		1201 views
 	Baltimore Ravens Defeat Rhode Island Shoggoths		915 views
 	Political Scandal Ends In Political Scandal		553 views
 	```

1. **Who are the most popular authors?**
	That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
1. **On which days did more than 1% of requests lead to errors?**
	The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Required Libraries and Dependencies
The project code requires the following software:

- [Python 3](https://www.python.org/downloads/)
- [psycopg2](https://pypi.org/project/psycopg2/) 
- [PostgreSQL](https://www.postgresql.org/download/)

## Setup and Instalation:
This project is run in a virutal machine created using Vagrant

1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the VM configuration, use Github to fork and clone, or download, the repository [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.
Alternatively use this link to go through instalation: [Instaling VM](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
1. Download the database file: [news](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip and get the newsdata.sql file.
1. Paste the newsdata.sql file into the vagrant directory
1. Inside  vagrant directory create new directory called: project-1-log-analysis
1. Download this project to you laptop: [log analysis](https://github.com/michellejl/log_analysis)
1. Upzip and copy all 3 files into the directory called project-1-log-analysis that you have just created

## Running the project
1. Using terminal navigate to your project e.g. Desktop/Projects/fullstack-nanodegree-vm
1. cd to vagrant direxctory
`cd vagrant`
1. Build your vm using
`vagrant up` command
1. It might take a while. Once it's build use
`vagrant ssh` command to connect
1. cd to correct directory 
`cd /vagrant/project-1-log-alalysis/`
1. run script
`python3 log2.py`
It will take few seconds to execure the script and fetch appropriate data.
1. Fetched information should match file output.txt 
1. To logout from vm use
`exit` command

##### No views have been created in this project






### SQL Resources
- Postgresql Documentation: [https://www.postgresql.org/docs/9.6/static/index.html]
-Filter in postgresql: [https://www.postgresql.org/docs/9.4/static/sql-expressions.html]
- Casting in postgresql: [https://​www.postgresql.org/docs/9.2/static/sql-createcast.html]
- Join: [https://www.postgresql.org/docs/8.3/tutorial-join.html]
- Counting: [​http://www.postgresqltutorial.com/postgresql-count-function/]
- Grouping: [http://www.postgresqltutorial.com/postgresql-group-by/]
- Formating: [​http://www.postgresqltutorial.com/postgresql-to_char/]


