import MySQLdb

root_passwd = open('passwd.txt', 'r').read().split('\n')[0]

class Dojo_database:
    """
    intefacing when dealing with data within the dojo databases, there are a
    few tables, the structure of which I shall outline here:

    users -- the tables for the ppl within the dojo
    TINYTEXT username, BINARY(64) pass_hash, TINYTEXT email, BIT access_level

    forum -- the table for threads in the forum
    """

def connect_to_db(path_to_db):
    """
    connect_to_d: returns a connection to the database specified by the
    argument

    Args:
        b(path_to_db (type): TODO
    
    Returns:
        a MySQLdb connection pointer
    
    Example:
        connect_to_db('db/users') -> a connection to the database located at
        'db/users' with root privilage
    """
    return MySQLdb.connect(host="localhost",
                           user="root",
                           passwd=root_passwd,
                           db='db/users')
