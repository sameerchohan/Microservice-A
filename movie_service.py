import zmq
import pandas as pd
import json
import sys
import time

# Load IMDb data
IMDB_FILE = "title.basics.tsv"
print("Loading IMDb data...")
try:
    imdb_data = pd.read_csv(IMDB_FILE, sep="\t", usecols=["tconst", "primaryTitle", "startYear", "runtimeMinutes", "genres"], na_values="\\N")
    imdb_data.fillna("", inplace=True)
except FileNotFoundError:
    print(f"Error: IMDb data file '{IMDB_FILE}' not found. Please ensure it is in the correct directory.")
    sys.exit(1)

# Initialize ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("Microservice running on port 5555...")

def get_movie_info(tconst, datatype):
    movie = imdb_data[imdb_data['tconst'] == tconst]
    if movie.empty:
        return {"error": "Movie not found"}

    if datatype == "year":
        return {"tconst": tconst, "datatype": "year", "data": movie.iloc[0]["startYear"]}
    elif datatype == "runtime":
        return {"tconst": tconst, "datatype": "runtime", "data": f"{movie.iloc[0]['runtimeMinutes']} minutes"}
    elif datatype == "genres":
        return {"tconst": tconst, "datatype": "genres", "data": movie.iloc[0]["genres"].split(",")}
    else:
        return {"error": "Invalid datatype requested"}

while True:
    # Wait for a request
    request = socket.recv_json()
    tconst = request.get("tconst")
    datatype = request.get("datatype")
    
    start_time = time.time()
    
    if not tconst or not datatype:
        response = {"error": "Missing parameters: 'tconst' and 'datatype' are required"}
    else:
        response = get_movie_info(tconst, datatype)
    
    # Check performance
    if time.time() - start_time > 2:
        response["warning"] = "Performance warning: Response exceeded 2 seconds"

    # Send response
    socket.send_json(response)
