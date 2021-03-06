"""
@author  : MG
@Time    : 2020/12/3 10:47
@File    : future_mid_night_task.py
@contact : mmmaaaggg@163.com
@desc    : 用于
"""
import logging

from tasks.wind.future import import_future_min, min_to_vnpy_increment

logger = logging.getLogger()


def run_mid_day_task():
    wind_code_set = None
    # wind_code_set = (
    #     'RB2105.SHF', 'RB2110.SHF',
    #     'HC2105.SHF', 'HC2110.SHF',
    # )
    # instrument_types = ['rb', 'hc', 'i', 'j', 'jm', 'jd', 'ap', 'a', 'p', 'm', 'y', 'b', 'jd', 'ru', 'bu', 'ma', 'cu',
    #                     'fg', 'cj', 'oi', 'rm', 'rs', 'sr', 'cf']
    # wind_code_set = get_main_secondary_contract_by_instrument_types(instrument_types=instrument_types)
    import_future_min(wind_code_set=wind_code_set, )
    min_to_vnpy_increment(
        # instrument_types=['rb', 'i', 'hc']
    )
    logger.info("all task finished")


if __name__ == "__main__":
    run_mid_day_task()
