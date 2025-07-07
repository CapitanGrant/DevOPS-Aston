# Инструкция для Windows 11

## Установка и настройка WSL

Откройте PowerShell (от имени администратора) и выполните:
   ```powershell
   wsl --install
   ```
Если WSL уже установлен, обновите его:
   ```
   powershell
   wsl --update
   ```
Проверьте список установленных дистрибутивов:
   ```
   powershell
   wsl --list --verbose
   ```
Запустите Ubuntu через WSL
В PowerShell просто введите:
   ```powershell
   wsl
   ```
В терминале WSL (Ubuntu) выполните:
   ```
   sudo apt update && sudo apt install ansible -y
   ```

Проверьте версию:
   ```
   ansible --version
   ```
Откройте файл inventory.ini
   ```
   nano inventory.ini
   ```
Пропишите host
   ```
   localhost ansible_connection=local
   ```
Проверьте работу ansible
   ```
   ansible -i inventory.ini all -m ping
   ```
Вставьте код из файла playbook.yml
   ```
   nano playbook.yml
   ```
Запустите ваш playbook.yml
   ```
   ansible-playbook -i inventory.ini playbook.yml
   ```

