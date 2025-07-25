# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OpenApiCommonModelMessages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n OpenApiCommonModelMessages.proto*I\n\x10ProtoPayloadType\x12\x11\n\rPROTO_MESSAGE\x10\x05\x12\r\n\tERROR_RES\x10\x32\x12\x13\n\x0fHEARTBEAT_EVENT\x10\x33*\xf0\x01\n\x0eProtoErrorCode\x12\x11\n\rUNKNOWN_ERROR\x10\x01\x12\x17\n\x13UNSUPPORTED_MESSAGE\x10\x02\x12\x13\n\x0fINVALID_REQUEST\x10\x03\x12\x11\n\rTIMEOUT_ERROR\x10\x05\x12\x14\n\x10\x45NTITY_NOT_FOUND\x10\x06\x12\x16\n\x12\x43\x41NT_ROUTE_REQUEST\x10\x07\x12\x12\n\x0e\x46RAME_TOO_LONG\x10\x08\x12\x11\n\rMARKET_CLOSED\x10\t\x12\x1b\n\x17\x43ONCURRENT_MODIFICATION\x10\n\x12\x18\n\x14\x42LOCKED_PAYLOAD_TYPE\x10\x0b\x42W\n(com.xtrader.protocol.proto.commons.modelB\x1c\x43ontainerCommonModelMessagesP\x01Z\x08/openapi\xa0\x01\x01')

_PROTOPAYLOADTYPE = DESCRIPTOR.enum_types_by_name['ProtoPayloadType']
ProtoPayloadType = enum_type_wrapper.EnumTypeWrapper(_PROTOPAYLOADTYPE)
_PROTOERRORCODE = DESCRIPTOR.enum_types_by_name['ProtoErrorCode']
ProtoErrorCode = enum_type_wrapper.EnumTypeWrapper(_PROTOERRORCODE)
PROTO_MESSAGE = 5
ERROR_RES = 50
HEARTBEAT_EVENT = 51
UNKNOWN_ERROR = 1
UNSUPPORTED_MESSAGE = 2
INVALID_REQUEST = 3
TIMEOUT_ERROR = 5
ENTITY_NOT_FOUND = 6
CANT_ROUTE_REQUEST = 7
FRAME_TOO_LONG = 8
MARKET_CLOSED = 9
CONCURRENT_MODIFICATION = 10
BLOCKED_PAYLOAD_TYPE = 11


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.xtrader.protocol.proto.commons.modelB\034ContainerCommonModelMessagesP\001Z\010/openapi\240\001\001'
  _PROTOPAYLOADTYPE._serialized_start=36
  _PROTOPAYLOADTYPE._serialized_end=109
  _PROTOERRORCODE._serialized_start=112
  _PROTOERRORCODE._serialized_end=352
# @@protoc_insertion_point(module_scope)
