# YouTube Data Harvesting and Warehousing

Welcome to the YouTube Data Harvesting and Warehousing project by Piyush Gone. This project is designed to collect, store, and analyze data from multiple YouTube channels, utilizing Python, MongoDB, SQL, and Streamlit.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Features](#project-features)
- [Project Components](#project-components)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Data Storage](#data-storage)
- [Data Visualization](#data-visualization)
- [SQL Queries](#sql-queries)
- [Project Evaluation](#project-evaluation)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project aims to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels. The application features data retrieval from the YouTube API, storage in a MongoDB data lake, migration to a SQL data warehouse, and various data analysis capabilities.

## Project Features

- Retrieve channel details including name, subscribers, and total video count.
- Collect video information including video ID, title, views, likes, dislikes, and comments.
- Store data in a MongoDB data lake.
- Migrate channel data from the data lake to a SQL data warehouse.
- Perform SQL queries to analyze and visualize data.
- Streamlit-based user interface for ease of use.

## Project Components

The project consists of the following components:

- **YouTube Data Retrieval**: Python scripts to connect to the YouTube API and retrieve channel and video data.

- **MongoDB Data Storage**: Code to store channel details, video information, and comments in a MongoDB Atlas data lake.

- **SQL Data Warehouse**: SQL code to design tables for storing channel and video data in a structured manner.

- **Streamlit App**: The user interface built using Streamlit to interact with the data, retrieve details, and perform analysis.

## Getting Started

1. Clone this repository to your local machine.

2. Set up your MongoDB Atlas cluster and obtain the connection URI.

3. Set up your MySQL or PostgreSQL database for the SQL data warehouse.

4. Install the required Python packages listed in `requirements.txt` using `pip install -r requirements.txt`.

## Usage

1. Run the Streamlit app using `streamlit run app.py`.

2. Enter a YouTube channel ID to retrieve channel details.

3. Use the app to migrate channels to the data warehouse, perform SQL queries, and visualize data.

## Data Storage

- MongoDB Atlas is used as a data lake to store retrieved data in a structured format.

- SQL databases (e.g., MySQL or PostgreSQL) serve as the data warehouse for structured data storage.

## Data Visualization

- The Streamlit app provides data visualization features such as charts and graphs for data analysis.

## SQL Queries

SQL queries to perform various analyses on the data:

- What are the names of all the videos and their corresponding channels?
- Which channels have the most number of videos, and how many videos do  they have?
- What are the top 10 most viewed videos and their respective channels?
- How many comments were made on each video, and what are their corresponding video names?
- Which videos have the highest number of likes, and what are their corresponding channel names?
- What is the total number of likes and dislikes for each video, and what are their corresponding video names?
- What is the total number of views for each channel, and what are their corresponding channel names?
- What are the names of all the channels that have published videos in the year 2022?
- What is the average duration of all videos in each channel, and what are their corresponding channel names?
- Which videos have the highest number of comments, and what are their corresponding channel names?


## Project Evaluation

The project is designed with maintainability, portability, and proper coding standards in mind. It includes a well-documented README file, and the code is modular for easy maintenance.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
