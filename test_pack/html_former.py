import psycopg2
import test_pack.constants
from test_pack.db_config import get_db_config

 
def get_data_html():
    # Connecting to the PostgreSQL database server
    _connection = None
    try:
        # Reading connection parameters
        _params = get_db_config("db_settings.ini", "postgresql")
 
        # Connecting to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        _connection = psycopg2.connect(**_params)
      
        # Creating a cursor
        _cursor = _connection.cursor()
        
        # Reading and preparing first table data (Europe countries)
        # Preparing SQL query
        _sql = test_pack.constants.SQL_AIRCRAFTS_EUROPE
        # Reading single html-table row format from constant
        _table_row_format = test_pack.constants.HTML_TABLE_ROW_FORMAT_EU
        # Variable to collect all table rows
        _table_eu = ""
        # Executing a statement
        _cursor.execute(_sql)
        # Reading received data
        _row = _cursor.fetchone()
        while _row is not None:
            # Data is formatted as required
            _table_row = _table_row_format % (_row)
            _table_eu = _table_eu + _table_row
            _row = _cursor.fetchone()

        # Formatting html-table as stated in constant
        _table_eu = test_pack.constants.HTML_TABLE_FORMAT % (
            test_pack.constants.HTML_TABLE_NAME_EU,
            _table_eu
            )

        # Reading and preparing second table data (non-Europe countries)
        # Preparing SQL query
        _sql = test_pack.constants.SQL_AIRCRAFTS_NON_EUROPE
        # Reading single html-table row format from constant
        _table_row_format = test_pack.constants.HTML_TABLE_ROW_FORMAT_NON_EU
        # Variable to collect all table rows
        _table_non_eu = ""
        # Executing a statement
        _cursor.execute(_sql)
        # Reading received data
        _row = _cursor.fetchone()
        while _row is not None:
            _table_row = _table_row_format % (_row)
            _table_non_eu = _table_non_eu + _table_row
            _row = _cursor.fetchone()

        # Formatting html-table as stated in constant
        _table_non_eu = test_pack.constants.HTML_TABLE_FORMAT % (
            test_pack.constants.HTML_TABLE_NAME_NON_EU,
            _table_non_eu
            )

        # Formatting html-document as stated in constant
        _html_doc = test_pack.constants.HTML_DOC_FORMAT % (
            _table_eu,
            _table_non_eu
            )

        # Closing communication with the PostgreSQL
        _cursor.close()

        return _html_doc
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if _connection is not None:
            _connection.close()
            print('Database connection closed.')