# RU
## Использование

1. Зайти в браузер Яндекс-музыка - коллекция - история
2. Нажать `F12` - вкладка `Network`
3. В фильтре написать `library.jsx` и очистить текущие трейсы, если есть
4. Нажать `F5`, чтобы обновить страницу
5. Выбрать второй `library.jsx` - ПКМ - `copy` - `copy response`
6. Создать файл `tracks.json`, вставить туда содержимое и сохранить
7. Установить pip-пакет
8. Запустить скрипт, в вопросе указать путь к файлу (**без кавычек и прочего!**)
9. В этой же директории, где скрипт запущен, будет создан файл `tracks.txt`, где перечислены *уникальные* позиции в формате `песня - исполнитель`

### Видео для шагов 1-5
https://github.com/Keonik1/YaMusicHistoryToTXT/assets/57857901/ba05d9f4-6e70-4c85-9c1b-450dc9c89522

## Установка
### Установить pip-пакет
```bash
pip install -U yandex-music
```

### Скачать скрипт
```bash
wget https://raw.githubusercontent.com/Keonik1/YaMusicHistoryToTXT/main/trackIdsToNames.py
```

## Запуск
```bash
python3 ./trackIdsToNames.py
#Enter path to file which contains trackIds: tracks.json
```
На выходе будет получен список треков сохраненный в файл `tracks.txt`

# EN
## Usage

1. Go to the browser Yandex-music - collection - history
2. Press `F12` - tab `Network`.
3. In the filter write `library.jsx` and clear the current traces, if there are any
4. Press `F5` to refresh the page
5. Select the second `library.jsx` - RMB - `copy` - `copy response`
6. Create a `tracks.json` file, paste the contents into it and save it
7. Install the pip package
8. Run the script, specify the path to the file in the question (**without quotes or anything else!**).
9. In the same directory where the script is run, a `tracks.txt` file will be created listing the *unique* positions in `song - artist` format

### Video for steps 1-5
https://github.com/Keonik1/YaMusicHistoryToTXT/assets/57857901/ba05d9f4-6e70-4c85-9c1b-450dc9c89522

### Installation
### Install the pip package
```bash
pip install -U yandex-music
```

### Download the script
```bash
wget https://raw.githubusercontent.com/Keonik1/YaMusicHistoryToTXT/main/trackIdsToNames.py
```

## Run
```bash
python3 ./trackIdsToNames.py
#Enter path to file which contains trackIds: tracks.json
```
The output will be a list of tracks saved in the file `tracks.txt`.
