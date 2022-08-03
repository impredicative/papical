# papi
**papi** (Personal Amazon Price Inflation) computes the running annual price inflation percentage using the [Laspereyes](https://en.wikipedia.org/w/index.php?title=List_of_price_index_formulas&oldid=1077502962#Laspeyres) formula. Using it meaningfully requires a substantial order history on Amazon over a long period. This software is not associated with Amazon.

## Usage

Download the CSV of your [order history]((https://www.amazon.com/b2b/reports)) using these parameters:
- Report Type: Items
- Start Date: 01/01/2006
- End Date: (today's date, e.g. 07/14/2022)

In a new Python 3.10 virtual environment:
```shell
pip install -r ./requirements.txt
python -m papi.papi ./your_data.csv
```