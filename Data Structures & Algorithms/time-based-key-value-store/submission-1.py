class TimeMap:

    def __init__(self):
       self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # appends empty list if key is black, then the tuple of
        # timestamp and value
        self.dictionary.setdefault(key,[]).append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # If no in there, return empty string
        if key not in self.dictionary:
            return ""
        
        # We need to find the of the largest timestamp_prev

        # We will need the values here
        values = self.dictionary[key]
        l, r = 0, len(values) - 1
        res = ""

        # Lets binary search this thang
        while l <= r:
            mid = (l+r) // 2
            mid_timestamp = values[mid][0]
            # Smaller or equal to case
            if mid_timestamp <= timestamp:
                # Set new best timestamp
                res = values[mid][1]
                # There may be better, so we still move l up
                l = mid + 1
            # Greater than case
            if mid_timestamp > timestamp:
                # We need to move it down no matter what
                r = mid -1
        return res
                
