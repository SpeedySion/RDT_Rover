import string

class Rover():
    '''Stores rover position and orientation and allows them to be changed'''

    directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

    def __init__(self, plat_size = [0,0], coords = [0, 0], r = 'N'):

        #All below statements check for valid coordinates and direction

        if type(plat_size) == list and len(plat_size) == 2 and plat_size[0] >= 0 and plat_size[1] >= 0:
            self.max_dir = plat_size
        else:
            print("Plateau Grid Error. Default Value ([0,0]) Used.")
            self.max_dir = [0,0]

        if type(plat_size) == list and len(plat_size) == 2 and 0 <= coords[0] <= plat_size[0] and 0 <= coords[1] <= plat_size[1]:
            self.coords = coords
        else:
            print("Invalid Starting Coordinates. Default Value ([0,0]) Used.")
            self.coords = [0,0]

        if r.upper() in self.directions.keys():
            self.card_direction = self.directions[r.upper()]
        else:
            print("Invalid Direction. Default Value (North) Used.")
            self.card_direction = 0
    
    def move(self):

        new_pos = self.coords[:]

        match self.card_direction:
            case 0:
                new_pos[1] += 1
            case 1:
                new_pos[0] += 1
            case 2:
                new_pos[1] -= 1
            case 3:
                new_pos[0] -= 1

        #Checks if the movement would move the rover out of the plateau
        for i in range(2):
            if new_pos[i] > self.max_dir[i] or new_pos[i] < 0:
                print("Rover Attempted to Exit Plateau. Movement Aborted.")
                new_pos = self.coords
 
        self.coords = new_pos

    def rotate(self, dir = 'L'):
        #Changes the index for the direction and loops around to the other side if limites are exceeded
        if dir == 'L':
            self.card_direction -= 1
        else:
            self.card_direction += 1
        
        if self.card_direction > 3:
            self.card_direction = 0
        elif self.card_direction < 0:
            self.card_direction = 3


def __main__():

    plateau_grid = [0,0]
    plateau_dimensions = input("Plateau Dimensions: ")

    #Scans for Integers and adds the first two as the dimensions of the plateau
    n = 0
    for i in range(len(plateau_dimensions)):
        if plateau_dimensions[i] in string.digits:
            plateau_grid[n] = int(plateau_dimensions[i])
            n+=1
        if n > 1:
            break

    #Main loop for creating and moving rovers
    while True:

        #Rover details validation/sanitisation loop
        while True:
            rover_det = input("Rover Details: ")
            try:
                rover_det = rover_det.split(' ')
            except:
                pass
            else:
                if len(rover_det) >= 3:
                    rover = Rover(plat_size = plateau_grid, coords = [int(rover_det[0]), int(rover_det[1])], r = rover_det[2])
                    break
            print("Invalid Rover Configuration.")

        #Command string validation/sanitisation loop
        while True:
            commands = input("Command String: ").upper()
            if commands.isalpha():
                break
            print("Invalid Command String.")

        #Checks all commands in prompts and executes them
        for command in commands:
            match command:
                case 'L':
                    rover.rotate(dir = 'L')
                case 'R':
                    rover.rotate(dir = 'R')
                case 'M':
                    rover.move()
                case _:
                    print("Invalid Command Char. Voiding Current Command.")

        #Not happy with this but given that my direction dict uses the chars as keys rather than the index its necessary
        curr_dir = ''
        for card_dir, index in rover.directions.items():
            if index == rover.card_direction:
                curr_dir = card_dir
                break

        print(str(rover.coords[0]) + ' ' + str(rover.coords[1]) + ' ' + curr_dir)

__main__()