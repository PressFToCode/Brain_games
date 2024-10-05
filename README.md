# Добро пожаловать в Brain-games!

## Структура проекта
Brain_games/
├── bin/                         # Папка с исполняемыми файлами\
│   ├── brain_games/             # Папка с исполняемым файлом для запуска проектов brain_games\
│   │   └── brain_games.py       # Главный исполняемый файл игры, точка входа\
│\
├── src/                         # Папка с основными скриптами\
│   ├── cli/                     # Папка с исходными файлами для командной строки\
│   │   ├── games/               # Папка с файлами описывающими основную логику игры\
│   │   │   ├── progression.py   # Игра "Геометрическая прогрессия"\
│   │   │   └── scm.py           # Игра "Наименьшее общее кратное(НОК)"\
│   │   └── game_engine.py       # Игровой движок, принимающий описанные функции по играм\
│\
└── README.md                    # Описание проекта



## Инструкция по запуску игры

```
git clone https://github.com/PressFToCode/Brain_games.git
cd Brain_games
```

Linux
```bash
python3 bin/brain_games/brain_games.py
```

Window
```powershell
.\bin\brain_games\brain_games.py
```

## Аскиинема демонстрирующая демо версию игры

[![asciicast](https://asciinema.org/a/tSIVgktq3TEUwnCjkxUyNVvqa.svg)](https://asciinema.org/a/tSIVgktq3TEUwnCjkxUyNVvqa)

## Отработка линтера(pylint)
![image](https://github.com/user-attachments/assets/0bc03f16-47bf-499c-82df-20cf8518ede4)


<a href="https://codeclimate.com/github/PressFToCode/Software-development-method/maintainability"><img src="https://api.codeclimate.com/v1/badges/2d72a040938b715dbc32/maintainability" /></a>
