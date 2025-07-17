# ieuk-task-2025
## Project overview
The project replicates a traffic problem causing website outtages for a small media startup. The objective is to identify the cause of the problem by reviewing the website logs and to recommend a strategy to resolve server overload.

## File structure
### `analyser` file
This program is made to analyse the activity of each IP address.
### `checker` file
This program is a real-time checker for the logs where it flags suspicious behaviours. This checker can be run from containers such as Docker which is used as an example.

## How to run
### Install dependencies
`pip install -r requirements.txt`
### Run the checker file
The chcker file can be used either with a container or by it's own on log files.

## License
This project is created for learning purposes during IEUK 2025 and is not licensed for commercial use.
