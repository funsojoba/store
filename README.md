# Store (for lack of good name)

## Not your regular e-commerce API, trust me

___
## How to get started

- Make sure you have Docker installed on your machine
- in whatever directory you'll like to work, run the following commands
```
git clone https://github.com/funsojoba/store.git
cd store
touch .env - to create an env file  
make build - this builds your Docker image
make up - this should start your project
```
You might want to configure your `.env` file to suit your prefered configuration, the required `.env` values are provided in the `.env.example` file

Your code should be running on `http://127.0.0.1:8000/` the default url is for the Swagger Docs





