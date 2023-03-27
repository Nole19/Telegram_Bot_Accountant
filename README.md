Telegram Accountant Bot


# Telegram bot Account


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Features](#features)
* [Usage](#usage)
* [License](#license)



## General Information
- This telegram bot without token can help with your incomes and costs calculations, connected with SQLite3 


## Technologies Used
- Python 
- Libraries: Aiogram, SQLite3

## Installation


1. Clone the repository:

```bash
  git clone https://github.com/Nole19/Telegram_bot_Accountant.git
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a new bot and obtain the API token from [BotFather](https://t.me/BotFather).

4. Add the API token to the **config.py** file in the project directory:
```bash
BOT_TOKEN="<BOT-TOKEN>" 
```

5. Run the bot
```bash
python bot.py
```

## Features
- Bot can write and remember how much you spent 
- Bot can write and remember how much you earened
- Bot can show hole history of transacions

## Usage

- /start - start the bot
- /help - display the help message
- /earned <amount> <description> - record a new income
- /spent <amount> <description> - record a new cost
- /history - display the transaction history
  
Example
```
> /earned 1000 Received payment from client
Income recorded successfully.

> /spent 500 Bought groceries
Spent recorded successfully.

> /history
Transaction history:

1. Earned: +$1000 - Received payment from client
2. Spent: -$500 - Bought groceries
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

