# Data Engineering Practice

Hello, welcome to my **Data Engineering Practice** repo! Here I keep all the python scripts and relevant files I used for practicing data pipelines via the  extract - transform - load (ETL) method. I am using the *Data Pipelines Pocket Reference (Densmore 2021)* to guide my ETL-practice journey. Below, I keep track of the **ETL Practice Steps** and the **Highlights** of my learning journey.

-----------
### Data Ingestion Pipeline *(Densmore 2021)*
#### **1. ETL Practice Steps**
##### Configuration and Local Environment:
- [x] Virtual Environment
- [x] AWS Account
- [x] MySQL database
- [x] Create table in MySQL
##### Data Extraction:
- [X] Python script (full extract table to s3 bucket)
- [x] Redshift Data Warehouse
- [x] Python script (incremental extract table to s3 bucket)
- [ ] ~BinLog Replication of MySQL data~ *Note - will practice CDC method at later point.*
- [x] MongoDB data extraction method 
- [x] REST API data extraction method
##### Data Loading:
- [x] Load CSV files to Redshift data warehouse via query editor
- [ ] Load CSV files to Redshift data warehouse via python script

#### **2. Highlights**
##### Data Extraction
| MySQL Database (via RDS) | Table Created in MySQL | S3 Bucket for Extracted MySQL Table | Redshift Data Warehouse | MongoDB Database |
| ----------- | ----------- | ----------- | ----------- | ----------- |
|![Screen Shot 2023-01-16 at 3 15 25 PM_thumbnail](https://user-images.githubusercontent.com/95442334/212779243-44f39162-5dfa-4ce3-8ba4-815015b28649.jpg)| ![Screen Shot 2023-01-16 at 3 11 24 PM_thumbnail](https://user-images.githubusercontent.com/95442334/212779266-612b5bc3-8161-467d-9af4-ec3b5bc16f08.jpg)| ![Screen Shot 2023-01-16 at 3 09 47 PM_thumbnail](https://user-images.githubusercontent.com/95442334/212779292-b5a11716-516d-4708-a4f6-b0f0e190abb9.jpg)| ![Screen Shot 2023-01-16 at 3 13 57 PM_thumbnail](https://user-images.githubusercontent.com/95442334/212779308-c373926b-c728-4eff-a0a6-0fbf012d2d79.jpg)| ![Screen Shot 2023-01-16 at 3 08 03 PM_thumbnail](https://user-images.githubusercontent.com/95442334/212779320-a295a713-4209-481b-88fc-f7393224b49e.jpg)|

##### Data Loading
| Load CSV Files to Redshift (Query Editor) | Successfully Loaded CSV Files to Redshift (Query Editor) |
| ----------- | ----------- |
|![Screen Shot 2023-01-18 at 5 08 12 PM_thumbnail](https://user-images.githubusercontent.com/95442334/213332303-b4d053b1-a104-4f5c-bfed-133bb6f804af.jpg)|![Screen Shot 2023-01-18 at 5 09 42 PM_thumbnail](https://user-images.githubusercontent.com/95442334/213332580-e8a7c6c0-9548-4af9-8d8e-d18e3d0e44aa.jpg)|
-----------
## Reference
Densmore, James (2021). *Data Pipelines Pocket Reference* (O'Reilly). Copyright 2021 James Densmore, 978-1-492-08783-0.
