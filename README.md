# papi
**papi** (Personal Amazon Price Inflation) computes your running annual price inflation percentage using the [Laspereyes](https://en.wikipedia.org/w/index.php?title=List_of_price_index_formulas&oldid=1077502962#Laspeyres) approach. This requires a substantial order history on Amazon.com over at least the last two years.

In the implemented [price index calculation](https://en.wikipedia.org/w/index.php?title=Price_index&oldid=1062591479#Formal_calculation),
* The **later period** is defined as the period from the most recent order date (of any order) to a year before it, e.g. from 22 May 2021 to 21 May 2022.
* The **base period** is defined as one year before the later period, e.g. from 22 May 2020 to 21 May 2021.

As a disclaimer, this software is not associated with Amazon. No guarantee is made about the correctness, usefulness, or representativeness of the computed numbers.

# Approach
Steps:
1. Find the average price (with tax) of each ordered item in each of the two periods. Only items having *Condition=new* are considered.

# Usage

Download the CSV of your [order history](https://www.amazon.com/b2b/reports) using these parameters:
- Report Type: Items
- Start Date: 01/01/2006
- End Date: (today's date, e.g. 07/14/2022)

In a new Python 3.10 virtual environment:
```shell
$ pip install -r ./requirements.txt
$ python -m papi ./your_data.csv
```