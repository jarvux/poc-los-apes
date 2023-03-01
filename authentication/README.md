# curls

## ping
```
curl --location 'http://127.0.0.1:5000/ping'
```

## Sign In

```

curl --location 'http://127.0.0.1:5000/users/signIn' \
--header 'Content-Type: application/json' \
--data '{    
    "name":"jarviz",
    "password":"moris123",
    "role": "1"
}

```


## logIn

```

curl --location 'http://127.0.0.1:5000/users/logIn' \
--header 'Content-Type: application/json' \
--data '{
    "name":"jarviz1",
    "password":"moris"
}'

```

## JWT

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NzkxMjk2MiwianRpIjoiNGNlYzVjYjgtOTJjNC00MWJhLThjNzUtZjI3OGFmN2FmYWI4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImphcnZpejEiLCJuYmYiOjE2Nzc5MTI5NjJ9.s1WDx4eWljJRjRY5W4B2h3PafTV4jQ8-M-HVBM29hfo

```

## Claims

```
{
  "fresh": false,
  "iat": 1677911194,
  "jti": "dbaee552-fe8d-46b4-b870-3c9e384c1c5c",
  "type": "access",
  "sub": "jarviz1",
  "nbf": 1677911194
}
```