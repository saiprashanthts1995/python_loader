# python_loader - to load data

## Description
    This project is done intended to load the data into postgres from 
    MYSQL. Tables to be loaded is based on the tables which are marked 
    as 'yes' in tables_to_loaded.txt file. Once the data is read from
    mysql it is being loaded into postgres after truncating the data
    if present. Once the data is loaded, a basic check is made to check
    the count of records between two databases.
    
## Contents
    This Project consist of these files
    * config.json
    * main.py
    * queries.yaml
    * read.py
    * README.md
    * requirement.txt
    * tables_to_loaded.txt
    * test.py
    * utils.py
    * write.py
    
## How to Run the Code
```commandline
python3 main.py -e DEV 
```
    
## Few Points to remember
1. After the cycle run is completed, a logfile is generated inside the logs folder.
2. Mysql and PostgreSQL is hosted inside Docker hosted in AWS EC2 Console
3. when creating EC2 instances 3306 and 5432 is open

## Docker commands
```commandline
docker pull mysql
docker pull postgres
docker network create -d bridge sai_network
docker run --name sai_mysql
           -e MYSQL_ROOT_PASSWORD=sai
           -p 3036:3036
           --network sai_network
           mysql
docker run --name sai_postgres
           -e POSTGRES_PASSWORD=sai
           -p 5432:5432
           --network sai_network
           postgres
docker exec -it sai_mysql bash
docker exec -it sai_postgres bash
```

##Postgres and MySQL Initial setup

### Postgres
```commandline
create database sai_postgres;
CREATE USER sai WITH PASSWORD 'sai';
grant all privileges on database sai_postgres to sai;

```
### MYSQL
```commandline
create database sai_mysql;
create user sai identified by 'sai';
grant all privileges on sai_mysql.* to sai;
flush privileges;
```

## Tools Used
1. Pycharm Community Edition
2. WinSCp to connect to EC2 Instance
3. Putty to execute docker commands
4. Dbeaver to connect to Mysql and Postes Database