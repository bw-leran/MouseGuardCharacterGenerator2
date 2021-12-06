#Author: Brandon Miller
#Date: Dec 5th, 2021
#Assignment: Final Project

# program to use a sql database to generate complete and random Mouse Guard character sheets

from creds import PostgresCredentials

import psycopg2


# this class holds funcs that submit SQL queries to the Postgres database
class MouseGuardCharacterGenerator:
    # postgres database credentials
    hostname = PostgresCredentials.hostname
    database = PostgresCredentials.database
    username = PostgresCredentials.username
    password = PostgresCredentials.password
    port_id = PostgresCredentials.port_id

    # func to send SQL commands
    def execute_and_fetch(self, sql_command: str):
        cur.execute(sql_command)
        return cur.fetchall()

    # the following "get" funcs get the formatted outputs from the SQL queries
    def get_name(self):
        sql_command = 'SELECT * FROM name ORDER BY random() LIMIT 1'
        return self.execute_and_fetch(sql_command)[0][1]

    def get_home(self):
        sql_command = 'SELECT * FROM home ORDER BY random() LIMIT 1'
        return self.execute_and_fetch(sql_command)[0][1]

    def get_specialty(self):
        sql_command = 'SELECT * FROM specialty ORDER BY random() LIMIT 1'
        return self.execute_and_fetch(sql_command)[0][1]

    def get_age(self):
        sql_command = 'SELECT * FROM age ORDER BY random() LIMIT 1'
        return self.execute_and_fetch(sql_command)[0][1]

    def get_stats(self):
        sql_command = 'SELECT * FROM stats ORDER BY random() LIMIT 1'
        return self.execute_and_fetch(sql_command)[0][1:]


if __name__ == '__main__':

    # init class
    mg = MouseGuardCharacterGenerator()

    # set vars to default None
    conn = None
    cur = None
    # try to connect to Postgres DB and execute the queries
    try:
        conn = psycopg2.connect(
            host=mg.hostname,
            dbname=mg.database,
            user=mg.username,
            password=mg.password,
            port=mg.port_id
        )

        # make queries
        cur = conn.cursor()
        name = mg.get_name()
        home = mg.get_home()
        specialty = mg.get_specialty()
        age = mg.get_age()

        stats = mg.get_stats()
        nature = stats[0]
        will = stats[1]
        health = stats[2]
        resources = stats[3]
        circles = stats[4]

        # print formatted output
        output = {'Name': name,
                  'Home': home,
                  'Specialty': specialty,
                  'Age': age,
                  'Nature': nature,
                  'Will': will,
                  'Health': health,
                  'Resources': resources,
                  'Circles': circles}

        for outputs, vals in output.items():
            print(outputs, ':', vals)

    # print exceptions
    except Exception as e:
        print('Database exception:', e)

    # close the connection to the database when queries are done
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
