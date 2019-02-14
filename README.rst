The websocket stomp listener
===========================
A websocket is an http protocol which is upgraed into a websocket connection. This connection is bi-directional and persistent which allows for low-latency, high volume and high frequency communication.

The stomp protocol is a Simple Text Orientated Messaging Protocol. It is built on top of the websocket and is utilized to establish connections to the stomp broker. 

Environment.
------------
The listener can be built with pip, setuptools, pipenv or poetry. Just go to the main directory and run the environment. The environment can also just ba accessed by downloading the tarball and running.
..codeblock:: bash
  curl https://github.com/Iamtheapexpredator/websocket-stomp-client-example/dist/websocket_stomp_client-0.1.0-py3-none-any.whl| pip install

Running the Listener:
-------------
Make sure that the websocket server is running. Once the server is running double check the URI in the script, then run the script. The listener should connect to the websocket server, then begin updating.
