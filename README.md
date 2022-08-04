# papi
**papi** (Personal Amazon Price Inflation) is a simple [PoC](https://en.wikipedia.org/wiki/Proof_of_concept) to compute your running annual price inflation percentage. It implements the [Laspereyes](https://en.wikipedia.org/w/index.php?title=List_of_price_index_formulas&oldid=1077502962#Laspeyres) and [Paasche](https://en.wikipedia.org/w/index.php?title=List_of_price_index_formulas&oldid=1077502962#Paasche) approaches. This requires a substantial order history on Amazon.com over at least the last two years.

In the implemented [price index calculation](https://en.wikipedia.org/w/index.php?title=Price_index&oldid=1062591479#Formal_calculation),
* The **later period** is defined as the period from the most recent order date (of any order) to a year before it, e.g. from 22 May 2021 to 21 May 2022.
* The **base period** is defined as one year before the later period, e.g. from 22 May 2020 to 21 May 2021.

As a disclaimer, this software is not associated with Amazon. No guarantee is made about the correctness, usefulness, or representativeness of the computed numbers.

# Usage

Download the CSV of your [order history](https://www.amazon.com/b2b/reports) using these parameters:

| Parameter   | Value                           |
|-------------|---------------------------------|
| Report Type | Items                           |
| Start Date  | 01/01/2006                      |
| End Date    | (today's date, e.g. 07/29/2022) |

In a new Python 3.10 virtual environment:
```shell
$ pip install -r ./requirements.txt
$ python -m papi ./your_amazon_data.csv
```

Sample output:
```
[LastOrderDate=2022-07-31] NumCommonUniqueItems=40, Laspeyres=5.6%, Paasche=5.6%
[LastOrderDate=2022-07-30] NumCommonUniqueItems=40, Laspeyres=5.8%, Paasche=6.0%
[LastOrderDate=2022-07-28] NumCommonUniqueItems=38, Laspeyres=6.0%, Paasche=5.9%
[LastOrderDate=2022-07-26] NumCommonUniqueItems=36, Laspeyres=5.8%, Paasche=5.9%
[LastOrderDate=2022-07-25] NumCommonUniqueItems=36, Laspeyres=5.8%, Paasche=5.9%
[LastOrderDate=2022-07-24] NumCommonUniqueItems=36, Laspeyres=5.9%, Paasche=5.8%
[LastOrderDate=2022-07-20] NumCommonUniqueItems=35, Laspeyres=6.5%, Paasche=6.4%
[LastOrderDate=2022-07-17] NumCommonUniqueItems=35, Laspeyres=6.5%, Paasche=6.4%
[LastOrderDate=2022-07-16] NumCommonUniqueItems=30, Laspeyres=6.3%, Paasche=5.9%
```