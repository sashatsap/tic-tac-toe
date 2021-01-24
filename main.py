moves = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def show_table():
	print(
		f'                \n'
		f'  CURRENT TABLE:\n'
		f'                \n'
		f'   —     —     —\n'
		f'|  {moves[0]}  |  {moves[1]}  |  {moves[2]}  |\n'
		f'   —     —     —\n'
		f'|  {moves[3]}  |  {moves[4]}  |  {moves[5]}  |\n'
		f'   —     —     —\n'
		f'|  {moves[6]}  |  {moves[7]}  |  {moves[8]}  |\n'
		f'   —     —     —\n'
		f'                 \n'
		f'SELECT THE FIELD 1 - 9:\n'
	)


def check_winner() -> bool:
	for symbol in ('X', 'O'):
		if (moves[0] == symbol and moves[1] == symbol and moves[2] == symbol) \
				or (moves[3] == symbol and moves[4] == symbol and moves[5] == symbol) \
				or (moves[6] == symbol and moves[7] == symbol and moves[8] == symbol) \
				or (moves[0] == symbol and moves[3] == symbol and moves[6] == symbol) \
				or (moves[1] == symbol and moves[4] == symbol and moves[7] == symbol) \
				or (moves[2] == symbol and moves[5] == symbol and moves[8] == symbol) \
				or (moves[0] == symbol and moves[4] == symbol and moves[8] == symbol) \
				or (moves[2] == symbol and moves[4] == symbol and moves[6] == symbol):
			print(f'WINNER PLAYER {symbol} !!!!!!!!!')
			return True

	return False


def make_move(i, choice) -> bool:
	if moves[choice - 1] == ' ':
		if i % 2 == 0:
			moves[choice - 1] = 'X'
		else:
			moves[choice - 1] = 'O'
		return True
	else:
		return False


def main():
	show_table()
	for i in range(9):
		choice = int(input())
		while not make_move(i, choice):
			choice = int(input())
		show_table()
		if check_winner():
			break


if __name__ == '__main__':
	main()
