import boto3
import configparser
import psycopg2

# get db Redshift connection info
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
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

# load the account_id and iam_role from the configuration file
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
account_id = parser.get("aws_boto_credentials", "account_id")
iam_role = parser.get("aws_creds", "iam_role")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

# run the `COPY` command to load the file into Redshift
file_path = (f"s3://{bucket_name}/export_iss_location_file.csv")
role_string = (f"arn:aws:iam::{account_id}:role/{iam_role}")

sql = "COPY public.international_space_station_location"
sql = sql + " from %s "
sql = sql + " iam_role %s;"

# create a cursor object and execute the `COPY`
cur = rs_conn.cursor()
cur.execute(sql,(file_path, role_string))

# close the cursor object and commit the transaction
cur.close()
rs_conn.commit()

# close the connection
rs_conn.close()