import Leap  

class AirController(Leap.Listener):
    def on_frame(self, controller):
        frame = controller.frame

        for hand in frame.hands:
            if not hand.left_hand:
                # we are intrested in right hand only
                palm = hand.palm
