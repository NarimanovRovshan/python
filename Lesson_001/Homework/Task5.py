x1 = int(input('\nВведите координаты первой точки:\nX = ')) 
y1 = int(input('Y = '))
x2 = int(input('Введите координаты второй точки:\nX = '))
y2 = int(input('Y = '))

print(f'\nРасстояние между точками ({x1},{y1}) и ({x2},{y2}) составляет {float(((x2 - x1)**2 + (y2 - y1)**2)**0.5):.2f} условных единиц\n')