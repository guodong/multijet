# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fpm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qpb_pb2 as qpb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fpm.proto',
  package='fpm',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\tfpm.proto\x12\x03\x66pm\x1a\tqpb.proto\"L\n\x07Nexthop\x12 \n\x05if_id\x18\x02 \x01(\x0b\x32\x11.qpb.IfIdentifier\x12\x1f\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x0e.qpb.L3Address\")\n\x08RouteKey\x12\x1d\n\x06prefix\x18\x01 \x01(\x0b\x32\r.qpb.L3Prefix\"\x98\x01\n\x0b\x44\x65leteRoute\x12\x0e\n\x06vrf_id\x18\x01 \x02(\r\x12*\n\x0e\x61\x64\x64ress_family\x18\x02 \x02(\x0e\x32\x12.qpb.AddressFamily\x12\x31\n\x12sub_address_family\x18\x03 \x02(\x0e\x32\x15.qpb.SubAddressFamily\x12\x1a\n\x03key\x18\x04 \x02(\x0b\x32\r.fpm.RouteKey\"\x8a\x02\n\x08\x41\x64\x64Route\x12\x0e\n\x06vrf_id\x18\x01 \x02(\r\x12*\n\x0e\x61\x64\x64ress_family\x18\x02 \x02(\x0e\x32\x12.qpb.AddressFamily\x12\x31\n\x12sub_address_family\x18\x03 \x02(\x0e\x32\x15.qpb.SubAddressFamily\x12\x1a\n\x03key\x18\x04 \x02(\x0b\x32\r.fpm.RouteKey\x12\"\n\nroute_type\x18\x05 \x01(\x0e\x32\x0e.fpm.RouteType\x12\x1f\n\x08protocol\x18\x06 \x02(\x0e\x32\r.qpb.Protocol\x12\x0e\n\x06metric\x18\x08 \x02(\x05\x12\x1e\n\x08nexthops\x18\t \x03(\x0b\x32\x0c.fpm.Nexthop\"\xae\x01\n\x07Message\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.fpm.Message.Type\x12 \n\tadd_route\x18\x02 \x01(\x0b\x32\r.fpm.AddRoute\x12&\n\x0c\x64\x65lete_route\x18\x03 \x01(\x0b\x32\x10.fpm.DeleteRoute\"8\n\x04Type\x12\x0f\n\x0bUNKNOWN_MSG\x10\x00\x12\r\n\tADD_ROUTE\x10\x01\x12\x10\n\x0c\x44\x45LETE_ROUTE\x10\x02*D\n\tRouteType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0f\n\x0bUNREACHABLE\x10\x02\x12\r\n\tBLACKHOLE\x10\x03')
  ,
  dependencies=[qpb__pb2.DESCRIPTOR,])

_ROUTETYPE = _descriptor.EnumDescriptor(
  name='RouteType',
  full_name='fpm.RouteType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREACHABLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACKHOLE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=751,
  serialized_end=819,
)
_sym_db.RegisterEnumDescriptor(_ROUTETYPE)

RouteType = enum_type_wrapper.EnumTypeWrapper(_ROUTETYPE)
UNKNOWN = 0
NORMAL = 1
UNREACHABLE = 2
BLACKHOLE = 3


_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='fpm.Message.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MSG', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_ROUTE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_ROUTE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=693,
  serialized_end=749,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)


_NEXTHOP = _descriptor.Descriptor(
  name='Nexthop',
  full_name='fpm.Nexthop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_id', full_name='fpm.Nexthop.if_id', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='fpm.Nexthop.address', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=105,
)


_ROUTEKEY = _descriptor.Descriptor(
  name='RouteKey',
  full_name='fpm.RouteKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefix', full_name='fpm.RouteKey.prefix', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=148,
)


_DELETEROUTE = _descriptor.Descriptor(
  name='DeleteRoute',
  full_name='fpm.DeleteRoute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_id', full_name='fpm.DeleteRoute.vrf_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address_family', full_name='fpm.DeleteRoute.address_family', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_address_family', full_name='fpm.DeleteRoute.sub_address_family', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='fpm.DeleteRoute.key', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=303,
)


