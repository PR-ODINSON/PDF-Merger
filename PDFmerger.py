# Import necessary libraries
from pypdf import PdfWriter
import os

# Write the path from where you want to input your PDFs
# List all files in the current directory with extension .pdf
Files = [file for file in os.listdir() if file.endswith(".pdf")]

# Create a PdfWriter object for merging PDFs
Merger = PdfWriter()

# Loop through each PDF file in the directory
for pdf in Files:
    # Append the current PDF file to the PdfWriter object
    Merger.append(pdf)

# Write the merged PDF to a new file named "merged-pdf.pdf"
Merger.write("merged-pdf.pdf")

# Close the PdfWriter object
Merger.close()
