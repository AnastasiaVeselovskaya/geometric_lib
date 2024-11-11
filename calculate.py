import circle
import square


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	# Выполняет заданную пользователем функцию для определённой фигуры.
	# Параметры: fig (str) - фигура, для которой требуется провести расчёты; 
	#			 func (str) - функция, соответствующая необходимым расчётам;
	#			 size (arr) - параметры фигуры.
	# Возвращаемое значение: выводит в консоль название, фигуру и значение заданной функции.
	# Примечание: если задана функция main, calc принимает параметры  с консоли. Вывод не меняется.

	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	return result

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square, 2-3 for triangle\n").split(' ')))
	
	calc(fig, func, size)