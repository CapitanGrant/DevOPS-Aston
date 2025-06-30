# Настройка локального домена `app.local` с использованием Nginx и HTTPS

Этот гайд поможет вам настроить локальный домен `app.local` с использованием веб-сервера **Nginx** и **самоподписанного SSL-сертификата**.

---

## 📦 Установка Nginx

```bash
sudo apt install nginx
```
# Запуск
```bash
sudo systemctl start nginx
```

# Перезапуск
```bash
sudo systemctl restart nginx
```

# Автозапуск при загрузке системы
```bash
sudo systemctl enable nginx
```

2. Создание конфигурации сайта app.local
Перейдите в директорию с конфигурациями:

```bash
cd /etc/nginx/sites-available
```
Создайте новый конфигурационный файл:

```bash
sudo nano applocal.conf
```
Вставьте следующий код:

```bash
server {
    listen 80;
    server_name app.local;
    root /var/www/app.local;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }

    access_log /var/log/nginx/applocal.access.log;
    error_log /var/log/nginx/applocal.error.log;
}
```
3. Настройка /etc/hosts
Откройте файл:

```bash
sudo nano /etc/hosts
```
Добавьте строку:

```bash
127.0.0.1   app.local
```
4. Активация конфигурации
Создайте симлинк и директорию:

```bash
sudo ln -s /etc/nginx/sites-available/applocal.conf /etc/nginx/sites-enabled/
sudo mkdir -p /var/www/app.local
```
Создайте тестовую страницу:

```bash
echo "<h1>Welcome to app.local</h1>" | sudo tee /var/www/app.local/index.html
```
Перезапустите Nginx:

```bash
sudo systemctl restart nginx
```
5. Настройка HTTPS (самоподписанный сертификат)
Создайте директорию и сгенерируйте сертификат:

```bash
sudo mkdir -p /etc/nginx/ssl/app.local
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/app.local/privkey.pem \
  -out /etc/nginx/ssl/app.local/fullchain.pem \
  -subj "/CN=app.local"
```
Обновите файл конфигурации:

```bash
sudo nano /etc/nginx/sites-available/applocal.conf
```
Вставьте следующее содержимое:

```bash
server {
    listen 443 ssl;
    server_name app.local;

    ssl_certificate /etc/nginx/ssl/app.local/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/app.local/privkey.pem;

    root /var/www/app.local;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

server {
    listen 80;
    server_name app.local;
    return 301 https://$host$request_uri;
}
```
Проверьте конфигурацию и перезапустите Nginx:
```bash
sudo nginx -t && sudo systemctl restart nginx
```
6. Запуск скрипта applocal.py
Перейдите в директорию со скриптом:
```bash
cd /путь/к/скрипту
```
Запустите скрипт:

```bash
python3 applocal.py
```



