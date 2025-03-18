#main file

#add libraries for color hexcodes

#defined constants
COLOR = (WHITE, RED, ORANGE, YELLOW, GREEN, BLUE) = (0, 1, 2, 3, 4, 5)

#structure of a cube 
class cube():
   #cube size: default is 3x3x3
   size = "3x3x3"

   #more attributes here
   
   def __init__(self):
      #init all sides to starting color as default
      self.Left = face("Left", COLOR[2])
      self.Front = face("Front", COLOR[4])
      self.Right = face("Right", COLOR[1])
      self.Back = face("Back", COLOR[5])
      self.Up = face("Up", COLOR[0])
      self.Down = face("Down", COLOR[3])
      self.faces = (self.Up, self.Left, self.Front, self.Right, self.Back, self.Down) #stored in printing order

#class for a cube face
class face():
   #top, mid, bot = [[9,9,9],[9,9,9],[9,9,9]]
   #map = [top, mid, bot]

   #need variable for adjacent face info?

   def __init__(self, name, color):
      self.name = name
      self.top, self.mid, self.bot = [[9,9,9],[9,9,9],[9,9,9]]
      self.map = [self.top, self.mid, self.bot]
      for i in range(len(self.map)):
         for j in range(len(self.map)):
            self.map[i][j] = color

#class for a cube node
class node():
   
   def __init__(self, type, color, face, pos):
      self.type = type #three possible types are center, corner, and edge | center types will never change their color
      self.color = color #inherited color from Face
      self.face = face #parent Face name (Left, Front, Right, Back, Up, or Down)
      self.pos = pos #(x, y) value indicating location in Face | related to type i.e. center is (1,1)
      self.adj = [7,7,7,7] #variable to store information about adjacent nodes | init as unknown color (7)

#function to map a whole face as a single color "set_face_color"

#function to print a single cube face | takes face object
def print_face(face):
   if face.name == 'Up' or face.name == 'Down':
      print(len(str(face.top))*' ',' '+str(face.top)+'\n', len(str(face.mid))*' ', str(face.mid)+'\n', len(str(face.bot))*' ', str(face.bot))
   else:
      print(' '+str(face.top)+'\n', str(face.mid)+'\n', str(face.bot))


#function to print the cube state
def print_cube(cube):
   #print Up face in first row with padding
   #print Left, Front, Right, and Back faces in second row
   #print Down face in third row with padding
   for i in range(len(cube.faces)):
      print_face(cube.faces[i])

#function to perform quarter turns

#function to perform half turns

#function to solve the cube

#main function
def main():
   Cube = cube()
   print_cube(Cube)

if __name__ == "__main__":
   main()