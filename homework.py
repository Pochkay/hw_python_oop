from dataclasses import dataclass, asdict
from typing import Union

import constants


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    info: str = constants.INFO_MESSAGE

    def get_message(self) -> str:
        """Вывод сообщения о тренировке"""
        return self.info.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = constants.LEN_STEP
    M_IN_KM: int = constants.M_IN_KM

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.calories = None

    def get_distance(self) -> float:
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
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Расчет потраченных калорий"""
        return (
            constants.COEFF_CALORIE_run_1
            * self.get_mean_speed()
            - constants.COEFF_CALORIE_run_2) * self.weight / constants.M_IN_KM * (self.duration * constants.M_IN_H)


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
        return (
            constants.COEFF_CALORIE_wlk_1
            * self.weight
            + (self.get_mean_speed()
            ** constants.COEFF_CALORIE_wlk_2
            // self.height)
            * constants.COEFF_CALORIE_wlk_3
            * self.weight) * self.duration * constants.M_IN_H


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = constants.LEN_STROKE

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
        return self.action * self.LEN_STEP / constants.M_IN_KM

    def get_mean_speed(self) -> float:
        """Формула рассчета средней скорости при плаванье"""
        return (self.length_pool
                * self.count_pool
                / constants.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        """Рассчет потраченных калорий при плаванье"""

        return ((self.get_mean_speed() + constants.COEFF_CALORIE_swm_1)
                * constants.COEFF_CALORIE_swm_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    train_dict = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking}
    return train_dict[workout_type](*data)


def main(training: Union[Training, Running, Swimming, SportsWalking]) -> None:
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
