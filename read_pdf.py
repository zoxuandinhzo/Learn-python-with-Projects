import pyttsx3
import PyPDF2

book = open("./Learn python with Projects/assets/code.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)

bot = pyttsx3.init()
voices = bot.getProperty("voices")
bot.setProperty("voice", voices[0].id)
for num in range(0, pages):
    pages = pdfReader.pages[num]
    text = pages.extract_text()
    bot.say(text)
    bot.runAndWait()
