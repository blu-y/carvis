# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from erp_driver/erpCmdMsg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class erpCmdMsg(genpy.Message):
  _md5sum = "6c8d779558341c7cf957ab6058219fbb"
  _type = "erp_driver/erpCmdMsg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool e_stop
uint8 gear
uint8 speed
int32 steer
uint8 brake"""
  __slots__ = ['e_stop','gear','speed','steer','brake']
  _slot_types = ['bool','uint8','uint8','int32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       e_stop,gear,speed,steer,brake

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(erpCmdMsg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.e_stop is None:
        self.e_stop = False
      if self.gear is None:
        self.gear = 0
      if self.speed is None:
        self.speed = 0
      if self.steer is None:
        self.steer = 0
      if self.brake is None:
        self.brake = 0
    else:
      self.e_stop = False
      self.gear = 0
      self.speed = 0
      self.steer = 0
      self.brake = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3BiB().pack(_x.e_stop, _x.gear, _x.speed, _x.steer, _x.brake))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.e_stop, _x.gear, _x.speed, _x.steer, _x.brake,) = _get_struct_3BiB().unpack(str[start:end])
      self.e_stop = bool(self.e_stop)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3BiB().pack(_x.e_stop, _x.gear, _x.speed, _x.steer, _x.brake))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.e_stop, _x.gear, _x.speed, _x.steer, _x.brake,) = _get_struct_3BiB().unpack(str[start:end])
      self.e_stop = bool(self.e_stop)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3BiB = None
def _get_struct_3BiB():
    global _struct_3BiB
    if _struct_3BiB is None:
        _struct_3BiB = struct.Struct("<3BiB")
    return _struct_3BiB
