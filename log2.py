#!/usr/bin/python3


# import postgresql library
import psycopg2

# define database name
DBNAME = "news"

# open database connection
db = psycopg2.connect(database=DBNAME)

# create a cursor object using cursor() method
cursor = db.cursor()


# Ceate query function for question one
def most_popular_article():
    query = """
    select title, count(title) as num
    from articles, log
    where log.path like '%' || articles.slug
    and status = '200 OK'
    group by title
    order by num desc
    limit 3
    """
    # catch and handle exceptions using try and except block
    try:
        # Execute sql command
        cursor.execute(query)
        # Fetch queried data
        results = cursor.fetchall()
        # Loop over and print data
        print("\t 1. WHAT ARE THE MOST POPULAR THREE ARTICLES OF ALL TIME?\n")
        for row in results:
            print("\t", row[0], " - ", row[1], " views")
    except Exception as e:
        print("Error: {}".format(e))


# Ceate query function for question two
def most_popular_authors():
    query = """
    select authors.name, count(articles.author) as views
    from articles, log, authors
    where log.path like '%' || articles.slug
    and articles.author = authors.id
    group by authors.name order by views desc
    """
    # catch and handle exceptions using try and except block
    try:
        # Execute sql command
        cursor.execute(query)
        # Fetch queried data
        results = cursor.fetchall()
        # Loop over and print data
        print("\n\t 2. WHAT ARE THE MOST POPULAR AUTHORS?\n")
        for row in results:
            print("\t", row[0], " - ", row[1], " views")
    except Exception as e:
        print("Error: {}".format(e))


# Ceate query function for question three
def most_error_requests():
    query = """
    select filtered_date,
    round(not_found::decimal / all_requests * 100, 2) as percentage
    from
    (select to_char(time, 'Mon DD, YYYY') as filtered_date,
    count(*) all_requests,
    sum((status !='200 OK')::int)::float as not_found
    from log
    group by filtered_date) as subquery
    where not_found/all_requests > 0.01;
    """
    # catch and handle exceptions using try and except block
    try:
        # Execute sql command
        cursor.execute(query)
        # Fetch queried data
        results = cursor.fetchall()
        # Loop over and print data
        print("\n\t 3. ON WHICH DAYS DID MORE THAN 1 % OF REQUESTS"
              " LEAD TO ERRORS?\n")
        for row in results:
            print("\t", row[0], " - ", row[1], "%")
    except Exception as e:
        print("Error: {}".format(e))

    # cloes cursor and disconnect from server
    cursor.close()
    db.close()

# call query function
most_popular_article()
most_popular_authors()
most_error_requests()
