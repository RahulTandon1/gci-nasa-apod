from fpdf import FPDF


def makePdf(caption):
    height = 150
    pdf = FPDF('L')
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 18)
    pdf.image('./imgs/img.jpg', h=height)
    pdf.ln(10)
    pdf.cell(200, 10, txt=caption, ln=1, align="C")
    pdf.output('balle.pdf')


makePdf('lmao')