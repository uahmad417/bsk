from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.__frame = []
        pass
    
    def add_frame(self, frame: Frame) -> None:
        if len(self.__frame) == 10:
            raise BowlingError
        self.__frame.append(frame)

    def get_frame_at(self, i: int) -> Frame:

        if i >= len(self.__frame):
            raise BowlingError
        
        return self.__frame[i]

    def calculate_score(self) -> int:
        
        score = 0
        is_spare = False
        for frame in self.__frame:
            
            if is_spare:
                score = score + frame.get_first_throw()
                is_spare = False

            if frame.is_spare():
                is_spare = True

            score = score + frame.score()
        
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
