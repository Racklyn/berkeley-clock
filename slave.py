import sys
import time
from concurrent import futures
import grpc
import time_pb2
import time_pb2_grpc

# Variável global para o deslocamento de tempo
time_offset = 0

class TimeService(time_pb2_grpc.TimeServiceServicer):
    def GetTimeDifference(self, request, context):
        # Usa o deslocamento de tempo para calcular a diferença
        server_time = time.time() + time_offset
        time_difference = server_time - float(request.client_time)
        return time_pb2.TimeResponse(time_difference=str(time_difference))

    def AdjustTime(self, request, context):
        # Imprime a hora atual antes do ajuste
        current_time = time.time() + time_offset
        print(f"Hora atual no slave antes do ajuste: {time.ctime(current_time)}")

        # Ajusta o relógio do servidor com base no ajuste recebido
        adjustment = float(request.time_adjustment)
        adjusted_time = current_time + adjustment

        # Imprime a hora atualizada após o ajuste
        print(f"Hora atualizada no slave após o ajuste: {time.ctime(adjusted_time)}")

        return time_pb2.TimeResponse(time_difference="0")

def serve(port, offset):
    global time_offset
    time_offset = offset
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    time_pb2_grpc.add_TimeServiceServicer_to_server(TimeService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else '50051'
    offset = float(sys.argv[2]) if len(sys.argv) > 2 else 0
    serve(port, offset)
