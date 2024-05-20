def read_en_ru_dict(file_path):
    en_ru_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Проверка наличия разделителя ' - ' в строке
            if ' - ' in line:
                en_word, ru_words = line.strip().split(' - ')
                ru_words_list = [word.strip() for word in ru_words.split(', ')]
                en_ru_dict[en_word] = ru_words_list
            else:
                print(f"Skipping invalid line: {line.strip()}")
    return en_ru_dict

def create_ru_en_dict(en_ru_dict):
    ru_en_dict = {}
    for en_word, ru_words_list in en_ru_dict.items():
        for ru_word in ru_words_list:
            if ru_word not in ru_en_dict:
                ru_en_dict[ru_word] = []
            ru_en_dict[ru_word].append(en_word)
    return ru_en_dict

def write_ru_en_dict(ru_en_dict, file_path):
    sorted_ru_en_dict = dict(sorted(ru_en_dict.items()))
    with open(file_path, 'w', encoding='utf-8') as file:
        for ru_word, en_words_list in sorted_ru_en_dict.items():
            en_words = ', '.join(en_words_list)
            file.write(f"{ru_word} – {en_words}\n")


en_ru_file_path = 'en-ru.txt'
ru_en_file_path = 'ru-en.txt'
    
# Чтение англо-русского словаря
en_ru_dict = read_en_ru_dict(en_ru_file_path)
    
# Создание русско-английского словаря
ru_en_dict = create_ru_en_dict(en_ru_dict)
    
# Запись русско-английского словаря в файл
write_ru_en_dict(ru_en_dict, ru_en_file_path)





