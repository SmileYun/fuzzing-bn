## Install

```sh
$ mkdir boofuzz && cd boofuzz
$ python3
```

### To understand what `yield` does

- Iterables

When you create a list you can read its items one by one - called iteration

```python
my_list = [1, 2, 3]
for i in my_list:
    print(i)
    
1
2
3
```

`my_list` is an iterable. Everything you can use `for ... in ...` on is an iterable; eg. lists, strings, files...

```python
my_list = [x*x for x in range(3)]
for i in my_list:
    print(i)
0
1
4
```

- Generators

Generators are iterators, a kind of iterable **you can only iterate over once**. 
Generators do not store all the values in memory, they generate the values on the fly.

```python
# generator
g = (x*x for x in range(3))
for i in g:
     print(i)
# output
0
1
4

for i in g:
    print(i)
# nothing output
``` 

The generator is just the same except you used `()` instead of `[]`. BUT, you cannot perform `for i in mygenerator` a 
second time since generators can only be used once; they calculate 0, 
then forget about it and calculate 1, and end calculating 4, one by one.

- Yield

`yield` is a keyword that is used like `return`, except the function will return a generator.

```python
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        
mygenerator = createGenerator() # create a generator

print(mygenerator) # mygenerator is an object!

# output: <generator object createGenerator at 0xb7555c34>

for i in mygenerator:
    print(i)
# output
0
1
4
```


### Http Protocol

#### Request

A request message from a client to a server includes, within the first line of that message, the method to be applied 
to the resource, the identifier of the resource, and the protocol version in use. 
For backwards compatibility with the more limited HTTP/0.9 protocol, there are two valid formats for an HTTP request:

```
Request        = Simple-Request | Full-Request

Simple-Request = "GET" SP Request-URI CRLF

Full-Request   = Request-Line            
                *( General-Header         
                 | Request-Header          
                 | Entity-Header )         
                CRLF
                [ Entity- -m venv env
$ source env/bin/activate
(env) $ pip install -U pip setuptools
(env) $ pip install boofuzzBody ]
                
Request-Line = Method SP Request-URI SP HTTP-Version CRLF

- CR:   Carriage Return，对应ASCII中转义字符\r，表示回车
- LF:   Linefeed，对应ASCII中转义字符\n，表示换行
- CRLF: Carriage Return & Linefeed，\r\n，表示回车并换行         
```

Notes: If an HTTP/1.1 server receives a Simple-Request, it must respond with an HTTP/0.9 Simple-Response.
An HTTP/1.1 client must never generate a Simple-Request.


##### Request-Line

The `Request-Line` begins with a method token, followed by the `Request-URI` and the protocol version, and ending with `CRLF`. 
The elements are separated by `SP` characters. No `CR` or `LF` are allowed except in the final `CRLF` sequence.

`Request-Line = Method SP Request-URI SP HTTP-Version CRLF`

Note that the difference between a `Simple-Request` and the `Request-Line` of a `Full-Request` is the presence of 
the `HTTP-Version` field and the availability of methods other than `GET`.

1. Method

The Method token indicates the method to be performed on the resource identified by the Request-URI. The method is case-sensitive.

```
Method    = "OPTIONS"
          | "GET"    
          | "HEAD"   
          | "POST"   
          | "PUT"    
          | "PATCH"  
          | "COPY"   
          | "MOVE"   
          | "DELETE" 
          | "LINK"   
          | "UNLINK" 
          | "TRACE"  
          | "WRAPPED"
          | extension-method
extension-method = token
```

2. Request-URI

The Request-URI is a Uniform Resource Identifier [Section 3.2](!https://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Request) 
and identifies the resource upon which to apply the request.

`Request-URI    = "*" | absoluteURI | abs_path`

The three options for Request-URI are dependent on the nature of the request. 
The asterisk "*" means that the request does not apply to a particular resource, but to the server itself, 
and is only allowed when the Method used does not necessarily apply to a resource. One example would be

`OPTIONS * HTTP/1.1`














