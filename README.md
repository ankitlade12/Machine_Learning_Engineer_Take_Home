# Fetch Rewards Take-home Exercise - Machine Learning Engineer

## Getting Started
To get started you need to install docker desktop and keep it running    
1) Clone repo locally
    ```
    git clone https://github.com/ankitlade12/Machine_Learning_Engineer_Take_Home.git
    ```

2) Build Docker Image (It may take a minute to install all dependencies)
    ```
    docker build -t app .
    ```

3) Run Docker Image
    ```
    docker run -p 8501:8501 app
    ```

4) To view Streamlit app in broswer use
    ```
    localhost:8501
    ```
    OR
    ```
    Double-click Network URL
    ```

5) To stop the Docker container, you can use Ctrl+C in your terminal

6) To remove the container use
    ```
    docker image rm -f app
    ```