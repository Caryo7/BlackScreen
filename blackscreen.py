from tkinter import *
from configparser import *

class Window:
    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('config/default.ini', encoding = 'utf-8')
        self.transparentcolor = self.parser.get('app', 'transparentcolor')
        self.alphakey = self.parser.get('app', 'alphakey')
        self.topmostkey = self.parser.get('app', 'topmostkey')
        self.bordercolor =self.parser.get('app', 'bordercolor')
        self.s = int(self.parser.get('window', 'size'))
        self.sizecross = int(self.parser.get('cross', 'size'))
        self.colorcross = self.parser.get('cross', 'color')
        self.drawingcolor = self.parser.get('app', 'drawingcolor')

        self.master = Tk()
        self.master.wm_state('zoomed')
        self.master.wm_attributes('-fullscreen', 1)
        self.master.wm_attributes('-transparentcolor', self.transparentcolor)
        self.master.wm_attributes('-alpha', 1.0)
        self.master['bg'] = 'black'
        self.master.title('Black Screen for projections')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.canvas = Canvas(self.master, bg = 'black')
        self.canvas.grid(sticky='nswe')

        self.pressed = False
        self.focused = True
        self.topmost = False
        self.add = 0
        self.areas = []
        self.master.bind_all('<ButtonPress-1>', self.button_press)
        self.master.bind_all('<ButtonRelease-1>', self.button_release)
        self.master.bind_all('<Button-3>', self.button_right)
        
        self.master.bind_all('<KeyPress>', self.shift_press)
        self.master.bind_all('<KeyRelease>', self.shift_release)
        self.master.bind('<FocusIn>', self.focus_in)
        self.master.bind('<FocusOut>', self.focus_out)
        self.master.bind_all('<Motion>', self.motion)
        self.first_x, self.first_y = None, None
        self.update()

        self.master.mainloop()

    def button_right(self, evt):
        z = Toplevel(self.master)
        z.transient(self.master)
        z.title('Aide')
        z.columnconfigure(0, weight=1)
        z.rowconfigure(0, weight=1)
        t = Text(z, width=50, height=15, wrap = 'word', bg = 'black', fg = 'white')
        t.grid(sticky = 'nswe')
        t.insert('end', """\
Documentation
Fermeture:
Cliquez sur la croix rouge (en haut à gauche) ou sur les touches Alt + F4.

Transparence:
Pour valider la zone à découper, vous pouvez cliquer sur la touche majuscule\
du clavier, qui rend la fenêtre transparente. Vous verrez ainsi ce qu'il y a\
en dessous. Attention, la fenêtre doit avoir le focus pour cela ! \
Cf §indicateurs.

Découpe:
Pour découper une zone de la fenêtre, cliquez sur le premier point, et en\
maintenant la souris enfoncé (ou le doigts sur le pavé tactile), allez jusqu'au\
point voulu. La découpe s'affiche en temps réel. Attention, la fenêtre doit \
avoir le focus pour cela ! Cf §indicateurs.

Indicateurs:
 - bleu correspond à la fonction premier plan. Si cet indicateur est allumé,\
c'est qu'aucune fenêtre en dessous ne peux venir par dessus. Cela peut être\
utile pour faire un trou avec le défilement depuis le clique de la souris,\
mais sans faire venir la fenêtre devant.
 - rouge correspond à la position de la fenêtre. Si l'indicateur rouge est \
allumé, c'est qu'une autre fenêtre a le focus, vous devrez donc cliquer sur\
la fenêtre noir pour lui rendre le focus. Vous ne pouvez pas changer la \
visibilité de la fenêtre du logiciel si elle n'a pas le focus !
 """)
        t.config(stat = 'disabled')
        t.focus()

    def focus_in(self, evt):
        self.focused = True
        self.update()

    def focus_out(self, evt):
        self.focused = False
        self.update()

    def shift_press(self, evt):
        if evt.keysym.lower().startswith(self.alphakey):
            self.master.wm_attributes('-alpha', 0.7)

        elif evt.keysym.lower().startswith(self.topmostkey):
            self.topmost = not self.topmost
            self.master.wm_attributes('-topmost', self.topmost)
            self.update()

    def shift_release(self, evt):
        if evt.keysym.lower().startswith(self.alphakey):
            self.master.wm_attributes('-alpha', 1.0)

    def button_press(self, evt):
        if 15 <= evt.x and evt.x <= 35:
            if 15 <= evt.y and evt.y <= 35:
                self.master.destroy()
                return

        for i, (x1, y1, x2, y2) in enumerate(self.areas):
            if (evt.x - x1) ** 2 + (evt.y - y1) < self.s ** 2:
                self.areas.pop(i)
                self.update()
                return

        self.first_x = evt.x
        self.first_y = evt.y
        self.pressed = True

    def motion(self, evt):
        if self.pressed:
            self.update(evt = evt, motion = True)
            self.add += 1

    def button_release(self, evt):
        self.pressed = False
        if self.add > 10:
            self.areas.append([self.first_x, self.first_y, evt.x, evt.y])

        self.update()
        self.first_x = None
        self.first_y = None
        self.add = 0

    def draw_dust(self, x, y):
        self.canvas.create_line(x-5, y-3, x-5, y+5)
        self.canvas.create_line(x+5, y-3, x+5, y+5)
        self.canvas.create_line(x-5, y+5, x+5, y+5)
        self.canvas.create_line(x, y-1, x, y+5)
        self.canvas.create_line(x-5, y-5, x+5, y-5)
        self.canvas.create_line(x, y-5, x, y-8)

    def update(self, evt = None, motion = False, create = False):
        self.canvas.delete('all')
        self.canvas.create_line(15, 15, 35, 35, fill = self.bordercolor)
        self.canvas.create_line(35, 15, 15, 35, fill = self.bordercolor)

        if self.topmost:
            self.canvas.create_oval(50, 15, 70, 35, fill = self.drawingcolor)
            
        if not self.focused:
            self.canvas.create_oval(85, 15, 105, 35, fill = self.bordercolor)

        for a in self.areas:
            self.canvas.create_rectangle(*a, fill = self.transparentcolor, outline = self.bordercolor)
            self.canvas.create_oval(a[0]-self.s, a[1]-self.s, a[0]+self.s, a[1]+self.s, fill = self.bordercolor)
            self.draw_dust(a[0], a[1])

        if motion:
            self.canvas.create_rectangle(self.first_x, self.first_y, evt.x, evt.y, fill = self.transparentcolor, outline = self.drawingcolor)

if __name__ == '__main__':
    app = Window()
