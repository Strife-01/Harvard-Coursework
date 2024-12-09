from fpdf import FPDF
from PIL import Image


class PDF(FPDF):
    def __init__(self, name):
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 30, "CS50P Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", x=0, y=60)
        self._pdf.set_font(size=40)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.cell(0, 200, f"{name} took CS50P", new_x="LMARGIN", new_y="NEXT", align="C")
    
    def save(self, fname):
        self._pdf.output(fname)


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
