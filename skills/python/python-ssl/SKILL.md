---
name: python-ssl
description: "Program with Python's ssl module: This module provides some more Pythonic support for SSL."
version: 1.0.0
tags: [programming, python, ssl, stdlib]
---

# Python: `ssl`

## Overview

This module provides some more Pythonic support for SSL.

Object types:

  SSLSocket -- subtype of socket.socket which does SSL over the socket

Exceptions:

  SSLError -- exception raised for I/O errors

Functions:

  cert_time_to_seconds -- convert time string used for certificate
                          notBefore and notAfter functions to integer
                          seconds past the Epoch (the time values
                          returned from time.time())

  get_server_certificate (addr, ssl_version, ca_certs, timeout) -- Retrieve the
                          certificate from the server at the specified
                          address and return it as a PEM-encoded string


Integer constants:

SSL_ERROR_ZERO_RETURN
SSL_ERROR_WANT_READ
SSL_ERROR_WANT_WRITE
SSL_ERROR_WANT_X509_LOOKUP
SSL_ERROR_SYSCALL
SSL_ERROR_SSL
SSL_ERROR_WANT_CONNECT

SSL_ERROR_EOF
SSL_ERROR_INVALID_ERROR_CODE

The following group define certificate requirements that one side is
allowing/requiring from the other side:

CERT_NONE - no certificates from the other side are required (or will
            be looked at if provided)
CERT_OPTIONAL - certificates are not required, but if provided will be
                validated, and if validation fails, the connection will
                also fail
CERT_REQUIRED - certificates are required, and will be validated, and
                if validation fails, the connection will also fail

The following constants identify various SSL protocol variants:

PROTOCOL_SSLv2
PROTOCOL_SSLv3
PROTOCOL_SSLv23
PROTOCOL_TLS
PROTOCOL_TLS_CLIENT
PROTOCOL_TLS_SERVER
PROTOCOL_TLSv1
PROTOCOL_TLSv1_1
PROTOCOL_TLSv1_2

The following constants identify various SSL alert message descriptions as per
http://www.iana.org/assignments/tls-parameters/tls-parameters.xml#tls-parameters-6

ALERT_DESCRIPTION_CLOSE_NOTIFY
ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
ALERT_DESCRIPTION_BAD_RECORD_MAC
ALERT_DESCRIPTION_RECORD_OVERFLOW
ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
ALERT_DESCRIPTION_HANDSHAKE_FAILURE
ALERT_DESCRIPTION_BAD_CERTIFICATE
ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
ALERT_DESCRIPTION_CERTIFICATE_REVOKED
ALERT_DESCRIPTION_CERTIFICATE_EXPIRED
ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN
ALERT_DESCRIPTION_ILLEGAL_PARAMETER
ALERT_DESCRIPTION_UNKNOWN_CA
ALERT_DESCRIPTION_ACCESS_DENIED
ALERT_DESCRIPTION_DECODE_ERROR
ALERT_DESCRIPTION_DECRYPT_ERROR
ALERT_DESCRIPTION_PROTOCOL_VERSION
ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
ALERT_DESCRIPTION_INTERNAL_ERROR
ALERT_DESCRIPTION_USER_CANCELLED
ALERT_DESCRIPTION_NO_RENEGOTIATION
ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE
ALERT_DESCRIPTION_UNRECOGNIZED_NAME
ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY

## When to use

Reach for `ssl` when your task calls for This module provides some more Pythonic support for SSL. It ships with Python — no dependency to install, available on every interpreter.

## Import

```python
import ssl
```

## Key functions

- `ssl.DER_cert_to_PEM_cert(der_cert_bytes)`
- `ssl.PEM_cert_to_DER_cert(pem_cert_string)`
- `ssl.RAND_add(string, entropy, /)`
- `ssl.RAND_bytes(n, /)`
- `ssl.RAND_status()`
- `ssl.cert_time_to_seconds(cert_time)`
- `ssl.create_connection(address, timeout=<object object at 0x000001B05F3318D0>, source_address=None, *, all_errors=False)`
- `ssl.create_default_context(purpose=<Purpose.SERVER_AUTH: _ASN1Object(nid=129, shortname='serverAuth', longname='TLS Web Server Authentication', oid='1.3.6.1.5.5.7.3.1')>, *, cafile=None, capath=None, cadata=None)`
- `ssl.enum_certificates(store_name)`
- `ssl.enum_crls(store_name)`
- `ssl.get_default_verify_paths()`
- `ssl.get_protocol_name(protocol_code)`
- `ssl.get_server_certificate(addr, ssl_version=<_SSLMethod.PROTOCOL_TLS_CLIENT: 16>, ca_certs=None, timeout=<object object at 0x000001B05F3318D0>)`
- `ssl.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`

