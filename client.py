import grpc
from datetime import datetime
from datetime import timedelta
import sys
import time
import threading


def run():
    value = int(input("Enter the value to calculate: "))
    with grpc.insecure_channel('localhost:50051') as channel:

        client = DateTimeClient(channel)
        print(values)
		

if __name__ == '__main__':
    run()