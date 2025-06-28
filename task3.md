# 🛠 Настройка systemd-сервиса на базе Bash-скрипта

## 1. Подготовка окружения

```bash
sudo mkdir -p /home/aston/opt/app
cd /home/aston/opt/app
sudo touch myscript.sh
nano myscript.sh
```

## 2. Содержимое скрипта (`myscript.sh`)

```bash
#!/bin/bash

echo "Create directory /home/aston/opt/app"
mkdir -p /home/aston/opt/app
echo "Create file /home/aston/opt/app/log.txt"
touch /home/aston/opt/app/log.txt

while true; do
  строка="Случайная строка $(date +%s)"
  echo "$строка" >> /home/aston/opt/app/log.txt
  sleep 17
done
```

## 3. Настройка прав и пользователя

```bash
# Даем права на исполнение
sudo chmod +x /home/aston/opt/app/myscript.sh

# Создаем отдельного пользователя для службы
sudo adduser --system --no-create-home aston_service

# Создаем лог-файл
sudo touch /home/aston/opt/app/my_service.log

# Настраиваем права
sudo chown -R aston_service:aston_service /home/aston/opt
sudo chmod 755 /home/aston/opt/app/myscript.sh
```

## 4. Создание systemd-сервиса

```bash
sudo nano /etc/systemd/system/aston_task3.service
```

### 📄 Содержимое файла `aston_task3.service`:

```ini
[Unit]
Description=My Aston Task 3 Service
After=network.target

[Service]
Type=simple
User=aston_service
WorkingDirectory=/home/aston/opt/app
ExecStart=/bin/bash /home/aston/opt/app/myscript.sh
Restart=always
RestartSec=5s
StandardOutput=file:/home/aston/opt/app/my_service.log
StandardError=file:/home/aston/opt/app/my_service.log

[Install]
WantedBy=multi-user.target
```

## 5. Активация сервиса

```bash
sudo systemctl daemon-reload
sudo systemctl enable aston_task3.service
sudo systemctl start aston_task3.service
sudo systemctl status aston_task3.service
```

## 6. Проверка работы

```bash
journalctl -u aston_task3.service -f
tail -f /home/aston/opt/app/log.txt
tail -f /home/aston/opt/app/my_service.log
```

## 7. Управление сервисом

```bash
sudo systemctl stop aston_task3.service
sudo systemctl restart aston_task3.service
sudo systemctl disable aston_task3.service
```
