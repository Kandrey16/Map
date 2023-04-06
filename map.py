coords = [[1,1],[2,2],[3,3],[4,4],[5,5]]
while(True):
    enter = int(input(
            "Выберите функцию: \n"
            "1 - Добавление\n"
            "2 - Изменение\n"
            "3 - Удаление\n"
            "4 - Удаление объектов в определенном диапозоне\n"))

    if (enter > 0 and enter <= 4):
        match enter:
            case 1:
                x = int(input('Введите координаты x: '))
                y = int(input('Введите координаты y: '))
                coords.insert(1,[x,y])
                print(coords)
            case 2:
                x = int(input('Введите координаты x для изменения: '))
                y = int(input('Введите координаты y для изменения: '))
                coords.remove([x,y])
                i = int(input('Введите новые координаты x: '))
                j = int(input('Введите новые координаты y: '))
                coords.insert(1,[i,j])
                print(coords)
            case 3:
                x = int(input('Введите координаты x: '))
                y = int(input('Введите координаты y: '))
                coords.remove([x,y])
                print(coords)
            case 4:
                i = int(input('Введите координату x для удаления 1 точки: '))
                j = int(input('Введите координату y для удаления 1 точки: '))
                a = int(input('Введите координату x для удаления 2 точки: '))
                b = int(input('Введите координату y для удаления 2 точки: '))
                count = 0
                for i in range(j):
                    for a in range(b):
                        del(coords[count])
                        count += count  
                print(coords)
    else:
        print("Неверная операция")

        



