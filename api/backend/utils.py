import pandas as pd
from fpdf import FPDF

""" def save_pdf(df: pd.DataFrame, filename: str):
    filename = 'out.tex'
    pdffile = 'out.pdf'

    template = r'''{}
    '''

    with open(filename, 'w') as f:
        f.write(template.format(df.to_latex()))

    subprocess.call([filename, pdffile])
 """
    # html = 'teste.html'
    # df.style.set_table_styles([{'selector' : '',
    #                         'props' : [('border',
    #                                     '10px solid yellow')]}])
    # df.to_html(html, index=False, border=1)
    # HTML(html).write_pdf(filename)
    


def save_pdf (df: pd.DataFrame, file_name: str):
    pdf = FPDF()
    pdf.add_page()
    
    page_width = pdf.w - 2 * pdf.l_margin
    
    pdf.set_font('Times','B',14.0) 
    pdf.image("../frontend/public/Xavier_1_1.png", x = 80, y = 4, w = 15, h = 15, type = '', link = '')
    pdf.cell(page_width, 0.0, 'Xavier - Ília', align='C')
    pdf.ln(10)

    pdf.set_font('Courier', '', 12)
    
    col_width = page_width/4
    
    pdf.ln(1)
    
    th = pdf.font_size
    
    for row in df.values:
        cidade_estado = row[1] + " - " + row[2]
        pdf.multi_cell(col_width*4, 5, "Empresa : "+row[0], border=1)
        pdf.multi_cell(col_width*4, 5, "Localidade : "+cidade_estado, border=1)
        pdf.multi_cell(col_width*4, 5, "Mercado : "+row[3], border=1)
        pdf.multi_cell(col_width*4, 5, "Stacks : "+row[4], border=1)
        pdf.ln(th)
    
    pdf.ln(12)
    
    pdf.set_font('Times','',10.0)
    pdf.cell(page_width, 0.0, '- end of report -', align='C')
    pdf.output(name = file_name, dest = '')
    #pdf.output(dest='S').encode('latin-1')
    # pdf.output((dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':f'attachment;filename={file_name}.pdf'})
    

    