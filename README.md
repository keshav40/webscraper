# Webscraper

A FastAPI-based web scraping application that allows you to scrape data from websites and store it in a structured format (CSV, JSON, etc.). This project is designed to be easy to use and customizable for different scraping needs.

## Features

- Built with **FastAPI** for fast and efficient web scraping.
- Scrapes data from specified URLs.
- Allows configuration through the `settings.yaml` file for easy customization.
- Supports multiple output formats such as CSV and JSON.
- Handles common scraping challenges like pagination and rate limiting.

## Requirements

- Python 3.7+
- `fastapi`
- `uvicorn`
- `requests`
- `beautifulsoup4`

## Configuration

All configurations, including URLs and scraping parameters, can be found inside the settings.yaml file. Modify this file to set your target URLs, data scraping rules, and output format.
