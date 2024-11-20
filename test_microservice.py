import zmq

def test_microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Test cases
    test_requests = [
        {"tconst": "tt1234567", "datatype": "year"},
        {"tconst": "tt1234567", "datatype": "runtime"},
        {"tconst": "tt1234567", "datatype": "genres"},
        {"tconst": "ttInvalid", "datatype": "runtime"},
        {"tconst": "tt1234567", "datatype": "invalidDatatype"}
    ]

    for request in test_requests:
        print(f"Sending request: {request}")
        socket.send_json(request)
        response = socket.recv_json()
        print(f"Response: {response}\n")

if __name__ == "__main__":
    test_microservice()
