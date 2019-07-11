import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, QThreadPool, pyqtSlot, QRunnable, QObject


class Signals(QObject):
    return_signal = pyqtSignal(str)


class Thread(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self):
        super(Thread, self).__init__()     
        self.signal = Signals()    

    @pyqtSlot()
    def run(self):
        time.sleep(5)
        result = "Some String"
        self.signal.return_signal.emit(result)


class App(QWidget):
    def __init__(self):
            super().__init__()
            self.title='Hello, world!'
            self.left=2100
            self.top=500
            self.width=640
            self.height=480
            self.threadpool = QThreadPool()
            self.initUI()

    def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left,self.top,self.width,self.height)
            checkbox = QCheckBox('Check Box', self)
            checkbox.stateChanged.connect(self.clickCheckbox)
            self.show()

    def clickCheckbox(self):
        thread = Thread()
        thread.signal.return_signal.connect(self.function_thread)
        self.threadpool.start(thread)

    def function_thread(self, signal):
        print(signal)


if __name__=='__main__':
        app=QApplication(sys.argv)
        ex=App()
        sys.exit(app.exec_())