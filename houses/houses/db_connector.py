import cx_Oracle
import os


def get_connection():
    host = os.getenv('ORACLE_HOST', 'localhost')
    port = os.getenv('ORACLE_PORT', '1521')
    service = os.getenv('ORACLE_SERVICE', 'your_service_name')
    user = os.getenv('ORACLE_USER', 'your_user')
    password = os.getenv('ORACLE_PASSWORD', 'your_password')
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service)
    conn = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)
    return conn
