# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import time_pb2 as time__pb2


class TimeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTimeDifference = channel.unary_unary(
                '/TimeService/GetTimeDifference',
                request_serializer=time__pb2.TimeRequest.SerializeToString,
                response_deserializer=time__pb2.TimeResponse.FromString,
                )
        self.AdjustTime = channel.unary_unary(
                '/TimeService/AdjustTime',
                request_serializer=time__pb2.TimeAdjustment.SerializeToString,
                response_deserializer=time__pb2.TimeResponse.FromString,
                )


class TimeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTimeDifference(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AdjustTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTimeDifference': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeDifference,
                    request_deserializer=time__pb2.TimeRequest.FromString,
                    response_serializer=time__pb2.TimeResponse.SerializeToString,
            ),
            'AdjustTime': grpc.unary_unary_rpc_method_handler(
                    servicer.AdjustTime,
                    request_deserializer=time__pb2.TimeAdjustment.FromString,
                    response_serializer=time__pb2.TimeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TimeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTimeDifference(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TimeService/GetTimeDifference',
            time__pb2.TimeRequest.SerializeToString,
            time__pb2.TimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AdjustTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TimeService/AdjustTime',
            time__pb2.TimeAdjustment.SerializeToString,
            time__pb2.TimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
