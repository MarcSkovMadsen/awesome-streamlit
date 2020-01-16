"""
## YahooQuery Demo

This app allows you to demo the yahooquery python package

Author: [Doug Guthrie](https://github/dpguthrie))\n
Source: [Github](https://github.com/dpguthrie/yahooquery)
Credits: [Marc Skov Madsen](https://datamodelsanalytics.com)
"""
import datetime
from typing import Dict, List

import altair as alt
import pandas as pd
import streamlit as st
from yahooquery import Ticker

BASE_ENDPOINTS = {
    "asset_profile": "Asset Profile",
    "calendar_events": "Calendar Events",
    "esg_scores": "ESG Scores",
    "financial_data": "Financial Data",
    "fund_profile": "Fund Profile",
    "key_stats": "Key Statistics",
    "major_holders": "Major Holders",
    "price": "Pricing",
    "quote_type": "Quote Type",
    "share_purchase_activity": "Share Purchase Activity",
    "summary_detail": "Summary Detail",
    "summary_profile": "Summary Profile",
    "balance_sheet": "Balance Sheet",
    "cash_flow": "Cash Flow",
    "company_officers": "Company Officers",
    "earning_history": "Earning History",
    "fund_ownership": "Fund Ownership",
    "grading_history": "Grading History",
    "income_statement": "Income Statement",
    "insider_holders": "Insider Holders",
    "insider_transactions": "Insider Transactions",
    "institution_ownership": "Institution Ownership",
    "recommendation_trend": "Recommendation Trends",
    "sec_filings": "SEC Filings",
    "fund_bond_holdings": "Fund Bond Holdings",
    "fund_bond_ratings": "Fund Bond Ratings",
    "fund_equity_holdings": "Fund Equity Holdings",
    "fund_holding_info": "Fund Holding Information",
    "fund_performance": "Fund Performance",
    "fund_sector_weightings": "Fund Sector Weightings",
    "fund_top_holdings": "Fund Top Holdings",
}

def get_default_format(data: pd.DataFrame) -> Dict[str, str]:
    """A dictionary of columns and formats for the Pandas DataFrame Styler

    Arguments:
        data {pd.DataFrame} -- A DataFrame of Data]

    Returns:
        Dict[str,str] -- A dictionary of default formats for the columns
    """
    format_dict = {}
    for column in data.columns:
        if data[column].dtype == "int64":
            format_dict[column] = "{0:,.0f}"
        elif data[column].dtype == "float64":
            format_dict[column] = "{0:,.2f}"
        else:
            format_dict[column] = "{0:}"
    return format_dict

def format_func(option: str) -> str:
    """Convert the BASE_ENDPOINTS key to a value

    Arguments:
        option {str} -- The key identifying the endpoint.

    Returns:
        str -- The value. A nice endpoint name
    """
    return BASE_ENDPOINTS[option]


@st.cache
def get_data(ticker: Ticker, attribute: str, *args) -> Dict:
    """Gets data from yahoo

    Arguments:
        ticker {Ticker} -- an instance of Ticker
        attribute {str} -- The attribute of Ticker to call. Will return the results of a call to
            corresponding yahoo finance endpoint.

    Returns:
        Dict -- A Dictionary of data from Yahoo
    """
    try:
        data = getattr(ticker, attribute)(*args)
    except TypeError:
        data = getattr(ticker, attribute)
    return data


def main():
    """Run this to run the application"""
    st.sidebar.subheader("YahooQuery")
    symbols = st.sidebar.text_input(
        "Enter symbol or list of symbols (comma separated)", value="aapl"
    )
    symbols = [x.strip() for x in symbols.split(",")]
    tickers = Ticker(symbols)

    page = st.sidebar.selectbox(
        "Choose a page", ["Homepage", "Base", "Base - Multiple", "Options", "Historical Pricing"]
    )

    st.markdown("# Welcome to [YahooQuery](https://github.com/dpguthrie/yahooquery)")

    if page == "Homepage":
        homepage_view(tickers, symbols)
    elif page == "Base":
        base_view(tickers, symbols)
    elif page == "Base - Multiple":
        base_multiple_view(tickers, symbols)
    elif page == "Options":
        options_view(tickers, symbols)
    else:
        history_view(tickers, symbols)

# Ideas for Improvements
# An image or video to catch the attention of the user and communicate what this is.
# Maybe a Yahoo logo, maybe a small gif video or youtube video. Maybe a price chart.
def homepage_view(tickers: Ticker, symbols: List[str]):
    """Provides the view of the Home Page

    Arguments:
        tickers {Ticker} -- A yahaooquery Ticker object
        symbols {List[str]} -- A list of symbols
    """

    st.markdown(
        f"""
        This app demonstrates the use of the [YahooQuery]\
            (https://github.com/dpguthrie/yahooquery) package

        ### Instructions

        Enter a symbol or list of symbols in the box to the left (**comma
        separated**).  Then select different pages in the dropdown to view
        the data available to you.

        ### Installation

        ```python
        pip install yahooquery
        ```

        ### Ticker Usage

        The `Ticker` class provides the access point to data residing on
        Yahoo Finance.  It accepts either a symbol or list of symbols.
        Additionally, you can supply `formatted` as a keyword argument
        to the class to format the data returned from the API (default is
        `True`)

        ```python
        from yahooquery import Ticker

        tickers = Ticker({symbols})
        ```
    """
    )
    st.help(tickers)


