import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''Функция принимает в себя первым аргументом имя фигуры, вторым аргусентом - то значение,
	которое функция должна получить у данной, третьим - размер, чтобы получить данное значение'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		'''Необходимо ввести фигуру, с которой будут произуведены операции'''
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		'''Необходимо ввести функцию, которая будет применена к фигуре'''
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		'''Необходимо ввести размер нужной фигуры'''
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



