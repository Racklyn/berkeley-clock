# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: time.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntime.proto\"\"\n\x0bTimeRequest\x12\x13\n\x0b\x63lient_time\x18\x01 \x01(\t\"\'\n\x0cTimeResponse\x12\x17\n\x0ftime_difference\x18\x01 \x01(\t\")\n\x0eTimeAdjustment\x12\x17\n\x0ftime_adjustment\x18\x01 \x01(\t2m\n\x0bTimeService\x12\x30\n\x11GetTimeDifference\x12\x0c.TimeRequest\x1a\r.TimeResponse\x12,\n\nAdjustTime\x12\x0f.TimeAdjustment\x1a\r.TimeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'time_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TIMEREQUEST']._serialized_start=14
  _globals['_TIMEREQUEST']._serialized_end=48
  _globals['_TIMERESPONSE']._serialized_start=50
  _globals['_TIMERESPONSE']._serialized_end=89
  _globals['_TIMEADJUSTMENT']._serialized_start=91
  _globals['_TIMEADJUSTMENT']._serialized_end=132
  _globals['_TIMESERVICE']._serialized_start=134
  _globals['_TIMESERVICE']._serialized_end=243
# @@protoc_insertion_point(module_scope)
