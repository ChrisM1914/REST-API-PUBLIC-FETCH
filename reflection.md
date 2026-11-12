# Reflection: REST API Public Fetch

This assignment required me to build an application that asynchronously fetches public vehicle data from the NHTSA API. I set up a project folder and virtual environment, installed Flask and requests, and wrote an app.py with a GET /items route that makes a request to the NHTSA vPIC website, parses the JSON, and returns only the entries whose GroupName equaled "Active Safety System." I ran the server locally, tested it in my browser, then created the REST-API-PUBLIC-FETCH repository with GitHub Desktop and uploaded my files.

What surprised me most was how the data was presented on https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleVariableList?format=json. It was not a simple, easy to read list. My code evolved to include a longer timeout because of the amount of data, .get() for safe key access, and clearer error messages.

I have a better understanding of HTTP requests, JSON parsing, and status codes. I would like to learn more about pagination and caching for larger APIs.
