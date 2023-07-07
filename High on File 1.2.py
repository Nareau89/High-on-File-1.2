import tkinter
from tkinter.ttk import Frame, Style, Label, Button
from tkinter import Tk, BOTH, filedialog, W, E, S, N, messagebox
import shutil
import os
import sys
import webbrowser
import pygame
import sv_ttk
dir = os.getcwd()

#The application moves files from the source folder and files from its subfolders to the destination folder.
# #I know there is many other windows build-in ways to do it but i wanted to make it using python :D"



class Window(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.initiate()
        self.play_sound_start()
        
        
    def get_sf(self):
        self.src = filedialog.askdirectory()
        if self.src=="":
            self.play_sound_error()
            messagebox.showerror("Dude!", "source is not assigned.")
        else:
            print(f"source folder set to {self.src}")
        return self.src
    def get_df(self):
        self.dst = filedialog.askdirectory()
        self.opendst.config(state="normal")
        if self.dst=="":
            self.play_sound_error()
            messagebox.showerror("Dude!", "destination folder is not assigned.")
        else:
            print(f"destination folder set to {self.dst}")
        return self.dst
    def play_sound(self):
        self.dir = dir
        sound = f"{self.dir}\\wedidit.mp3"
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
    def play_sound_start(self):
        self.dir = dir
        sound = f"{self.dir}\\lezdoit.mp3"
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
    def play_sound_error(self):
        self.dir = dir
        sound = f"{self.dir}\\icant.mp3"
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
    def play_sound_error2(self):
        self.dir = dir
        sound = f"{self.dir}\\icant2.mp3"
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()    
    def show_info(self):
        message = "The application moves files from the source folder and files from its subfolders to the destination folder."
        messagebox.showinfo("MISSION DETAILS!", message, icon='info')
    def open_url(self):
        url="https://github.com/Nareau89"
        webbrowser.open(url)
    def open_dst(self):
        os.startfile(self.dst)
    def transfer_files(self):
        while(True):
            try:
                src = self.src
                dst = self.dst
            except AttributeError:
                self.play_sound_error()
                messagebox.showerror("Dude!", "source or destination folder are not assigned.")
            os.chdir(src)
            files = os.listdir(src)
            if os.path.exists(src) and os.path.exists(dst) == True:
                try:
                    for f in files :
                            if os.path.isfile(f):
                                shutil.move(f, dst)
                                print(f"""\nTeleporting file: {f}
from {src} to {dst}.""")
                            elif os.path.isdir(f):
                                os.chdir(f)
                                sub = os.listdir()
                                for f in sub:
                                    shutil.move(f, dst)
                                    print(f"""\nTeleporting file: {f}
from {src} to {dst}.""")
                                os.chdir(src)
                                continue
                except shutil.Error:
                    self.play_sound_error2()
                    messagebox.showerror("Dude!", f"{f} already exists. Mission abort!")
                    break
                self.play_sound()
                messagebox.showinfo("LEZDOIT", "SUCK-CESS!")
                break
                        
        
                    
    def initiate(self):
        self.parent.title("High on File 1.2")
        self.style=Style()
        self.pack(fill=BOTH,expand=1)
        self.columnconfigure(1, weight=1)
        sv_ttk.set_theme("dark")
        pygame.mixer.init()

        self.sfbtn=Button(self, text="SOURCE FOLDER", command=self.get_sf)
        self.sfbtn.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E+W+S+N)
        
        self.dfbtn=Button(self, text="DESTINATION FOLDER", command=self.get_df)
        self.dfbtn.grid(row=2, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E+W+S+N)

        self.opendst=Button(self, text="OPEN DESTINATION FOLDER", command=self.open_dst)
        self.opendst.grid(row=3, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E+W+S+N)
        self.opendst.config(state="disabled")

        self.lezdoit=Button(self, text="LEZDOIT!", command=self.transfer_files)
        self.lezdoit.grid(row=4, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E+W+S+N)

        self.info=Button(self, text="INFO!", command=self.show_info)
        self.info.grid(row=5, column=0, rowspan=1, padx=5, pady=4, sticky=W)

        self.github=Button(self, text="GITHUB!", command=self.open_url)
        self.github.grid(row=5, column=1, rowspan=1, padx=5, pady=4, sticky=E)

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tkinter.END, text)


def main():
    gui=Tk()
    gui.geometry("600x590")
    output_text = tkinter.Text(gui)
    output_text.pack()
    sys.stdout = StdoutRedirector(output_text)
    app=Window(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()