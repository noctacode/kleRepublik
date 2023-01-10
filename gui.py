from functions import *
from tkinter import *
import tkinter.font as font
from time import sleep

def finish():
    global window
    try:
        browser.quit()
        window.destroy()
    except:
        window.destroy()

def custom_url():
    try: browser.get(url_input.get())
    except:
        browser_start()
        browser.get(url_input.get())


window = Tk()

window.title('kleRepublik')
window.geometry('1080x720')

colour_bg = '#1c1c1c'
colour_fg = '#257550'

font_16_bold = font.Font(size=16, weight='bold')
font_bold = font.Font(weight='bold')

window.configure(background = colour_bg)

window.grid_columnconfigure(3, minsize=200)
window.grid_rowconfigure(0, minsize=10)


group_1_column = 2
label_group_1 = Label(window, text='SESSION COMMANDS', font=font_16_bold, bg=colour_bg, fg=colour_fg).grid(column=2, row=0)

url_input = StringVar()
url_input_field = Entry(window, textvariable = url_input).grid(column=1, row=1)
custom_url_button = Button(window, text = 'CUSTOM URL', command =lambda: custom_url()).grid(column=group_1_column, row=1)
standard_start_button = Button(window, text = 'STANDARD START', command =lambda: standard_start()).grid(column=group_1_column, row=2)
write_cookies_button = Button(window, text = 'SAVE COOKIES', command =lambda: cookies_save()).grid(column=group_1_column, row=3)
spacing = Label(window, bg=colour_bg).grid(row=4)
restart_button = Button(window, text = 'RESTART', state='disabled', command =lambda: restart()).grid(column=group_1_column, row=5)
exit_button = Button(window, text = 'EXIT', command =lambda: finish()).grid(column=group_1_column, row=6)


spacing = Label(window, bg=colour_bg).grid(row=7)
spacing = Label(window, bg=colour_bg).grid(row=8)


group_2_column = 7
debug_label = Label(window, text = 'ADVANCED TOOLS', font=font_16_bold, bg=colour_bg, fg=colour_fg).grid(column=group_2_column, row=0)

offers_file_read_button = Button(window, text = '(FILE) OFFERS READ', command =lambda: offers_read()).grid(column=group_2_column, row=1)
compare_offers_button = Button(window, text = 'COMPARE OFFERS', command =lambda: offers_compare()).grid(column=group_2_column, row=2)
offers_file_write_button = Button(window, text = '(FILE) OFFERS SAVE', command =lambda: offers_save()).grid(column=group_2_column, row=3)


group_3_column = 2
label_group_3 = Label(window, text='GET TOOLS', font=font_16_bold, bg=colour_bg, fg=colour_fg).grid(column=group_3_column, row=9)

get_money_button = Button(window, text = 'GET MONEY', command =lambda: read_money()).grid(column=group_3_column, row=10)
get_storage_button = Button(window, text = 'GET STORAGE', command =lambda: storage_get()).grid(column=group_3_column, row=11)
get_offers_button = Button(window, text = 'GET OFFERS', command =lambda: offers_get()).grid(column=group_3_column, row=12)


group_4_column = 7
label_group_4 = Label(window, text='PRINT TOOLS', font=font_16_bold, bg=colour_bg, fg=colour_fg).grid(column=7, row=9)

variable_input = StringVar()
variable_input_field = Entry(window, textvariable = variable_input).grid(column=group_4_column-1, row=10)
print_button = Button(window, text = 'VARIABLE PRINT', state='disabled', command =lambda: variable_print(variable_input)).grid(column=group_4_column, row=10)
print_money_button = Button(window, text = 'PRINT MONEY', command =lambda: print_money()).grid(column=group_4_column, row=11)
print_storage_button = Button(window, text = 'PRINT STORAGE', command =lambda: print_storage()).grid(column=group_4_column, row=12)
print_offers_read_button = Button(window, text = 'PRINT OPEN OFFERS', command =lambda: print_offers_got()).grid(column=group_4_column, row=13)
print_offers_set_button = Button(window, text = 'PRINT SET OFFERS', command =lambda: print_offers_set()).grid(column=group_4_column, row=14)

spacing = Label(window, bg=colour_bg).grid(row=17)
spacing = Label(window, bg=colour_bg).grid(row=18)

group_5_column = 2
label_group_5 = Label(window, text='WAR TOOLS', font=font_16_bold, bg=colour_bg, fg=colour_fg).grid(column=group_5_column, row=19)

wars_late_open_button = Button(window, text = 'OPEN LATE WARS', command =lambda: wars_late_open()).grid(column=group_5_column, row=20)

window.mainloop()
