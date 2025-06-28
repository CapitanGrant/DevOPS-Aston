1. Подготовка окружения
sudo mkdir /home/aston/opt/app
cd /home/aston/opt/app
sudo touch myscript.sh
nano myscript.sh

3. Содержимое скрипта (myscript.sh)
#!/bin/bash

echo "Create directory home/aston/opt/app"
mkdir /home/aston/opt/app
echo "Create file home/aston/opt/app/log.txt"
touch /home/aston/opt/app/log.txt
while true; do
  строка="Случайная строка $(date +%s)"
  echo "$строка" >> /home/aston/opt/app/log.txt
  sleep 17
done

3. Настройка прав и пользователя
# Даем права на исполнение
sudo chmod +x /home/aston/myscript.sh

# Создаем отдельного пользователя для службы
sudo adduser --system --no-create-home aston_service

# Создаем my_service.log
sudo touch /home/aston/opt/app/my_service.log

# Настраиваем права
sudo chown -R aston_service:aston_service /home/aston/opt
sudo chmod 755 /home/aston/opt/app/myscript.sh


4. Создание Systemd сервиса
sudo nano /etc/systemd/system/aston_task3.service

Содержимое файла сервиса:
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

5. Активация сервиса
# Обновляем конфигурацию systemd
sudo systemctl daemon-reload

# Включаем автозапуск
sudo systemctl enable aston_task3.service

# Запускаем сервис
sudo systemctl start aston_task3.service

# Проверяем статус
sudo systemctl status aston_task3.service
   
6. Проверка работы
journalctl -u aston_task3.service -f
tail -f /home/aston/opt/app/log.txt
tail -f /home/aston/opt/app/my_service.log
7. Управление сервисом
Остановка сервиса:
sudo systemctl stop aston_task3.service
Перезапуск:
sudo systemctl restart aston_task3.service
Отключение автозапуска:
sudo systemctl disable aston_task3.service
