#!/usr/bin/env python

import pika

parameters = pika.URLParameters('amqps://admin:3de4922d8b6ac5a1aad9@172.24.4.5:5671/%2f')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
method_frame, header_frame, body = channel.basic_get('hello')
if method_frame:
    print method_frame, header_frame, body
    channel.basic_ack(method_frame.delivery_tag)
else:
    print 'No message returned'
