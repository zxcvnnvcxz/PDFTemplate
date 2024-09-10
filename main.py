from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
x1 = 10
y1 = 21
x2 = 200
y2 = 21

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)

    y1 = 21
    y2 = 21

    # Add Lines
    while y1 < 265 and y2 < 265:
        pdf.line(x1, y1, x2, y2)
        y1 = y1 + 10
        y2 = y2 + 10


    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

    for i in range(row["Pages"]):
        pdf.add_page()
        y1 = 21
        y2 = 21

        # Add Lines
        while y1 < 265 and y2 < 265:
            pdf.line(x1, y1, x2, y2)
            y1 = y1 + 10
            y2 = y2 + 10

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

pdf.output("output.pdf")