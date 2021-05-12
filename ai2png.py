import fitz
import os

def convert_ai_to_png(dest_folder, result_folder):
  for filename in os.listdir(dest_folder):
    doc = fitz.open(os.path.join(dest_folder,filename))
    page = doc.loadPage(0)  # number of page
    pix = page.getPixmap()
    pix.writePNG(os.path.join(result_folder,f"{filename}.png"))