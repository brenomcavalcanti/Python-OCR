import threading

from reader import Reader

class Main:

    def run():

        MainThread.start()

    def runImage():

        print("Começando [...]\n")

        Reader.run()

MainThread = threading.Thread(target = Main.runImage)

class Backup:
        
    def save():

        with open('../save/data.txt', 'w') as data:
            data.write(str(Reader.runningList))
        print("[Backup]: Reader.runningList foi salvo em save/data.txt com", len(Reader.runningList)," números.\n")

    def doBackup(name=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")):

        with open('../save/backup/'+name+'.txt', 'w') as backupFile:
            backupFile.write(str(Reader.runningList))
        print("[Backup]: Reader.runningList foi salvo em save/backup/"+name+".txt com", len(Reader.runningList)," números.\n")

    def doBackupAndSave(name=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")):

        Backup.doBackup()
        Backup.save()

Main.run()
