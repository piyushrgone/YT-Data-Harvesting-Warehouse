import streamlit as st
from pymongo import MongoClient
import os
from googleapiclient.discovery import build

st.image("https://lh3.googleusercontent.com/3zkP2SYe7yYoKKe47bsNe44yTgb4Ukh__rBbwXwgkjNRe4PykGG409ozBxzxkrubV7zHKjfxq6y9ShogWtMBMPyB3jiNps91LoNH8A=s500")
# Streamlit app title and description
st.title("YouTube Data Harvesting and Warehousing")
st.write("Welcome to the YouTube Data app! "
         " by Piyush Gone.")

# Set your API key
API_KEY = 'AIzaSyCczvVZLHvHKVXCMIthbiYOa-2IyV_Bees'  # Replace with your actual API key

# Initialize the YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

st.write("Enter a YouTube channel ID to retrieve channel details.")

# Input field for entering YouTube channel ID
channel_id = st.text_input("Enter Channel ID:", "")

# Button to retrieve channel details
if st.button("Retrieve Details"):
    try:
        request = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        )
        response = request.execute()
        channel_info = response['items'][0]

        st.write("Channel Name:", channel_info['snippet']['title'])
        st.write("Subscribers:", channel_info['statistics']['subscriberCount'])
        st.write("Total Videos:", channel_info['statistics']['videoCount'])
    except Exception as e:
        st.error("An error occurred. Please check the channel ID and API key.")

# Initialize MongoDB Atlas connection
mongo_client = MongoClient('mongodb+srv://piyushgone:tinku.2499@clusteryt.xaijn8b.mongodb.net/')  # My MongoDB Atlas connection details
db = mongo_client['youtube_data']
channel_collection = db['channels']
video_collection = db['videos']

# Button to retrieve and store channel details
if st.button("Retrieve and Store Details"):
    try:
        request = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        )
        response = request.execute()
        channel_info = response['items'][0]

        # Store channel details in MongoDB Atlas
        channel_document = {
            'channel_id': channel_id,
            'channel_name': channel_info['snippet']['title'],
            'subscribers': channel_info['statistics']['subscriberCount'],
            'total_videos': channel_info['statistics']['videoCount']
        }
        channel_collection.insert_one(channel_document)

        st.success("Channel details stored successfully in MongoDB Atlas.")
    except Exception as e:
        st.error("An error occurred. Please check the channel ID and API key.")


# Checkbox for channel migration
migrate_channels = st.checkbox("Migrate Channels to Data Warehouse")

# List of channels for migration
channels_for_migration = st.multiselect("Select Channels for Migration:", ["Channel 1", "Channel 2", "Channel 3"])

# Button to initiate migration
if st.button("Migrate Selected Channels"):
    if migrate_channels:
        st.write(f"Migrating selected channels: {channels_for_migration}")
        # You can write logic to migrate channel data to the data warehouse

# Data visualization section
st.header("Data Visualization")
# You can add charts, tables, and graphs to visualize data here

# Search options for querying SQL data warehouse
st.header("SQL Data Warehouse Query")
search_option = st.selectbox("Select Query Option:", ["Top Videos", "Channel Views", "Comments"])

# Implement SQL query logic based on selected option
if search_option == "Top Videos":
    # Implement logic to retrieve top videos from SQL data warehouse
    st.write("Displaying top videos...")
elif search_option == "Channel Views":
    # Implement logic to retrieve channel views from SQL data warehouse
    st.write("Displaying channel views...")
elif search_option == "Comments":
    # Implement logic to retrieve comments from SQL data warehouse
    st.write("Displaying comments...")

# Provide a link to your GitHub repository
st.sidebar.markdown("[GitHub Repository](https://github.com/yourusername/your-repo)")

# Display project information and instructions
st.sidebar.header("Project Information")
st.sidebar.write("This Streamlit app allows users to interact with YouTube data.")
st.sidebar.write("Enter a YouTube channel ID, retrieve details, and more.")
