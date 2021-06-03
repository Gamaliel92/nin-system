### NIN-SYSTEM

A test API to enable users link their NIN to their phone numbers.

#### Setup

- Create your virtual environment using `virtualenv env`, `pipenv shell` or which ever virtual environment library you prefer 
- Clone this repository - `git clone https://github.com/DeeStarks/nin-system.git`
- `cd nin-system` and install all requirements using - `pip install -r requirements.txt`
- Runserver `python manage.py runserver`

#### Contributing

- Use the fork button at the top of this repo to fork the project
- Write your codes and open pull requests
- Remember to always include newly installed libraries in the requirements i.e `pip freeze > requirements.txt`

#### Documentation

To link NIN, a payment of NGN 500 (by default) will be made (note that this is a test mode and no amount whatsoever will be deducted from the account you provided, you can use random numbers instead) and you will get a secret key which you will pass to the Authorization header.

Once a payment is made with a particular phone number and a secret key is been responded upon success to request, only that phone number will be able to use the secret as Authorization header during linkage.

The secret key can be used once. After a successful linkage, the secret provided to the Authorization header will no more be usable and will require another payment to get a new secret key.

Note: I used `<HOST>` where you should input the host you're on.

- Make payments on `<HOST>/pay` which requires a single header `Content-Type: application/json` if using an API tool like postman or curl. All keys are required and should be sent in a format like below:
```json
{
    "phone_number": "09000000001",
    "bank_code": "063",
    "account_number": "1010000010"
}
```

If data is sent correctly, there should be a response like below:
```json
{
    "status": "success",
    "message": "Your payment was successful. Note that your secret key can only be used once to link NIN with the phone number you provided, and can't be retrived once this response is closed.",
    "data": {
        "amount": "500",
        "currency": "NGN",
        "secret_key": "NIN_7HYWEJnq4bpCGB1rw_AXI2NTPmvOktx0jDMSfLoVgezcyZhKs6"
    }
}
```

- To get a list of banks and their codes, `GET` request to endpoint `<HOST>/banks`. 
- All requests to link NIN will be accessible on `<HOST>`.
- To link NIN to phone number, make a `POST` request to `<HOST>/nin/link` with the headers below:

```
    Content-Type: application/json
    Authorization: Bearer <YOUR_SECRET_KEY>
```
And body should be passed in the format below:
```json
{
    "nin": "1010111111",
    "phone_number": "09000000001"
}
```
Success response will be sent like below if request objects are checked:
```json
{
    "status": "success",
    "message": "Your NIN was successfully linked. Note that you can no more use the provided Authorization header",
    "data": {
        "nin": "1010111111",
        "phone_number": "09000000001"
    }
}
```