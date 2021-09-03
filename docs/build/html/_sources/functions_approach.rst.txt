.. _functions-approach-label:

Functions approach
##################

******************************************
Get the difference of days between 2 dates
******************************************

============================
Import get_days_diff_between
============================

First, import :code:`get_days_diff_between` from :code:`date_assistant`:

.. code-block:: python
   :emphasize-lines: 1

   from date_assistant import get_days_diff_between


   get_days_diff_between('2021-01-01', '2021-01-11')
   # 10

===========================
Pass the dates as arguments
===========================

Using the function is every easy. Just pass the dates you want use as parameters:

.. code-block:: python
   :emphasize-lines: 4

   from date_assistant import get_days_diff_between


   get_days_diff_between('2021-01-01', '2021-01-11')
   # 10

.. note::
   💡 Please consider that the default date format is :code:`'%Y-%m-%d'`, eg: :code:`'2021-12-25'`. Anyways, you can indicate the format of your date if you need to.

===============================
Indicate the format of the date
===============================

Maybe the dates you are using have a different format, you can indicate that:

.. code-block:: python
   :emphasize-lines: 7,8

   from date_assistant import get_days_diff_between


   get_days_diff_between(
       '01-01-2021',
       '01-11-2021',
       date1_format='%d-%m-%Y',
       date2_format='%m-%d-%Y',
   )
   # 10

========================
Use the format constants
========================

When indicating the format of a date, it may be hard to remember which is the string that matches the format of the date. Use the format constants which have a more intuitive name for the format of the date:

.. code-block:: python
   :emphasize-lines: 2,8,9

   from date_assistant import get_days_diff_between
   from date_assistant.formats import DD_MM_YYYY, MM_DD_YYYY


   get_days_diff_between(
       '01-01-2021',
       '01-11-2021',
       date1_format=DD_MM_YYYY,
       date2_format=MM_DD_YYYY,
   )
   # 10

********************************************
Get the difference of months between 2 dates
********************************************

============================
Use get_months_diff_between
============================

The same things described for the :code:`get_days_diff_between` function applies when using :code:`get_months_diff_between`. You need to import the function, pass the dates as arguments and you can indicate the format of the dates if you need to:

.. code-block:: python

   from date_assistant import get_months_diff_between
   from date_assistant.formats import DD_MM_YYYY


   get_months_diff_between(
       '2021-02-14',
       '14-02-2022',
       date2_format=DD_MM_YYYY,
   )
   # 12

.. note::
   💡 Notice that we didn't indicate a format for :code:`date1`, that's because :code:`date1` has the same format as the default format: :code:`%Y-%m-%d`.

What happens if we use this function with the last day of a month and the first day of the next one? What do you think the output will be? Let's take a look:

.. code-block:: python
   :emphasize-lines: 5,6

   from date_assistant import get_months_diff_between


   get_months_diff_between(
       '2021-01-31',
       '2021-02-01',
   )
   # 0

As you can see, we get a 0. Because this function only counts the full months between dates. If you need to know how many months have started between 2 dates, use :code:`get_months_started_between`.

************************************************
Get the amount of months started between 2 dates
************************************************

Sometimes you need to know how many months have started between 2 dates. That means that between the last day of a month and the first day of the next one, 1 month started. Let's look explore that use case in this section.

=================================
Import get_months_started_between
=================================

First, import :code:`get_months_started_between` from :code:`date_assistant`:


.. code-block:: python
   :emphasize-lines: 1

   from date_assistant import get_months_started_between


   get_months_started_between(
       '2021-01-31',
       '2021-02-01',
   )
   # 1

===========================
Pass the dates as arguments
===========================

Using the function is every easy. Just pass the dates you want use as parameters, in this case we are using the last day of a month and the first day of the next one as dates:

.. code-block:: python
   :emphasize-lines: 5,6

   from date_assistant import get_months_started_between


   get_months_started_between(
       '2021-01-31',
       '2021-02-01',
   )
   # 1

See how we get a 1 as result. That's because a new month started between the dates, in this case february.

.. note::
   💡 This function allows the same parameters as the previous functions we saw. For example, you can indicate the format of the dates.

*******************************************
Get the difference of years between 2 dates
*******************************************

==========================
Use get_years_diff_between
==========================

The same things described for the :code:`get_days_diff_between` function applies when using :code:`get_years_diff_between`. You need to import the function, pass the dates as arguments and you can indicate the format of the dates if you need to:

.. code-block:: python

   from date_assistant import get_years_diff_between
   from date_assistant.formats import DD_MM_YYYY


   get_years_diff_between(
       '2021-02-14',
       '14-02-2022',
       date2_format=DD_MM_YYYY,
   )
   # 1

.. note::
   💡 Notice that we didn't indicate a format for :code:`date1`, that's because :code:`date1` has the same format as the default format: :code:`%Y-%m-%d`.

What happens if we use this function with the last day of a year and the first day of the next one? What do you think the output will be? Let's take a look:

.. code-block:: python
   :emphasize-lines: 5,6

   from date_assistant import get_months_diff_between


   get_years_diff_between(
       '2021-12-31',
       '2022-01-01',
   )
   # 0

As you can see, we get a 0. Because this function only counts the full years between dates. If you need to know how many years have started between 2 dates, use :code:`get_years_started_between`.

***********************************************
Get the amount of years started between 2 dates
***********************************************

Sometimes you need to know how many years have started between 2 dates. That means that between the last day of a year and the first day of the next one, 1 year started. Let's look explore that use case in this section.

================================
Import get_years_started_between
================================

First, import :code:`get_years_started_between` from :code:`date_assistant`:


.. code-block:: python
   :emphasize-lines: 1

   from date_assistant import get_years_started_between


   get_years_started_between(
       '2021-12-31',
       '2022-01-01',
   )
   # 1

===========================
Pass the dates as arguments
===========================

Using the function is every easy. Just pass the dates you want use as parameters, in this case we are using the last day of a year and the first day of the next one as dates:

.. code-block:: python
   :emphasize-lines: 5,6

   from date_assistant import get_years_started_between


   get_years_started_between(
       '2021-12-31',
       '2022-01-01',
   )
   # 1

See how we get a 1 as result. That's because a new year started between the dates, in this case the year 2022.

.. note::
   💡 This function allows the same parameters as the previous functions we saw. For example, you can indicate the format of the dates.
