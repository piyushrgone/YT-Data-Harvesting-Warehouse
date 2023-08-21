# YT-Data-Harvesting-Warehouse
Python scripting, Data Collection, MongoDB, Streamlit, API integration, Data Managment using MongoDB (Atlas) and SQL
This project involves various steps, from retrieving data from the YouTube API to storing it in a MongoDB data lake, migrating it to a SQL data warehouse, and then visualizing and querying the data in a Streamlit application. Here's a summary of the approach and key components of the project:

Approach and Key Components:

Set up a Streamlit App:

Use Streamlit to create a user-friendly interface where users can interact with the application.
Implement input fields for entering YouTube channel IDs and buttons for data retrieval and migration.
Connect to the YouTube API:

Use the google-api-python-client library to connect to the YouTube Data API.
Retrieve channel information, video details, and related data using API requests.
Store Data in MongoDB:

Use MongoDB as a data lake to store the retrieved data in a structured format.
Store channel details, video information, comments, and related data in separate documents.
Migrate Data to SQL Data Warehouse:

Choose a SQL database like MySQL or PostgreSQL to serve as the data warehouse.
Design tables to store channel, video, and comment data in a structured manner.
Query the SQL Data Warehouse:

Use SQL queries to retrieve and join data from different tables in the SQL data warehouse.
Allow users to search for specific data using different search criteria.
Display Data in Streamlit App:

Use Streamlit's data visualization features to create tables, charts, and graphs.
Display retrieved data from both MongoDB and the SQL data warehouse in the Streamlit UI.
GitHub Repository and Documentation:
