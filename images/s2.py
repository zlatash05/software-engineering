def read_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise Exception("Файл пустой")
            print(content)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(e)

read_file_content('empty.txt')
read_file_content('aaa.txt')