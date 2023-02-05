import boto3
import configparser
import psycopg2
import os

# get db Redshift connection info
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'pipeline.conf')

parser = configparser.RawConfigParser()
parser.read(initfile)
dbname = parser.get("aws_creds", "database")
user = parser.get("aws_creds", "username")
password = parser.get("aws_creds", "password")
host = parser.get("aws_creds", "host")
port = parser.get("aws_creds", "port")

#Connect to Redshift cluster
rs_conn = psycopg2.connect(
    "dbname=" + dbname
    + " user=" + user
    + " password=" + password
    + " host=" + host
    + " port=" + port
)

rs_sql = """
INSERT INTO iss_locations (location_at, longitude, latitude, message, appended_at)
with last_appended as (
    select 
        max(location_at) as last_appended_at
    from iss_locations
)
SELECT
    timestamp 'epoch' + timestamp * interval '1 second' as location_at,
    longitude,
    latitude,
    message,
    getdate() as appended_at
FROM international_space_station_location
where location_at > (select last_appended_at from last_appended);
"""
rs_cursor = rs_conn.cursor()
rs_cursor.execute(rs_sql)

rs_cursor.close()
rs_conn.commit()
