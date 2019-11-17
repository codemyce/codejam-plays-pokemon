# Imports
import threading

# Import files
import KeyboardInput
import PoseEstimation

if __name__ == '__main__':
    # Set up emulator and initial keypresses
    KeyboardInput.setup_keyboard('bsnes-hd_beta9_windows\\bsnes-hd_beta9.exe')

    # Start thread for listening to other input
    task = KeyboardInput.keyboard_listener
    t = threading.Thread(target=task)
    t.start()

    # Start and run engine that will run comp vision
    PoseEstimation.main(PoseEstimation.create_parser().parse_args())