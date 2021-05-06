import os
from fpdf import FPDF
import img2pdf

class PDFCreator:
    def __init__(self):
        pass

    def createPDF(self, folder):
        print("Creatingn PDF")
        for chapter in os.listdir(folder):
            chapter_dir = os.path.join(folder, chapter)
            print(chapter_dir)
            if os.path.isdir(chapter_dir):
                images_to_include = []

                for filename in os.listdir(chapter_dir):
                    if "jpg" in filename or "png" in filename:
                        images_to_include.append(os.path.join(chapter_dir, filename))

                images_to_include.sort()

                with open(f'{chapter_dir}/Ch-{chapter}.pdf', "wb") as f:
                    f.write(img2pdf.convert(images_to_include))


                print(images_to_include)

