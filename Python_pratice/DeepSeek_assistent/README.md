/ai_assistant\
│── Dockerfile\
│── requirements.txt\
│── app.py # Основной код с Tkinter GUI\
│── screen_capture.py # Код для захвата экрана\
│── deepseek_api.py # Код для запроса к DeepSeek-R1\
│── text_processing.py # OCR обработка текста\
│── tts.py # Голосовой движок\
│── hotkeys.py # Горячие клавиши\
│── config.py # Конфигурации проекта

Сборка и запуск в Docker

docker build -t ai_assistant .
docker run --rm -it --name assistant ai_assistant
xhost +local:root
sudo docker run --rm -it --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix ai_assistant

Итог

✅ Код разбит на файлы для удобства.

✅ Работает в Docker, не требует сложной настройки.

✅ Есть GUI, горячие клавиши и голосовой вывод.

✅ DeepSeek-R1 подключен к системе.