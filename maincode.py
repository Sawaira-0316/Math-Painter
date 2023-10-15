from canvas import Canvas
from shapes import Rectangular, Square

#Get canvas width and height from users
canvas_width=int(input("Enter canvas width:"))
canvas_height=int(input("Enter canvas height:"))

#MAke a dictionary of color code and promote color
colors= {"White": (255,255,255),"black":(0, 0, 0)}
canvas_color=input("Enter canvas color (white or black): ")

#Creat canvas with user data
canvas=Canvas(height=canvas_height,width=canvas_width,color=colors[canvas_color])

while True:
    shapes_type=input("What do you like to draw? Enter quit to quit.")
#craet rectangular if user ask
    if shapes_type.lower() == "rectangular":
        rec_x=int(input("Enter x of rectangular: "))
        rec_y=int(input("Enter y of rectangular: "))
        rec_width=int(input("Enter width of rectangular: "))
        rec_height=int(input("Enter height of rectangular "))
        red=int(input("how much red should rectgular have? "))
        green=int(input("How much green? "))
        blue=int(input("How much blue"))

        r1=Rectangular(x=rec_x,y=rec_y,height=rec_height,width=rec_width,color=(red,green,blue))
        r1.draw(canvas)
#Creat Square if user ask

    if shapes_type.lower() == "square":
        sqr_x = int(input("Enter x of square: "))
        sqr_y = int(input("Enter y of squar: "))
        sqr_side_= int(input("Enter the side lenght of square? "))
        red = int(input("how much red should square have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue"))

        s1=Square(x=sqr_x,y=sqr_y,side=sqr_side_,color=(red,green,blue))
        s1.draw(canvas)

    if shapes_type == "quit":
        break
canvas.make('canvas.png')
