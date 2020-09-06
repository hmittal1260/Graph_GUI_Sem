from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from . import blossom.py

class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        title = "JGraphEd"
        top = 400
        left = 400
        width = 800
        height = 600

        icon = "icons/JGraphEd.png"
     

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.nod=1
        self.bloss=0
        self.four=0
        self.five=0
        self.edge=0
        self.del1=0
        self.save=0
        self.open=0
        self.clicked=0
        self.mov=0
        

        self.drawing = False
        self.brushSize = 5
        self.brushColor = [Qt.red,Qt.green,Qt.yellow,Qt.black,Qt.blue]
        self.brushColor1 = [Qt.red,Qt.green,Qt.yellow,Qt.black,Qt.blue]
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        edit = mainMenu.addMenu("Edit")
        algorithm = mainMenu.addMenu("Algorithm")    
        nodeColor = mainMenu.addMenu("Node Color")
        edgeColor = mainMenu.addMenu("Edge Color")

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save_input)
        
        openAction = QAction(QIcon("icons/open.png"), "Open", self)
        openAction.setShortcut("Ctrl+O")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.open_file)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+N")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        addnodeAction = QAction( QIcon("icons/addnode.png"), "add node", self)
        edit.addAction(addnodeAction)
        addnodeAction.triggered.connect(self.add_node)

        addedgeAction = QAction(QIcon("icons/addedge.png"), "add edge", self)
        edit.addAction(addedgeAction)
        addedgeAction.triggered.connect(self.add_edge)

        deletenodeAction = QAction(QIcon("icons/deletenode.png"),"delete node", self)
        edit.addAction(deletenodeAction)
        deletenodeAction.triggered.connect(self.delete_node)

        movenodeAction = QAction(QIcon("icons/movenode.png"), "move node", self)
        edit.addAction(movenodeAction)
        movenodeAction.triggered.connect(self.move_node)

        blossomAction = QAction(QIcon("icons/blossom.png"), "Blossom", self)
        algorithm.addAction(blossomAction)
        blossomAction.triggered.connect(self.blossom_file)

        fourcoloringAction = QAction(QIcon("icons/four_colouring.png"), "FOUR Coloring Problem", self)
        algorithm.addAction(fourcoloringAction)
        fourcoloringAction.triggered.connect(self.four_coloring_file)

        fivecoloringAction = QAction(QIcon("icons/five_colouring.png"), "FIVE Coloring Problem", self)
        algorithm.addAction(fivecoloringAction)
        fivecoloringAction.triggered.connect(self.five_coloring_file)

        normalAction = QAction(QIcon("icons/normal.png"), "Back to normal graph", self)
        algorithm.addAction(normalAction)
        normalAction.triggered.connect(self.add_node)

        redAction = QAction(QIcon("icons/red.png"), "Red", self)
        edgeColor.addAction(redAction)
        redAction.triggered.connect(self.red_Color)

        greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        edgeColor.addAction(greenAction)
        greenAction.triggered.connect(self.green_Color)

        yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        edgeColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellow_Color)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        edgeColor.addAction(blackAction)
        blackAction.triggered.connect(self.black_Color)


        bluekAction = QAction(QIcon("icons/blue.png"), "Blue", self)
        edgeColor.addAction(bluekAction)
        bluekAction.triggered.connect(self.blue_Color)


        redAction = QAction(QIcon("icons/red.png"), "Red", self)
        nodeColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        nodeColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        nodeColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        nodeColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)


        bluekAction = QAction(QIcon("icons/blue.png"), "Blue", self)
        nodeColor.addAction(bluekAction)
        bluekAction.triggered.connect(self.blueColor)

        self.initUI()
    ### Defining self.nod =0 means if self.nod is 1 then in the mouse release event method
    ### A nod will be added in the variable self.vertex.........
    def add_node(self):
        if self.nod==0:
            self.nod=1
            self.five=0
            self.edge=0
            self.del1=0
            self.mov=0
            self.bloss=0
            self.four=0
            self.update()
            
    ### Defining self.edge =0 means if self.edge is 1 then in the mouse release event method
    ### A edge will be added in the variable self.edge.........
    def add_edge(self):
        if self.edge==0:
            self.edge=1
            self.nod=0
            self.five=0
            self.del1=0
            self.bloss=0
            self.four=0
            self.mov=0
            self.update()
            
    def delete_node(self):
        if self.del1==0:
            self.del1=1
            self.nod=0
            self.edge=0
            self.five=0
            self.four=0
            self.bloss=0
            self.mov=0
            self.update()
            
    def move_node(self):
        if self.mov==0:
            self.mov=1
            self.del1=0
            self.four=0
            self.nod=0
            self.five=0
            self.bloss=0
            self.edge=0
            self.update()

    def clear(self):
        self.vertex=[]
        self.edges=[]
        self.update()
            
    def isSafe(self, v, colour, c,Matrix): 
        for i in range(len(self.vertex)): 
            if Matrix[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    def graphColourUtil(self, m, colour, v,Matrix): 
        if v == len(self.vertex): 
            return True
  
        for c in range(0, m): 
            if self.isSafe(v, colour, c,Matrix) == True: 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v+1,Matrix) == True: 
                    return True
                colour[v] = 0
  
    def graphColouring(self, m,Matrix):
        colour = [0] * len(self.vertex) 
        if self.graphColourUtil(m, colour, 0,Matrix) == None:
            print("NOT POSSIBLE")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Not Possible")
            msg.setWindowTitle("Error")
            msg.exec_()
            self.four = 0
            self.five = 0
            return False
        
        #newvertexarray=[None]*len(self.vertex)
        #newedgearray=[None]*len(self.edges)
        for i in range(len(self.vertex)):
            self.vertex1.append([self.vertex[i][0],self.vertex[i][1],colour[i]])
            #newvertexarray[i]=self.vertex[i]
            #newvertexarray[i][2]=colour[i]
        for j in range(len(self.edges)):
            #newedgearray[j]=self.edges[j]
            self.edges1.append([self.edges[j][0],self.edges[j][1],self.edges[j][2]])
        #print ("Solution exist and Following are the assigned colours:")
        #print(self.vertex1)

        return True
    

    def four_coloring_file(self):
        if self.four==0:
            self.four=1
            self.five=0
            self.bloss=0
            self.mov=0
            self.del1=0
            self.nod=0
            self.edge=0
        Matrix = [[0 for x in range(len(self.vertex))] for y in range(len(self.vertex))] 
        # outfile_1 = open('input.txt','w')
        v1 = self.vertex
        e1 = self.edges
        for tempedge in self.edges:
            x1=self.vertex.index(tempedge[0])
            x2=self.vertex.index(tempedge[1])
            Matrix[x1][x2]=1
            Matrix[x2][x1]=1

        self.graphColouring(4,Matrix)

    def five_coloring_file(self):
        if self.five==0:
            self.five=1
            self.four=0
            self.bloss=0
            self.mov=0
            self.del1=0
            self.nod=0
            self.edge=0
            Matrix = [[0 for x in range(len(self.vertex))] for y in range(len(self.vertex))] 
            #outfile_1 = open('input.txt','w')
            v1 = self.vertex
            e1 = self.edges
            for tempedge in self.edges:
                x1=self.vertex.index(tempedge[0])
                x2=self.vertex.index(tempedge[1])
                Matrix[x1][x2]=1
                Matrix[x2][x1]=1

            self.graphColouring(5,Matrix)
            self.update()

    def blossom_file(self):
        if self.bloss==0:
            self.bloss=1
            self.mov=0
            self.del1=0
            self.five=0
            self.four=0
            self.nod=0
            self.edge=0
            outfile_1 = open('input.txt','w')
            v1 = len(self.vertex)
            e1 = len(self.edges)
            outfile_1.write(str(v1) + " " + str(e1) + '\n')
            self.vertex1 = []
            self.edges1 = []
            self.edges2 = []
            for i in range(len(self.vertex)):
                self.vertex1.append([self.vertex[i][0],self.vertex[i][1],i+1])
            for i in self.edges:
                for j in self.vertex1:
                    if(i[0][0] == j[0] and i[0][1] == j[1]):
                        for k in self.vertex1:
                            if(i[1][0] == k[0] and i[1][1] == k[1]):
                                #self.edges1.append([j[2],k[2]])
                                outfile_1.write(str(j[2]) + " " + str(k[2]) + " 1" + '\n')

            outfile_1.close()
            os.system('python blossom.py')

            infile_1 = open('output.txt','r')
            content_1 = infile_1.read()
            lines_1 = content_1.split('\n')
            for line in lines_1:
                self.edges1.append([int(line.split(' ')[0]),int(line.split(' ')[1])])

            for i in self.edges1:
                self.edges2.append([self.vertex[i[0]-1],self.vertex[i[1]-1]])

            infile_1.close()
            self.update()

    
    def initUI(self):      
        
        self.x = 0
        self.y = 0
        self.col=0
        self.edgecol=3
        
        
        self.vertex=[]
        self.edges=[]

        self.vertex1 = []
        self.edges1 = []

        self.setMouseTracking(True)
        self.show()
        self.update()

    def save_input(self):
        if self.save==0:
            self.folder=os.getcwd()
            self.del1=0
            self.nod=0
            self.edge=0
            fileName, _ = QFileDialog.getSaveFileName(self, "Save Design", os.path.join(str(self.folder), "untitled.txt"), "Input Files(*.txt)")

            if not fileName:
                return

            try:
                out_file = open(str(fileName), 'w')

            except IOError:
                QMessageBox.information(self, "Unable to open file", "There was an error opening \"%s\"" % fileName)
                return
            
            for i in range(len(self.vertex)):
                out_file.write(str(self.vertex[i][0])+','+str(self.vertex[i][1])+','+str(self.vertex[i][2])+'\n')
            out_file.write('*Edges* \n')
            for i in range(len(self.edges)):
                out_file.write(str(self.edges[i][0][0])+','+str(self.edges[i][0][1])+','+str(self.edges[i][0][2])+','+str(self.edges[i][1][0])+','+str(self.edges[i][1][1])+','+str(self.edges[i][1][2])+','+str(self.edges[i][2])+'\n')
            out_file.close()
            pass
        
    
    #This function is for opening the pre loaded file for prdefined graph for
    #File which has First total vertex and then ***....** and then Edges....
    def open_file(self):
        if self.open==0:
            
            self.folder=os.getcwd()
            self.x = 0
            self.y = 0
            self.vertex=[]
            self.edges=[]
            self.edges1=[]
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            filename,_= QFileDialog.getOpenFileName(self, 'Open File', os.path.join(str(self.folder), "*.txt"))
            
           
            f=open(filename, "r")
            if f.mode == 'r':
                contents =f.read()
            lines = contents.split('\n')
            flag=1



            for line in lines:
                if line:
                    if(line[0]=='*'):
                        flag=0
                        continue
                    if(flag):
                        self.vertex.append([int(line.split(',')[0]), int(line.split(',')[1]),int(line.split(',')[2])])
                    else:
                        self.edges.append([[int(line.split(',')[0]), int(line.split(',')[1]),int(line.split(',')[2])],[int(line.split(',')[3]), int(line.split(',')[4]),int(line.split(',')[5])],int(line.split(',')[6])])
            self.update()
        

            
    def mousePressEvent(self, ev):
            self.x = ev.x()
            self.y = ev.y()
        
    
    def mouseReleaseEvent(self, ev):
            ### self.vertex contains all vertex in the [x-coordinate, y-coordinate] format
            ### Like each element of self.vertex is the 2-elemented list of x-coordinate, y-coordinate of vertex
            ### And self.vertex is itself a list of all points
            if self.nod==1:
                if self.x==ev.x() and self.y==ev.y():
                    self.vertex.append([self.x,self.y,self.col])
                    
                    self.update()
                    
            
            ### self.vertex contains all edges in the format [ [x1,y1] , [x2,y2] ]
            ### (x1,y1) and (x2,y2) are coordinates of starting and ending point of the edge
            elif self.edge==1:
                if self.x!=ev.x() and self.y!=ev.y():
                    
                    ### index1 is used here for storing the index of such vertex in the list of vertices self.vertex
                    ### on adding edge if the point of clicked point is in range of circle of radius of 10 unit
                    ### then change the value of index from -1--> to the index of such vertex in self.vertex
                    ### index1 is used for starting of the edge and
                    ### index2 is used for ending of edge means mouse_release_event
                    index1=-1
                    index2=-1
                    for i in range(len(self.vertex)):
                        if self.x<self.vertex[i][0]+10 and self.x>self.vertex[i][0]-10 and self.y<self.vertex[i][1]+10 and self.y>self.vertex[i][1]-10:
                            index1=i
                            
                        if ev.x()<self.vertex[i][0]+10 and ev.x()>self.vertex[i][0]-10 and ev.y()<self.vertex[i][1]+10 and ev.y()>self.vertex[i][1]-10:
                            index2=i
                    ### If there exist starting and ending vertex of edge in the list self.vertex
                    if index1!=-1 and index2!=-1:       
                        self.edges.append([self.vertex[index1],self.vertex[index2],self.edgecol])
                    ### Basically self.update is used for calling whole programme again to paint or adding node
                    ### edge or deleting the node Painting the node or edge
                    self.update()
                    
                    
                    
            ### If the clicked point is in the range of any vertex in the self.vertex
            ### Then all edges which are not containing this vertex is stored in lst list
            ### and then it is being is copied into self.edges back to back
            ### same is being is done for vertex
            elif self.del1==1:
                if self.x==ev.x() and self.y==ev.y():
                    index=-1
                    for i in range(len(self.vertex)):
                        if self.x<self.vertex[i][0]+10 and self.x>self.vertex[i][0]-10 and self.y<self.vertex[i][1]+10 and self.y>self.vertex[i][1]-10:
                            index=i
                            break
                    lst=[]
                    if index!=-1:
                        for i in range(len(self.edges)):
                            if self.vertex[index] not in self.edges[i]:
                                lst.append(self.edges[i])

                        self.edges=lst

                        lst=[]
                        for i in range(len(self.vertex)):
                            if i!=index:
                                lst.append(self.vertex[i])
                        self.vertex=lst
                    ### Now again defining the canvas and painting each node and edges
                    self.update()
                
            elif self.mov==1:
                if self.x!=ev.x() and self.y!=ev.y():
                    index=-1
                    for i in range(len(self.vertex)):
                        if self.x<self.vertex[i][0]+10 and self.x>self.vertex[i][0]-10 and self.y<self.vertex[i][1]+10 and self.y>self.vertex[i][1]-10:
                            index=i
                            break
                    lst=[]
                    temp=0
                    if index!=-1:
                        for i in range(len(self.edges)):
                            for j in range(3):
                                if self.vertex[index] == self.edges[i][j]:
                                    self.edges[i][j][0]=ev.x()
                                    self.edges[i][j][1]=ev.y()

                        self.vertex.append([ev.x(),ev.y(),self.vertex[index][2]])    
                        del self.vertex[index]
                        
                        
                    self.update()
                    
    def paintEvent(self,event):

        canvasPainter  = QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect() )
        
        self.image.fill(Qt.white)
        painter = QPainter(self.image)
        
        
        for pt in range(len(self.vertex)):
            painter.setPen(QPen(self.brushColor[self.vertex[pt][2]],9, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawEllipse(QtCore.QPoint(self.vertex[pt][0], self.vertex[pt][1]), 5, 5)

        for i in range(len(self.edges)):
            painter.setPen(QPen(self.brushColor1[self.edges[i][2]],3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.edges[i][0][0],self.edges[i][0][1],self.edges[i][1][0],self.edges[i][1][1])

        if self.bloss==1:
            painter.setPen(QPen(Qt.cyan,4, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            for i in range(len(self.edges2)):
                painter.drawLine(self.edges2[i][0][0],self.edges2[i][0][1],self.edges2[i][1][0],self.edges2[i][1][1])

        if self.four==1 or self.five==1:
             for pt in range(len(self.vertex1)):
                painter.setPen(QPen(self.brushColor[self.vertex1[pt][2]],9, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
                painter.drawEllipse(QtCore.QPoint(self.vertex1[pt][0], self.vertex1[pt][1]), 5, 5)

             for i in range(len(self.edges1)):
                painter.setPen(QPen(self.brushColor1[self.edges1[i][2]],3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
                painter.drawLine(self.edges1[i][0][0],self.edges1[i][0][1],self.edges1[i][1][0],self.edges1[i][1][1])

              

        self.update()
            

    def blackColor(self):
        self.col = 3

    def blueColor(self):
        self.col = 4

    def redColor(self):
        self.col = 0

    def greenColor(self):
        self.col = 1

    def yellowColor(self):
        self.col = 2

    def black_Color(self):
        self.edgecol = 3

    def blue_Color(self):
        self.edgecol = 4

    def red_Color(self):
        self.edgecol= 0

    def green_Color(self):
        self.edgecol= 1

    def yellow_Color(self):
        self.edgecol = 2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
