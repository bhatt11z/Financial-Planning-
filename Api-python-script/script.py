{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Unit 5 - Financial Planning"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 1 - Personal Finance Planner"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Intial Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import requests\n",
    "import pandas as pd\n",
    "from dotenv import load_dotenv\n",
    "import alpaca_trade_api as tradeapi\n",
    "from MCForecastTools import MCSimulation\n",
    "\n",
    "%matplotlib inline\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Crypto Prices"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_btc = 1.2\n",
    "my_eth = 5.3\n",
    "btc_url = \"https://api.alternative.me/v2/ticker/Bitcoin/?convert=CAD\"\n",
    "btc_url= btc_url + \"?format=json\"\n",
    "eth_url = \"https://api.alternative.me/v2/ticker/Ethereum/?convert=CAD\"\n",
    "eth_url= eth_url + \"?format=json\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Calling The Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'data': {'1': {'id': 1,\n",
       "   'name': 'Bitcoin',\n",
       "   'symbol': 'BTC',\n",
       "   'website_slug': 'bitcoin',\n",
       "   'rank': 1,\n",
       "   'circulating_supply': 18606912,\n",
       "   'total_supply': 18606912,\n",
       "   'max_supply': 21000000,\n",
       "   'quotes': {'USD': {'price': 30529.0,\n",
       "     'volume_24h': 78453958657,\n",
       "     'market_cap': 564452245338,\n",
       "     'percentage_change_1h': 3.185070595419,\n",
       "     'percentage_change_24h': -11.513682369327,\n",
       "     'percentage_change_7d': -22.1854328069371,\n",
       "     'percent_change_1h': 3.185070595419,\n",
       "     'percent_change_24h': -11.513682369327,\n",
       "     'percent_change_7d': -22.1854328069371}},\n",
       "   'last_updated': 1611282786}},\n",
       " 'metadata': {'timestamp': 1611282786,\n",
       "  'num_cryptocurrencies': 1383,\n",
       "  'error': None}}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "btc = requests.get(btc_url).json()\n",
    "btc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'data': {'1027': {'id': 1027,\n",
       "   'name': 'Ethereum',\n",
       "   'symbol': 'ETH',\n",
       "   'website_slug': 'ethereum',\n",
       "   'rank': 2,\n",
       "   'circulating_supply': 114350689,\n",
       "   'total_supply': 114350689,\n",
       "   'max_supply': 0,\n",
       "   'quotes': {'USD': {'price': 1138.62,\n",
       "     'volume_24h': 56043749421,\n",
       "     'market_cap': 130201609119,\n",
       "     'percentage_change_1h': 5.36324628531592,\n",
       "     'percentage_change_24h': -13.9275220548141,\n",
       "     'percentage_change_7d': -6.43414390986057,\n",
       "     'percent_change_1h': 5.36324628531592,\n",
       "     'percent_change_24h': -13.9275220548141,\n",
       "     'percent_change_7d': -6.43414390986057}},\n",
       "   'last_updated': 1611282625}},\n",
       " 'metadata': {'timestamp': 1611282625,\n",
       "  'num_cryptocurrencies': 1383,\n",
       "  'error': None}}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "eth = requests.get(eth_url).json()\n",
    "eth"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Computing Portfolio Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The current value of your 1.2 BTC is $36634.80\n",
      "The current value of your 5.3 ETH is $6034.69\n"
     ]
    }
   ],
   "source": [
    "eth_price = eth[\"data\"][\"1027\"][\"quotes\"][\"USD\"][\"price\"] * my_eth\n",
    "btc_price = btc[\"data\"][\"1\"][\"quotes\"][\"USD\"][\"price\"] * my_btc\n",
    "print(f\"The current value of your {my_btc} BTC is ${btc_price:0.2f}\")\n",
    "print(f\"The current value of your {my_eth} ETH is ${eth_price:0.2f}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Collecting Investments Data Using Alpaca: SPY (stocks) and AGG (bonds)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Setting Quantity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_agg = 200\n",
    "my_spy = 50"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Prepration for pulling data from Alpaca"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "api_key = os.getenv(\"alpaca_key\")\n",
    "api_seceret_key = os.getenv(\"alpaca_secert\")\n",
    "alpaca = tradeapi.REST(api_key,api_seceret_key, api_version= \"v2\")\n",
    "today = pd.Timestamp(\"2021-01-21\", tz=(\"America/New_york\")).isoformat()\n",
    "tickers = [\"AGG\", \"SPY\"]\n",
    "timeframe = \"1D\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Calling Data From Alpaca"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "portfolio = alpaca.get_barset(tickers,timeframe,start=today,end=today).df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Creating Variables From The Alpaca Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "spy_closing = portfolio[\"SPY\"][\"close\"].item()\n",
    "agg_closing = portfolio[\"AGG\"][\"close\"].item()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Computing The Portfolio Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " The current value of my 200 AGG shares is $23452.0\n",
      " The current value of my 50 SPY shares is $19210.0\n"
     ]
    }
   ],
   "source": [
    "my_spy_value = spy_closing*my_spy\n",
    "my_agg_value = agg_closing*my_agg\n",
    "print(f\" The current value of my {my_agg} AGG shares is ${my_agg_value}\")\n",
    "print(f\" The current value of my {my_spy} SPY shares is ${my_spy_value}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Savings Health Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "monthly_income = 12000"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Calculating Totals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_crypto = eth_price+btc_price\n",
    "total_share = my_agg_value+my_spy_value"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Creating Data Frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Crypto</th>\n",
       "      <td>42669.486</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Shares</th>\n",
       "      <td>42662.000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                0\n",
       "Crypto  42669.486\n",
       "Shares  42662.000"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "df_saving= pd.DataFrame([total_crypto,total_share],index=[\"Crypto\",\"Shares\"])\n",
    "df_saving"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_saving.rename(columns={0:\"Amount\"}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Amount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Crypto</th>\n",
       "      <td>42669.486</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Shares</th>\n",
       "      <td>42662.000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Amount\n",
       "Crypto  42669.486\n",
       "Shares  42662.000"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_saving"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Plotting Savings Pie Chart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([<AxesSubplot:ylabel='Amount'>], dtype=object)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_saving.plot(kind =\"pie\",subplots=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Analyzing Savings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Congratulations! You have enough money in your emergency fund\n"
     ]
    }
   ],
   "source": [
    "emergency_fund = monthly_income * 3\n",
    "total_saving = total_crypto+total_share\n",
    "if total_saving > emergency_fund:\n",
    "    print(\"Congratulations! You have enough money in your emergency fund\")\n",
    "elif total_saving == emergency_fund:\n",
    "    print(\"Congratulations! on reaching your financial goal\")\n",
    "elif total_saving < emergency_fund:\n",
    "    print((emergency_fund-total_saving), \"dollars away from your goal\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 2 - Retirement Planning"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Monte Carlo Simulation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Preparing Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>AGG</th>\n",
       "      <th>SPY</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2015-01-21</th>\n",
       "      <td>111.5000</td>\n",
       "      <td>203.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-22</th>\n",
       "      <td>111.4299</td>\n",
       "      <td>206.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-23</th>\n",
       "      <td>111.7400</td>\n",
       "      <td>204.95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-26</th>\n",
       "      <td>111.6500</td>\n",
       "      <td>205.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-27</th>\n",
       "      <td>111.6300</td>\n",
       "      <td>202.75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 AGG     SPY\n",
       "2015-01-21  111.5000  203.09\n",
       "2015-01-22  111.4299  206.09\n",
       "2015-01-23  111.7400  204.95\n",
       "2015-01-26  111.6500  205.46\n",
       "2015-01-27  111.6300  202.75"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "start_date = pd.Timestamp('2015-01-21', tz='America/New_York').isoformat()\n",
    "end_date = pd.Timestamp('2020-01-21', tz='America/New_York').isoformat()\n",
    "portfolio_data = alpaca.get_barset(tickers,timeframe,start=start_date,end=end_date).df\n",
    "historical_data = pd.DataFrame()\n",
    "historical_data[\"AGG\"]= portfolio_data[\"AGG\"][\"close\"]\n",
    "historical_data[\"SPY\"]= portfolio_data[\"SPY\"][\"close\"]\n",
    "historical_data.index = historical_data.index.date\n",
    "historical_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Setting Simulation Instance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th colspan=\"6\" halign=\"left\">AGG</th>\n",
       "      <th colspan=\"6\" halign=\"left\">SPY</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>open</th>\n",
       "      <th>high</th>\n",
       "      <th>low</th>\n",
       "      <th>close</th>\n",
       "      <th>volume</th>\n",
       "      <th>daily_return</th>\n",
       "      <th>open</th>\n",
       "      <th>high</th>\n",
       "      <th>low</th>\n",
       "      <th>close</th>\n",
       "      <th>volume</th>\n",
       "      <th>daily_return</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>time</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2015-01-21 00:00:00-05:00</th>\n",
       "      <td>111.68</td>\n",
       "      <td>111.81</td>\n",
       "      <td>111.3901</td>\n",
       "      <td>111.5000</td>\n",
       "      <td>1916736</td>\n",
       "      <td>NaN</td>\n",
       "      <td>201.50</td>\n",
       "      <td>203.66</td>\n",
       "      <td>200.94</td>\n",
       "      <td>203.09</td>\n",
       "      <td>106170094</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-22 00:00:00-05:00</th>\n",
       "      <td>111.72</td>\n",
       "      <td>111.72</td>\n",
       "      <td>111.2900</td>\n",
       "      <td>111.4299</td>\n",
       "      <td>1868700</td>\n",
       "      <td>-0.000629</td>\n",
       "      <td>203.99</td>\n",
       "      <td>206.26</td>\n",
       "      <td>202.33</td>\n",
       "      <td>206.09</td>\n",
       "      <td>124570218</td>\n",
       "      <td>0.014772</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-23 00:00:00-05:00</th>\n",
       "      <td>111.65</td>\n",
       "      <td>111.81</td>\n",
       "      <td>111.5400</td>\n",
       "      <td>111.7400</td>\n",
       "      <td>1449774</td>\n",
       "      <td>0.002783</td>\n",
       "      <td>205.79</td>\n",
       "      <td>206.10</td>\n",
       "      <td>204.81</td>\n",
       "      <td>204.95</td>\n",
       "      <td>90576108</td>\n",
       "      <td>-0.005532</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-26 00:00:00-05:00</th>\n",
       "      <td>111.79</td>\n",
       "      <td>111.79</td>\n",
       "      <td>111.4500</td>\n",
       "      <td>111.6500</td>\n",
       "      <td>2477962</td>\n",
       "      <td>-0.000805</td>\n",
       "      <td>204.71</td>\n",
       "      <td>205.56</td>\n",
       "      <td>203.85</td>\n",
       "      <td>205.46</td>\n",
       "      <td>71274935</td>\n",
       "      <td>0.002488</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-27 00:00:00-05:00</th>\n",
       "      <td>111.97</td>\n",
       "      <td>111.97</td>\n",
       "      <td>111.5450</td>\n",
       "      <td>111.6300</td>\n",
       "      <td>1538783</td>\n",
       "      <td>-0.000179</td>\n",
       "      <td>202.97</td>\n",
       "      <td>204.12</td>\n",
       "      <td>201.74</td>\n",
       "      <td>202.75</td>\n",
       "      <td>109506387</td>\n",
       "      <td>-0.013190</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              AGG                                       \\\n",
       "                             open    high       low     close   volume   \n",
       "time                                                                     \n",
       "2015-01-21 00:00:00-05:00  111.68  111.81  111.3901  111.5000  1916736   \n",
       "2015-01-22 00:00:00-05:00  111.72  111.72  111.2900  111.4299  1868700   \n",
       "2015-01-23 00:00:00-05:00  111.65  111.81  111.5400  111.7400  1449774   \n",
       "2015-01-26 00:00:00-05:00  111.79  111.79  111.4500  111.6500  2477962   \n",
       "2015-01-27 00:00:00-05:00  111.97  111.97  111.5450  111.6300  1538783   \n",
       "\n",
       "                                           SPY                          \\\n",
       "                          daily_return    open    high     low   close   \n",
       "time                                                                     \n",
       "2015-01-21 00:00:00-05:00          NaN  201.50  203.66  200.94  203.09   \n",
       "2015-01-22 00:00:00-05:00    -0.000629  203.99  206.26  202.33  206.09   \n",
       "2015-01-23 00:00:00-05:00     0.002783  205.79  206.10  204.81  204.95   \n",
       "2015-01-26 00:00:00-05:00    -0.000805  204.71  205.56  203.85  205.46   \n",
       "2015-01-27 00:00:00-05:00    -0.000179  202.97  204.12  201.74  202.75   \n",
       "\n",
       "                                                   \n",
       "                              volume daily_return  \n",
       "time                                               \n",
       "2015-01-21 00:00:00-05:00  106170094          NaN  \n",
       "2015-01-22 00:00:00-05:00  124570218     0.014772  \n",
       "2015-01-23 00:00:00-05:00   90576108    -0.005532  \n",
       "2015-01-26 00:00:00-05:00   71274935     0.002488  \n",
       "2015-01-27 00:00:00-05:00  109506387    -0.013190  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mc_fiveyear = MCSimulation(portfolio_data=portfolio_data,weights=[0.4,0.60],num_simulation=500,num_trading_days=7560)\n",
    "mc_fiveyear.portfolio_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Running Simulation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running Monte Carlo simulation number 0.\n",
      "Running Monte Carlo simulation number 10.\n",
      "Running Monte Carlo simulation number 20.\n",
      "Running Monte Carlo simulation number 30.\n",
      "Running Monte Carlo simulation number 40.\n",
      "Running Monte Carlo simulation number 50.\n",
      "Running Monte Carlo simulation number 60.\n",
      "Running Monte Carlo simulation number 70.\n",
      "Running Monte Carlo simulation number 80.\n",
      "Running Monte Carlo simulation number 90.\n",
      "Running Monte Carlo simulation number 100.\n",
      "Running Monte Carlo simulation number 110.\n",
      "Running Monte Carlo simulation number 120.\n",
      "Running Monte Carlo simulation number 130.\n",
      "Running Monte Carlo simulation number 140.\n",
      "Running Monte Carlo simulation number 150.\n",
      "Running Monte Carlo simulation number 160.\n",
      "Running Monte Carlo simulation number 170.\n",
      "Running Monte Carlo simulation number 180.\n",
      "Running Monte Carlo simulation number 190.\n",
      "Running Monte Carlo simulation number 200.\n",
      "Running Monte Carlo simulation number 210.\n",
      "Running Monte Carlo simulation number 220.\n",
      "Running Monte Carlo simulation number 230.\n",
      "Running Monte Carlo simulation number 240.\n",
      "Running Monte Carlo simulation number 250.\n",
      "Running Monte Carlo simulation number 260.\n",
      "Running Monte Carlo simulation number 270.\n",
      "Running Monte Carlo simulation number 280.\n",
      "Running Monte Carlo simulation number 290.\n",
      "Running Monte Carlo simulation number 300.\n",
      "Running Monte Carlo simulation number 310.\n",
      "Running Monte Carlo simulation number 320.\n",
      "Running Monte Carlo simulation number 330.\n",
      "Running Monte Carlo simulation number 340.\n",
      "Running Monte Carlo simulation number 350.\n",
      "Running Monte Carlo simulation number 360.\n",
      "Running Monte Carlo simulation number 370.\n",
      "Running Monte Carlo simulation number 380.\n",
      "Running Monte Carlo simulation number 390.\n",
      "Running Monte Carlo simulation number 400.\n",
      "Running Monte Carlo simulation number 410.\n",
      "Running Monte Carlo simulation number 420.\n",
      "Running Monte Carlo simulation number 430.\n",
      "Running Monte Carlo simulation number 440.\n",
      "Running Monte Carlo simulation number 450.\n",
      "Running Monte Carlo simulation number 460.\n",
      "Running Monte Carlo simulation number 470.\n",
      "Running Monte Carlo simulation number 480.\n",
      "Running Monte Carlo simulation number 490.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>...</th>\n",
       "      <th>490</th>\n",
       "      <th>491</th>\n",
       "      <th>492</th>\n",
       "      <th>493</th>\n",
       "      <th>494</th>\n",
       "      <th>495</th>\n",
       "      <th>496</th>\n",
       "      <th>497</th>\n",
       "      <th>498</th>\n",
       "      <th>499</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.002651</td>\n",
       "      <td>0.999971</td>\n",
       "      <td>0.999226</td>\n",
       "      <td>1.001194</td>\n",
       "      <td>1.002751</td>\n",
       "      <td>1.000957</td>\n",
       "      <td>0.999336</td>\n",
       "      <td>0.992799</td>\n",
       "      <td>1.002662</td>\n",
       "      <td>1.006806</td>\n",
       "      <td>...</td>\n",
       "      <td>1.007684</td>\n",
       "      <td>0.997199</td>\n",
       "      <td>1.000901</td>\n",
       "      <td>1.008772</td>\n",
       "      <td>1.000370</td>\n",
       "      <td>0.993287</td>\n",
       "      <td>1.003120</td>\n",
       "      <td>1.000727</td>\n",
       "      <td>1.004612</td>\n",
       "      <td>0.989748</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.006892</td>\n",
       "      <td>1.004339</td>\n",
       "      <td>1.004026</td>\n",
       "      <td>0.991777</td>\n",
       "      <td>1.005162</td>\n",
       "      <td>1.000348</td>\n",
       "      <td>1.006071</td>\n",
       "      <td>0.997772</td>\n",
       "      <td>1.000252</td>\n",
       "      <td>1.011607</td>\n",
       "      <td>...</td>\n",
       "      <td>1.007068</td>\n",
       "      <td>0.992569</td>\n",
       "      <td>1.004503</td>\n",
       "      <td>1.012251</td>\n",
       "      <td>1.008841</td>\n",
       "      <td>1.002550</td>\n",
       "      <td>1.001028</td>\n",
       "      <td>1.007845</td>\n",
       "      <td>1.012897</td>\n",
       "      <td>0.982142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.002125</td>\n",
       "      <td>1.005588</td>\n",
       "      <td>1.013729</td>\n",
       "      <td>0.999245</td>\n",
       "      <td>1.007031</td>\n",
       "      <td>1.001894</td>\n",
       "      <td>0.992664</td>\n",
       "      <td>1.000224</td>\n",
       "      <td>1.002818</td>\n",
       "      <td>1.008909</td>\n",
       "      <td>...</td>\n",
       "      <td>1.005248</td>\n",
       "      <td>0.983301</td>\n",
       "      <td>1.004465</td>\n",
       "      <td>1.014404</td>\n",
       "      <td>1.011478</td>\n",
       "      <td>0.997485</td>\n",
       "      <td>0.999594</td>\n",
       "      <td>1.008023</td>\n",
       "      <td>1.016619</td>\n",
       "      <td>0.981247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.004688</td>\n",
       "      <td>1.010948</td>\n",
       "      <td>1.011948</td>\n",
       "      <td>0.995236</td>\n",
       "      <td>1.009160</td>\n",
       "      <td>1.007684</td>\n",
       "      <td>0.991656</td>\n",
       "      <td>1.009666</td>\n",
       "      <td>1.001161</td>\n",
       "      <td>1.007102</td>\n",
       "      <td>...</td>\n",
       "      <td>0.997536</td>\n",
       "      <td>0.989042</td>\n",
       "      <td>0.998093</td>\n",
       "      <td>1.014471</td>\n",
       "      <td>1.013414</td>\n",
       "      <td>0.992796</td>\n",
       "      <td>0.997132</td>\n",
       "      <td>0.996992</td>\n",
       "      <td>1.013003</td>\n",
       "      <td>0.980820</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7556</th>\n",
       "      <td>7.418559</td>\n",
       "      <td>11.752105</td>\n",
       "      <td>6.290841</td>\n",
       "      <td>4.291647</td>\n",
       "      <td>5.853081</td>\n",
       "      <td>3.100268</td>\n",
       "      <td>5.755271</td>\n",
       "      <td>3.949272</td>\n",
       "      <td>11.824760</td>\n",
       "      <td>4.405770</td>\n",
       "      <td>...</td>\n",
       "      <td>5.249553</td>\n",
       "      <td>7.402719</td>\n",
       "      <td>7.592062</td>\n",
       "      <td>11.902620</td>\n",
       "      <td>6.244765</td>\n",
       "      <td>4.149217</td>\n",
       "      <td>8.005816</td>\n",
       "      <td>8.443989</td>\n",
       "      <td>5.392952</td>\n",
       "      <td>8.797962</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7557</th>\n",
       "      <td>7.408352</td>\n",
       "      <td>11.786283</td>\n",
       "      <td>6.307754</td>\n",
       "      <td>4.275844</td>\n",
       "      <td>5.821141</td>\n",
       "      <td>3.106492</td>\n",
       "      <td>5.787873</td>\n",
       "      <td>3.923032</td>\n",
       "      <td>11.765497</td>\n",
       "      <td>4.413355</td>\n",
       "      <td>...</td>\n",
       "      <td>5.244249</td>\n",
       "      <td>7.444708</td>\n",
       "      <td>7.541860</td>\n",
       "      <td>11.800228</td>\n",
       "      <td>6.292859</td>\n",
       "      <td>4.126502</td>\n",
       "      <td>7.975437</td>\n",
       "      <td>8.404385</td>\n",
       "      <td>5.375155</td>\n",
       "      <td>8.692242</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7558</th>\n",
       "      <td>7.385741</td>\n",
       "      <td>11.885504</td>\n",
       "      <td>6.313652</td>\n",
       "      <td>4.260976</td>\n",
       "      <td>5.828155</td>\n",
       "      <td>3.107016</td>\n",
       "      <td>5.801991</td>\n",
       "      <td>3.922754</td>\n",
       "      <td>11.823634</td>\n",
       "      <td>4.422064</td>\n",
       "      <td>...</td>\n",
       "      <td>5.245254</td>\n",
       "      <td>7.397911</td>\n",
       "      <td>7.650701</td>\n",
       "      <td>11.917651</td>\n",
       "      <td>6.301537</td>\n",
       "      <td>4.137200</td>\n",
       "      <td>7.928786</td>\n",
       "      <td>8.434043</td>\n",
       "      <td>5.421813</td>\n",
       "      <td>8.712148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7559</th>\n",
       "      <td>7.460555</td>\n",
       "      <td>11.860012</td>\n",
       "      <td>6.311994</td>\n",
       "      <td>4.263848</td>\n",
       "      <td>5.776743</td>\n",
       "      <td>3.112333</td>\n",
       "      <td>5.816586</td>\n",
       "      <td>3.969481</td>\n",
       "      <td>11.858775</td>\n",
       "      <td>4.430715</td>\n",
       "      <td>...</td>\n",
       "      <td>5.232884</td>\n",
       "      <td>7.436138</td>\n",
       "      <td>7.693239</td>\n",
       "      <td>11.919641</td>\n",
       "      <td>6.323591</td>\n",
       "      <td>4.091721</td>\n",
       "      <td>7.872142</td>\n",
       "      <td>8.411054</td>\n",
       "      <td>5.459841</td>\n",
       "      <td>8.649426</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7560</th>\n",
       "      <td>7.422073</td>\n",
       "      <td>11.815060</td>\n",
       "      <td>6.399582</td>\n",
       "      <td>4.282536</td>\n",
       "      <td>5.789170</td>\n",
       "      <td>3.103318</td>\n",
       "      <td>5.862042</td>\n",
       "      <td>3.951757</td>\n",
       "      <td>11.838512</td>\n",
       "      <td>4.410340</td>\n",
       "      <td>...</td>\n",
       "      <td>5.221167</td>\n",
       "      <td>7.423868</td>\n",
       "      <td>7.671287</td>\n",
       "      <td>11.910675</td>\n",
       "      <td>6.312420</td>\n",
       "      <td>4.118003</td>\n",
       "      <td>7.843967</td>\n",
       "      <td>8.364926</td>\n",
       "      <td>5.452879</td>\n",
       "      <td>8.575948</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>7561 rows × 500 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           0          1         2         3         4         5         6    \\\n",
       "0     1.000000   1.000000  1.000000  1.000000  1.000000  1.000000  1.000000   \n",
       "1     1.002651   0.999971  0.999226  1.001194  1.002751  1.000957  0.999336   \n",
       "2     1.006892   1.004339  1.004026  0.991777  1.005162  1.000348  1.006071   \n",
       "3     1.002125   1.005588  1.013729  0.999245  1.007031  1.001894  0.992664   \n",
       "4     1.004688   1.010948  1.011948  0.995236  1.009160  1.007684  0.991656   \n",
       "...        ...        ...       ...       ...       ...       ...       ...   \n",
       "7556  7.418559  11.752105  6.290841  4.291647  5.853081  3.100268  5.755271   \n",
       "7557  7.408352  11.786283  6.307754  4.275844  5.821141  3.106492  5.787873   \n",
       "7558  7.385741  11.885504  6.313652  4.260976  5.828155  3.107016  5.801991   \n",
       "7559  7.460555  11.860012  6.311994  4.263848  5.776743  3.112333  5.816586   \n",
       "7560  7.422073  11.815060  6.399582  4.282536  5.789170  3.103318  5.862042   \n",
       "\n",
       "           7          8         9    ...       490       491       492  \\\n",
       "0     1.000000   1.000000  1.000000  ...  1.000000  1.000000  1.000000   \n",
       "1     0.992799   1.002662  1.006806  ...  1.007684  0.997199  1.000901   \n",
       "2     0.997772   1.000252  1.011607  ...  1.007068  0.992569  1.004503   \n",
       "3     1.000224   1.002818  1.008909  ...  1.005248  0.983301  1.004465   \n",
       "4     1.009666   1.001161  1.007102  ...  0.997536  0.989042  0.998093   \n",
       "...        ...        ...       ...  ...       ...       ...       ...   \n",
       "7556  3.949272  11.824760  4.405770  ...  5.249553  7.402719  7.592062   \n",
       "7557  3.923032  11.765497  4.413355  ...  5.244249  7.444708  7.541860   \n",
       "7558  3.922754  11.823634  4.422064  ...  5.245254  7.397911  7.650701   \n",
       "7559  3.969481  11.858775  4.430715  ...  5.232884  7.436138  7.693239   \n",
       "7560  3.951757  11.838512  4.410340  ...  5.221167  7.423868  7.671287   \n",
       "\n",
       "            493       494       495       496       497       498       499  \n",
       "0      1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  \n",
       "1      1.008772  1.000370  0.993287  1.003120  1.000727  1.004612  0.989748  \n",
       "2      1.012251  1.008841  1.002550  1.001028  1.007845  1.012897  0.982142  \n",
       "3      1.014404  1.011478  0.997485  0.999594  1.008023  1.016619  0.981247  \n",
       "4      1.014471  1.013414  0.992796  0.997132  0.996992  1.013003  0.980820  \n",
       "...         ...       ...       ...       ...       ...       ...       ...  \n",
       "7556  11.902620  6.244765  4.149217  8.005816  8.443989  5.392952  8.797962  \n",
       "7557  11.800228  6.292859  4.126502  7.975437  8.404385  5.375155  8.692242  \n",
       "7558  11.917651  6.301537  4.137200  7.928786  8.434043  5.421813  8.712148  \n",
       "7559  11.919641  6.323591  4.091721  7.872142  8.411054  5.459841  8.649426  \n",
       "7560  11.910675  6.312420  4.118003  7.843967  8.364926  5.452879  8.575948  \n",
       "\n",
       "[7561 rows x 500 columns]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mc_fiveyear.calc_cumulative_return()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Plotting Simulation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "line_plot = mc_fiveyear.plot_simulation()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dist_plot = mc_fiveyear.plot_distribution()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Retirement Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Summary Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count           500.000000\n",
       "mean              7.228404\n",
       "std               3.207443\n",
       "min               1.539472\n",
       "25%               4.886978\n",
       "50%               6.623664\n",
       "75%               8.994072\n",
       "max              21.589846\n",
       "95% CI Lower      2.826616\n",
       "95% CI Upper     15.755638\n",
       "Name: 7560, dtype: float64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary = mc_fiveyear.summarize_cumulative_return()\n",
    "summary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Calculating Returns Based On 20K Investment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There is a 95% chance that an initial investment of $20000 in the portfolio over the next 30 years will end within in the range of $56532.32 and $315112.76\n"
     ]
    }
   ],
   "source": [
    "initial_investment = 20000\n",
    "ci_lower = round(summary[8]*initial_investment,2)\n",
    "ci_upper = round(summary[9]*initial_investment,2)\n",
    "print(f\"There is a 95% chance that an initial investment of ${initial_investment} in the portfolio\"\n",
    "      f\" over the next 30 years will end within in the range of\"\n",
    "      f\" ${ci_lower} and ${ci_upper}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Calculating Returns Based On 30K Investment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There is a 95% chance that an initial investment of $30000.0 in the portfolio over the next 30 years will end within in the range of $84798.49 and $472669.13\n"
     ]
    }
   ],
   "source": [
    "initials_investment = 20000 * 1.5\n",
    "ci_lowers = round(summary[8]*initials_investment,2)\n",
    "ci_uppers = round(summary[9]*initials_investment,2)\n",
    "print(f\"There is a 95% chance that an initial investment of ${initials_investment} in the portfolio\"\n",
    "      f\" over the next 30 years will end within in the range of\"\n",
    "      f\" ${ci_lowers} and ${ci_uppers}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:dev]",
   "language": "python",
   "name": "conda-env-dev-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
