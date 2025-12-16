from pytesseract import pytesseract
from ast import literal_eval
from PIL import ImageGrab

from debug import Debug

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Reader:

    runningList = []
    temp = [None, [], [0.0, 0.0, 0.0]]

    deletingCharacters = [character for character in string.printable if not character.isdigit()]

    processVerifyNumber = 0
    processVerifyList = []
    catchedANewItem = False

    def run():

        while True:

            Reader.catchedANewItem = False
            Reader.temp[1] = []
            time.sleep(0.25)

            Reader.temp[0] = ImageGrab.grab(bbox = (25, 210, 380, 245))
            
            tempText = pytesseract.image_to_string(Reader.temp[0], config='--psm 6')
            tempText = tempText.split()

            for position, each in enumerate(tempText):
                for delCharacter in Reader.deletingCharacters:
                    each = each.replace(delCharacter, '')
                if position < 3 and each != '':
                    Reader.temp[1].append(each)

            if len(Reader.temp[1]) == 3:
                for position, each in enumerate(Reader.temp[1]):
                    if each != Reader.temp[2][position]:

                        if Reader.processVerifyNumber == 0:
                            Reader.processVerifyList = Reader.temp[1]

                        if each == Reader.processVerifyList[position]:
                            Reader.processVerifyNumber += 1
                        else:
                            Reader.processVerifyNumber = 0

                        if Reader.processVerifyNumber > 9:
                            Reader.processVerifyNumber = 0
                            Reader.catchedANewItem = True

                if Reader.catchedANewItem:
                    Reader.temp[2] = Reader.temp[1]

                    try:

                        catchedItem = int(Reader.temp[2][0])
                        catchedItem = float(catchedItem)
                        catchedItem = catchedItem/100

                        if catchedItem < 1.0:
                            catchedItem = catchedItem + 1.0

                        Reader.runningList.append(catchedItem)
                        print("Novo item capturado: ", Reader.runningList[-1], ".\n")

                    except:

                        catchedItem = Reader.temp[2][0]
                        Debug.bugReport(catchedItem, len(Reader.runningList), Reader.temp[0])
