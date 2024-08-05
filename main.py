#Tkinter
try:
    import tkinter as tk
except Exception: print('Error: importing tkinter failed'); exit()
try:
    from tkinter import messagebox
except Exception: print('Error: importing tkinter.messagebox failed'); exit()
#os
try:
    import os
except Exception: messagebox.showerror(title='GradeCalculator', message='El paquete nativo "os" no se encuentra o esta corrupto, el programa no puede iniciar'); exit()
try:
    from os.path import expanduser
except Exception: messagebox.showerror(title='GradeCalculator', message='El modulo nativo "os.path" no se encuentra o esta corrupto, el programa no puede iniciar'); exit()
#datetime
try:
    from datetime import datetime
except Exception: messagebox.showerror(title='GradeCalculator', message='El paquete nativo "datetime" no se encuentra o esta corrupto, el programa no puede iniciar'); exit()

window = tk.Tk()
window.config(background='light grey')
#---------- Global variables----------#
file_name_data = None
nMinG = 1.0
nMaxG = 7.0
bg_color= 'light grey'
desktopDir = expanduser('~') + '\\Desktop\\'
radio_button_control = tk.IntVar()
check_button_control = tk.BooleanVar()
#----------Functions----------#
def nMinGRadioB():
    global nMinG
    if radio_button_control.get() == 0:
        nMinG = 1.0
    elif radio_button_control.get() == 1:
        nMinG = 2.0

def check_button():
    #Control of the checkbutton
    chb_control = check_button_control.get()
    if chb_control:
        TlFileName()
        calculateButton.config(text='Generar tabla\nde notas', height=2, command=cal_all_grades)
        calculateButton.place(x=130,y=150)
        entry4.config(state='disabled')
        label4.config(state='disabled')
    elif not chb_control:
        calculateButton.config(text='Calcular nota', height=1, command=cal_grade)
        calculateButton.place(x=130,y=160)
        entry4.config(state='normal')
        label4.config(state='normal')

def cal_grade():
    #Calculate the grade with the given parameters
    global nMinG
    global nMaxG
    nMax = 7.0
    if radio_button_control.get() == 0: nMin = 1.0
    elif radio_button_control.get() == 1: nMin = 2.0
    elif radio_button_control.get() == 2: nMin = float(nMinG)
    nApr = entry1.get()
    e = entry2.get()
    pMax = entry3.get()
    p = entry4.get()
    if nApr == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Nota de aprobacion" esta vacio'); return
    elif e == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Exigencia" esta vacio'); return
    elif pMax == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Puntuacion máxima" esta vacio'); return
    elif p == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Puntuacion del alumno" esta vacio'); return
    if e.count('%'): e = e.replace('%', '')
    if nApr.count(','): nApr = nApr.replace(',','.')
    try:
        nApr = float(nApr)
        e = int(e)
        pMax = int(pMax)
        p = int(p)
    except ValueError: messagebox.showerror(title='GradeCalculator', message='Un error ha ocurrido, por favor, revise e ingrese los parametros denuevo, si el error persiste, contactese con Carlos Dos Santos'); return
    if p > pMax: messagebox.showerror(title='GradeCalculator', message='El puntaje del alumno no puede ser mayor a el puntaje maximo'); return
    elif p < 0: messagebox.showerror(title='GradeCalculator', message='El puntaje del alumno no puede ser menor que 0'); return
    elif e > 100: messagebox.showerror(title='GradeCalculator', message='La exigencia solo se limita hasta 100%'); return
    elif e < 0: messagebox.showerror(title='GradeCalculator', message='La exigencia solo se limita hasta 0%'); return
    elif nApr > nMax: messagebox.showerror(title='GradeCalculator', message=f'La nota de aprobacion no debe ser mayor a {nMax}'); return
    elif nApr < nMin: messagebox.showerror(title='GradeCalculator', message=f'La nota de aprobacion no debe ser menor a {nMin}'); return
    elif pMax >= 1000: messagebox.showerror(title='GradeCalculator', message='La puntuacion máxima tiene como maximo 3 caracteres, pero se ingresaron 4'); return
    elif pMax <= 0: messagebox.showerror(title='GradeCalculator', message='La puntuacion máxima no puede ser igual o menor a 0'); return
    pApr = pMax * e / 100
    if p <= pApr: n = (nApr - nMin) * (p / pApr) + nMin
    elif p > pApr: n = (nMax - nApr) * (p - pApr) / (pMax - pApr) + nApr
    n = round(n, 1)
    if n > nMaxG:
        n = nMaxG
    if n > nMax: messagebox.showerror(title='GradeCalculator', message=f'Error de calculo, la nota del alumno es mayor a la nota máxima, Nota: "{n}"'); return
    elif n < nMin: messagebox.showerror(title='GradeCalculator', message=f'Error de calculo, la nota del alumno es menor a la nota mínima, Nota: "{n}"'); return
    if n >= nApr: messagebox.showinfo(title='GradeCalculator', message=f'La nota del alumno es: "{n}" Aprobado')
    else: messagebox.showinfo(title='GradeCalculator', message=f'La nota del alumno es: "{n}" Reprobado')

