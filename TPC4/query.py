import requests # bib permite fzr pedidos http
from tabulate import tabulate
import random 

def query_graphdb(endpoint_url, sparql_query):
    # Set up the headers
    headers = {
        'Accept': 'application/json',  # You can change this based on the response format you need
    }
    
    # Make the GET request to the GraphDB endpoint
    # receber pedidos
    response = requests.get(endpoint_url, params={'query': sparql_query}, headers=headers)
    
    if response.status_code == 200: # resposta SUCCESS de um GET
        return response.json()  # Return the JSON response from the GraphDB endpoint
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")




