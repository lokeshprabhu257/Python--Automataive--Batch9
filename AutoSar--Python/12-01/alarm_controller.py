class SpeedAlarmController:
    def __init__(self, speed_limit):
        self.speed_limit = speed_limit
        self.alarm_active = False
        self.alarm_start_time = None

    def check_speed(self, current_speed):
        if current_speed > self.speed_limit:
            if not self.alarm_active:
                self.On_alarm()
        else:
            if self.alarm_active:
                self.Off_alarm()

    def On_alarm(self):
        self.alarm_active = True
        print("Alarm Activated: Speed limit exceeded!")
        print("Indicator ON")

    def Off_alarm(self):
        self.alarm_active = False
        self.alarm_start_time = None
        print("Alarm Deactivated: Speed back to normal.")
        print("Indicator OFF")
    


if __name__ == "__main__":  
    controller = SpeedAlarmController(speed_limit=60)

    speeds = [int(x) for x in input("Enter speeds separated by spaces: ").split()]
    for speed in speeds:
        controller.check_speed(speed)