from tkinter import *

class Interface():
	def __init__(self, win):

		self.win = win

		self.win.title('Connect Four AI setup menu')
		self.win.resizable(width = False, height = False)

		player_list=['Human', 'Random AI', 'Monte Carlo AI']
		

		self.p1 = StringVar(self.win)
		self.p1.set(player_list[0])
		player_one_text = Label(self.win, text = "Select Player 1")
		player_one_select = OptionMenu(self.win, self.p1, *player_list, command = self.check_options)
		player_one_select.config(width = 12)
		
		verses_text=Label(text = 'Verses',anchor = N)
		verses_text.config(font=("TKDefaultFont",16))

		self.p2 = StringVar(self.win)
		self.p2.set(player_list[0])
		player_two_text = Label(self.win, text = "Select Player 2")
		player_two_select = OptionMenu(self.win, self.p2, *player_list, command = self.check_options)
		player_two_select.config(width = 12)

		self.vis_response = IntVar()
		self.vis_response.set(1)
		self.vis_checkbox = Checkbutton(self.win, text = "Visualize Match", variable = self.vis_response, state = DISABLED)

		self.sims_one = StringVar()
		self.sims_one.set('300')
		self.simulations_one = Entry(self.win, textvariable = self.sims_one, state = DISABLED, justify = CENTER, width = 12)
		self.sims_two = StringVar()
		self.sims_two.set('300')
		self.simulations_two = Entry(self.win, textvariable = self.sims_two, state = DISABLED, justify = CENTER, width = 12)

		self.sims_text_left = Label(self.win, text = "Simulations to run", state = DISABLED)
		self.sims_text_right = Label(self.win, text = "Simulations to run", state = DISABLED)

		self.games = StringVar(value = '# of games')
		games_entry = Entry(self.win, textvariable = self.games, justify = CENTER, width = 12)

		play_button = Button(self.win, text = "Play", command = self.play_button_pressed, justify = CENTER, width = 10, height = 2, bd = 3)
		
		# Create place method?
		x_pad = 15
		y_pad = 7
		player_one_text.grid(row = 1, column = 1, padx = x_pad, pady = (10,0))
		player_one_select.grid(row = 2, column = 1, padx = x_pad, pady = (0,10))
		verses_text.grid(row = 2, column = 2, padx = x_pad, pady = y_pad)
		player_two_text.grid(row = 1, column = 3, padx = x_pad, pady = (10,0))
		player_two_select.grid(row = 2, column = 3, padx = x_pad, pady = (0,10))
		self.vis_checkbox.grid(row = 3, column = 2)
		self.simulations_one.grid(row = 3, column = 1, padx = x_pad, pady = y_pad)
		self.simulations_two.grid(row = 3, column = 3, padx = x_pad, pady = y_pad)
		games_entry.grid(row = 4, column = 2)
		play_button.grid(row = 5, column = 2, pady = y_pad)


	def play_button_pressed(self):
		self.trim_sims()
		self.trim_games()
		self.close_setup()


	def check_options(self, value):
		if self.p1.get() == "Human" or self.p2.get() == "Human":
			self.vis_checkbox.config(state=DISABLED)
			self.vis_response.set(1)
		else:
			self.vis_checkbox.config(state=NORMAL)

		if self.p1.get()=="Monte Carlo AI":
			self.simulations_one.config(state=NORMAL)
			self.sims_text_left.grid(row = 4, column = 1, padx = 15, sticky = N)
		else:
			self.simulations_one.config(state=DISABLED)
			self.sims_text_left.grid_forget()

		if self.p2.get()=="Monte Carlo AI":
			self.simulations_two.config(state=NORMAL)
			self.sims_text_right.grid(row = 4, column = 3, padx = 15, sticky = N)

		else:
			self.simulations_two.config(state=DISABLED)
			self.sims_text_right.grid_forget()


	def trim_sims(self):
		if int(self.sims_one.get()) < 100:
			self.sims_one.set('100')
		elif int(self.sims_one.get()) > 5000:
			self.sims_one.set('5000')

		if int(self.sims_two.get()) < 100:
			self.sims_two.set('100')
		elif int(self.sims_two.get()) > 5000:
			self.sims_two.set('5000')


	def trim_games(self):
		try:
			num_games = int(self.games.get())
			if num_games < 1:
				self.games.set('1')
			elif num_games > 500000:
				self.games.set('500000')
		except ValueError:
			num_games = 1
			self.games.set('1')

	def get_menu_results(self):
		return((self.p1.get(),self.p2.get(),int(self.games.get()),self.vis_response.get(),int(self.sims_one.get()),int(self.sims_two.get())))


	def close_setup(self):
		print('close')
		self.win.quit()
		self.win.destroy()

def menu_main():
	root = Tk()
	window = Interface(root)
	root.mainloop()
	return(window.get_menu_results())

if __name__ == "__main__":
	root = Tk()
	window = Interface(root)
	root.mainloop()
	print(window.get_menu_results())