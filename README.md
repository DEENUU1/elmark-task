
<br />
<div align="center">
  <h3 align="center">Parts Warehouse</h3>
</div>

## Description

### Architecture
#### Short description of architecture
Unfortunately, I had problems connecting to the database available in the project manual. 
Instead, I created my own database and deployed the project to an AWS EC2 instance. 
I also used the Continuous Deployment (CD) technique using AWS Actions to automatically deploy code to an AWS EC2 instance

<img src="assets/elmark.drawio.png" alt="architecture"/>

#### Why FastAPI
I chose the FastAPI framework because of:
- Database requirements. In the case of the NoSQL database, I decided to use FastAPI due to its greater control, for comparison, Django has its own built-in ORM system which does not officially support NoSQL databases
- The project is relatively small, with only 2 models/collections and a few basic endpoints for data operations

#### API design
- Used singular and don't mix them with plurals 
```
/part
/category
```
- Used API versioning
```
/api/v1
```

### Endpoints

##### [POST] /api/v1/category/
<details>
  <summary><strong>cURL Example</strong></summary>

 cURL:
```
curl --location 'localhost:8000/api/v1/category/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Wiadra",
    "parent_name": "Metal"
}'
```

Response:
```
{
    "name": "Wiadra",
    "parent_name": "Metal"
}
```

</details>


##### [GET] /api/v1/category/{name}
<details>
  <summary><strong>cURL Example</strong></summary>
cURL:

```
curl --location 'localhost:8000/api/v1/category/Wiadra'
```

Response:
```
{
    "name": "Wiadra",
    "parent_name": "Metal"
}
```

</details>

##### [PUT] /api/v1/category/{name}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request PUT 'localhost:8000/api/v1/category/Tools' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Wiaderka"
}'
```

Response:
```
{
    "name": "Wiaderka",
    "parent_name": null
}
```
</details>


##### [DELETE] /api/v1/category/{name}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request DELETE 'localhost:8000/api/v1/category/Wiadra'
```

Response:
```
{
    "message": "Category deleted successfully"
}
```
</details>


##### [POST] /api/v1/part/
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location 'localhost:8000/api/v1/part/' \
--header 'Content-Type: application/json' \
--data '{
  "serial_number": "aadasjadsadsadsb",
  "name": "Allen key",
  "description": "Some description for this part",
  "category": "Allen",
  "quantity": 5,
  "price": 25,
  "location": {
    "room": "Room11",
    "bookcase": "A",
    "shelf": "C1",
    "cuvette": "H",
    "column": 10,
    "row": 5
  }
}'
```

Response:
```
{
    "serial_number": "aadasjadsadsadsb",
    "name": "Allen key",
    "description": "Some description for this part",
    "category": "Allen",
    "quantity": 5,
    "price": 25.0,
    "location": {
        "room": "Room11",
        "bookcase": "A",
        "shelf": "C1",
        "cuvette": "H",
        "column": 10,
        "row": 5
    }
}
```
</details>


##### [GET] /api/v1/part/
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location 'localhost:8000/api/v1/part/?name=Allen&description=Some&category=Allen&serial_number=aa'
```

Response:
```
[
    {
        "serial_number": "aadasjadsadsadsb",
        "name": "Allen key",
        "description": "Some description for this part",
        "category": "Allen",
        "quantity": 5,
        "price": 25.0,
        "location": {
            "room": "Room11",
            "bookcase": "A",
            "shelf": "C1",
            "cuvette": "H",
            "column": 10,
            "row": 5
        }
    },
    {
        "serial_number": "aadasjadssssadsadsb",
        "name": "Allen key 2",
        "description": "Some description for this part",
        "category": "Allen",
        "quantity": 1,
        "price": 100.0,
        "location": {
            "room": "Room11",
            "bookcase": "Z",
            "shelf": "C1",
            "cuvette": "H",
            "column": 10,
            "row": 5
        }
    }
]
```
</details>


##### [GET] /api/v1/part/{serial_number}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location 'localhost:8000/api/v1/part/aadasjadsadsadsb'
```

Response:
```
{
    "serial_number": "aadasjadsadsadsb",
    "name": "Allen key",
    "description": "Some description for this part",
    "category": "Allen",
    "quantity": 5,
    "price": 25.0,
    "location": {
        "room": "Room11",
        "bookcase": "A",
        "shelf": "C1",
        "cuvette": "H",
        "column": 10,
        "row": 5
    }
}
```
</details>

##### [PUT] /api/v1/part/{serial_number}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request PUT 'localhost:8000/api/v1/part/aadasjadssssadsadsb' \
--header 'Content-Type: application/json' \
--data '{
    "serial_number": "aadasjadssssadsadsb",
    "name": "Allen key 123",
    "description": "Some description for this part",
    "category": "AllenTool",
    "quantity": 5,
    "price": 25.0,
    "location": {
        "room": "Room11",
        "bookcase": "A",
        "shelf": "C1",
        "cuvette": "H",
        "column": 10,
        "row": 5
    }
}'
```

Response:
```
{
    "serial_number": "aadasjadssssadsadsb",
    "name": "Allen key 123",
    "description": "Some description for this part",
    "category": "AllenTool",
    "quantity": 5,
    "price": 25.0,
    "location": {
        "room": "Room11",
        "bookcase": "A",
        "shelf": "C1",
        "cuvette": "H",
        "column": 10,
        "row": 5
    }
}
```
</details>

##### [DELETE] /api/v1/part/{serial_number}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request DELETE 'localhost:8000/api/v1/part/newSerial123'
```

Response:
```
{
    "message": "Part deleted successfully"
}
```

</details>


## Tech stack:
- Python
  - FastAPI
  - Uvicorn
- AWS 
  - EC2
  - ElasticIP
- Docker & Docker-compose
- MongoDB

## Installation
Clone repository
```bash
git clone https://github.com/DEENUU1/elmark-task.git
```
Create .env file
```bash
cp .env_example .env
```

Example of .env
```txt 
DEBUG="True"
TITLE="ELMARK TASK"
MONGO_DATABASE_NAME=KACPER_WLODARCZYK
MONGO_CONNECTION_STRING=
```

Build docker-compose
```bash
docker-compose build
```

Run docker-compose
```bash
docker-compose up
```
Or
```bash
docker-compose up -d
```

## Authors

- [@DEENUU1](https://www.github.com/DEENUU1)

<!-- LICENSE -->

## License

See `LICENSE.txt` for more information.

