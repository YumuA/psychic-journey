import cx_Oracle
def conexionDB():
    try:
        connection = cx_Oracle.connect( 
            user='C##Ssant', 
            password='1013',
            dsn='localhost:1521/XE',
                            
        )
        return connection
    except cx_Oracle.Error as error:
        print(f'Error Oracle: {error}')
        return None