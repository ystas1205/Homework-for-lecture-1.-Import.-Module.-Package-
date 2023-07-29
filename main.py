from data_package.salary import calculate_salary
from data_package.people import get_employees
import datetime
import progress.bar
import time


def progressbar():
    bar = progress.bar.FillingSquaresBar("Загрузка")
    for i in range(100):
        bar.next()
        time.sleep(0.001)
    bar.finish()
    print("Загрузка завершена")


if __name__ == '__main__':
    progressbar()
    calculate_salary()
    get_employees()
    print(datetime.datetime.today())
