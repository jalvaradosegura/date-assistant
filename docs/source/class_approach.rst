.. _class-approach-label:

Class approach
##############

************************************************************
Get the difference of days, months and years between 2 dates
************************************************************

============================
Import DateAssistant
============================

First, import :code:`DateAssistant` from :code:`date_assistant`, it will grant you access to all the main methods:

.. code-block:: python
   :emphasize-lines: 1

   from date_assistant import DateAssistant


   my_birthday_2021 = DateAssistant('2021-07-13')
   date_assistant_birthday = '2021-08-18'

   my_birthday_2021.days_diff_with(date_assistant_birthday)
   # 36
   my_birthday_2021.months_diff_with(date_assistant_birthday)
   # 1
   my_birthday_2021.years_diff_with(date_assistant_birthday)
   # 0

=======================================================
Instantiate the class and define another date as string
=======================================================

You don't actually need to define another variable, but it will improve the readability:

.. code-block:: python
   :emphasize-lines: 4,5

   from date_assistant import DateAssistant


   my_birthday_2021 = DateAssistant('2021-07-13')
   date_assistant_birthday = '2021-08-18'

   my_birthday_2021.days_diff_with(date_assistant_birthday)
   # 36
   my_birthday_2021.months_diff_with(date_assistant_birthday)
   # 1
   my_birthday_2021.years_diff_with(date_assistant_birthday)
   # 0

===============
Use the methods
===============

Now execute the methods to get the answer as an integer:

.. code-block:: python
   :emphasize-lines: 7-12

   from date_assistant import DateAssistant


   my_birthday_2021 = DateAssistant('2021-07-13')
   date_assistant_birthday = '2021-08-18'

   my_birthday_2021.days_diff_with(date_assistant_birthday)
   # 36
   my_birthday_2021.months_diff_with(date_assistant_birthday)
   # 1
   my_birthday_2021.years_diff_with(date_assistant_birthday)
   # 0

You can indicate the format of both of your dates, on the :code:`__init__` method for the base date and on each operation method when using another date (exactly as the :ref:`functions-approach-label`).

.. note::
   💡 Please consider that the default date format is :code:`'%Y-%m-%d'`, eg: :code:`'2021-12-25'`. Anyways, you can indicate the format of your date if you need to.
