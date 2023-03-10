from base import BaseRabbitMQ



class ServerRabbit(BaseRabbitMQ):


    def callback_msg(self, ch, mehtod, properties, body):

        print("[x] recieve a msg :  {}".format(body))

    
    def consuming(self,exchange_type, queue="", exchange=""):

        if exchange:
            self.channel.exchange_declare(
                exchange=exchange,
                exchange_type=exchange_type
            )

        q = self.channel.queue_declare(queue, exclusive=True)

        if exchange:
            self.channel.queue_bind(
                queue= q.method.queue,
                exchange=exchange
            )

        self.channel.basic_consume(
            queue=queue,
            on_message_callback=self.callback_msg,
            auto_ack=True
        )

        self.channel.start_consuming()


if __name__ == "__main__":
    
    server = ServerRabbit()

    server.consuming(exchange_type="fanout", exchange="testy")
