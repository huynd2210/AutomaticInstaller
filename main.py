from PyQt5.QtWidgets import QApplication
import sys
import installer
import installerGUI

def main(): 
    '''
    print("1 - Install openJDK")
    print("2 - Install Maven")
    print("3 - Search Bucket")
    while True:
        choice = int(input("\nInput: "))
        if (choice == 1):
            installer.instalAzulZulu()
        if (choice == 2): 
            installer.installMaven()
        if (choice == 3):
            program = input("\nProgram: ")
            installer.scoopSearch(program)        
        if (choice == 0):
            break'   
    '''
    app = QApplication(sys.argv)
    
    window = installerGUI.MainWindow('Automatic Installer')
    
    app.exec_()

if __name__ == '__main__':
    main()
