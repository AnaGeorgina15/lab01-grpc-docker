
import os
import grpc
import generated.calculadora_pb2 as pb2
import generated.calculadora_pb2_grpc as pb2_grpc

def main():
    servidor = os.getenv("GRPC_SERVER", "localhost:50051")
    channel = grpc.insecure_channel(servidor)
    stub = pb2_grpc.CalculadoraServiceStub(channel)

    n1 = 10
    n2 = 5

    request = pb2.OperacionRequest(n1=n1, n2=n2)

    rsum = stub.suma(request, timeout=5)
    rrest = stub.resta(request, timeout=5)
    rmult = stub.mult(request, timeout=5)
    rdiv = stub.div(request, timeout=5)

    print(f"{n1} + {n2} = {rsum.result}")
    print(f"{n1} - {n2} = {rrest.result}")
    print(f"{n1} * {n2} = {rmult.result}")
    print(f"{n1} / {n2} = {rdiv.result}")

    print("end client..")
    channel.close()

if __name__ == '__main__':
    main()
