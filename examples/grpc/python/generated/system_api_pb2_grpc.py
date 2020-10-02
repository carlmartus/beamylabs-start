# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import common_pb2 as common__pb2
import system_api_pb2 as system__api__pb2


class SystemServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfiguration = channel.unary_unary(
        '/base.SystemService/GetConfiguration',
        request_serializer=common__pb2.Empty.SerializeToString,
        response_deserializer=common__pb2.Configuration.FromString,
        )
    self.ListSignals = channel.unary_unary(
        '/base.SystemService/ListSignals',
        request_serializer=common__pb2.NameSpace.SerializeToString,
        response_deserializer=common__pb2.Frames.FromString,
        )
    self.UploadFileChunk = channel.unary_unary(
        '/base.SystemService/UploadFileChunk',
        request_serializer=system__api__pb2.FileUploadChunkRequest.SerializeToString,
        response_deserializer=system__api__pb2.FileUploadResponse.FromString,
        )
    self.UploadFile = channel.stream_unary(
        '/base.SystemService/UploadFile',
        request_serializer=system__api__pb2.FileUploadRequest.SerializeToString,
        response_deserializer=system__api__pb2.FileUploadResponse.FromString,
        )
    self.ReloadConfiguration = channel.unary_unary(
        '/base.SystemService/ReloadConfiguration',
        request_serializer=common__pb2.Empty.SerializeToString,
        response_deserializer=system__api__pb2.ReloadMessage.FromString,
        )


class SystemServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetConfiguration(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListSignals(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadFileChunk(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadFile(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReloadConfiguration(self, request, context):
    """will not return until new configuration is tested an active, make sure to set timeout to a large value. (fibex on pi > 50s)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SystemServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfiguration': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfiguration,
          request_deserializer=common__pb2.Empty.FromString,
          response_serializer=common__pb2.Configuration.SerializeToString,
      ),
      'ListSignals': grpc.unary_unary_rpc_method_handler(
          servicer.ListSignals,
          request_deserializer=common__pb2.NameSpace.FromString,
          response_serializer=common__pb2.Frames.SerializeToString,
      ),
      'UploadFileChunk': grpc.unary_unary_rpc_method_handler(
          servicer.UploadFileChunk,
          request_deserializer=system__api__pb2.FileUploadChunkRequest.FromString,
          response_serializer=system__api__pb2.FileUploadResponse.SerializeToString,
      ),
      'UploadFile': grpc.stream_unary_rpc_method_handler(
          servicer.UploadFile,
          request_deserializer=system__api__pb2.FileUploadRequest.FromString,
          response_serializer=system__api__pb2.FileUploadResponse.SerializeToString,
      ),
      'ReloadConfiguration': grpc.unary_unary_rpc_method_handler(
          servicer.ReloadConfiguration,
          request_deserializer=common__pb2.Empty.FromString,
          response_serializer=system__api__pb2.ReloadMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'base.SystemService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
