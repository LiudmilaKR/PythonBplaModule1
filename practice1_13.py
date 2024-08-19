# with open('bpla_storage_info.csv', 'r', encoding='utf-8') as f:
#     title = f.readline()
#     content = f.readlines()
#     # content1 = f.read()

# print(title)
# print(content)
# # print(content1)

with open('bpla_storage_warehouse.csv', 'r', encoding='utf-8') as f:
    title = f.readline()
    content = f.read()
    content = content.split('\n')
    
for i in range(len(content)):
    content[i] = content[i].split(',')
    
print(title)
for item in content:
    print(item)
    
try:
    for drone in content:
        if not (drone[5] in ('исправно', 'неисправно')):
            raise ValueError('Такого состояния не существует')
except ValueError as e:
    print('Что творится с твоей БД?')
print('Программа завершена корректно')
        