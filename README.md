# web_api_lesson_4
## Загрузка фото космической тематики
### Установка
Для корректной работы скрипта необходимо установить библиотеки из файла requirements.txt:
```
$ pip3 install -r requirements.txt
```
### Запуск
Скрипт может скачивать фото с сайтов SpaceX и NASA. Для подключения к API последнего потребуется токен. Вы можете получить его на [их сайте](https://api.nasa.gov/).
Для того чтобы использовать токен в скрипте создайте файл *.env* и положите его туда, в формате `NASA_API_TOKEN={nasa_api_token}`.
Для загрузки фотографий с запуска spaceX нужно прописать в консоли команду:
```
$ python3 fetch_spacex.py 
```
ПО умолчанию скрипт скачает и сохранит фотографии с последнего запуска spaceX, если они были. Также вы можете скачать фотографии определённого запуска, зная его ID. Для этого надо указать параметр launch_id при запуске:
```
$ python3 fetch_spacex.py --launch_id={insert launch_id here}
```
Для получения списка запусков spaceX воспользуйтесь README их официального [репозитория](https://github.com/r-spacex/SpaceX-API) 
Скрипт создаст директорию *images/*, скачает и сохранит в неё фото запуска spaceX. Если хотите скачать фото от NASA, запустите 
```
$python3 fetch_nasa.py
```
Скрипт предложит вам указать количество фото, которые вы хотите скачать. Они сохранятся также в директорию *images/*.

## Отправка фото в телеграм-канал
Перед запуском сохраните в файл *.env* токен вашего тг-бота, а также id канала, в который хотите загружать фото, 
в формате `TG_BOT_TOKEN={tg_bot_token}` и `TG_CHAT_ID={tg_chat_id}` соответственно. Убедитесь что бот является администратором канала и может отправлять туда сообщения. По умолчанию бот будет последовательно отправлять фото из папки *images/* с интревалом раз в сутки. Вы можете выбрать любой другой интервал, для этого в файле *.env* укажите время в секундах, в формате `INTERVAL={interval}`
