
## Installation
1) Clone the repository:

```bash
  git clone https://github.com/venk404/SRE--RestAPI.git
```
2) Docker Componse for Postgres Installation:
```bash
  cd .\Assignment 2\DB\
  #Rename the .env example to .env and fill details for DB schema to create.
  docker-compose up -d
```
3) Execute the makeFile command (assuming make is installed on your system). This will initiate the servers and generate the student schema:

```bash
  #Rename the .env example to .env and fill details for DB schema to create.
  cd ..
  make all
```

__If you don't have make, then follow the steps below:-__

3) Docker command:

```bash
 cd .\Assignment 2
 #Rename the .env example to .env.
 docker build -t rest-api .
 docker run --rm --name venkatesh -d -p 8000:8000 --network dem rest-api

```


