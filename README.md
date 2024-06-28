# Usage

1. Зайти в браузер Яндекс-музыка - коллекция - история
2. Нажать F12 - вкладка `Network`
3. В фильтре написать `library.jsx` и очистить текущие трейсы, если есть
4. Нажать F5, чтобы обновить страницу
5. Выбрать второй `library.jsx` - ПКМ - `copy` - `copy response`
6. Создать файл `tracks.json` и вставляешь туда содержимое и сохраняешь
7. Установить pip-пакет
8. Запустить скрипт, в вопросе указать путь к файлу (**без кавычек и прочего!**)
9. В этой же директории, где скрипт запущен, будет создан файл `tracks.txt`, где перечислены *уникальные* позиции в формате `песня - исполнитель`

# Installation
## Установить pip-пакет
```bash
pip install -U yandex-music
```

## Скачать скрипт
```bash
wget https://raw.githubusercontent.com/Keonik1/YaMusicHistoryToTXT/main/trackIdsToNames.py
```

# Startup
```bash
python3 ./trackIdsToNames.py
#Enter path to file which contains trackIds: tracks.json
```
На выходе будет получен список треков сохраненный в файл `tracks.txt`

