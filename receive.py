#!/usr/bin/env python

import pika

parameters = pika.URLParameters('amqp://rabbitmq:4daa08c6-4b2c-4f25-89c4-b4d36e7519bd@10.0.0.161:5672/%2f')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
method_frame, header_frame, body = channel.basic_get('hello')
if method_frame:
    print method_frame, header_frame, body
    channel.basic_ack(method_frame.delivery_tag)
else:
    print 'No message returned'
