import fitz

pdffile = "1.pdf"
doc = fitz.open(pdffile)
for page_num in range(0, doc.page_count):    
    page = doc.loadPage(page_num)  # number of page
    pix = page.getPixmap()
    output = f"1_{page_num}.jpg"
    pix.writePNG(output)