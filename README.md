### thinkSafe

- enviar uma requisição POST para http://127.0.0.1:8000/api/user/ com os seguintes dados:

``` json
{
    "username": "talita",
    "password": "123",
    "is_instructor": true
}
```

- enviar uma requisição GET para http://127.0.0.1:8000/api/token/:

```json
{
    "username": "talita",
    "password": "123",
}

```