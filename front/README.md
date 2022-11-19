IP

GET http://IP/products?user_id

Response application/json
{
    products: [
        'tomato',
        'pasta',
        'chicken'
    ]
}

POST http://IP/products?user_id=

body: {
    products: [
        'cheese',
    ]
}

response OK

DELETE http://IP/products?user_id=