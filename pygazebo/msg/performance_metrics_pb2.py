# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: performance_metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='performance_metrics.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19performance_metrics.proto\x12\x0bgazebo.msgs\"\xe5\x01\n\x12PerformanceMetrics\x12\x1b\n\x10real_time_factor\x18\x01 \x02(\x01:\x01\x30\x12H\n\x06sensor\x18\x02 \x03(\x0b\x32\x38.gazebo.msgs.PerformanceMetrics.PerformanceSensorMetrics\x1ah\n\x18PerformanceSensorMetrics\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x18\n\x10real_update_rate\x18\x02 \x02(\x01\x12\x17\n\x0fsim_update_rate\x18\x03 \x02(\x01\x12\x0b\n\x03\x66ps\x18\x04 \x01(\x01')
)




_PERFORMANCEMETRICS_PERFORMANCESENSORMETRICS = _descriptor.Descriptor(
  name='PerformanceSensorMetrics',
  full_name='gazebo.msgs.PerformanceMetrics.PerformanceSensorMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.PerformanceMetrics.PerformanceSensorMetrics.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='real_update_rate', full_name='gazebo.msgs.PerformanceMetrics.PerformanceSensorMetrics.real_update_rate', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sim_update_rate', full_name='gazebo.msgs.PerformanceMetrics.PerformanceSensorMetrics.sim_update_rate', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fps', full_name='gazebo.msgs.PerformanceMetrics.PerformanceSensorMetrics.fps', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=272,
)

_PERFORMANCEMETRICS = _descriptor.Descriptor(
  name='PerformanceMetrics',
  full_name='gazebo.msgs.PerformanceMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='real_time_factor', full_name='gazebo.msgs.PerformanceMetrics.real_time_factor', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor', full_name='gazebo.msgs.PerformanceMetrics.sensor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PERFORMANCEMETRICS_PERFORMANCESENSORMETRICS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=272,
)

_PERFORMANCEMETRICS_PERFORMANCESENSORMETRICS.containing_type = _PERFORMANCEMETRICS
_PERFORMANCEMETRICS.fields_by_name['sensor'].message_type = _PERFORMANCEMETRICS_PERFORMANCESENSORMETRICS
DESCRIPTOR.message_types_by_name['PerformanceMetrics'] = _PERFORMANCEMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PerformanceMetrics = _reflection.GeneratedProtocolMessageType('PerformanceMetrics', (_message.Message,), dict(

  PerformanceSensorMetrics = _reflection.GeneratedProtocolMessageType('PerformanceSensorMetrics', (_message.Message,), dict(
    DESCRIPTOR = _PERFORMANCEMETRICS_PERFORMANCESENSORMETRICS,
    __module__ = 'performance_metrics_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.PerformanceMetrics.PerformanceSensorMetrics)
    ))
  ,
  DESCRIPTOR = _PERFORMANCEMETRICS,
  __module__ = 'performance_metrics_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.PerformanceMetrics)
  ))
_sym_db.RegisterMessage(PerformanceMetrics)
_sym_db.RegisterMessage(PerformanceMetrics.PerformanceSensorMetrics)


# @@protoc_insertion_point(module_scope)
