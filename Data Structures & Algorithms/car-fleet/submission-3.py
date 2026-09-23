class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cool = sorted(list(zip(position,speed)), reverse = True)
        
        print(position)
        #time = (target - position) / speed
        max_time_seen_so_far = 0
        for pos, spd in cool:
            time = (target - pos) / spd
            if time <= max_time_seen_so_far:
                continue
            else:
                max_time_seen_so_far = time
                stack.append(time)



        return len(stack)

