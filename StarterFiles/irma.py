import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    import csv
    ''' 
    reads irma.csv and uses its data to
    construct hurricane irma's path based on 
    its location and wind pressure (category).
    Red for Category 5 (157 mph or higher)
    Orange for Category 4 (130-156 mph)
    Yellow for Category 3 (111-129 mph)
    Green for Category 2 (96-110 mph)
    Blue for Category 1 (74-95 mph)
    White for low wind pressure (73 mph or less)
    '''
    with open('data/irma.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == 'Date':
                continue
            t.goto(float(row[3]),float(row[2]))
            if int(row[4]) < 74:     #Category 0
                t.color('white')
                t.pensize(0)
            elif int(row[4]) < 96:     #Category 1
                t.color('blue')
                t.pensize(2)
                t.write("1", False, "center", ("Arial", 10, "normal"))
            elif int(row[4]) < 111:  #Category 2
                t.color('green')
                t.pensize(4)
                t.write("2", False, "center", ("Arial", 10, "normal"))
            elif int(row[4]) < 130:  #Category 3
                t.color('yellow')
                t.pensize(6)
                t.write("3", False, "center", ("Arial", 10, "normal"))
            elif int(row[4]) < 157:  #Category 4
                t.color('orange')
                t.pensize(8)
                t.write("4", False, "center", ("Arial", 10, "normal"))
            else:                    #Category 5
                t.color('red')
                t.pensize(10)
                t.write("5", False, "center", ("Arial", 10, "normal"))


    wn.exitonclick()



if __name__ == "__main__":
    irma()