_ADDROUTE = _descriptor.Descriptor(
  name='AddRoute',
  full_name='fpm.AddRoute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_id', full_name='fpm.AddRoute.vrf_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address_family', full_name='fpm.AddRoute.address_family', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_address_family', full_name='fpm.AddRoute.sub_address_family', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='fpm.AddRoute.key', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route_type', full_name='fpm.AddRoute.route_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='fpm.AddRoute.protocol', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric', full_name='fpm.AddRoute.metric', index=6,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nexthops', full_name='fpm.AddRoute.nexthops', index=7,
      number=9, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=572,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='fpm.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='fpm.Message.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_route', full_name='fpm.Message.add_route', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_route', full_name='fpm.Message.delete_route', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=575,
  serialized_end=749,
)

_NEXTHOP.fields_by_name['if_id'].message_type = qpb__pb2._IFIDENTIFIER
_NEXTHOP.fields_by_name['address'].message_type = qpb__pb2._L3ADDRESS
_ROUTEKEY.fields_by_name['prefix'].message_type = qpb__pb2._L3PREFIX
_DELETEROUTE.fields_by_name['address_family'].enum_type = qpb__pb2._ADDRESSFAMILY
_DELETEROUTE.fields_by_name['sub_address_family'].enum_type = qpb__pb2._SUBADDRESSFAMILY
_DELETEROUTE.fields_by_name['key'].message_type = _ROUTEKEY
_ADDROUTE.fields_by_name['address_family'].enum_type = qpb__pb2._ADDRESSFAMILY
_ADDROUTE.fields_by_name['sub_address_family'].enum_type = qpb__pb2._SUBADDRESSFAMILY
_ADDROUTE.fields_by_name['key'].message_type = _ROUTEKEY
_ADDROUTE.fields_by_name['route_type'].enum_type = _ROUTETYPE
_ADDROUTE.fields_by_name['protocol'].enum_type = qpb__pb2._PROTOCOL
_ADDROUTE.fields_by_name['nexthops'].message_type = _NEXTHOP
_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE.fields_by_name['add_route'].message_type = _ADDROUTE
_MESSAGE.fields_by_name['delete_route'].message_type = _DELETEROUTE
_MESSAGE_TYPE.containing_type = _MESSAGE
DESCRIPTOR.message_types_by_name['Nexthop'] = _NEXTHOP
DESCRIPTOR.message_types_by_name['RouteKey'] = _ROUTEKEY
DESCRIPTOR.message_types_by_name['DeleteRoute'] = _DELETEROUTE
DESCRIPTOR.message_types_by_name['AddRoute'] = _ADDROUTE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['RouteType'] = _ROUTETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Nexthop = _reflection.GeneratedProtocolMessageType('Nexthop', (_message.Message,), dict(
  DESCRIPTOR = _NEXTHOP,
  __module__ = 'fpm_pb2'
  # @@protoc_insertion_point(class_scope:fpm.Nexthop)
  ))
_sym_db.RegisterMessage(Nexthop)

RouteKey = _reflection.GeneratedProtocolMessageType('RouteKey', (_message.Message,), dict(
  DESCRIPTOR = _ROUTEKEY,
  __module__ = 'fpm_pb2'
  # @@protoc_insertion_point(class_scope:fpm.RouteKey)
  ))
_sym_db.RegisterMessage(RouteKey)

DeleteRoute = _reflection.GeneratedProtocolMessageType('DeleteRoute', (_message.Message,), dict(
  DESCRIPTOR = _DELETEROUTE,
  __module__ = 'fpm_pb2'
  # @@protoc_insertion_point(class_scope:fpm.DeleteRoute)
  ))
_sym_db.RegisterMessage(DeleteRoute)

AddRoute = _reflection.GeneratedProtocolMessageType('AddRoute', (_message.Message,), dict(
  DESCRIPTOR = _ADDROUTE,
  __module__ = 'fpm_pb2'
  # @@protoc_insertion_point(class_scope:fpm.AddRoute)
  ))
_sym_db.RegisterMessage(AddRoute)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'fpm_pb2'
  # @@protoc_insertion_point(class_scope:fpm.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)