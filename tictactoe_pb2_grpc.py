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
        self.AssignSymbol = channel.unary_unary(
                '/TicTacToe/AssignSymbol',
                request_serializer=tictactoe__pb2.AssignSymbolRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.AssignSymbolResponse.FromString,
                )
        self.FetchSymbols = channel.unary_unary(
                '/TicTacToe/FetchSymbols',
                request_serializer=tictactoe__pb2.FetchSymbolsRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.FetchSymbolsResponse.FromString,
                )
        self.PlayerSendCommand = channel.unary_unary(
                '/TicTacToe/PlayerSendCommand',
                request_serializer=tictactoe__pb2.PlayerSendCommandRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.PlayerSendCommandResponse.FromString,
                )
        self.CoordinatorAcceptCommand = channel.unary_unary(
                '/TicTacToe/CoordinatorAcceptCommand',
                request_serializer=tictactoe__pb2.CoordinatorAcceptCommandRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.CoordinatorAcceptCommandResponse.FromString,
                )
        self.CoordinatorSendCommandResult = channel.unary_unary(
                '/TicTacToe/CoordinatorSendCommandResult',
                request_serializer=tictactoe__pb2.CoordinatorSendCommandResultRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.CoordinatorSendCommandResultResponse.FromString,
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

    def AssignSymbol(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchSymbols(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayerSendCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CoordinatorAcceptCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CoordinatorSendCommandResult(self, request, context):
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
            'AssignSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignSymbol,
                    request_deserializer=tictactoe__pb2.AssignSymbolRequest.FromString,
                    response_serializer=tictactoe__pb2.AssignSymbolResponse.SerializeToString,
            ),
            'FetchSymbols': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchSymbols,
                    request_deserializer=tictactoe__pb2.FetchSymbolsRequest.FromString,
                    response_serializer=tictactoe__pb2.FetchSymbolsResponse.SerializeToString,
            ),
            'PlayerSendCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.PlayerSendCommand,
                    request_deserializer=tictactoe__pb2.PlayerSendCommandRequest.FromString,
                    response_serializer=tictactoe__pb2.PlayerSendCommandResponse.SerializeToString,
            ),
            'CoordinatorAcceptCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.CoordinatorAcceptCommand,
                    request_deserializer=tictactoe__pb2.CoordinatorAcceptCommandRequest.FromString,
                    response_serializer=tictactoe__pb2.CoordinatorAcceptCommandResponse.SerializeToString,
            ),
            'CoordinatorSendCommandResult': grpc.unary_unary_rpc_method_handler(
                    servicer.CoordinatorSendCommandResult,
                    request_deserializer=tictactoe__pb2.CoordinatorSendCommandResultRequest.FromString,
                    response_serializer=tictactoe__pb2.CoordinatorSendCommandResultResponse.SerializeToString,
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
    def AssignSymbol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/AssignSymbol',
            tictactoe__pb2.AssignSymbolRequest.SerializeToString,
            tictactoe__pb2.AssignSymbolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/FetchSymbols',
            tictactoe__pb2.FetchSymbolsRequest.SerializeToString,
            tictactoe__pb2.FetchSymbolsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlayerSendCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/PlayerSendCommand',
            tictactoe__pb2.PlayerSendCommandRequest.SerializeToString,
            tictactoe__pb2.PlayerSendCommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CoordinatorAcceptCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/CoordinatorAcceptCommand',
            tictactoe__pb2.CoordinatorAcceptCommandRequest.SerializeToString,
            tictactoe__pb2.CoordinatorAcceptCommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CoordinatorSendCommandResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/CoordinatorSendCommandResult',
            tictactoe__pb2.CoordinatorSendCommandResultRequest.SerializeToString,
            tictactoe__pb2.CoordinatorSendCommandResultResponse.FromString,
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
