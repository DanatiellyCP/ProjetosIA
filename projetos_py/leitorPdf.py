# Bibliotecas Utilizadas:
# - pip install PyPDF2
# - pip install pyttsx3

import PyPDF2, pyttsx3

name="teste_PDF.pdf" 

path = open(name, "rb")
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()


newrate=200 #velocidade do audio
newvolume=200 #volume do audioclear
newvoice="brazil" #idioma

#percorre as paginas do ebook, extrai o texto e faz a leitura
for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.setProperty('rate',newrate)
    speak.setProperty('volume', newvolume)
    speak.setProperty('voice', newvoice)
    speak.say(text)
    speak.runAndWait()
speak.stop()
