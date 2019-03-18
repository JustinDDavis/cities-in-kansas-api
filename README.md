
# Simple Flask Demo

## Purpose
This project is something I put together to help reiterate my understanding of Flask. It is not meant to be production ready or really that useful, but as something that I can help
judge my own development progress. 

## Structure
    - API (Flask)
        - Only one "GET" method is implemented
            - Return all results
            - Return results that start with specific character(s)
    - Database
        - I put together a static TXT file that contains city names. The class will parse the file and assign values to a data property. 
        - This is not a production implementation. It is only to help practice and illistrate file IO. 
    - Tests
        - There are simple tests for both uses of the single GET method in the API