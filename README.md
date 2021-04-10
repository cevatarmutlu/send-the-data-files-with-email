> [Türkçe README için](/doc/tr-README.md)

# Send the data files with email

This project provides the data obtained with a database query to be converted into a file format (eg Excel) and sent by the email. 

This project supports 1 SMTP connection and 1 database. For more information read [Contribute] (#contribute).

# Motivation

The purpose of this project is to gain certain habits. These habits; Unittest, docstring, planning before starting a project and doing the project by following specific steps.

# Installation

This project has been developed in a debian based linux environment.

```
    sudo apt-get install libpq-dev # for psycopg2 module
    pip install -r req.txt
```

# How to use?

You need to fill in the `Assign this variables` section in the `main.py` file in the root directory of the project. This section is as follows;

```python

    db_type = DBEnum.PostgreSQL # The database you are using. 
    # The login information about the database comes ready in 
    # the required database file under the db folder. You need to change it manually. 
    # It is not given as a parameter.
    data_query = 'SELECT * FROM temp' # The query you will use.

    # attach_file_name = '' # The name of the file you want to add to the mail.
    # It is added by default with the name Data. If you want a different name, remove the comment line.
    attach_file_type = FileTypeEnum.Excel # Type of file to attach to the mail.

    mail_service = MailEnum.Hotmail # Mail service you use
    auth = {
        'user': '', # Mail address
        'password': '' # Mail password
    }
    mailTo = '' # The address you want to send an e-mail to.
    mailSubject = '' # The subject of the mail
    mailMessage = '' # The message of the mail

```

# Contribute

## Add a database

The database supported by this project is only `PostgreSQL`. `MySQL` is a copy of `postgre`.

Create a file with the name of the database you want to add under the `db` folder. This file inherits `IDB` class.

The class you will create must consist of 3 functions. These; `connect`,` fetch`, `disconnect`.

The `connect` function provides the connection with the database. <br/>
The `fetch` function performs the specified query and converts the obtained data to the DataFrame. <br/>
`disconnect` closes the database connection.

Add the database you added to the `DBEnum` file under the `db` folder.

Finally add it to the `if` condition in the `DBFactory` file in the root directory.

## Add to SMTP connection

In this project there is only `hotmail` connection information.

If you want to add mail connection to this project;

You need to add it to the `MailEnum` file under the `Mail` folder.

You need to add the `STMP` connection information as a `dict`.

## Add to File Type

The file types supported by this project are `CSV` and `Excel`.

If you want to add a file type to this project;

Create a file with the name of the file type you want to add under the `writer` folder. This file inherits `IWriter` class.

The class you will create must consist of a single function: `generate`

`generate` function is creating files in the file format you add.

Add the file type you added to the `DBWriter` file under the `writer` folder.

Finally add it to the `if` condition in the `DBWriter` file in the root directory.
