import pika

parameters = pika.URLParameters('amqp://rabbitmq:4daa08c6-4b2c-4f25-89c4-b4d36e7519bd@10.0.0.161:5672/%2f')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
