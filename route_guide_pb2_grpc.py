# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import route_guide_pb2 as route__guide__pb2


class EventsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PutEvent = channel.unary_unary(
        '/wawcode_shame.EventsService/PutEvent',
        request_serializer=route__guide__pb2.Event.SerializeToString,
        response_deserializer=route__guide__pb2.PutEventResponse.FromString,
        )
    self.PutEvents = channel.unary_unary(
        '/wawcode_shame.EventsService/PutEvents',
        request_serializer=route__guide__pb2.Events.SerializeToString,
        response_deserializer=route__guide__pb2.PutEventResponse.FromString,
        )
    self.EventsInDistance = channel.unary_unary(
        '/wawcode_shame.EventsService/EventsInDistance',
        request_serializer=route__guide__pb2.EventsInDistanceRequest.SerializeToString,
        response_deserializer=route__guide__pb2.Events.FromString,
        )
    self.GetEvent = channel.unary_unary(
        '/wawcode_shame.EventsService/GetEvent',
        request_serializer=route__guide__pb2.GetEventRequest.SerializeToString,
        response_deserializer=route__guide__pb2.Event.FromString,
        )


class EventsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PutEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutEvents(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EventsInDistance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EventsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PutEvent': grpc.unary_unary_rpc_method_handler(
          servicer.PutEvent,
          request_deserializer=route__guide__pb2.Event.FromString,
          response_serializer=route__guide__pb2.PutEventResponse.SerializeToString,
      ),
      'PutEvents': grpc.unary_unary_rpc_method_handler(
          servicer.PutEvents,
          request_deserializer=route__guide__pb2.Events.FromString,
          response_serializer=route__guide__pb2.PutEventResponse.SerializeToString,
      ),
      'EventsInDistance': grpc.unary_unary_rpc_method_handler(
          servicer.EventsInDistance,
          request_deserializer=route__guide__pb2.EventsInDistanceRequest.FromString,
          response_serializer=route__guide__pb2.Events.SerializeToString,
      ),
      'GetEvent': grpc.unary_unary_rpc_method_handler(
          servicer.GetEvent,
          request_deserializer=route__guide__pb2.GetEventRequest.FromString,
          response_serializer=route__guide__pb2.Event.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'wawcode_shame.EventsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
