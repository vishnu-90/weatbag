class Tile:
   def describe(self):
       print("Looks like you are in a walking mood!\n"
             "You hear birds singing, some small waves on the background, "
             "there is a nice flowery smell, rays of sun make the tree "
             "scenery heavenly...\n"
             "I totaly get you, it's a nice path to have a walk!\n")
                   
   def action(self, player, do):
       print("Sorry, I don't understand.")
       
   def leave(self, player, direction):
       if direction == "n":
           print("No trespasing. Violators will vanish without a trace.")
           return False
       else:
           return True
