
<br />
<div align="center">
  <h3 align="center">Parts Warehouse</h3>
</div>

## Description

### Architecture
#### Short description of architecture
I created my own database and deployed the project to an AWS EC2 instance. 
I also used the Continuous Deployment (CD) technique using AWS Actions to automatically deploy code to an AWS EC2 instance

<img src="assets/elmark-Strona-1.drawio.png" alt="architecture"/>
<img src="assets/elmark-Strona-2.drawio.png" alt="architecture"/>
<img src="assets/endpoints.png" alt="architecture"/>

#### Why FastAPI
I chose the FastAPI framework because of:
- Database requirements. In the case of the NoSQL database, I decided to use FastAPI due to its greater control, for comparison, Django has its own built-in ORM system which does not officially support NoSQL databases
- The project is relatively small, with only 2 models/collections and a few basic endpoints for data operations

#### API design
- Id for Categories and serial_number for Parts


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
    "_id": "65b2e261d1fd45025628a880",
    "name": "Wiadra",
    "parent_name": "Metal"
}
```

</details>


##### [GET] /api/v1/category/{id}
<details>
  <summary><strong>cURL Example</strong></summary>
cURL:

```
curl --location 'localhost:8000/api/v1/category/65b2e261d1fd45025628a880'
```

Response:
```
{
    "_id": "65b2e261d1fd45025628a880"
    "name": "Wiadra",
    "parent_name": "Metal"
}
```

</details>

##### [PUT] /api/v1/category/{id}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request PUT 'localhost:8000/api/v1/category/65b2e261d1fd45025628a880' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Wiaderka"
}'
```

Response:
```
{
    "_id": "65b2e261d1fd45025628a880",
    "name": "Wiaderka",
    "parent_name": null
}
```
</details>


##### [DELETE] /api/v1/category/{id}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request DELETE 'localhost:8000/api/v1/category/65b2e261d1fd45025628a880'
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
    "_id": "65b2d3947b2f630d89bad853",
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
        "_id": "65b2d3947b2f630d89bad853",
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
        "_id": "65b2d3947b2f630d89bad853",
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


##### [GET] /api/v1/part/{id}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location 'localhost:8000/api/v1/part/65b2d3947b2f630d89bad853'
```

Response:
```
{
    "_id": "65b2d3947b2f630d89bad853",
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

##### [PUT] /api/v1/part/{id}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request PUT 'localhost:8000/api/v1/part/65b2d3947b2f630d89bad853' \
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
    "_id": "65b2d3947b2f630d89bad853",
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

##### [DELETE] /api/v1/part/{id}
<details>
  <summary><strong>cURL Example</strong></summary>

cURL:
```
curl --location --request DELETE 'localhost:8000/api/v1/part/65b2d3947b2f630d89bad853'
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
- Nginx

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

