import pygame
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget
from playerCode import player

here = str(os.path.abspath(str(os.path.dirname(os.path.realpath(__file__)))))

#gui
class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 320, 120, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 480, 120, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 400, 120, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 351, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #self.lineEdit = QtWidgets.QLineEdit(self.frame)
        #self.lineEdit.setGeometry(QtCore.QRect(170, 290, 171, 20))
        #self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        #self.lineEdit_2.setGeometry(QtCore.QRect(170, 320, 171, 20))
        #self.lineEdit_2.setObjectName("lineEdit_2")
        #self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        #self.lineEdit_3.setGeometry(QtCore.QRect(170, 350, 171, 20))
        #self.lineEdit_3.setObjectName("lineEdit_3")
        #self.label = QtWidgets.QLabel(self.frame)
        #self.label.setGeometry(QtCore.QRect(20, 290, 141, 21))
        #self.label.setObjectName("label")
        #self.label_2 = QtWidgets.QLabel(self.frame)
        #self.label_2.setGeometry(QtCore.QRect(20, 320, 141, 21))
        #self.label_2.setObjectName("label_2")
        #self.label_3 = QtWidgets.QLabel(self.frame)
        #self.label_3.setGeometry(QtCore.QRect(20, 350, 141, 21))
        #self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def temp(self):
        #onClicked(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #buttons
        self.pushButton.setText(_translate("MainWindow", "Start game"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        #self.pushButton_3.setText(_translate("MainWindow", "Settings"))
        #labels
        """
        self.label.setText(_translate("MainWindow", "Height"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.label_3.setText(_translate("MainWindow", "WSAD controll"))

        #settings
        self.lineEdit.setText(_translate("MainWindow", "800"))
        self.lineEdit_2.setText(_translate("MainWindow", "1600"))
        self.lineEdit_3.setText(_translate("MainWindow", "False"))

        self.lineEdit.textChanged[str].connect(self.lineEdit1)
        self.lineEdit_2.textChanged[str].connect(self.lineEdit2)
        self.lineEdit_3.textChanged[str].connect(self.lineEdit3)
        """

        
        self.pushButton.clicked.connect(start)
        self.pushButton_2.clicked.connect(exit_)
        #self.pushButton_3.clicked.connect(self.temp)

    #def lineEdit1(self, text):
        #print(text)
        #game.input1 = float(text)
    #def lineEdit2(self, text):
        #print(text)
        #game.input2 = float(text)
    #def lineEdit3(self, text):
        #print(text)
        #game.input3 = str(text)
        



    
def start():
    game()

def exit_():
    sys.exit(app.exec_())


class bullet:
    def __init__(self, X, Y):
        self.bulletX = X+16
        self.bulletY = Y
    
    def update_pos(self, speed, plane):
        self.bulletY -= speed
        plane.blit(pygame.image.load(here+'/player/bullet.png'), (self.bulletX-8, self.bulletY-8))

    def out(self, max_X, max_Y):
        if self.bulletX > max_X+16 or self.bulletY > max_Y+16 or self.bulletX < -16 or self.bulletY < -16:
            return True
        else:
            return False
        


class game:
    def __init__(self):

        #initialize data
        self.input1 = 0
        self.input2 = 0
        self.input3 = ''

        
        pygame.display.init()
        print(self.input1)
        print(self.input2)
        self.screenHeight = 600
        self.screenWidth = 1200
        print(self.screenHeight)
        print(self.screenWidth)
        self.wsad = self.input3
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_icon(pygame.image.load(here+'/icon/icon.png'))
        pygame.display.set_caption('The game of boomers')
        self.playerImg = pygame.image.load(here+'/player/player.png')
        self.playerX = ((self.screenWidth)/2)-16
        self.playerY = self.screenHeight - 100
        self.p1 = player(self)
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.speed = self.screenWidth / 3000
        self.bullet_speed = self.screenWidth / 2000
        self.bullets = []
        self.time_bullet = 0

        

        #main loop
        on_value = True
        while on_value:
            self.screen.fill((125, 125, 125)) #background color

            if self.time_bullet < 1000: #bullet cooldown
                self.time_bullet=self.time_bullet+1


            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on_value = False
                    sys.exit(app.exec_())



            for bullet_instance in self.bullets:
                bullet_instance.update_pos(self.bullet_speed, self.screen)
                if bullet_instance.out(self.screenWidth, self.screenHeight):
                    self.bullets.remove(bullet_instance)



            if True:#self.wsad == 'False' or self.wsad == 'false'

                pressed = pygame.key.get_pressed() #get pressed keys

                #press
                if pressed[pygame.K_UP]:
                    self.up = True

                if pressed[pygame.K_DOWN]:
                    self.down = True

                if pressed[pygame.K_LEFT]:
                    self.left = True

                if pressed[pygame.K_RIGHT]:
                    self.right = True

                #release
                if not pressed[pygame.K_UP]:
                    self.up = False

                if not pressed[pygame.K_DOWN]:
                    self.down = False

                if not pressed[pygame.K_LEFT]:
                    self.left = False

                if not pressed[pygame.K_RIGHT]:
                    self.right = False

                #fire bullet
                if pressed[pygame.K_SPACE]:
                    if (len(self.bullets) < 20) and (self.time_bullet == 1000):
                        self.time_bullet = 0
                        self.bullets.append(bullet(self.playerX, self.playerY))

            '''

            elif self.wsad == 'True' or self.wsad == 'true':

                pressed = pygame.key.get_pressed() #get pressed keys

                #press
                if pressed[pygame.K_w]:
                    self.up = True

                if pressed[pygame.K_s]:
                    self.down = True

                if pressed[pygame.K_a]:
                    self.left = True

                if pressed[pygame.K_d]:
                    self.right = True

                #release
                if not pressed[pygame.K_w]:
                    self.up = False

                if not pressed[pygame.K_s]:
                    self.down = False

                if not pressed[pygame.K_a]:
                    self.left = False

                if not pressed[pygame.K_d]:
                    self.right = False

            else:
                #print('unexpected outcome')
                pass

            '''

            self.p1.movement() #call for testing movement


            self.p1.render()

            pygame.display.update()

if __name__ == '__main__': #lauch the game
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
