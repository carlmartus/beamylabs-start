# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traffic_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='traffic_api.proto',
  package='base',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11traffic_api.proto\x12\x04\x62\x61se\x1a\x0c\x63ommon.proto\"9\n\rPlaybackInfos\x12(\n\x0cplaybackInfo\x18\x01 \x03(\x0b\x32\x12.base.PlaybackInfo\"B\n\x0ePlaybackConfig\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\"\n\tnamespace\x18\x02 \x01(\x0b\x32\x0f.base.NameSpace\"^\n\x0cPlaybackInfo\x12,\n\x0eplaybackConfig\x18\x01 \x01(\x0b\x32\x14.base.PlaybackConfig\x12 \n\x04mode\x18\x02 \x01(\x0e\x32\x12.base.PlaybackMode\"@\n\x10PlayBackStatuses\x12,\n\x0eplayBackStatus\x18\x01 \x03(\x0b\x32\x14.base.PlayBackStatus\"\x93\x01\n\x0ePlayBackStatus\x12,\n\x0eplaybackConfig\x18\x01 \x01(\x0b\x32\x14.base.PlaybackConfig\x12\x16\n\x0c\x65rrorMessage\x18\x02 \x01(\tH\x00\x12\r\n\x03\x45OF\x18\x03 \x01(\tH\x00\x12\"\n\x04mode\x18\x04 \x01(\x0e\x32\x12.base.PlaybackModeH\x00\x42\x08\n\x06status*-\n\x0cPlaybackMode\x12\x08\n\x04PLAY\x10\x00\x12\t\n\x05PAUSE\x10\x01\x12\x08\n\x04STOP\x10\x02\x32T\n\x0eTrafficService\x12\x42\n\rStartPlayback\x12\x13.base.PlaybackInfos\x1a\x16.base.PlayBackStatuses\"\x00(\x01\x30\x01\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_PLAYBACKMODE = _descriptor.EnumDescriptor(
  name='PlaybackMode',
  full_name='base.PlaybackMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=480,
  serialized_end=525,
)
_sym_db.RegisterEnumDescriptor(_PLAYBACKMODE)

PlaybackMode = enum_type_wrapper.EnumTypeWrapper(_PLAYBACKMODE)
PLAY = 0
PAUSE = 1
STOP = 2



_PLAYBACKINFOS = _descriptor.Descriptor(
  name='PlaybackInfos',
  full_name='base.PlaybackInfos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playbackInfo', full_name='base.PlaybackInfos.playbackInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=98,
)


_PLAYBACKCONFIG = _descriptor.Descriptor(
  name='PlaybackConfig',
  full_name='base.PlaybackConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='base.PlaybackConfig.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='base.PlaybackConfig.namespace', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=166,
)


_PLAYBACKINFO = _descriptor.Descriptor(
  name='PlaybackInfo',
  full_name='base.PlaybackInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playbackConfig', full_name='base.PlaybackInfo.playbackConfig', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='base.PlaybackInfo.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=262,
)


_PLAYBACKSTATUSES = _descriptor.Descriptor(
  name='PlayBackStatuses',
  full_name='base.PlayBackStatuses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playBackStatus', full_name='base.PlayBackStatuses.playBackStatus', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=328,
)


_PLAYBACKSTATUS = _descriptor.Descriptor(
  name='PlayBackStatus',
  full_name='base.PlayBackStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playbackConfig', full_name='base.PlayBackStatus.playbackConfig', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='base.PlayBackStatus.errorMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EOF', full_name='base.PlayBackStatus.EOF', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='base.PlayBackStatus.mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='status', full_name='base.PlayBackStatus.status',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=331,
  serialized_end=478,
)

