import circle
import square

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {}


def validate_size(fig, size, expected_len):
    if len(size) != expected_len:
        raise ValueError(f"Size must be {expected_len} positive number(s).")

    if not all(isinstance(x, (int, float)) and x > 0 for x in size):
        raise ValueError(f"Size for '{fig}' must be a positive number.")

def calc(fig, func, size):
    # Выполняет заданную пользователем функцию для определённой фигуры.
    # Параметры: fig (str) - фигура, для которой требуется провести расчёты;
    #             func (str) - функция, соответствующая необходимым расчётам;
    #             size (arr) - параметры фигуры.
    # Возвращаемое значение: выводит в консоль название,
    # фигуру и значение заданной функции.
    # Примечание: если задана функция main, calc
    # принимает параметры с консоли. Вывод не меняется.

    if fig not in figs:
        raise ValueError(f"Figure '{fig}' is not valid.")

    if func not in funcs:
        raise ValueError(f"Function '{func}' is not valid function.")

    if fig in ['circle', 'square']:
        validate_size(fig, size, expected_len=1)
    elif fig == 'triangle':
        validate_size(fig, size, expected_len=2)

    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space\n").split(' ')))

    calc(fig, func, size)
