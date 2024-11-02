import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from .filters_area import get_filters_area
from configurations.config import *

# Function to create a card with filters for trends and data
def create_trends_and_data_card(placeholder='Select an option'):
    """Creates a card displaying the data trends and patterns overview.

    This function generates a card component containing headers and a body
    where users can find interactive visualizations related to sentiment
    and emotion analyses. It provides an overview of how these metrics vary
    over time and across companies.

    Args:
        placeholder (str): The placeholder text for dropdowns (default is 'Select an option').

    Returns:
        dbc.Card: A Dash Bootstrap Card component containing the trends and data overview.
    """
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H1(
                    'Data Trends & Patterns',
                    id={'type': 'sentiment-header-card-header', 'page': trends_page_name},
                    style={'text-align': 'center'}
                ),
            ),
            dbc.CardHeader([
                html.P(
                    '📈 Data Trends & Patterns Overview 📈',
                    style={'fontWeight': 'bold', 'fontSize': '1.5em'}
                ),
                html.P(
                    'Welcome to the Data Trends & Patterns page, where you can explore sentiment and emotion analyses across the entire dataset or specific subsets. This page provides interactive visualizations that reveal overarching trends and insights into how sentiment and emotions vary over time and by company. 📊'
                ),
                html.P(
                    'From tracking article counts by month and week to identifying top entities and sentiment distributions, each plot offers a comprehensive view of the data landscape. You\'ll gain valuable insights into the emotional dynamics of articles and how they relate to different companies and time periods.'
                ),
                html.P(
                    'With this information, you can better understand the narrative landscape and make informed decisions. Dive in and uncover the patterns hidden within the data! 🔍'
                )
            ]),

            dbc.CardBody(
                html.Div(
                    get_filters_area(trends_page_name),
                ),
                id={'type': 'article-selection-card-body', 'page': trends_page_name},
            ),
        ],
        className='mb-4',
    )
