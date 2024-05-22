import tkinter

class ColoriageApp:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Coloriage")

        self.largeur_canevas = int((16 / 9) * 800)
        self.hauteur_canevas = 800

        self.canvas = tkinter.Canvas(fenetre, width=self.largeur_canevas, height=self.hauteur_canevas, bg="white")
        self.canvas.pack()

        self.dernierX, self.dernierY = 0, 0
        self.couleur = "black"
        self.taille_pinceau = 5

        self.setup_interface()

    def setup_interface(self):
        tkinter.Label(self.fenetre, text="Pour dessiner, déplacez votre souris en appuyant sur le bouton gauche.").pack()
        tkinter.Label(self.fenetre, text="Pour changer de couleur, cliquez sur la couleur.").pack()
        tkinter.Label(self.fenetre, text="Utilisez la couleur 'eraser' pour gommer.").pack()
        tkinter.Label(self.fenetre, text="Utilisez l'échelle en bas pour changer la taille du pinceau.").pack()

        self.canvas.bind("<ButtonPress-1>", self.quand_clique)
        self.canvas.bind("<B1-Motion>", self.quand_deplace)

        self.create_couleurs()

        echelle_pinceau = tkinter.Scale(self.fenetre, from_=1, to=20, orient=tkinter.HORIZONTAL, label="Taille du Pinceau", command=self.definir_taille_pinceau)
        echelle_pinceau.pack()

    def create_couleurs(self):
        y_pos = 10
        for couleur_canevas in couleurs:
            self.create_rectangle_with_color(10, y_pos, couleur_canevas)
            if couleur_canevas != "eraser":
                self.canvas.tag_bind(couleur_canevas, "<Button-1>", lambda event, c=couleur_canevas: self.definir_couleur(event, c))
            y_pos += 25

    def create_rectangle_with_color(self, x, y, color):
        if color != "eraser":
            return self.canvas.create_rectangle(x, y, x + 20, y + 20, fill=color, outline="white", tags=(color,))

    def enregistrer_position(self, event):
        self.dernierX, self.dernierY = event.x, event.y

    def quand_clique(self, event):
        self.enregistrer_position(event)

    def quand_deplace(self, event):
        if self.couleur == "eraser":
            taille_demi = self.taille_pinceau // 2
            self.canvas.create_rectangle(event.x - taille_demi, event.y - taille_demi, event.x + taille_demi, event.y + taille_demi, fill="white", outline="white")
        else:
            taille_demi = self.taille_pinceau / 2.0
            self.canvas.create_line(self.dernierX, self.dernierY, event.x, event.y, fill=self.couleur, width=self.taille_pinceau, capstyle=tkinter.ROUND, smooth=tkinter.TRUE)

        self.enregistrer_position(event)

    def definir_couleur(self, event, c):
        self.couleur = c

    def definir_taille_pinceau(self, value):
        self.taille_pinceau = int(value)

if __name__ == "__main__":
    couleurs = ["red", "blue", "black", "white", "green", "yellow", "pink", "orange", "gray", "brown", "purple",
                "tomato", "tomato3", "goldenrod3", "cyan", "magenta", "violet", "turquoise", "maroon", "indigo", "eraser"]

    fenetre = tkinter.Tk()
    app = ColoriageApp(fenetre)
    fenetre.mainloop()
