import grpc
from concurrent import futures
import time
import datetime
from concurrent.futures import ThreadPoolExecutor
import datetime

def serve():
	num_threads = int(input("Enter the number of threads to use: "))
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=num_threads))
	server.add_insecure_port('[::]:50051')
	server.start()
	print("Server CONNECTED to port 50051...")
	server.wait_for_termination()

if __name__ == '__main__':
    serve()
