"""
03 Prove : Assignment

Student: Sebastian Gomez

Instructor: Brother Poulson
"""

class Robot:
    
    # Assigning each attribute of the robot
    def __init__(self):
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel_amount = 100

    # Left command should subtract one from the x-coordinate and subtract five from the fuel amount if it has more than one fuel amount
    def move_left(self):
        if self.fuel_amount <= 0:
            print("Insufficient fuel to perform action")
        else:
            self.x_coordinate -= 1
            self.fuel_amount -= 5
        return

    # Right command should add one from the x-coordinate and subtract five from the fuel amount if it has more than one fuel amount
    def move_right(self):
        if self.fuel_amount <= 0:
            print("Insufficient fuel to perform action")
        else:
            self.x_coordinate += 1
            self.fuel_amount -=5
        return
    
    # Down command should subtract one from the y-coordinate and subtract five from the fuel amount if it has more than one fuel amount
    def move_down(self):
        if self.fuel_amount <= 0:
            print("Insufficient fuel to perform action")
        else:
            self.y_coordinate += 1
            self.fuel_amount -=5
        return

    # Up command should add one from the y-coordinate and subtract five from the fuel amount if it has more than one fuel amount
    def move_up(self):
        if self.fuel_amount <= 0:
            print("Insufficient fuel to perform action")
        else:
            self.y_coordinate -= 1
            self.fuel_amount -=5
        return

    # Fire command should print "Pew! Pew!" and subtract fifteen from the fuel amount if it has more than fifteen fuel amount
    def display_fire(self):
        if self.fuel_amount <= 15:
            print("Insufficient fuel to perform action")
        else:
            print("Pew! Pew!")
            self.fuel_amount -= 15
        return

    # Status command should display the attributes information of the robot
    def display_status(self):
        print(f"({self.x_coordinate}, {self.y_coordinate}) - Fuel: {self.fuel_amount}")
        return

def main():
    
    play_robot = Robot()
    msg = ""

    while msg != "quit":

        msg = input("Enter command: ")

        if msg == "left":
            play_robot.move_left()
        elif msg == "right":
            play_robot.move_right()
        elif msg == "down":
            play_robot.move_down()
        elif msg == "up":
            play_robot.move_up()
        elif msg == "fire":
            play_robot.display_fire()
        elif msg == "status":
            play_robot.display_status()
        elif msg == "quit":
            print("Goodbye.")

if __name__ == "__main__":
    print()
    print("Hi! You have to model the driving of a robot using the following commands:")
    print("-left \n-right \n-up \n-down \n-fire")
    print("If you want to know the status of your robot use:")
    print("-status")
    print("If you want to finish write:")
    print("-quit\n")
    main()