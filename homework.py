from typing import Union, Type

import constants


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 info: str):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_massage(self) -> str:
        """Вывод сообщения о тренировке"""
        print(f'Тип тренеровки: {self.training_type};'
              'Длительность: {self.duration} ч.;'
              'Дистанция: {self.distance} км;'
              'Ср. скорость: {self.speed} км/ч;'
              'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.calories = None

    def get_distance(self, LEN_STEP, M_IN_KM) -> float:
        """Получить дистанцию в км."""
        return self.action * constants.LEN_STEP / constants.M_IN_KM
    
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration
        
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
    pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 M_IN_KM) -> None:
        super().__init__(action, duration, weight, constants.M_IN_KM)

    def get_spent_calories(self) -> float:
        """Расчет потраченных калорий"""
        return ((constants.COEFF_CALORIE_run_1 * self.get_mean_speed() 
                - constants.COEFF_CALORIE_run_2) 
                * self.weight / constants.M_IN_KM 
                * (self.duration / constants.M_IN_H))
        

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
            
    def get_spent_calories(self) -> float:
        """Рассчет потраченных калорий"""
        return ((constants.COEFF_CALORIE_wlk_1 
                * self.weight) + (self.get_mean_speed() 
                * constants.COEFF_CALORIE_wlk_2 // self.height) 
                * constants.COEFF_CALORIE_wlk_3 * self.weight 
                * (self.duration / constants.M_IN_H))


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
    
    def get_distance(self) -> float:
        """Переопределения дистанции для плаванья"""
        return (self.action * self.LEN_STROKE / constants.M_IN_KM)
    
    def get_mean_speed(self) -> float:
        """Формула рассчета средней скорости при плаванье"""
        return (self.length_pool 
                * self.count_pool / constants.M_IN_KM / (self.duration / 60))
        
    def get_spent_calories(self) -> float:
        """Рассчет потраченных калорий при плаванье"""

        return ((self.get_mean_speed() + constants.COEFF_CALORIE_swm_1) 
                * constants.COEFF_CALORIE_swm_ * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_generator: dict[str, Type[
        Union[Training, Running, SportsWalking, Swimming]]] = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking
    }
    training: Union[Training, 
                    Running, 
                    SportsWalking, 
                    Swimming] = workout_generator[workout_type] * (data)
    return training


def main(training: Union[Training, Running, SportsWalking, Swimming]) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

