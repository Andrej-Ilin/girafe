import os
import pandas as pd

def list_files(startpath):
    data = []
    for root, dirs, files in os.walk(startpath):
        for name in files:
            file_path = os.path.join(root, name)
            data.append({'Directory': root, 'File': name})
    return data

def main():
    # Укажите путь к директории, которую хотите обойти
    startpath = '~/Бза_прошивок'  # Замените на ваш путь

    file_list = list_files(startpath)

    # Создаем DataFrame
    df = pd.DataFrame(file_list)

    # Сохраняем DataFrame в Excel
    output_file = 'output.xlsx'
    df.to_excel(output_file, index=False)

    print(f'Список файлов сохранен в {output_file}')

if __name__ == "__main__":
    main()