import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', "8978848"))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "24ce3cff2d32cf529df1c0018e28d6cf")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5964978379:AAH0qquiDaWv_Xk2QlhO9XyMNuhDHemesoM")
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgres://auwoxqvd:vXIRMzHU1DalcaVwWgbGo8ZFfNTQ3fHt@balarama.db.elephantsql.com/auwoxqvd")
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', "-1001800504636")
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "-1001800504636")
else:
    # Fill the Values
    API_ID = 8978848
    API_HASH = "24ce3cff2d32cf529df1c0018e28d6cf"
    BOT_TOKEN = "5964978379:AAH0qquiDaWv_Xk2QlhO9XyMNuhDHemesoM"
    DATABASE_URL = "postgres://auwoxqvd:vXIRMzHU1DalcaVwWgbGo8ZFfNTQ3fHt@balarama.db.elephantsql.com/auwoxqvd"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "-1001800504636"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[-1001800504636]

DEV=[1995886602]