def base_view(tickers: Ticker, symbols: List[str]):
    """A view of the basic functionality of Ticker.

    The user can select an endpoint and the help text, code and result will be presented.

    Arguments:
        tickers {Ticker} -- A yahaooquery Ticker object
        symbols {List[str]} -- A list of symbols
    """

    st.header("Base Endpoints")
    st.write(
        """
        Select an option below to see the data available through
        the base endpoints."""
    )
    endpoint = st.selectbox(
        "Select Endpoint", options=sorted(list(BASE_ENDPOINTS.keys())), format_func=format_func
    )
    st.help(getattr(Ticker, endpoint))
    is_property = isinstance(getattr(Ticker, endpoint), property)
    if is_property:
        st.code(f"Ticker('{symbols}').{endpoint}", language="python")
        data = get_data(tickers, endpoint)
    else:
        frequency = st.selectbox("Select Frequency", options=["Annual", "Quarterly"])
        arg = frequency[:1].lower()
        st.code(f"Ticker('{symbols}').{endpoint}(frequency='{arg}')")
        data = get_data(tickers, endpoint, arg)

    if isinstance(data, pd.DataFrame):
        data = data.reset_index(drop=True) # Hack - Otherwise we get error
        format_dict = get_default_format(data)
        st.dataframe(data.style.format(format_dict))
    else:
        st.json(data)

def base_multiple_view(tickers: Ticker, symbols: List[str]):
    """A view for multiple Ticker requests

    The user can select all or multiple endpoints and the help text, code and result will be 
    presented.

    Arguments:
        tickers {Ticker} -- A yahaooquery Ticker object
        symbols {List[str]} -- A list of symbols
    """

    st.header("Base Endpoints - Multiple")
    st.markdown(
        """
        Two methods to the `Ticker` class allow you to obtain multiple
        endpoints with one call.

        - the `get_endpoints` method takes a list
        of allowable endpoints, which you can view through `Ticker._ENDPOINTS`
        - the `all_endpoints` property retrieves all Base endpoints"""
    )
    method = st.selectbox("Select Method", options=["All Endpoints", "Multiple Endpoints"], index=1)
    if method == "All Endpoints":
        st.help(getattr(Ticker, "all_endpoints"))
        st.code(f"Ticker({symbols}).all_endpoints", language="python")
        data = get_data(tickers, "all_endpoints")
        st.json(data)
    else:

        default_endpoints = ["assetProfile"]
        endpoints = st.multiselect(
            "Select endpoints",
            options=sorted(Ticker._ENDPOINTS),  # pylint: disable=protected-access
            default=default_endpoints,
        )
        st.help(getattr(Ticker, "get_endpoints"))
        st.code(f"Ticker({symbols}).get_endpoints({endpoints})", language="python")
        if not endpoints:
            st.warning("You must select at least one endpoint")
        else:
            data = get_data(tickers, "get_endpoints")(endpoints)
            st.json(data)


# Ideas for Improvements
# Reset index to get column headers
# Buttons under Table to download data
# Some kind of chart that helps me understand the data/ get insights.
def options_view(tickers: Ticker, symbols: List[str]):
    """Provides an illustration of the `option_chain` method

    Arguments:
        tickers {Ticker} -- A yahaooquery Ticker object
        symbols {List[str]} -- A list of symbols
    """
    st.header("Option Chain")
    st.write(
        """
        Yahooquery also gives you the ability to view [option chain]\
            (https://www.investopedia.com/terms/o/optionchain.asp) data for all expiration
            dates for a given symbol(s)
    """
    )
    st.help(getattr(Ticker, "option_chain"))
    st.code(f"Ticker({symbols}).option_chain", language="python")
    data = get_data(tickers, "option_chain")
    st.dataframe(data)


def history_view(tickers: Ticker, symbols: List[str]):
    """Provides an illustration of the `Ticker.history` method

    Arguments:
        tickers {Ticker} -- A yahaooquery Ticker object
        symbols {List[str]} -- A list of symbols
    """
    st.header("Historical Pricing")
    st.write(
        """
        Retrieve historical pricing data for a given symbol(s)
    """
    )
    st.help(getattr(Ticker, "history"))
    st.markdown(
        """
        1. Select a period **or** enter start and end dates.
        2. Select interval (**note:  some intervals are not available for
            certain lengths of time**)
    """
    )
    history_args = {
        "period": "1y",
        "interval": "1d",
        "start": datetime.datetime.now() - datetime.timedelta(days=365),
        "end": None,
    }
    option_1 = st.selectbox("Select Period or Start / End Dates", ["Period", "Dates"], 0)
    if option_1 == "Period":
        history_args["period"] = st.selectbox(
            "Select Period", options=Ticker._PERIODS, index=5  # pylint: disable=protected-access
        )

        history_args["start"] = None
        history_args["end"] = None
    else:
        history_args["start"] = st.date_input("Select Start Date", value=history_args["start"])
        history_args["end"] = st.date_input("Select End Date")
        history_args["period"] = None

    st.markdown("**THEN**")
    history_args["interval"] = st.selectbox(
        "Select Interval", options=Ticker._INTERVALS, index=8  # pylint: disable=protected-access
    )
    args_string = [str(k) + "='" + str(v) + "'" for k, v in history_args.items() if v is not None]
    st.code(f"Ticker({symbols}).history({', '.join(args_string)})", language="python")
    dataframe = tickers.history(**history_args)

    if isinstance(dataframe, dict):
        st.write(dataframe)
    else:
        if len(symbols) > 1:
            chart = (
                alt.Chart(dataframe.reset_index())
                .mark_line()
                .encode(alt.Y("close:Q", scale=alt.Scale(zero=False)), x="dates", color="symbol")
            )
        else:
            chart = (
                alt.Chart(dataframe.reset_index())
                .mark_line()
                .encode(alt.Y("close:Q", scale=alt.Scale(zero=False)), x="dates:T")
            )
        st.write("", "", chart)
        st.dataframe(dataframe)


main()