## Key classes

`AlertDescription`, `CertificateError`, `DefaultVerifyPaths`, `MemoryBIO`, `Options`, `Purpose`, `SSLCertVerificationError`, `SSLContext`, `SSLEOFError`, `SSLError`, `SSLErrorNumber`, `SSLObject`, `SSLSession`, `SSLSocket`, `SSLSyscallError`, `SSLWantReadError`, `SSLWantWriteError`, `SSLZeroReturnError`, `TLSVersion`, `VerifyFlags`, `VerifyMode`, `socket`, `socket_error`

## Constants / attributes

`ALERT_DESCRIPTION_ACCESS_DENIED`, `ALERT_DESCRIPTION_BAD_CERTIFICATE`, `ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE`, `ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE`, `ALERT_DESCRIPTION_BAD_RECORD_MAC`, `ALERT_DESCRIPTION_CERTIFICATE_EXPIRED`, `ALERT_DESCRIPTION_CERTIFICATE_REVOKED`, `ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN`, `ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE`, `ALERT_DESCRIPTION_CLOSE_NOTIFY`, `ALERT_DESCRIPTION_DECODE_ERROR`, `ALERT_DESCRIPTION_DECOMPRESSION_FAILURE`, `ALERT_DESCRIPTION_DECRYPT_ERROR`, `ALERT_DESCRIPTION_HANDSHAKE_FAILURE`, `ALERT_DESCRIPTION_ILLEGAL_PARAMETER`, `ALERT_DESCRIPTION_INSUFFICIENT_SECURITY`, `ALERT_DESCRIPTION_INTERNAL_ERROR`, `ALERT_DESCRIPTION_NO_RENEGOTIATION`, `ALERT_DESCRIPTION_PROTOCOL_VERSION`, `ALERT_DESCRIPTION_RECORD_OVERFLOW`, `ALERT_DESCRIPTION_UNEXPECTED_MESSAGE`, `ALERT_DESCRIPTION_UNKNOWN_CA`, `ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY`, `ALERT_DESCRIPTION_UNRECOGNIZED_NAME`, `ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE`, `ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION`, `ALERT_DESCRIPTION_USER_CANCELLED`, `CERT_NONE`, `CERT_OPTIONAL`, `CERT_REQUIRED`

## Structuring it in a program

Import once at the top of the module, then call into it where you need it. A
robust pattern wraps the call, handles the errors the module can raise, and
keeps the interface small:

```python
import ssl

def do_work(...):
    """Use ssl to accomplish one well-defined task."""
    result = ssl.DER_cert_to_PEM_cert(...)
    return result
```

- Read the reference below for the exact signatures and exceptions.
- Prefer the highest-level function that does the job; drop to lower-level
  primitives only when you need the control.
- Keep `ssl` calls behind a small function so the rest of your code does not
  depend on its details.

## Full reference (introspected from this machine)

