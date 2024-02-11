from pypdf import PdfWriter
import os
#Write the path from where you want to input your PDFs
Files=[file for file in os.listdir() if file.endswith(".pdf")]
Merger = PdfWriter()

for pdf in Files:
  Merger.append(pdf)

Merger.write("merged-pdf.pdf")
Merger.close()
