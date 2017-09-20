# Stub http server

#### Steps to run server
1. Ensure python 2.7 and pip is installed.
2. run `pip install -r requirements.txt`
3. run `python app.py <stub_folder_location>`

#### Add/Update stub responses
1. JSON response files (file extension .json) should be placed in stub_responses folder

#### Accessing the stub server
1. curl http://localhost:5000/<any-path>?response_file=sample
2. The query string `response_file` should have the file name (excluding extension .json) of the file content
 to be served.