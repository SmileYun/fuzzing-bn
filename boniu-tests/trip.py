#!/usr/bin/env python3

from boofuzz import *


def ps(*args, **kwargs):
    # print(args)
    # print(kwargs)
    # the kwargs contains: target, fuzz_data_logger, session, sock(target)
    pass


def main():
    # Session object is the center of your fuzz.
    # You'll pass it a Target object, which will itself receive a Connection obj.
    # 1. Connection objects implement ITargetConnection,
    session = Session(target=Target(connection=TCPSocketConnection("127.0.0.1", 8021)), sleep_time=1,
                      receive_data_after_fuzz=True, receive_data_after_each_request=True, pre_send_callbacks=[ps])

    # 2. define the message in your protocol. Each message starts with an `s_initialize` function
    create_get_request()
    create_post_request()

    # 3. Once you've defined your messages, you will connect them into a graph using the Session object.
    # return the request with the specified name or the current request if name is not specified.
    # req = s_get("GetRequest")
    req = s_get("PostRequest")
    session.connect(req)

    # 4. ready to fuzz.
    session.fuzz()

    # Notes
    # - making it kick butt is up to you
    # - there are some examples and request definitions in the repository that might help you get started
    # - the log data of each run will be saved to a SQLite databse located in the `boofuzz-results` directory
    #   at your current workdir.
    # - Can reopen the webinterface on any of those databses at any time with `boo open <run-*.db>`

    # To do cool stuff like checking response, use `post_test_case_callbacks` in `Session`,


def create_get_request():
    # GET /path?param= HTTP/1.1
    # Accept: */*
    # Cache-Control: no-cache
    # Host: 127.0.0.1:8021
    # Accept-Encoding: gzip, deflate, br
    # Connection: keep-alive

    s_initialize(name="GetRequest")
    with s_block("Request-Line"):
        s_string("GET", fuzzable=False)
        s_delim(" ", name='space-1', fuzzable=False)
        s_string("/path", name='Request-URI', fuzzable=True)
        s_string('?param=', fuzzable=False)
        s_string("val")
        s_delim(" ", name='space-2', fuzzable=False)
        s_string('HTTP/1.1', fuzzable=False)
        s_static("\r\n")
        s_string('Accept: */*', fuzzable=False)
        s_static("\r\n")
        s_string('Cache-Control: no-cache', fuzzable=False)
        s_static("\r\n")
        s_string('Accept-Encoding: gzip, deflate, br', fuzzable=False)
        s_static("\r\n")
        s_string('Connection: keep-alive', fuzzable=False)
        s_static("\r\n")
        s_string("Host", fuzzable=False)
        s_delim(": ", fuzzable=False)
        s_string("127.0.0.1:8021", fuzzable=False)
        s_static("\r\n")
    s_static("\r\n")

    # s_delim  # push a delimiter onto the current block stack
    # s_string # push a string onto the current block stack
    # s_static # push a static value onto the current block stack


def create_post_request():
    # POST /path HTTP/1.1
    # Host: localhost:8021
    # Accept: */*
    # Content-Type: application/json
    # Content-Length: 10
    # Full-Request   = Request-Line (R-L = Method SP Request-URI SP HTTP-Version CRLF)
    #                         *( General-Header
    #                          | Request-Header
    #                          | Entity-Header)
    #                         CRLF
    #                         [ Entity-Body ]
    s_initialize("PostRequest")
    with s_block("Full-Request"):
        s_string("POST", fuzzable=False)
        s_delim(" ", name='space-1', fuzzable=False)
        s_string("/path", name='Request-URI', fuzzable=False)
        s_delim(" ", name='space-2', fuzzable=False)
        s_string('HTTP/1.1', fuzzable=False)
        s_static("\r\n")
        s_string('Accept: */*', fuzzable=False)
        s_static("\r\n")
        s_string('Cache-Control: no-cache', fuzzable=False)
        s_static("\r\n")
        s_string("Content-Type: application/json; charset=utf-8", name="Entity-Header", fuzzable=False)
        s_static("\r\n")
        s_string("Host", fuzzable=False)
        s_delim(": ", fuzzable=False)
        s_string("127.0.0.1:8021", fuzzable=False)
        s_static("\r\n")

        # s_string('Content-Length: %d' % len("{\"k\": \"vasdsadas\"}"), fuzzable=False)

        s_string("Content-Length: ", fuzzable=False)
        s_size("Body", output_format="ascii", fuzzable=False)

        # s_static("\r\n\r\n")
        s_static("\r\n")
        # s_string("{\"k\": \"v\"}", name="Content1", fuzzable=True)
        # s_string("{\"k\": \"v\"}", name="Content2", fuzzable=True)
        # s_static("\r\n")
    s_static("\r\n")

    with s_block("Body"):
        s_string("{\"k\": \"", fuzzable=False)
        s_string("value")
        s_string("\"}", name="Content1", fuzzable=False)


if __name__ == '__main__':
    main()
