import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt
import socket


def SocketFuc(MESSAGE):
    UDP_IP = "127.0.0.1"
    # UDP_IP = "192.168.72.152"
    UDP_PORT = 9930

    # MESSAGE = b"Hello, World!"
    # MESSAGE = b"Mr;1,0,1.73,0.43,1.74,diff,0,0.5,ivam_3F;2,3,2.48,-5.01,1.74,diff,0,0.5,ivam_3F,2;E" #line
    # MESSAGE = b"Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,0,0.5,ivam_3F;3,3,4.01,-3.44,1.68,diff,0,0.5,ivam_3F,2;E" #one turn
    # MESSAGE = b"Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,1,0.5,ivam_3F;3,1,4.01,-3.44,1.68,diff,0,0.5,ivam_3F;4,3,1.31,-3.73,0.12,diff,0,0.5,ivam_3F,2;E" #two turn
    # MESSAGE = b"Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,0,0.5,ivam_3F;3,1,3.77,-0.85,-1.46,diff,1,0.5,ivam_3F;4,1,4.01,-3.44,1.68,diff,1,0.5,ivam_3F;5,1,1.31,-3.73,0.12,diff,0,0.5,ivam_3F;6,3,0.72,-0.358,-1.45,diff,0,0.5,ivam_3F,2;E"  # o turn
    # "Mr;1,0,1.68822,0.432922,1.71258,diff,0,0.5,ivam_3F;2,3,2.46556,-4.44588,1.66535,diff,0,0.5,ivam_3F,2;E"

    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print()


def button1Fuc():
    SocketFuc(b"Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,0,0.5,ivam_3F;3,1,3.77,-0.85,-1.46,diff,1,0.5,ivam_3F;4,1,4.01,-3.44,1.68,diff,1,0.5,ivam_3F;5,1,1.31,-3.73,0.12,diff,0,0.5,ivam_3F;6,3,0.72,-0.358,-1.45,diff,0,0.5,ivam_3F,2;E")

def button2Fuc():
    SocketFuc(b"F;10;E")

# back o
def button3Fuc():
    SocketFuc(b"Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,0,0.5,ivam_3F;3,1,3.77,-0.85,-1.46,diff,1,0.5,ivam_3F;4,1,4.01,-3.44,1.68,diff,1,0.5,ivam_3F;5,1,1.31,-3.73,0.12,diff,0,0.5,ivam_3F;6,3,0.72,-0.358,-1.45,diff,0,0.5,ivam_3F,2;E")

# square
def SendSquPath():
    SocketFuc(b"Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,0,0.5,ivam_3F;3,1,3.77,-0.85,-1.46,diff,1,0.5,ivam_3F;4,1,4.01,-3.44,1.68,diff,1,0.5,ivam_3F;5,1,1.31,-3.73,0.12,diff,0,0.5,ivam_3F;6,3,0.72,-0.358,-1.45,diff,0,0.5,ivam_3F,2;E")

# back
def SendBack():
    SocketFuc(b"F;10;E")

# front
def SendFront():
    SocketFuc(b"F;11;E")

def main():
    app = QApplication([])

    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    # The rest of the code is the same as for the "normal" text editor.
    app.setApplicationName("IVAM")
    text = QPlainTextEdit()

    window = QWidget()
    layout = QGridLayout()

    button1 = QPushButton("button1")
    button1.clicked.connect(button1Fuc)
    layout.addWidget(button1, 0, 0)

    button2 = QPushButton("button2")
    button2.clicked.connect(button2Fuc)
    layout.addWidget(button2, 0, 1)

    button3 = QPushButton("button3")
    button3.clicked.connect(button3Fuc)
    layout.addWidget(button3, 1, 0)

    button4 = QPushButton("Square")
    button4.clicked.connect(SendSquPath)
    layout.addWidget(button4, 1, 1)

    button5 = QPushButton("Back")
    button5.clicked.connect(SendBack)
    layout.addWidget(button5, 2, 0)

    button6 = QPushButton("Front")
    button6.clicked.connect(SendFront)
    layout.addWidget(button6, 2, 1)

    window.setLayout(layout)
    window.show()

    app.exec_()

main()
