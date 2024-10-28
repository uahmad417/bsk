from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.__frames = []
        pass
    
    def add_frame(self, frame: Frame) -> None:
        if len(self.__frames) == 10:
            raise BowlingError
        self.__frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:

        if i >= len(self.__frames):
            raise BowlingError
        
        return self.__frames[i]

    def calculate_score(self) -> int:
        
        score = 0
        for index, frame in enumerate(self.__frames):

            if frame.is_spare():
                frame.set_bonus(self.__frames[index+1].get_first_throw())

            if frame.is_strike():
                if self.__frames[index+1].is_strike():
                    frame.set_bonus(self.__frames[index+1].get_first_throw() + self.__frames[index+2].get_first_throw())
                else:
                    frame.set_bonus(self.__frames[index+1].get_first_throw() + self.__frames[index+1].get_second_throw())

            score = score + frame.score()
        
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
