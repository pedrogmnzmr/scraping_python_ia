# scraping_python_ia
Web Scraping + OpenAI API Proccesing

## Project Description

This project implements an automated system to perform web scraping using Selenium WebDriver and process the extracted data using the OpenAI API. The goal is to extract relevant information from a web page and generate summaries, analyses, or customized responses using advanced language models.

## Main Features

### Web Scraping with Selenium
- Automates navigation on a web page.
- Extracts specific data (such as titles, paragraphs, tables, etc.) using CSS or XPath selectors.

### Processing with OpenAI
- Sends the extracted data to the OpenAI API.
- Generates summaries, analyses, or responses based on the scraped content.

### Result Storage
- Saves the scraped data and OpenAI responses in text files for later review.

## Requirements

### Dependencies
- Python 3.8 or higher.
- Python libraries:
  - `selenium`
  - `openai` >> https://platform.openai.com/docs/api-reference/introduction

- ChromeDriver (compatible with your version of Google Chrome).

## Initial Setup

### Install Dependencies
Run the following command to install the required Python libraries:

pip install selenium openai