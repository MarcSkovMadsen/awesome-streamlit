"""
## YahooQuery Demo

This app allows you to demo the yahooquery python package

Author: [Doug Guthrie](https://github/dpguthrie))\n
Source: [Github](https://github.com/dpguthrie/yahooquery)
"""
import streamlit as st

import altair as alt
from yahooquery import Ticker
import datetime


BASE_ENDPOINTS = {
    'asset_profile': 'Asset Profile',
    'calendar_events': 'Calendar Events',
    'esg_scores': 'ESG Scores',
    'financial_data': 'Financial Data',
    'fund_profile': 'Fund Profile',
    'key_stats': 'Key Statistics',
    'major_holders': 'Major Holders',
    'price': 'Pricing',
    'quote_type': 'Quote Type',
    'share_purchase_activity': 'Share Purchase Activity',
    'summary_detail': 'Summary Detail',
    'summary_profile': 'Summary Profile',
    'balance_sheet': 'Balance Sheet',
    'cash_flow': 'Cash Flow',
    'company_officers': 'Company Officers',
    'earning_history': 'Earning History',
    'fund_ownership': 'Fund Ownership',
    'grading_history': 'Grading History',
    'income_statement': 'Income Statement',
    'insider_holders': 'Insider Holders',
    'insider_transactions': 'Insider Transactions',
    'institution_ownership': 'Institution Ownership',
    'recommendation_trend': 'Recommendation Trends',
    'sec_filings': 'SEC Filings',
    'fund_bond_holdings': 'Fund Bond Holdings',
    'fund_bond_ratings': 'Fund Bond Ratings',
    'fund_equity_holdings': 'Fund Equity Holdings',
    'fund_holding_info': 'Fund Holding Information',
    'fund_performance': 'Fund Performance',
    'fund_sector_weightings': 'Fund Sector Weightings',
    'fund_top_holdings': 'Fund Top Holdings',
}

def format_func(option):
    return BASE_ENDPOINTS[option]


@st.cache
def get_data(ticker, attribute, *args):
    try:
        data = getattr(ticker, attribute)(*args)
    except TypeError:
        data = getattr(ticker, attribute)
    return data


