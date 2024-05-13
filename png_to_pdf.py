from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()
imagelist = []                                                 # Dönüştüreceğimiz fotoğraflar için liste oluşturalım.


# kullanıcının dosya uzantısı ve koymak istediği isim .

folder = r"C:\Users\cemil\Desktop\Converter"                    # Folder containing all the images.
name = "fotolar.pdf"                                            # Name of the output PDF file.


# Fotoğrafları listeye koyaım.

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        full_path = os.path.join(dirpath, filename)
        imagelist.append(full_path)

imagelist.sort()                                               # Fotoğrafları adına göre sırala 
for i in range(0, len(imagelist)):                             # İsteğe bağlı
    print(imagelist[i])

# PDF A4 boyutunda olacağı fotoğrafları düzenleyelim

for i in range(0, len(imagelist)):
    im1 = Image.open(imagelist[i])                             # Fotoğrafı aç.
    width, height = im1.size                                   # Fotoğrafın genişlikini ve yükseklikini kaydet.
    if width > height:
        im2 = im1.transpose(Image.ROTATE_270)                  # Eğer genişlik > yükseklik ise fotoğrafı a4'e sığması için döndür.
        os.remove(imagelist[i])                                # Önceki fotografı sil.
        im2.save(imagelist[i])                                 # Döndürülmüş fotoğrafı kaydet.
        # im.save

print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")


# Fotoğrafları PDF'e dönüştürür.

for image in imagelist:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)                           # 210 ve 297 A4 kagidini boyutlari 

pdf.output(f"{folder}/{name}")                                 # PDF'i kaydet

print("PDF basariyla olusturuldu")