from base import BaseRabbitMQ, pika



class RPCServer(BaseRabbitMQ):
    
    def on_msg_func(self, ch, method, props, body):

        self.channel.basic_publish(
            exchange="",
            routing_key=props.reply_to,
            body= "response_data_sample",
            properties=pika.BasicProperties(
                correlation_id=props.correlation_id
            )
        )
        self.channel.basic_ack(delivery_tag=method.delivery_tag)
        


    def cosuming(self):

        self.channel.queue_declare(queue="rpc_queue")
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue="rpc_queue",
            on_message_callback=self.on_msg_func
        )

        print("[x] awaiting for req ...")
        self.channel.start_consuming()




if __name__ == "__main__":

    server = RPCServer()
    server.cosuming()