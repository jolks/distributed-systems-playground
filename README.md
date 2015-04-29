Distributed Systems Playground
==============================

1. python
  * Just run it...

2. zeromq - follows [Brokerless](http://zeromq.org/whitepapers:brokerless) design.
  * To get it running on Mac OS X (Yosemite):-
  * `$ wget http://download.zeromq.org/zeromq-4.1.0-rc1.tar.gz`
  * `$ tar xvf zeromq-4.1.0-rc1.tar.gz`
  * `$ cd zeromq-4.1.0`
  * `$ ./configure`
  * `$ make`
  * `$ sudo make install`
  * `$ sudo pip3 install pyzmq`
  * Now your machine should be able to support C++ and Python for ØMQ.
  * The hwserver.cpp depends on the lib/zmq.hpp which is obtained from [[1]](https://github.com/zeromq/cppzmq). 
  * `$ g++ hwserver.cpp -o hwserver -lzmq`
  * The `-lzmq` switch is very important to avoid compile time error `Undefined symbols for architecture x86_64:...` [[2]](http://stackoverflow.com/questions/12470117/compile-simple-hello-world-zeromq-c-example-compile-flags).
  * Test by running `hwserver` and `hwclient.py` on separate screens. 
  
   

