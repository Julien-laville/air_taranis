import Leap, sys
from air_controller import AirController

def main():
    controller = Leap.Controller()
    listener = AirController()
    controller.add_listener(listener)

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
