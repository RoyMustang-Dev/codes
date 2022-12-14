import PyPDF2

template = PyPDF2.PdfFileReader(open('./pdfs/13.3super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('./pdfs/11.1wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('wm-output-file.pdf','wb') as file:
        output.write(file)
