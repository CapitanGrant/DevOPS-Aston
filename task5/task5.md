# Инструкция для Windows 11

## Установка и настройка WSL

1. Откройте PowerShell (от имени администратора) и выполните:
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
```

```
ansible -i inventory.ini all -m ping
```
nano playbook.yml
```
ansible-playbook -i inventory.ini playbook.yml
```
