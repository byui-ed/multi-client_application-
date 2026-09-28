# multi-client_application- (Multi-Client Python Networking Application)
# Overview

As a software engineer, my goal with this project was to deepen my understanding of low-level network protocols, socket programming, and concurrent connection management in Python. Building networking tools from scratch allows me to master how distributed systems communicate, handle state, and manage data serialization over raw TCP connections.

This project consists of a multi-threaded TCP Client-Server networking application. The Server operates continuously to accept multiple incoming client socket connections, processing commands sequentially per thread. The Client provides an interactive command-line interface that allows users to send structured requests to the server and receive formatted responses in real time.

How to Run the Software
Start the Server:

Open a terminal or IDE prompt and navigate to the project root.

Run the server script first:

Bash
python server.py
The server will initialize and begin listening on 127.0.0.1:65432.

Start the Client(s):

Open a separate terminal window (or multiple terminal windows to test concurrent multi-client support).

Run the client script:

Bash
python client.py
Once connected, type any supported command into the prompt (TIME, ECHO <msg>, or STATS).

Type EXIT or QUIT to safely terminate the client connection.

Purpose
The purpose of writing this software is to gain hands-on experience with:

Establishing persistent network socket connections using standard network protocols.

Implementing multi-threading on the server side to handle multiple client sessions concurrently without blocking execution.

Building command parsing logic and error handling for socket communications.

[Software Demo Video](https://youtu.be/6hq06tOnwbc)

# Network Communication

Architecture
This application follows a Client-Server Architecture. The server acts as a centralized host that listens for incoming connection requests on a dedicated port. Upon connection, the server spawns a dedicated daemon thread for each client, maintaining isolated communication streams while sharing thread-safe global server metrics.

Protocol and Ports
Protocol: TCP (Transmission Control Protocol) using socket.SOCK_STREAM.

IP Address: 127.0.0.1 (Localhost).

Port: 65432 (Non-privileged high port).

Message Format
Communication occurs over UTF-8 encoded text payloads:

Client Requests: Plain text string commands sent over the TCP stream (TIME, ECHO <msg>, or STATS).

Server Responses: Formatted string messages returned to the client containing timestamps, transformed text with length metadata, or formatted uptime and request count statistics.

# Development Environment

Tools & IDE
PyCharm (Community/Professional Edition) as the primary Integrated Development Environment.

Git & GitHub for version control and source code management.

Language & Libraries
Language: Python 3.x

Standard Libraries:

socket: Low-level networking interface for creating TCP sockets.

threading: Concurrent thread execution and lock synchronization (threading.Lock) for safe multi-client request counting.

datetime & time: Server runtime metrics and timestamp generation.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](https://docs.python.org/3/library/socket.html?utm_source=gemini)
* [Web Site Name](https://realpython.com/python-sockets/?utm_source=gemini)
* [Web Site Name](https://docs.python.org/3/library/threading.html?utm_source=gemini)

# Future Work
JSON Payload Serialization: Upgrade string message passing to structured JSON payloads for extensible request/response objects.

Authentication & TLS Encryption: Add SSL/TLS wrappers to secure socket communication between client and server.

Graceful Server Shutdown: Implement keyboard interrupt listeners (Ctrl+C) on the server to safely close all active client threads and open sockets before terminating.

