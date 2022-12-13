# papical
**papical** (**P**ersonal **A**mazon **P**rice **I**nflation **Cal**culator) is a simple [PoC](https://en.wikipedia.org/wiki/Proof_of_concept) to calculate your running annual price inflation percentage. It implements the [Laspereyes](https://en.wikipedia.org/w/index.php?title=List_of_price_index_formulas&oldid=1077502962#Laspeyres), [Paasche](https://en.wikipedia.org/w/index.php?title=List_of_price_index_formulas&oldid=1077502962#Paasche), and [Fisher](https://en.wikipedia.org/w/index.php?title=List_of_price_index_formulas&oldid=1103634762#Fisher) approaches. This requires a substantial order history on Amazon.com over at least the last two years.

In the implemented [price index calculation](https://en.wikipedia.org/w/index.php?title=Price_index&oldid=1062591479#Formal_calculation),
* The **later period** is defined as the period from the most recent order date (of any order) to a year before it, e.g. from 22 May 2021 to 21 May 2022.
* The **base period** is defined as one year before the later period, e.g. from 22 May 2020 to 21 May 2021.

As a disclaimer, this software is not associated with Amazon. No guarantee is made about the correctness, usefulness, or representativeness of the computed numbers.

# Usage

Download the CSV of your [order history](https://www.amazon.com/b2b/reports) using these parameters:

| Parameter   | Value                                                      |
|-------------|------------------------------------------------------------|
| Report Type | Items                                                      |
| Start Date  | 01/01/2006 (or at least 2 full years ago, e.g. 02/02/2020) |
| End Date    | (today's date, e.g. 10/10/2022)                            |

In a new Python 3.10 virtual environment:
```shell
$ pip install -r ./requirements.txt
$ python -m papical ./your_amazon_data.csv
```

Sample output:
```
[LastOrderDate=2022-12-10] NumCommonUniqueItems=46, Laspeyres=6.8%, Paasche=6.6% Fisher=6.7%
[LastOrderDate=2022-12-09] NumCommonUniqueItems=45, Laspeyres=6.8%, Paasche=6.6% Fisher=6.7%
[LastOrderDate=2022-12-08] NumCommonUniqueItems=45, Laspeyres=6.8%, Paasche=6.5% Fisher=6.6%
[LastOrderDate=2022-12-07] NumCommonUniqueItems=46, Laspeyres=6.6%, Paasche=6.4% Fisher=6.5%
[LastOrderDate=2022-12-01] NumCommonUniqueItems=46, Laspeyres=6.2%, Paasche=6.4% Fisher=6.3%
[LastOrderDate=2022-11-28] NumCommonUniqueItems=46, Laspeyres=6.2%, Paasche=6.4% Fisher=6.3%
[LastOrderDate=2022-11-25] NumCommonUniqueItems=46, Laspeyres=6.3%, Paasche=6.6% Fisher=6.4%
[LastOrderDate=2022-11-21] NumCommonUniqueItems=46, Laspeyres=5.7%, Paasche=6.1% Fisher=5.9%
[LastOrderDate=2022-11-19] NumCommonUniqueItems=46, Laspeyres=5.5%, Paasche=5.4% Fisher=5.5%
[LastOrderDate=2022-11-18] NumCommonUniqueItems=46, Laspeyres=5.5%, Paasche=5.3% Fisher=5.4%
[LastOrderDate=2022-11-12] NumCommonUniqueItems=46, Laspeyres=5.5%, Paasche=5.2% Fisher=5.3%
[LastOrderDate=2022-11-07] NumCommonUniqueItems=46, Laspeyres=5.5%, Paasche=5.2% Fisher=5.3%
[LastOrderDate=2022-11-05] NumCommonUniqueItems=47, Laspeyres=5.5%, Paasche=5.9% Fisher=5.7%
[LastOrderDate=2022-10-30] NumCommonUniqueItems=47, Laspeyres=5.5%, Paasche=6.0% Fisher=5.7%
[LastOrderDate=2022-10-17] NumCommonUniqueItems=48, Laspeyres=5.9%, Paasche=6.1% Fisher=6.0%
```
