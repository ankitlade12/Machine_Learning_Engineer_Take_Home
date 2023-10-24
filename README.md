# Fetch Rewards Take-home Exercise - Machine Learning Engineer

## Getting Started

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

4) To stop the Docker container, you can use Ctrl+C in your terminal

5) To remove the container use:
    ```
    docker image rm -f app
    ```