import cx_Oracle


def get_connection():
    dsn_tns = cx_Oracle.makedsn('172.16.50.201', '1521', service_name='riskpdb')
    conn = cx_Oracle.connect(user='CR', password='newpa$$word', dsn=dsn_tns)
    return conn
