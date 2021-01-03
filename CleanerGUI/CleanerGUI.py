
import tkinter as tk
import cleanerfunc


class Application(tk.Frame):
    """Helps create panel and button with string cleaner function.

    creates button and text panel, with a string cleaning function connected to the button"""
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.clean=tk.Button(self, text="Clean Input",fg="green",command=(self.runStringCleaner))  
        self.inputText=tk.Text(self,height=20,width=100)
        self.spell=tk.Button(self, text="Check Spelling",fg="green",command=(self.spellCheck))  
        self.inputText2=tk.Text(self,height=20,width=100)
        self.clean.pack()
        self.inputText.pack()
        self.spell.pack()
        self.inputText2.pack()
    def runStringCleaner(self):
        String=cleanerfunc.removespecchar(self.inputText.get(1.0,tk.END))
        self.inputText.delete(1.0,tk.END)
        self.inputText.insert(tk.END,String)
    def spellCheck(self):
        candidates=cleanerfunc.spellCheck(self.inputText.get(1.0,tk.END))
        String="Most Likely Corrections:\n"+cleanerfunc.correctSpell(self.inputText.get(1.0,tk.END))+"Possible Corrections:\n"+candidates
        self.inputText2.insert(1.0,String)
        

root=tk.Tk()
app=Application(master=root)
app.mainloop()