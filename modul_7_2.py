import io
from pprint import pprint
def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a', encoding = 'utf-8')
    for i, s in enumerate(strings):
        key = (i+1, file.tell())
        strings_positions[key] = s
        file.write(s + '\n')
    file.close()
    return strings_positions

def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

if __name__ == '__main__':
    main()

'''
Вывод на консоль:
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')'''