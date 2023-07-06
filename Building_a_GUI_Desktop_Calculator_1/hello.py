import sys      # Allow you to handle the application’s termination and exit status through the exit() function

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100,100,280,80) # (x,y,width,height)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent = window)
helloMsg.move(60,15) 

window.show()
sys.exit(app.exec())