def cal_all_grades():
    #Make a file with all the grades
    global nMinG
    global nMaxG
    try:
        os.mkdir(f'{desktopDir}GC Tables')
    except FileExistsError: pass
    nMax = 7.0
    if radio_button_control.get() == 0: nMin = 1.0
    elif radio_button_control.get() == 1: nMin = 2.0
    elif radio_button_control.get() == 2: nMin = float(nMinG)
    nApr = entry1.get()
    e = entry2.get()
    pMax = entry3.get()
    p = 0
    if nApr == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Nota de aprobacion" esta vacio'); return
    elif e == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Exigencia" esta vacio'); return
    elif pMax == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Puntuacion máxima" esta vacio'); return
    if e.count('%'): e = e.replace('%', '')
    if nApr.count(','): nApr = nApr.replace(',','.')
    try:
        nApr = float(nApr)
        e = int(e)
        pMax = int(pMax)
    except ValueError: messagebox.showerror(title='GradeCalculator', message='Un error ha ocurrido, por favor, revise e ingrese los parametros denuevo, si el error persiste, contactese con Carlos Dos Santos'); return
    if e > 100: messagebox.showerror(title='GradeCalculator', message='La exigencia solo se limita hasta 100%'); return
    elif e < 0: messagebox.showerror(title='GradeCalculator', message='La exigencia solo se limita hasta 0%'); return
    elif nApr > nMax: messagebox.showerror(title='GradeCalculator', message=f'La nota de aprobacion no debe ser mayor a {nMax}'); return
    elif nApr < nMin: messagebox.showerror(title='GradeCalculator', message=f'La nota de aprobacion no debe ser menor a {nMin}'); return
    elif pMax >= 1000: messagebox.showerror(title='GradeCalculator', message='La puntuacion máxima tiene como maximo 3 caracteres, pero se ingresaron 4'); return
    elif pMax <= 0: messagebox.showerror(title='GradeCalculator', message='La puntuacion máxima no puede ser igual o menor a 0'); return
    pApr = pMax * e / 100
    file_name = file_name_data
    try:
        with open(f'{desktopDir}GC Tables\\{file_name} {datetime.today().strftime('%d-%m-%Y')}.txt', 'x', encoding='UTF-8') as file:
            file.write(f'Esta es la tabla "{file_name}", fecha del archivo: "{datetime.today().strftime(f'%d-%m-%Y %I:%M %p')}"\n\n--------------------\n')
            try:
                while p <= pMax:
                    if p <= pApr: n = (nApr - nMin) * (p / pApr) + nMin
                    elif p > pApr: n = (nMax - nApr) * (p - pApr) / (pMax - pApr) + nApr
                    n = round(n, 1)
                    if n > nMaxG:
                        n = nMaxG
                    if p < pMax: file.writelines(f'Puntuación = {p}, Nota = {n}\n--------------------\n')
                    else: file.writelines(f'Puntuación = {p}, Nota = {n}\n')
                    p +=1
                messagebox.showinfo(title='GradeCalculator', message='El Archivo se ha creado correctamente!')
            except Exception:
                messagebox.showerror(title='GradeCalculator', message='Un error ha ocurrido durante la creación del archivo, porfavor, intentelo otra vez'); return
    except FileExistsError:
        messagebox.showerror(title='GradeCalculator', message='Error: Archivo ya existe, porfavor, seleccione otro nombre'); return

