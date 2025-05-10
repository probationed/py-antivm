import os

class Detection:
    @staticmethod
    def antivm():
        if os.cpu_count() is not None and os.cpu_count() < 2:
            return 1
        else:
            print("no vm")
            return 0
        
Detection.antivm()
