# Developers:

#################################
# Henil Patel                   #
# Muhammad Asim                 # 
# Amandeep Kaur                 #
# Sadiya Islam                  #
# Nischey                       #
#################################


# This is the main.py which is the compilation of all the python files, it will start from login page
import sys
from PyQt6.QtWidgets import QApplication
from login import MainWindow as LoginMainWindow

def main():
    app = QApplication(sys.argv)
    login_window = LoginMainWindow()
    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
