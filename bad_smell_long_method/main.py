# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    # Чтение данных из строки
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(csv):
    result = [user.split(';') for user in csv.split('\n')]
    return result


def _sort(data):
    result = sorted(data, key=lambda x: x[1], reverse=True)
    return result


def _filter(data):
    result = [user for user in data if int(user[1]) > 10]
    return result


if __name__ == '__main__':
    print(get_users_list())
