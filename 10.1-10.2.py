import json

def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"products": []}

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def display_products(products):
    for product in products:
        name = product['name']
        price = product['price']
        weight = product['weight']
        available = "В наличии" if product['available'] else "Нет в наличии!"
        
        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        print(available)
        print()  # Пустая строка для разделения продуктов

def add_product():
    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии (да/нет): ").strip().lower() == 'да'
    
    return {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }


file_path = 'products.json'
    
# Загружаем текущие данные
data = load_data(file_path)
    
# Добавляем новый продукт
new_product = add_product()
data['products'].append(new_product)
    
# Сохраняем обновленные данные в файл
save_data(file_path, data)
    
# Выводим обновленное содержимое файла на экран
display_products(data['products'])
