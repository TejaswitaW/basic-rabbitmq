import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = "localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="hello")
    # Specify callback function with the queue so that whenever a message posted in the queue,
    # the corresponding callback funciton will get executed.
    # This function prints the incoming message, message is recieved in binary format so %r, it will print the raw message.
    def callback(ch, method, properties, body):
        print("[x] received %r" %body)

    # Associating the callback function with thq queue.
    # auto_ack=True, as soon as the subscriber recives the message from the queue,
    # as soon as the callback function is executed, even before processing the message, it is acknowledging back to the messsage queue,
    # so that queue can delete this particular message from itself, if we do not do this then message will keep on lingering in the message 
    # queue, it will not be automatically deleted, so there will be a memory problem, because as the number of incoming messages increase,
    # they keep on piling inside the message queue and they will keep on consuming the memory.
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack = True)

    print(" [*] waiting for the messages. To exit press Ctrl-C")

    # Start listening queue.
    # Start consuming messages from the queue.
    # This is the blocking call.
    # The program will go into a loop , it will just keep on listening to the queue and as soon as the message is recieved in the queue,
    # the corresponding callback function will get executed.
    # It is infinite loop so press Ctrl+C to interrupt the program, so we have used in try-except block.
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

