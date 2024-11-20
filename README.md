# Microservice-A
This microservice allows you to retrieve information about movies from a local IMDb dataset using ZeroMQ for communication. It provides three data types: year, runtime, and genres.


UML sequence:

Client Sends Request:

The client (e.g., a requesting program) creates a request containing a tconst (movie identifier) and a datatype (e.g., "year," "runtime," or "genres").
This request is sent to the ZeroMQ Communication Pipe.
CommPipe Forwards Request:

The ZeroMQ pipe passes the request to the Movie Data Microservice for processing.
Microservice Queries IMDb Dataset:

The Movie Data Microservice processes the request by querying the local IMDb Dataset using the provided tconst to locate the movie.
IMDb Dataset Responds:

The dataset returns the requested information (e.g., the release year, runtime, or genres of the movie) or an error if the movie is not found.
Microservice Sends Response:

The Movie Data Microservice formats the response as a JSON object containing the requested data or an error message (e.g., "Movie not found").
It sends this response back to the CommPipe.
CommPipe Forwards Response:

The ZeroMQ Communication Pipe passes the response to the Client.
Client Receives Response:

The client receives and processes the JSON response, which includes either the requested movie data or an error message.


![movie_service_uml_sequence_diagram](https://github.com/user-attachments/assets/3a99d2dd-cb84-4b90-8c2a-23580e317309)




Communication Contract


Request Format:

Parameters:

tconst (string): IMDb identifier for the movie (e.g., tt1234567).
datatype (string): Type of data requested, one of year, runtime, or genres.

Example Request (Python Code):

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = {
    "tconst": "tt1234567",
    "datatype": "runtime"
}
socket.send_json(request)
response = socket.recv_json()
print("Response:", response)





Response Format:

JSON object with the requested data or an error message.

Fields:

tconst (string): IMDb identifier of the movie.

datatype (string): Data type requested.

data (varies): The requested data (e.g., year, runtime, or genres).

error (string, optional): Error message if the request cannot be fulfilled.


Example Response:

{
    "tconst": "tt1234567",
    "datatype": "runtime",
    "data": "142 minutes"
}

