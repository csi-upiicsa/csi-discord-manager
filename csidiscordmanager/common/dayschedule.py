class DaySchedule:
    def __init__(self, week_day, interval):
        self.week_day = week_day
        self.starts_at = 0
        self.ends_at = 0
        self._splitInterval(interval)

    def _splitInterval(self, interval):
        time = interval.split("-")
        starts_at = time[0].split(":")
        starts_at_time = int(starts_at[0]) * 60 + int(starts_at[1])
        ends_at = time[1].split(":")
        ends_at_time = int(ends_at[0]) * 60 + int(ends_at[1])
        if starts_at_time > ends_at_time:
            raise Exception(
                f"Start time greater than end time at {self.name}.")
        self.starts_at = starts_at_time
        self.ends_at = ends_at_time