```
Python Library Documentation: module ssl

NAME
    ssl - This module provides some more Pythonic support for SSL.

MODULE REFERENCE
    https://docs.python.org/3.14/library/ssl.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Object types:

      SSLSocket -- subtype of socket.socket which does SSL over the socket

    Exceptions:

      SSLError -- exception raised for I/O errors

    Functions:

      cert_time_to_seconds -- convert time string used for certificate
                              notBefore and notAfter functions to integer
                              seconds past the Epoch (the time values
                              returned from time.time())

      get_server_certificate (addr, ssl_version, ca_certs, timeout) -- Retrieve the
                              certificate from the server at the specified
                              address and return it as a PEM-encoded string


    Integer constants:

    SSL_ERROR_ZERO_RETURN
    SSL_ERROR_WANT_READ
    SSL_ERROR_WANT_WRITE
    SSL_ERROR_WANT_X509_LOOKUP
    SSL_ERROR_SYSCALL
    SSL_ERROR_SSL
    SSL_ERROR_WANT_CONNECT

    SSL_ERROR_EOF
    SSL_ERROR_INVALID_ERROR_CODE

    The following group define certificate requirements that one side is
    allowing/requiring from the other side:

    CERT_NONE - no certificates from the other side are required (or will
                be looked at if provided)
    CERT_OPTIONAL - certificates are not required, but if provided will be
                    validated, and if validation fails, the connection will
                    also fail
    CERT_REQUIRED - certificates are required, and will be validated, and
                    if validation fails, the connection will also fail

    The following constants identify various SSL protocol variants:

    PROTOCOL_SSLv2
    PROTOCOL_SSLv3
    PROTOCOL_SSLv23
    PROTOCOL_TLS
    PROTOCOL_TLS_CLIENT
    PROTOCOL_TLS_SERVER
    PROTOCOL_TLSv1
    PROTOCOL_TLSv1_1
    PROTOCOL_TLSv1_2

    The following constants identify various SSL alert message descriptions as per
    http://www.iana.org/assignments/tls-parameters/tls-parameters.xml#tls-parameters-6

    ALERT_DESCRIPTION_CLOSE_NOTIFY
    ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
    ALERT_DESCRIPTION_BAD_RECORD_MAC
    ALERT_DESCRIPTION_RECORD_OVERFLOW
    ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
    ALERT_DESCRIPTION_HANDSHAKE_FAILURE
    ALERT_DESCRIPTION_BAD_CERTIFICATE
    ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
    ALERT_DESCRIPTION_CERTIFICATE_REVOKED
    ALERT_DESCRIPTION_CERTIFICATE_EXPIRED
    ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN
    ALERT_DESCRIPTION_ILLEGAL_PARAMETER
    ALERT_DESCRIPTION_UNKNOWN_CA
    ALERT_DESCRIPTION_ACCESS_DENIED
    ALERT_DESCRIPTION_DECODE_ERROR
    ALERT_DESCRIPTION_DECRYPT_ERROR
    ALERT_DESCRIPTION_PROTOCOL_VERSION
    ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
    ALERT_DESCRIPTION_INTERNAL_ERROR
    ALERT_DESCRIPTION_USER_CANCELLED
    ALERT_DESCRIPTION_NO_RENEGOTIATION
    ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
    ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE
    ALERT_DESCRIPTION_UNRECOGNIZED_NAME
    ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
    ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
    ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY

CLASSES
    _ssl._SSLContext(builtins.object)
        SSLContext
    builtins.OSError(builtins.Exception)
        SSLError
            SSLCertVerificationError(SSLError, builtins.ValueError)
            SSLEOFError
            SSLSyscallError
            SSLWantReadError
            SSLWantWriteError
            SSLZeroReturnError
    builtins.object
        SSLObject
    builtins.tuple(builtins.object)
        DefaultVerifyPaths
    enum.Enum(builtins.object)
        Purpose(_ASN1Object, enum.Enum)
    enum.IntEnum(builtins.int, enum.ReprEnum)
        AlertDescription
        SSLErrorNumber
        TLSVersion
        VerifyMode
    enum.IntFlag(builtins.int, enum.ReprEnum, enum.Flag)
        Options
        VerifyFlags
    socket.socket(_socket.socket)
        SSLSocket
    _ASN1Object(_ASN1Object)
        Purpose(_ASN1Object, enum.Enum)

    class AlertDescription(enum.IntEnum)
     |  AlertDescription(*values)
     |
     |  An enumeration.
     |
     |  Method resolution order:
     |      AlertDescription
     |      enum.IntEnum
     |      builtins.int
     |      enum.ReprEnum
     |      enum.Enum
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __format__(self, format_spec, /) from builtins.int
     |      Convert to a string according to format_spec.
     |
     |  __new__(cls, value) from enum.Enum
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  ALERT_DESCRIPTION_ACCESS_DENIED = <AlertDescription.ALERT_DESCRIPTION_...
     |
     |  ALERT_DESCRIPTION_BAD_CERTIFICATE = <AlertDescription.ALERT_DESCRIPTIO...
     |
     |  ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE = <AlertDescription.ALERT...
     |
     |  ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE = <AlertDescription....
     |
     |  ALERT_DESCRIPTION_BAD_RECORD_MAC = <AlertDescription.ALERT_DESCRIPTION...
     |
     |  ALERT_DESCRIPTION_CERTIFICATE_EXPIRED = <AlertDescription.ALERT_DESCRI...
     |
     |  ALERT_DESCRIPTION_CERTIFICATE_REVOKED = <AlertDescription.ALERT_DESCRI...
     |
     |  ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN = <AlertDescription.ALERT_DESCRI...
     |
     |  ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE = <AlertDescription.ALERT_D...
     |
     |  ALERT_DESCRIPTION_CLOSE_NOTIFY = <AlertDescription.ALERT_DESCR
```

## Related

Other standard-library modules pair well with `ssl`; explore the `python` domain of this catalog.
