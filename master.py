import grpc
import time_pb2
import time_pb2_grpc
import time

def get_time_difference(stub):
    client_time = str(time.time())
    response = stub.GetTimeDifference(time_pb2.TimeRequest(client_time=client_time))
    return float(response.time_difference)

def adjust_time(stub, time_adjustment):
    stub.AdjustTime(time_pb2.TimeAdjustment(time_adjustment=str(time_adjustment)))

def run():
    slaves = ['localhost:5001', 'localhost:5002', 'localhost:5003']
    time_differences = []

    # Obtem a diferença de tempo de cada slave
    for address in slaves:
        with grpc.insecure_channel(address) as channel:
            stub = time_pb2_grpc.TimeServiceStub(channel)
            time_difference = get_time_difference(stub)
            time_differences.append(time_difference)

    # Calcula o ajuste médio de tempo necessário
    average_difference = sum(time_differences) / len(time_differences)

    # Envia o ajuste de tempo para cada slave
    for i, address in enumerate(slaves):
        with grpc.insecure_channel(address) as channel:
            stub = time_pb2_grpc.TimeServiceStub(channel)
            diff = average_difference - time_differences[i]
            adjust_time(stub, diff)
            print(f"Enviado ajuste de tempo para {address}: {diff} segundos")

if __name__ == '__main__':
    run()
