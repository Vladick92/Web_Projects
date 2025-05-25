This api is for bank. 
    Types of users:
    1) Client - can issue credit or deposit, add up to 3 credit cards, and add real estate so lately this property will be mortage in credit
    2) Banker - can do same as client, but also can approve credit from client

    Entities in db:
    1) Client
    2) Banker
    3) Credit card
    4) Credit
    5) Deposit
    6) Real estate

    Built with: FastAPI, sqlalchemy, postgresql, pydantic