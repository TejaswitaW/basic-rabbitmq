import pika
# creating connection with RabbitMq broker.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Creating channel in the connection.
# Using channel method of connection object
channel = connection.channel()
# We are using default exchange , so we need not create any exchange.
# Creating queue.
# Queue name is "hello"
channel.queue_declare(queue="hello")
# After creating queue then publisher can send message to the exchange,
# so again it will use the channel object.
# Using deafult excahnge so blank("")
# RK is same as queue name.
# Inside body specify message you want to send.
channel.basic_publish(exchange="", routing_key="hello", body="hello_world 2")
print("[x] Sent Hello World")
# Close connection, then channel will also get closed.
connection.close()
