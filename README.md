# Store-Manager-API

[![Build Status](https://travis-ci.org/Jnjerry/Store-Manager-API.svg?branch=ch-test-api-endpoints-161276308)](https://travis-ci.org/Jnjerry/Store-Manager-API)
[![Coverage Status](https://coveralls.io/repos/github/Jnjerry/Store-Manager-API/badge.svg?branch=ch-test-sale-api-endpoints-161307051)](https://coveralls.io/github/Jnjerry/Store-Manager-API?branch=ch-test-sale-api-endpoints-161307051)
<a href="https://codeclimate.com/github/Jnjerry/Store-Manager-API/maintainability"><img src="https://api.codeclimate.com/v1/badges/fbc4aabf9c839cbe4fcc/maintainability" /></a>

Store manager api is a flask api that helps storeowners to manage their products and sales with the help of store attendants

# STORE-MANAGER API
- Admin can add a product
- Admin/store attendant can get all products
- Admin/store attendant can get a specific product
- Store attendant can add a sale order
- Admin can get all sale order records

## Available endpoints
| Http Method | Endpoint Route | Endpoint Functionality |
| --- | --- | --- |
| POST| /api/v1/auth/register | Signs Up User
| POST | /api/v1/auth/login | Log in User
| POST | /api/v1/auth/logout | Log out User
| GET | /api/v1/products | retrieve all products
| GET |/api/v1/products/productid| retrieve a product by id
| GET| /api/v1/sales | retrieve all sales
| GET |/api/v1/products/saleid | retrieve a sale by id
| POST | /api/v1/products | create a product 
| POST |  /api/v1/sales | create a sale

## Prerequisites
- pip
- virtualenv
- python 3 or python 2.7

# How to Set Up locally
- Clone the repo<br>
git clone https://github.com/Jnjerry/Store-Manager-API.git<br>
- create a virtual environment and activate it <br>
virtualenv env<br>
- install dependencies <br>
pip install -r requirements.txt<br>
