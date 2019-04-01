import Leap  

class AirController(Leap.Listener):

    def on_init(self, controller):
        print(' - Initialized - ')
        self.acc = 0
        self.vector = {0,0,0}

    def get_status(self): 
        return {self.acc, self.angles}

    def on_connect(self):
        print(' - Connect - ')



    def on_frame(self, controller):
        frame = controller.frame

        for hand in frame.hands:
            if not hand.left_hand:
                # we are intrested in right hand only
                palm = hand.palm
                self.acc = palm.height
                self.vector = palm.vector