def main():
    symbols = st.sidebar.text_input(
        "Enter symbol or list of symbols (comma separated)", value="aapl")
    symbols = [x.strip() for x in symbols.split(',')]
    tickers = Ticker(symbols)

    page = st.sidebar.selectbox("Choose a page", [
        "Homepage", "Base", "Base - Multiple", "Options", "Historical Pricing"])

    history_args = {
        'period': '1y', 'interval': '1d',
        'start': datetime.datetime.now() - datetime.timedelta(days=365),
        'end': None}

    st.markdown("# Welcome to [YahooQuery](https://github.com/dpguthrie/yahooquery)")

    if page == "Homepage":
        st.markdown(f"""
            ## Streamlit Instructions
            Enter a symbol or list of symbols in the box to the left (**comma
            separated**).  Then select different pages in the dropdown to view
            the data available to you.

            ## Short README

            ### Install
            ```python
            pip install yahooquery
            ```

            ### Ticker
            The `Ticker` class provides the access point to data residing on
            Yahoo Finance.  It accepts either a symbol or list of symbols.
            Additionally, you can supply `formatted` as a keyword argument
            to the class to format the data returned from the API (default is
            `True`)

            ```python
            from yahooquery import Ticker

            tickers = Ticker({symbols})
            ```
        """)
        st.help(tickers)
    elif page == "Base":
        st.header("Base Endpoints")
        st.write("""
            Select an option below to see the data available through
            the base endpoints.""")
        endpoint = st.selectbox(
            "Select Endpoint", options=sorted(list(BASE_ENDPOINTS.keys())),
            format_func=format_func)
        st.help(getattr(Ticker, endpoint))
        is_property = isinstance(getattr(Ticker, endpoint), property)
        if is_property:
            st.code(f"Ticker({symbols}).{endpoint}", language="python")
            data = get_data(tickers, endpoint)
        else:
            frequency = st.selectbox(
                "Select Frequency", options=["Annual", "Quarterly"])
            arg = frequency[:1].lower()
            st.code(f"Ticker({symbols}).{endpoint}(frequency='{arg}')")
            data = get_data(tickers, endpoint, arg)
        st.write(data)
    elif page == "Base - Multiple":
        st.header("Base Endpoints - Multiple")
        st.markdown("""
            Two methods to the `Ticker` class allow you to obtain multiple
            endpoints with one call.  The `get_endpoints` method takes a list
            of allowable endpoints, which you can view through `Ticker._ENDPOINTS`,
            and the `all_endpoints` property retrieves all Base endpoints""")
        method = st.selectbox(
            "Select Method", options=['All Endpoints', 'Multiple Endpoints'],
            index=1)
        if method == "All Endpoints":
            st.help(getattr(Ticker, 'all_endpoints'))
            st.code(f"Ticker({symbols}).all_endpoints", language="python")
            data = get_data(tickers, "all_endpoints")
            st.json(data)
        else:

            default_endpoints = ['assetProfile']
            endpoints = st.multiselect(
                "Select endpoints", options=sorted(Ticker._ENDPOINTS),
                default=default_endpoints)
            st.help(getattr(Ticker, "get_endpoints"))
            st.code(f"Ticker({symbols}).get_endpoints({endpoints})", language="python")
            if not endpoints:
                st.warning("You must select at least one endpoint")
            else:
                data = get_data(tickers, "get_endpoints")(endpoints)
                st.json(data)
    elif page == "Options":
        st.header("Option Chain")
        st.write("""
            Yahooquery also gives you the ability to view option chain data
            for all expiration dates for a given symbol(s)
        """)
        st.help(getattr(Ticker, 'option_chain'))
        st.code(f"Ticker({symbols}).option_chain", language="python")
        data = get_data(tickers, 'option_chain')
        st.dataframe(data)
    else:
        st.header("Historical Pricing")
        st.write("""
            Retrieve historical pricing data for a given symbol(s)
        """)
        st.help(getattr(Ticker, 'history'))
        st.markdown("""
            1. Select a period **or** enter start and end dates.
            2. Select interval (**note:  some intervals are not available for
                certain lengths of time**)
        """)
        option_1 = st.selectbox(
            "Select Period or Start / End Dates", ["Period", "Dates"], 0)
        if option_1 == "Period":
            history_args['period'] = st.selectbox(
                "Select Period", options=Ticker._PERIODS, index=5)
            history_args['start'] = None
            history_args['end'] = None
        else:
            history_args['start'] = st.date_input(
                "Select Start Date", value=history_args['start'])
            history_args['end'] = st.date_input("Select End Date")
            history_args['period'] = None

        st.markdown("**THEN**")
        history_args['interval'] = st.selectbox(
            "Select Interval", options=Ticker._INTERVALS, index=8)
        args_string = [
            str(k) + "='" + str(v) + "'"  for k, v in history_args.items()
            if v is not None]
        st.code(f"Ticker({symbols}).history({', '.join(args_string)})",
                language="python")
        df = tickers.history(**history_args)

        if isinstance(df, dict):
            st.write(df)
        else:
            if len(symbols) > 1:
                chart = (
                    alt.Chart(df.reset_index()).mark_line().encode(
                        alt.Y('close:Q', scale=alt.Scale(zero=False)),
                        x='dates',
                        color='symbol'
                    )
                )
            else:
                chart = (
                    alt.Chart(df.reset_index()).mark_line().encode(
                        alt.Y('close:Q', scale=alt.Scale(zero=False)),
                        x='dates:T',
                    )
                )
            st.write("", "", chart)
            st.dataframe(df)


if __name__ == "__main__":
    main()
