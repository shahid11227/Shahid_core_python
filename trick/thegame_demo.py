from tkinter import *
import time 
class Mygame:
    def __init__(self):
        frame=Tk()
        frame.geometry("500x600")
        frame.title("Bouncing Ball")

        Mycan=Canvas(frame,width="500", height="600")
        ball=Mycan.create_oval(10,10,40,40,fill="red")
        Mycan.pack()

        x_move1=2
        y_move1=3


        while True:
            Mycan.move(ball,x_move1,y_move1)

    
            ball_cords=Mycan.coords(ball)

            
            print(ball_cords)

            

            if ball_cords[1]<0  or ball_cords[3]>600:
                y_move1=-y_move1
            if ball_cords[0]<0  or ball_cords[2]>500:
                x_move1=-x_move1

            
            
            Mycan.update()
            time.sleep(0.02)
                
            





BB=Mygame()
