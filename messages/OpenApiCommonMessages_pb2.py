# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OpenApiCommonMessages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bOpenApiCommonMessages.proto\x12\x0eOpenApi.Common\"(\n\x13ProtoHeartBeatEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\"I\n\x0cProtoMessage\x12\x13\n\x0bpayloadType\x18\x01 \x01(\x05\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x13\n\x0b\x63lientMsgId\x18\x03 \x01(\tb\x06proto3')



_PROTOHEARTBEATEVENT = DESCRIPTOR.message_types_by_name['ProtoHeartBeatEvent']
_PROTOMESSAGE = DESCRIPTOR.message_types_by_name['ProtoMessage']
ProtoHeartBeatEvent = _reflection.GeneratedProtocolMessageType('ProtoHeartBeatEvent', (_message.Message,), {
  'DESCRIPTOR' : _PROTOHEARTBEATEVENT,
  '__module__' : 'OpenApiCommonMessages_pb2'
  # @@protoc_insertion_point(class_scope:OpenApi.Common.ProtoHeartBeatEvent)
  })
_sym_db.RegisterMessage(ProtoHeartBeatEvent)

ProtoMessage = _reflection.GeneratedProtocolMessageType('ProtoMessage', (_message.Message,), {
  'DESCRIPTOR' : _PROTOMESSAGE,
  '__module__' : 'OpenApiCommonMessages_pb2'
  # @@protoc_insertion_point(class_scope:OpenApi.Common.ProtoMessage)
  })
_sym_db.RegisterMessage(ProtoMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROTOHEARTBEATEVENT._serialized_start=47
  _PROTOHEARTBEATEVENT._serialized_end=87
  _PROTOMESSAGE._serialized_start=89
  _PROTOMESSAGE._serialized_end=162
# @@protoc_insertion_point(module_scope)