#----------Tkinter Toplevel classes----------#
class TlFileName():
    def __init__(self):
        #Window
        self.tl_filename = tk.Toplevel()
        self.tl_filename.config(background=bg_color)
        self.tl_filename.geometry('280x200')
        self.tl_filename.resizable(False, False)
        self.tl_filename.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.tl_filename.grab_set()
        self.tl_filename.focus()
        try:
            self.tl_filename.iconbitmap('icon.ico')
        except Exception: print('Error: file "icon.ico" not founded'); pass

        self.entrytl = tk.Entry(self.tl_filename)
        self.entrytl.config(font=('normal', 13, 'normal'))
        self.entrytl.place(x=47, y=124)
        self.labeltl = tk.Label(self.tl_filename, text='Ingrese el nombre del archivo con el\nque quiere guardar la tabla.\nALERTA: El archivo solo se guardara\nen formato ".txt", cualquier otro formato\nno esta disponible por el momento')
        self.labeltl.config(background=bg_color, font=('normal', 10, 'bold'))
        self.labeltl.place(x=10, y=10)
        buttontl = tk.Button(self.tl_filename, text='Confirmar datos')
        buttontl.config(width=15, height=1, command=self.tl_button, font=('normal', 13, 'bold'))
        buttontl.place(x=57, y=157)
    def tl_button(self):
        #Apply the name of the file
        global file_name_data
        global check_button_control
        try: 
            if self.entrytl.get() == '': messagebox.showerror(title='GradeCalculator', message='Los parametros estan vacios, porfavor, coloquele un nombre al archivo'); return
            file_name_data = self.entrytl.get()
            self.tl_filename.destroy()
            return file_name_data
        except Exception: messagebox.showerror(title='GradeCalculator', message='Un error ha ocurrido al guardar el nombre, porfavor, intentelo denuevo'); check_button_control = 0; return
    def on_closing(self):
        #when the toplevel window is closing
        global check_button_control
        check_button_control.set(False)
        calculateButton.config(text='Calcular nota', height=1, command=cal_grade)
        calculateButton.place(x=130,y=160)
        entry4.config(state='normal')
        label4.config(state='normal')
        self.tl_filename.destroy()

class TlnMinMaxButton():
    def __init__(self):
        #Window
        self.tl_nMinMax = tk.Toplevel()
        self.tl_nMinMax.config(background=bg_color)
        self.tl_nMinMax.geometry('380x200')
        self.tl_nMinMax.resizable(False, False)
        self.tl_nMinMax.grab_set()
        self.tl_nMinMax.focus()
        try:
            self.tl_nMinMax.iconbitmap('icon.ico')
        except Exception: print('Error: file "icon.ico" not founded'); pass
        
        self.chbcontrol = tk.BooleanVar()
        self.chbcontrol.set(False)
        nMinL = nMinG
        nMaxL = nMaxG
        self.tlnnm_l1 = tk.Label(self.tl_nMinMax, text='Ingrese aqui la nota\nminima que necesite\n(Ejemplo: 1,5)')
        self.tlnnm_l1.config(background=bg_color, font=('calibri', 12, 'bold'))
        self.tlnnm_l1.place(x=10,y=30)
        self.tlnnm_e1 = tk.Entry(self.tl_nMinMax)
        self.tlnnm_e1.config(font=('normal', 14, 'normal'), width=5)
        self.tlnnm_e1.insert(0, '1,5')
        self.tlnnm_e1.place(x=53,y=100)
        self.tlnnm_msg1 = tk.Label(self.tl_nMinMax, text=f'Nota mínima actual: {nMinL}')
        self.tlnnm_msg1.config(background=bg_color)
        self.tlnnm_msg1.place(x=17,y=8)
        self.tlnnm_l2 = tk.Label(self.tl_nMinMax, text='Limite la nota\nmaxima que necesite\n(Ejemplo: 6,0)')
        self.tlnnm_l2.config(background=bg_color, font=('calibri', 12, 'bold'), state='normal')
        self.tlnnm_l2.place(x=200,y=30)
        self.tlnnm_e2 = tk.Entry(self.tl_nMinMax)
        self.tlnnm_e2.insert(0, '7,0')
        self.tlnnm_e2.config(font=('normal', 14, 'normal'), width=5, state='normal')
        self.tlnnm_e2.place(x=245,y=100)
        self.tlnnm_msg2 = tk.Label(self.tl_nMinMax, text=f'Nota máxima limitada: {nMaxL}')
        self.tlnnm_msg2.config(background=bg_color)
        self.tlnnm_msg2.place(x=203,y=8)
        self.tlnnm_b = tk.Button(self.tl_nMinMax, text='Confirmar parametros')
        self.tlnnm_b.config(font=('normal', 15, 'bold'), command=self.customNminMax)
        self.tlnnm_b.place(x=80,y=145)
    def customNminMax(self):
        #Apply the changes on the parameters
        global nMinG
        global nMaxG
        cnMin = self.tlnnm_e1.get()
        cnMax = self.tlnnm_e2.get()
        if cnMin.count(','): cnMin = cnMin.replace(',', '.')
        if cnMax.count(','): cnMax = cnMax.replace(',', '.')
        if cnMin == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Nota mínima" esta vacio'); return
        if cnMax == '': messagebox.showerror(title='GradeCalculator', message='El parametro "Nota máxima" esta vacio'); return
        try:
            cnMin = float(cnMin)
        except Exception: messagebox.showerror(title='GradeCalculator', message='Error al convertir "Nota mínima" de String a Float'); return
        try:
            cnMax = float(cnMax)
        except Exception: messagebox.showerror(title='GradeCalculator', message='Error al convertir "Nota máxima" de String a Float'); return
        nAprMax = float(entry1.get())
        if cnMin >= nAprMax: messagebox.showerror(title='GradeCalculator', message=f'El parametro "Nota Minima" no puede ser mayor a {nAprMax}'); return
        if cnMin < 0: messagebox.showerror(title='GradeCalculator', message='El parametro "Nota Minima" no puede ser menor que 0'); return
        if cnMax >= 10: messagebox.showerror(title='GradeCalculator', message='El parametro "Nota Maxima" no puede ser mayor a 10'); return
        if cnMax < nAprMax: messagebox.showerror(title='GradeCalculator', message=f'El parametro "Nota máxima" no puede ser menor que {nAprMax}'); return
        round(cnMin, 1)
        round(cnMax, 1)
        nMinG = cnMin
        nMaxG = cnMax
        radio_button_control.set(2)
        self.tl_nMinMax.destroy()
