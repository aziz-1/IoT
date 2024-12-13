# IoT Data Processing and Visualization

This repository contains a Jupyter Notebook for processing IoT data for weather, energy consumption, and tweet's sentiment analysis.

The notebook also generates public URLs for the uploaded Google Sheets, which can be used for further analysis and visualization.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Files](#files)
- [License](#license)

## Introduction

The notebook performs the following tasks:
1. Processes IoT data and performs time-series and sentiment analysis.
2. Analyse the visualise findings
3. Generates public URLs for the uploaded Google Sheets.

## Setup

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Google Cloud account with access to Google Sheets API

### Install Required Libraries

```sh
pip install pandas gspread oauth2client
