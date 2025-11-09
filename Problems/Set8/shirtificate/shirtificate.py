from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()
        self.set_font("helvetica", style="B", size=50)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(60)
        self.image("shirtificate.png", h=self.epw, w=self.epw, y=50)
        self.set_font_size(25)
        self.set_text_color(250, 250, 250)
        self.text(x=52, y=140, text=f"{name} took CS50")

    def save(self):
        self.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.save()

if __name__ == '__main__':
    main()