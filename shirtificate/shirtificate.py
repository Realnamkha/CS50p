from fpdf import FPDF
def main():
    name = input('Name: ')
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 30)
    pdf.cell(200, 50, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
