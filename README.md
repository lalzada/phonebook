###### A demo application (REST APIs) built in Django and SQLite to manage a user's contacts and phone numbers

##### Tested Enviroment
```
Python 2.7
Python 3.4
Django 1.11
Django Rest Framework 3.6
SQLite3
Ubuntu 14.04
```

##### Switch to project root directory and run below command to install project dependencies
```
pip install -r requirements.txt
```

##### Switch to project root directory and run below command to run project using built-in server
```
python manage.py runserver
```

##### API Endpoints
<table>
    <tr>
        <th>Endpoint</th>
        <th>Desc</th>
        <th>Method</th>
        <th>Data</th>
        <th>Require</th>
        <th>Response</th>
    </tr>
    <tr>
        <td>/users/</td>
        <td>Register new user</td>
        <td>POST</td>
        <td>{"username": "Alex", "password": 123}</td>
        <td>username, password</td>
        <td>User Object</td>
    </tr>
    <tr>
        <td>/contacts/</td>
        <td>Get list of contacts for logged in user</td>
        <td>GET</td>
        <td>{}</td>
        <td>No data required</td>
        <td>List of all contacts</td>
    </tr>
    <tr>
        <td>/contacts/</td>
        <td>Add New Contact with or without phone numbers</td>
        <td>POST</td>
        <td>{"name": "Mike", "phone_numbers": [{"number": "+23018574741"}, {"number": "+23018574741"}] }</td>
        <td>name</td>
        <td>Contact object including phone number list</td>
    </tr>
    <tr>
        <td>/contacts/{pk}/</td>
        <td>Update existing contact</td>
        <td>PUT</td>
        <td>{"name": "New Contact name"}</td>
        <td>name</td>
        <td>Contact object including phone number list</td>
    </tr>
    <tr>
        <td>/contacts/{pk}/</td>
        <td>Delete existing contact</td>
        <td>DELETE</td>
        <td>{}</td>
        <td>No data required</td>
        <td>Empty response</td>
    </tr>
    <tr>
        <td>/contacts/{pk}/phone_numbers/</td>
        <td>Add phone number to existing contact</td>
        <td>POST</td>
        <td>{"phone_number": "+914545414524"}</td>
        <td>phone_number</td>
        <td>Phone number object</td>
    </tr>
</table>

```
NOTE: To view/add/delete users/contacts/phonenumbers login to Admin panel /admin/ with admin/demo1234
```

##### Available Users for testing purposes

```
user: demo1
pass: demo1

user: demo2
pass: demo2
```

##### Validations
```
1. Validing all international phone numbers

2. One contact can have 0 or more phone numbers

3. More than one contact can have the same phone number (think household landlines)
```
