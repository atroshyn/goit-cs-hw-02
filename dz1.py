#!/bin/bash

# Визначаємо масив з URL вебсайтів
websites=("https://google.com" "https://facebook.com" "https://twitter.com")

# Визначаємо назву файлу логів
log_file="website_status.log"

# Очищуємо файл логів перед початком перевірки
> $log_file

# Перевірка доступності кожного сайту
for site in "${websites[@]}"
do
    # Виконуємо HTTP GET запит та отримуємо статус код
    status_code=$(curl -o /dev/null -s -w "%{http_code}" $site)
    
    # Перевіряємо, чи статус код дорівнює 200
    if [ $status_code -eq 200 ]; then
        echo "$site is UP" | tee -a $log_file
    else
        echo "$site is DOWN" | tee -a $log_file
    fi
done

# Вивід повідомлення про записані результати у файл логів
echo "Результати перевірки записані у файл $log_file"
