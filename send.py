import pika

parameters = pika.URLParameters('amqps://admin:b9afcf0373310067792a1c8c1a9df6264a88cc1a@10.8.59.81:5671/%2f')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
