from settings import *


def find_streak(list, needle, n=VICTORY_STRICK):
    if n >= 0:
        index = 0
        count = 0
        streak = False

        while count < n and index < len(list):
            if needle == list[index]:
                streak = True
                count += 1
            else:
                streak = False
                count = 0
            
            index += 1
        return count >= n and streak
    else:
        return False
