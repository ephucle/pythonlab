#https://realpython.com/intermediate-python-project-ideas/
#https://pysimplegui.readthedocs.io/en/latest/
import PySimpleGUI as sg
import pandas as pd
import numpy as np
import sqlite3 
import sys

#------------------------------- This is to include a matplotlib figure in a Tkinter canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as Tk

def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)

    def on_key_press(event):
        key_press_handler(event, canvas, toolbar)
        canvas.TKCanvas.mpl_connect("key_press_event", on_key_press)
    return


class Toolbar(NavigationToolbar2Tk):
    # only display the buttons we need
    toolitems = [t for t in NavigationToolbar2Tk.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom')]
                # t[0] in ('Home', 'Pan', 'Zoom','Save')]

    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)
#-------------------------------end This is to include a matplotlib figure in a Tkinter canvas


def create_sqlite_table():
	conn = sqlite3.connect('expenses.db')
	c = conn.cursor()
	# Create table
	#check if table exist
	c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='expenses' ''')
	if c.fetchone()[0]==1:
		print("Table existed")
		
	else:
		print("start to create table:")
		
		c.execute('''CREATE TABLE expenses (name text, ammount INTEGER, daytime text PRIMARY KEY)''')
		
		conn.commit()
		print("Successful create sqlite expenses.db with table expenses")
	conn.close()

def get_and_print_all_database():
	print("Reading sqlite3 database expenses.db...")
	result = []
	conn = sqlite3.connect('expenses.db')
	c = conn.cursor()
	for row in c.execute('SELECT * FROM expenses ORDER BY daytime'):
		print(row)
		result.append(row)
		
	return result

def get_by_name(name):
	'''get data, store to a list, and print all row, line by line'''
	#get row from database
	
	result = []
	conn = sqlite3.connect('expenses.db')
	c = conn.cursor()
	#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
	for row in c.execute("SELECT * FROM expenses WHERE name=?", (name,)):
		#print(row) #('8.8.8.8', 53, 1)
		result.append(row)
	return result

def insert_database(data =('mua sach',53000,'30-07-2020')):
	conn = sqlite3.connect('expenses.db')
	c = conn.cursor()
	c.execute("INSERT INTO expenses VALUES (?,?,?)", data)
	
	conn.commit()
	conn.close()
	
def delete_database(daytime):
	conn = sqlite3.connect('expenses.db')
	c = conn.cursor()
	c.execute("DELETE from expenses where daytime = ?", (daytime,))
	
	#sql_delete_query = """DELETE from SqliteDb_developers where id = 6"""
	#for row in c.execute("SELECT * FROM expenses WHERE name=?", (name,)):
	
	conn.commit()
	conn.close()


	
create_sqlite_table()
#tao cac giao dich gia de test database
#insert_database(data = ('sach',53000,"2020-07-29 16:14:45"))
#insert_database(data = ('quan_ao',200000,"2020-07-17 13:14:45"))
#insert_database(data = ('giay',1000000,"2020-07-30 16:14:45"))
#insert_database(data = ('xedap',4000000,"2020-05-10 13:14:45"))
get_and_print_all_database()

name = "xedap"
print(f"Test get data from database by name: {name}")
print(get_by_name(name))
#sys.exit()

##test delete database
#print ("deleting some item in database")
#delete_database("2020-07-20 15:00:00")
#delete_database("2020-09-20 17:00:00")
#delete_database("2020-10-20 09:00:00")
#print ("deleting done")

 
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Some text on Row 1')],
			[sg.Text('Name'), sg.InputText()],
			[sg.Text('Ammount'), sg.InputText()],
			[sg.Text('Daytime'), sg.InputText()],
			[sg.Button('Insert'), sg.Button('Cancel')], 
			[sg.Button('Read')],
			[sg.Button('Plot')],
			[sg.Multiline(size=(50, 5), key='textbox')],
			[sg.Canvas(key='controls_cv')],
			[sg.Column(
	layout=[
			[sg.Canvas(key='fig_cv',
						# it's important that you set this size
						size=(200 * 2, 200)
						)]
			],
			background_color='#DAE0E6',
			pad=(0, 0)
			)],
		]
# Create the Window
window = sg.Window('Expense Tracker', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
		break
	if event == "Insert":
		print ("Button Insert is pressed")
		name = values[0]
		ammount = int(values[1])
		daytime = values[2]
		print('name ', name)
		print('ammount ', ammount)
		print('daytime ', daytime)
		
		#update database
		insert_database( (name,ammount,daytime))
		print("insert successful data to database")
	if event == "Read":
		print("Button Read is pressed")
		all_rows =get_and_print_all_database()
		datas =""
		for row in all_rows:
			#datas +=str(row)
			datas += "{0:<15}{1:<17}{2:<30}".format(row[0], row[1], row[2])
			datas += "\n"
			
		#https://www.reddit.com/r/learnpython/comments/f7zklb/pysimplegui_update_multiline_element_with_new_text/
		#window['textbox'].update('This is how you update the LEFT hand multiline')
		window['textbox'].update(datas)
	if event == "Plot":
		#------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
		plt.figure(1)
		fig = plt.gcf()
		DPI = fig.get_dpi()
		#------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
		fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
		#-------------------------------
		#x = np.linspace(0, 2 * np.pi)
		#y = np.sin(x)
		#plt.plot(x, y)
		#plt.title('y=sin(x)')
		#plt.xlabel('X')
		#plt.ylabel('Y')
		#plt.grid()
		
		data = get_and_print_all_database()
		df = pd.DataFrame(data)
		df.columns = ['name','ammount','daytime']
		print (df)
		
		#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
		objects = df['daytime']
		y_pos = np.arange(len(objects))
		#performance = [10,8,6,4,2,1]
		performance = df['ammount']
		
		plt.bar(y_pos, performance, align='center', alpha=0.5)
		plt.xticks(y_pos, objects)
		plt.ylabel('Ammount')
		plt.title('Ammount per day')
		
		#------------------------------- Instead of plt.show()
		draw_figure_w_toolbar(window.FindElement('fig_cv').TKCanvas, fig, window.FindElement('controls_cv').TKCanvas)
		#-------------------------------

window.close()