#----------Tkinder setup/main loop/main window----------#
window.geometry('360x250')
window.resizable(False, False)
try:
    window.iconbitmap('icon.ico')
except Exception: print('Error: file "icon.ico" not founded'); pass
window.title('GradeCalculator')
title_window = tk.Label(window, text='Grade Calculator', font=('Arial', 12, "bold"), background=bg_color)
title_window.pack()

framelabel1 = tk.LabelFrame(window, text='Nota mínima')
framelabel1.config(background=bg_color)
framelabel1.place(x=10, y=0)
Radio1 = tk.Radiobutton(framelabel1, text= 1.0, value=0, variable=radio_button_control, background=bg_color, activebackground=bg_color, command=nMinGRadioB)
Radio1.pack()
Radio2 = tk.Radiobutton(framelabel1, text= 2.0, value=1, variable=radio_button_control, background=bg_color, activebackground=bg_color, command=nMinGRadioB)
Radio2.pack()
Radio3 = tk.Radiobutton(framelabel1, text='Otro', value=2, variable=radio_button_control, background=bg_color, activebackground=bg_color)
Radio3.config(state='disabled')
Radio3.pack()

entry1 = tk.Entry(window)
entry1.config(width=3)
entry1.place(x=120,y=25)
entry1.insert(0, '4.0')
label1 = tk.Label(text='Nota de aprobación', background=bg_color, font=('normal', 9, "bold"))
label1.place(x=145,y=25)
entry2 = tk.Entry(window)
entry2.config(width=3)
entry2.place(x=120,y=55)
entry2.insert(0,'60')
label2 = tk.Label(text='Exigencia (ejemplo: 46 = 0.46%)', background=bg_color, font=('normal', 9, 'bold'))
label2.place(x=145,y= 55)
entry3 = tk.Entry(window)
entry3.config(width=3)
entry3.place(x=120,y=85)
entry3.insert(0, '100')
label3 = tk.Label(text='Puntuación máxima', background=bg_color, font=('normal', 9, 'bold'))
label3.place(x=145,y=85)
entry4 = tk.Entry(window)
entry4.config(width=3)
entry4.place(x=120,y=115)
label4 = tk.Label(text='Puntuación del alumno', background=bg_color, font=('normal', 9, 'bold'))
label4.place(x=145,y=115)

checkButton = tk.Checkbutton(window, text='Hacer una tabla\ncon todos\nlos puntajes y\ntodas las notas')
checkButton.config(background=bg_color, command=check_button, variable=check_button_control, onvalue=1, offvalue=0, activebackground=bg_color)
checkButton.place(x=5,y=110)
calculateButton = tk.Button(window, text='Calcular nota', font=('normal', 12, 'bold'))
calculateButton.config(width=10, height=1, command=cal_grade)
calculateButton.place(x=130,y=160)
otherNMINMAXButton = tk.Button(window, text='Nota min/max')
otherNMINMAXButton.config(font=('normal', 10, 'bold'), command=TlnMinMaxButton)
otherNMINMAXButton.place(x=250,y=162)

labelC = tk.Label(text='Version: 0.2.1\nHecho por Carlos Dos Santos 2024')
labelC.config(bg=bg_color, font=('normal', 13, 'bold'), foreground='dark slate gray')
labelC.place(x=37,y=207)
#-----Loop-----#
window.mainloop()