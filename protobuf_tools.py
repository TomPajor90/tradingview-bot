import struct
from google.protobuf.message import Message

def pack(proto_message: Message, payload_type: int) -> bytes:
    encoded_payload = proto_message.SerializeToString()
    header = struct.pack(">H", payload_type)
    message_length = struct.pack(">I", len(header) + len(encoded_payload))
    return message_length + header + encoded_payload

def unpack(binary_data: bytes, message_class: type) -> Message:
    return message_class.FromString(binary_data[6:])

