from turtle import distance, window_height


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    def get_massage(self) -> str:
        print (f'Тип тренеровки: {training_type};' 
               f'Длительность: {duration} ч.;' 
               f'Дистанция: {distance} км;' 
               f'Ср. скорость: {speed} км/ч;'
               f'Потрачено ккал: {calories}.')




class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        LEN_STEP = 0,65
        M_IN_KM = 1000
        self.distance = action * LEN_STEP/M_IN_KM
        return distance


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        self.speed = self.distance/self.duration
        return speed 


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
    pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""



class Running(Training):
    """Тренировка: бег."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action: int,
                 duration: float,
                 weight: float)
    
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        self.calories = (coeff_calorie_1 * self.speed - coeff_calorie_2) * self.weight/ M_IN_KM*(self.duration/60)
        return calories



class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action: int,
                 duration: float,
                 weight: float)
        self.height = height 
    def get_spent_calories(self) -> float:
        coeff_callorie_1 = 0,035
        coeff_callorie_2 = 2
        coeff_callorie_3 = 0,029
        self.spent_calories = (coeff_callorie_1 * self.weight + (self.speed * coeff_callorie_2 // self.height)* coeff_callorie_3 * self.weight)* (self.duration/60)



class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: float,
                 count_pool: float) -> None:
        super().__init__(action: int,
                 duration: float,
                 weight: float)
        self.length_pool = length_pool
        self.count_pool = count_pool
    def get_mean_speed (self) -> float:
        """Формула рассчета средней скорости при плаванье"""
        self.speed = self.length_pool * self.count_pool / M_IN_KM/ (self.duration/60)
        return speed
    
    def get_spent_calories(self) -> float:
        call_coef = 1,1
        call_coef = 2
        self.calories = (self.speed + call_coef) * call_coef_2 * self.weight
        return calories




def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

