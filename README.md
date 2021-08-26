[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/date_assistant/badge.svg?branch=main)](https://coveralls.io/github/jalvaradosegura/date_assistant?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![basic-quality-check](https://github.com/jalvaradosegura/date_assistant/actions/workflows/code_quality.yml/badge.svg)](https://github.com/jalvaradosegura/date_assistant/actions/workflows/code_quality.yml)
[![GitHub license](https://img.shields.io/github/license/jalvaradosegura/date_assistant)](https://github.com/jalvaradosegura/date_assistant/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/date-assistant)](https://pepy.tech/project/date-assistant)
[![Documentation Status](https://readthedocs.org/projects/date-assistant/badge/?version=latest)](https://date-assistant.readthedocs.io)

# Date Assistant
For more details take a look at the [docs](https://date-assistant.readthedocs.io) 

## Installation
date-assistant is published on [PyPI](https://pypi.org/project/date-assistant/) and can be installed from there:
```
pip install date-assistant
```

## Usage
> 💡 Please consider that the default date format is '%Y-%m-%d'. Anyways, you can indicate the format of your date if you need to.

### Functions approach

#### Get the difference of days, months or years between 2 dates
```py
from date_assistant import (
    get_days_diff_between,
    get_months_diff_between,
    get_years_diff_between,
)
from date_assistant.formats import DD_MM_YYYY, YYYY_MM


get_days_diff_between('2021-01-01', '2021-01-11')
# 10
get_days_diff_between('2021-01-01', '21-01-2021', date2_format=DD_MM_YYYY)
# 20

get_months_diff_between('2021-01-01', '2022-01-11')
# 12
get_months_diff_between('2021-01-05', '2021-02-01')
# 0
get_months_diff_between('2021-01', '2021-02-21', date1_format=YYYY_MM)
# 1

get_years_diff_between('2021-01-01', '2022-01-11')
# 1
get_years_diff_between('2021-01-05', '2022-01-01')
# 0
get_years_diff_between('2021-01', '2023-01-01', date1_format=YYYY_MM)
# 2
```
> 💡 See how months and years are only counted if a full year or month has passed.

#### Get the amount of years or months started between 2 dates
```py
from date_assistant import (
    get_months_started_between,
    get_years_started_between,
)
from date_assistant.formats import YYYY_MM


get_months_started_between('2021-01-05', '2021-02-01')
# 1
get_months_started_between('2021-01-01', '2022-01-11')
# 12
get_months_started_between('2021-01', '2021-02-21', date1_format=YYYY_MM)
# 1

get_years_started_between('2021-01-01', '2020-12-31')
# 1
get_years_started_between('2021-01-05', '2022-01-01')
# 1
get_years_started_between('2021-01', '2023-01-01', date1_format=YYYY_MM)
# 2
```

> 💡 In contrast with the previous block example, here you don't need a full year or month between dates to count. If a new year or month started, it count.

### Classes approach

#### Get the difference of days, months or years between 2 dates
```py
from date_assistant import DateAssistant

my_birthday_2021 = DateAssistant('2021-07-13')
date_assistant_birthday = '2021-08-18'

my_birthday_2021.days_diff_with(date_assistant_birthday)
# 36
my_birthday_2021.months_diff_with(date_assistant_birthday)
# 1
my_birthday_2021.years_diff_with(date_assistant_birthday)
# 0
```

#### Get the amount of years or months started since or until some date
```py
from date_assistant import DateAssistant

last_day_of_2021 = DateAssistant('2021-12-31')
first_day_of_2022 = '2022-01-01'
first_day_of_2023 = '2023-01-01'
date_assistant_birthday = '2021-08-18'

last_day_of_2021.years_started_until(first_day_of_2022)
# 1
last_day_of_2021.years_started_until(first_day_of_2023)
# 2
last_day_of_2021.months_started_until(first_day_of_2022)
# 1
last_day_of_2021.months_started_since(date_assistant_birthday)
# 4
```