_PLAYBACKINFOS.fields_by_name['playbackInfo'].message_type = _PLAYBACKINFO
_PLAYBACKCONFIG.fields_by_name['namespace'].message_type = common__pb2._NAMESPACE
_PLAYBACKINFO.fields_by_name['playbackConfig'].message_type = _PLAYBACKCONFIG
_PLAYBACKINFO.fields_by_name['mode'].enum_type = _PLAYBACKMODE
_PLAYBACKSTATUSES.fields_by_name['playBackStatus'].message_type = _PLAYBACKSTATUS
_PLAYBACKSTATUS.fields_by_name['playbackConfig'].message_type = _PLAYBACKCONFIG
_PLAYBACKSTATUS.fields_by_name['mode'].enum_type = _PLAYBACKMODE
_PLAYBACKSTATUS.oneofs_by_name['status'].fields.append(
  _PLAYBACKSTATUS.fields_by_name['errorMessage'])
_PLAYBACKSTATUS.fields_by_name['errorMessage'].containing_oneof = _PLAYBACKSTATUS.oneofs_by_name['status']
_PLAYBACKSTATUS.oneofs_by_name['status'].fields.append(
  _PLAYBACKSTATUS.fields_by_name['EOF'])
_PLAYBACKSTATUS.fields_by_name['EOF'].containing_oneof = _PLAYBACKSTATUS.oneofs_by_name['status']
_PLAYBACKSTATUS.oneofs_by_name['status'].fields.append(
  _PLAYBACKSTATUS.fields_by_name['mode'])
_PLAYBACKSTATUS.fields_by_name['mode'].containing_oneof = _PLAYBACKSTATUS.oneofs_by_name['status']
DESCRIPTOR.message_types_by_name['PlaybackInfos'] = _PLAYBACKINFOS
DESCRIPTOR.message_types_by_name['PlaybackConfig'] = _PLAYBACKCONFIG
DESCRIPTOR.message_types_by_name['PlaybackInfo'] = _PLAYBACKINFO
DESCRIPTOR.message_types_by_name['PlayBackStatuses'] = _PLAYBACKSTATUSES
DESCRIPTOR.message_types_by_name['PlayBackStatus'] = _PLAYBACKSTATUS
DESCRIPTOR.enum_types_by_name['PlaybackMode'] = _PLAYBACKMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlaybackInfos = _reflection.GeneratedProtocolMessageType('PlaybackInfos', (_message.Message,), {
  'DESCRIPTOR' : _PLAYBACKINFOS,
  '__module__' : 'traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:base.PlaybackInfos)
  })
_sym_db.RegisterMessage(PlaybackInfos)

PlaybackConfig = _reflection.GeneratedProtocolMessageType('PlaybackConfig', (_message.Message,), {
  'DESCRIPTOR' : _PLAYBACKCONFIG,
  '__module__' : 'traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:base.PlaybackConfig)
  })
_sym_db.RegisterMessage(PlaybackConfig)

PlaybackInfo = _reflection.GeneratedProtocolMessageType('PlaybackInfo', (_message.Message,), {
  'DESCRIPTOR' : _PLAYBACKINFO,
  '__module__' : 'traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:base.PlaybackInfo)
  })
_sym_db.RegisterMessage(PlaybackInfo)

PlayBackStatuses = _reflection.GeneratedProtocolMessageType('PlayBackStatuses', (_message.Message,), {
  'DESCRIPTOR' : _PLAYBACKSTATUSES,
  '__module__' : 'traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:base.PlayBackStatuses)
  })
_sym_db.RegisterMessage(PlayBackStatuses)

PlayBackStatus = _reflection.GeneratedProtocolMessageType('PlayBackStatus', (_message.Message,), {
  'DESCRIPTOR' : _PLAYBACKSTATUS,
  '__module__' : 'traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:base.PlayBackStatus)
  })
_sym_db.RegisterMessage(PlayBackStatus)



_TRAFFICSERVICE = _descriptor.ServiceDescriptor(
  name='TrafficService',
  full_name='base.TrafficService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=527,
  serialized_end=611,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartPlayback',
    full_name='base.TrafficService.StartPlayback',
    index=0,
    containing_service=None,
    input_type=_PLAYBACKINFOS,
    output_type=_PLAYBACKSTATUSES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRAFFICSERVICE)

DESCRIPTOR.services_by_name['TrafficService'] = _TRAFFICSERVICE

# @@protoc_insertion_point(module_scope)