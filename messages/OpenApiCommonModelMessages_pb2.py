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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n OpenApiCommonModelMessages.proto\x12\x13OpenApi.CommonModel*\x8d\x01\n\x0eProtoErrorCode\x12\x11\n\rUNKNOWN_ERROR\x10\x00\x12\x11\n\rINVALID_TOKEN\x10\x01\x12\x13\n\x0fINVALID_ACCOUNT\x10\x02\x12\x16\n\x12INSUFFICIENT_FUNDS\x10\x03\x12\x12\n\x0eORDER_REJECTED\x10\x04\x12\x14\n\x10SYMBOL_NOT_FOUND\x10\x05\x62\x06proto3')

_PROTOERRORCODE = DESCRIPTOR.enum_types_by_name['ProtoErrorCode']
ProtoErrorCode = enum_type_wrapper.EnumTypeWrapper(_PROTOERRORCODE)
UNKNOWN_ERROR = 0
INVALID_TOKEN = 1
INVALID_ACCOUNT = 2
INSUFFICIENT_FUNDS = 3
ORDER_REJECTED = 4
SYMBOL_NOT_FOUND = 5


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROTOERRORCODE._serialized_start=58
  _PROTOERRORCODE._serialized_end=199
# @@protoc_insertion_point(module_scope)
