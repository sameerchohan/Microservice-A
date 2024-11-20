# Microservice-A
This microservice allows you to retrieve information about movies from a local IMDb dataset using ZeroMQ for communication. It provides three data types: year, runtime, and genres.




![uml_sequence_diagram](https://github.com/user-attachments/assets/dc11973b-b505-4779-b8ab-606998378af0)



Communication Contract
Request Format:

Parameters:

tconst (string): IMDb identifier for the movie (e.g., tt1234567).
datatype (string): Type of data requested, one of year, runtime, or genres.
Example Request (Python Code):
"
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
"



Response Format:

JSON object with the requested data or an error message.

Fields:

tconst (string): IMDb identifier of the movie.
datatype (string): Data type requested.
data (varies): The requested data (e.g., year, runtime, or genres).
error (string, optional): Error message if the request cannot be fulfilled.
Example Response:
"
{
    "tconst": "tt1234567",
    "datatype": "runtime",
    "data": "142 minutes"
}
"
