import psycopg2


def get_connection():
    hostname = 'dbleapbusiness.postgres.database.azure.com'
    database = 'postgres'
    username = 'dba_leapbusiness'
    pwd = 'Businessleap22'
    port_id = 5432

    return psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)



def get_connection_local():
    hostname = 'localhost'
    database = 'db_leapbusiness'
    username = 'postgres'
    pwd = 'Idranoide11'
    port_id = 5432

    return psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
