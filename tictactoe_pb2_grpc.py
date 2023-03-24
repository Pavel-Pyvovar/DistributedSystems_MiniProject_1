# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tictactoe_pb2 as tictactoe__pb2


class TicTacToeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinGame = channel.unary_unary(
                '/TicTacToe/JoinGame',
                request_serializer=tictactoe__pb2.JoinGameRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.JoinGameResponse.FromString,
                )
        self.StartGame = channel.unary_unary(
                '/TicTacToe/StartGame',
                request_serializer=tictactoe__pb2.StartGameRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.StartGameResponse.FromString,
                )
        self.SetSymbol = channel.unary_unary(
                '/TicTacToe/SetSymbol',
                request_serializer=tictactoe__pb2.SetSymbolRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.SetSymbolResponse.FromString,
                )
        self.CommandRequest = channel.unary_unary(
                '/TicTacToe/CommandRequest',
                request_serializer=tictactoe__pb2.CommandRequestMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.CommandReplyResult.FromString,
                )
        self.SetNodeTime = channel.unary_unary(
                '/TicTacToe/SetNodeTime',
                request_serializer=tictactoe__pb2.SetNodeTimeRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.SetNodeTimeResponse.FromString,
                )


class TicTacToeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JoinGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSymbol(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommandRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNodeTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TicTacToeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinGame': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinGame,
                    request_deserializer=tictactoe__pb2.JoinGameRequest.FromString,
                    response_serializer=tictactoe__pb2.JoinGameResponse.SerializeToString,
            ),
            'StartGame': grpc.unary_unary_rpc_method_handler(
                    servicer.StartGame,
                    request_deserializer=tictactoe__pb2.StartGameRequest.FromString,
                    response_serializer=tictactoe__pb2.StartGameResponse.SerializeToString,
            ),
            'SetSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSymbol,
                    request_deserializer=tictactoe__pb2.SetSymbolRequest.FromString,
                    response_serializer=tictactoe__pb2.SetSymbolResponse.SerializeToString,
            ),
            'CommandRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.CommandRequest,
                    request_deserializer=tictactoe__pb2.CommandRequestMessage.FromString,
                    response_serializer=tictactoe__pb2.CommandReplyResult.SerializeToString,
            ),
            'SetNodeTime': grpc.unary_unary_rpc_method_handler(
                    servicer.SetNodeTime,
                    request_deserializer=tictactoe__pb2.SetNodeTimeRequest.FromString,
                    response_serializer=tictactoe__pb2.SetNodeTimeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TicTacToe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TicTacToe(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JoinGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/JoinGame',
            tictactoe__pb2.JoinGameRequest.SerializeToString,
            tictactoe__pb2.JoinGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/StartGame',
            tictactoe__pb2.StartGameRequest.SerializeToString,
            tictactoe__pb2.StartGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSymbol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/SetSymbol',
            tictactoe__pb2.SetSymbolRequest.SerializeToString,
            tictactoe__pb2.SetSymbolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommandRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/CommandRequest',
            tictactoe__pb2.CommandRequestMessage.SerializeToString,
            tictactoe__pb2.CommandReplyResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNodeTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/SetNodeTime',
            tictactoe__pb2.SetNodeTimeRequest.SerializeToString,
            tictactoe__pb2.SetNodeTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
