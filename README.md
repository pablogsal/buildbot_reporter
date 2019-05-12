Buildbot reporter tool
======================

Installation
------------

You can install the tool via pip:

```bash
python -m pip install .
```

or use *pipenv* to manage the virtual environment for you:

```bash
pipenv install
```

Usage
=====

```
Usage: buildbotreporter [OPTIONS] COMMAND [ARGS]...

Options:
  --token TEXT  GitHub personal token to authenticate with the buildbot API
  --help        Show this message and exit.

Commands:
  last-failures  Obtain urls for last failures.
  report         Produce buildbot failure reports from buildbot build urls.
```
  
For example, the following command:
  
```
buildbotreporter report https://buildbot.python.org/all/\#/builders/33/builds/581 --token=MY_GITHUB_TOKEN
```

will produce this report:

```
BUILDBOT FAILURE REPORT
=======================

Builder name: AMD64 Windows8.1 Refleaks 2.7
Builder url: https://buildbot.python.org/all/#/builders/33/
Build url: https://buildbot.python.org/all/#/builders/33/builds/581

Failed tests
------------

- test_connect (test.test_ssl.NetworkedTests)

- test_get_ca_certs_capath (test.test_ssl.NetworkedTests)

- test_connect_with_context (test.test_ssl.NetworkedTests)

- test_context_argument (test.test_urllibnet.urlopen_HttpsTests)

- test_connect_capath (test.test_ssl.NetworkedTests)

- test_connect_ex (test.test_ssl.NetworkedTests)

- test_networked_good_cert (test.test_httplib.HTTPSTest)

- test_get_server_certificate (test.test_ssl.NetworkedTests)

- test_non_blocking_connect_ex (test.test_ssl.NetworkedTests)

- test_connect_cadata (test.test_ssl.NetworkedTests)


Test leaking resources
----------------------

- test_ssl

Build summary
-------------

== Tests result: FAILURE then FAILURE ==

358 tests OK.

10 slowest tests:
- test_bsddb3: 3971.8s
- test_largefile: 533.3s
- test_mailbox: 295.3s
- test_bufio: 281.6s
- test_mmap: 265.2s
- test_multiprocessing: 257.9s
- test_dumbdbm: 142.3s
- test_lib2to3: 125.0s
- test_urllib2_localnet: 118.6s
- test_decimal: 118.4s

3 tests failed:
    test_httplib test_ssl test_urllibnet

42 tests skipped:
    test_aepack test_al test_applesingle test_bsddb185 test_cd test_cl
    test_commands test_crypt test_curses test_dbm test_dl test_epoll
    test_fcntl test_fork1 test_gdb test_gdbm test_gl test_grp
    test_imgfile test_ioctl test_kqueue test_linuxaudiodev test_macos
    test_macostools test_mhlib test_nis test_openpty test_ossaudiodev
    test_pipes test_poll test_posix test_pty test_pwd test_readline
    test_resource test_scriptpackages test_spwd test_sunaudiodev
    test_threadsignals test_wait3 test_wait4 test_zipfile64
2 skips unexpected on win32:
    test_gdb test_readline

3 re-run tests:
    test_httplib test_ssl test_urllibnet

Total duration: 1 hour 22 min


Tracebacks
----------

Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_httplib.py", line 867, in test_networked_good_cert
    h.request('GET', '/')
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 1042, in request
    self._send_request(method, url, body, headers)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 1082, in _send_request
    self.endheaders(body)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 1038, in endheaders
    self._send_output(message_body)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 882, in _send_output
    self.send(msg)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 844, in send
    self.connect()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 1263, in connect
    server_hostname=server_hostname)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 369, in wrap_socket
    _context=self)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 599, in __init__
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1513, in test_connect_capath
    s.connect((REMOTE_HOST, 443))
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 864, in connect
    self._real_connect(addr, False)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 855, in _real_connect
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1618, in test_get_server_certificate
    _test_get_server_certificate(REMOTE_HOST, 443, REMOTE_ROOT_CERT)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1612, in _test_get_server_certificate
    ca_certs=cert)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 1005, in get_server_certificate
    with closing(context.wrap_socket(sock)) as sslsock:
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 369, in wrap_socket
    _context=self)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 599, in __init__
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1646, in test_get_ca_certs_capath
    s.connect((REMOTE_HOST, 443))
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 864, in connect
    self._real_connect(addr, False)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 855, in _real_connect
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1699, in wrap_conn
    self.sock, server_side=True)
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 369, in wrap_socket
    _context=self)
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 599, in __init__
    self.do_handshake()
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
 SSLError: [SSL: NO_SHARED_CIPHER] no shared cipher (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1426, in test_non_blocking_connect_ex
    s.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1391, in test_connect
    s.connect((REMOTE_HOST, 443))
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 864, in connect
    self._real_connect(addr, False)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 855, in _real_connect
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_urllibnet.py", line 212, in test_context_argument
    response = urllib.urlopen("https://self-signed.pythontest.net", context=context)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\urllib.py", line 87, in urlopen
    return opener.open(url)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\urllib.py", line 213, in open
    return getattr(self, name)(url)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\urllib.py", line 443, in open_https
    h.endheaders(data)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 1038, in endheaders
    self._send_output(message_body)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 882, in _send_output
    self.send(msg)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 844, in send
    self.connect()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\httplib.py", line 1263, in connect
    server_hostname=server_hostname)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 369, in wrap_socket
    _context=self)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 599, in __init__
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
IOError: [Errno socket error] [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1699, in wrap_conn
    self.sock, server_side=True)
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 369, in wrap_socket
    _context=self)
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 599, in __init__
    self.do_handshake()
   File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
 SSLError: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (_ssl.c:727)
 server:  new connection from ('127.0.0.1', 61983)
 server: connection cipher is now ('ECDHE-RSA-AES256-SHA', 'TLSv1/SSLv3', 256)
 server: selected protocol is now None


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1495, in test_connect_with_context
    s.connect((REMOTE_HOST, 443))
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 864, in connect
    self._real_connect(addr, False)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 855, in _real_connect
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1540, in test_connect_cadata
    s.connect((REMOTE_HOST, 443))
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 864, in connect
    self._real_connect(addr, False)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 855, in _real_connect
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Traceback (most recent call last):
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\test\test_ssl.py", line 1403, in test_connect_ex
    self.assertEqual(0, s.connect_ex((REMOTE_HOST, 443)))
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 869, in connect_ex
    return self._real_connect(addr, True)
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 855, in _real_connect
    self.do_handshake()
  File "D:\buildarea\2.7.ware-win81-release.refleak\build\lib\ssl.py", line 828, in do_handshake
    self._sslobj.do_handshake()
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)


Current builder status
----------------------

Last builds for the builder are successful. This error might be already fixed or it may be a race condition.

Other builds with similar failures
----------------------------------

-  https://buildbot.python.org/all/#/builders/77/builds/784
-  https://buildbot.python.org/all/#/builders/141/builds/1682
-  https://buildbot.python.org/all/#/builders/53/builds/2838
-  https://buildbot.python.org/all/#/builders/37/builds/795
-  https://buildbot.python.org/all/#/builders/50/builds/797
-  https://buildbot.python.org/all/#/builders/29/builds/799
-  https://buildbot.python.org/all/#/builders/21/builds/2849
-  https://buildbot.python.org/all/#/builders/54/builds/802
-  https://buildbot.python.org/all/#/builders/47/builds/2725
-  https://buildbot.python.org/all/#/builders/144/builds/423
-  https://buildbot.python.org/all/#/builders/58/builds/2345
-  https://buildbot.python.org/all/#/builders/13/builds/2867
-  https://buildbot.python.org/all/#/builders/63/builds/822
-  https://buildbot.python.org/all/#/builders/83/builds/724
-  https://buildbot.python.org/all/#/builders/85/builds/2661
-  https://buildbot.python.org/all/#/builders/31/builds/744
-  https://buildbot.python.org/all/#/builders/90/builds/747
-  https://buildbot.python.org/all/#/builders/145/builds/1531
```
