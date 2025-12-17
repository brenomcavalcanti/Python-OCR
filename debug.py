from datetime import datetime

class Debug:
        
    bugCounter = 0

    def bugReport(item, location, image):

        print('[BugReport]: Este item (',item,') não pôde ser trasnformado no tipo desejável de variável.\nA imagem que o gerou foi salva em save/debug/debugImage'+str(Debug.bugCounter)+'.jpg.\n')

        with open('../save/debug/debugList.txt', 'a') as debugList:
            debugList.write('Bug de número: '+str(Debug.bugCounter)+'.\nLocal: '+str(location)+'.\nItem: '+str(item)+'.\nHorário: '+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.\n\n')
        Debug.bugCounter += 1

        image.save('../save/debug/debugImage'+str(Debug.bugCounter)+datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")+'.jpg')
