# genius-lyrics-bot
Telegram bot in inline mode that can search and send songs lyrics from genius.com


[<img src="https://img.shields.io/badge/Telegram-%40lyrics__genius__bot-blue">](https://t.me/lyrics_genius_bot)
[![wakatime](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/2409764a-1704-4a62-84b0-70b7ff66a46f.svg)](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/2409764a-1704-4a62-84b0-70b7ff66a46f)

![Aiogram](https://img.shields.io/badge/aiogram-14354C?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

 # Contents
 1. <a href="#install">Install</a>
  * <a href="#prequisites">Prequisites</a> 
  * <a href="#basic-startup">Basic startup</a>
  * <a href="#systemd">Systemd</a>
 2. <a href="#todo">TODO</a>


## Install

### Prequisites
1. Python 3.11 or higher
2. Systemd (if you want to run bot as service)
3. Genius client access token

### Basic startup
Get your access token for Genius API there: https://genius.com/developers
Then clone the repository and install all dependencies by:
```bash
pip install -r requirements.txt
```
Paste your Bot Token and Genius API Token into .env.example and rename it to just .env, then
start bot by:
```bash
python main.py
```

### Systemd
Work-in-progress


## TODO
Make endless inline-menu, because now it's limited and only display 5 songs