### Если просто просмотреть работу сервера - [здесь](https://dry-crag-99858.herokuapp.com/)

### Если необходимо проверить еще и на sentry.io как идет запись логов, то:
1. Скачать файлы
2. В файле **settings.ini** прописать линк на свой sentry(по умолчанию)
3. Поднять новый сервер на хероку и залить файлы или просто заменить файлы через Heroku CLI в своём уже существующем проекте
4. Понажимать на ссылки и проверить в своём аккаунте на *sentry.io*

Интеграция с Sentry - путем добавления зависимости в файл **requirements.txt**