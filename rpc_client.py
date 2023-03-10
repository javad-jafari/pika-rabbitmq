from base import BaseRabbitMQ, pika
import uuid



class RPClient(BaseRabbitMQ):

    def __init__(self) -> None:
        super().__init__()
        
        self.q = self.channel.queue_declare(
            queue="",
            exclusive=True
        )

        self.channel.basic_consume(
            queue=self.q.method.queue,
            auto_ack=True,
            on_message_callback=self.callback_func

        )
        self.response = None
        self.corr_id = None

    def callback_func(self, ch, method, properties, body):

        if self.corr_id == properties.correlation_id:
            
            self.response = body

    
    def call(self):

        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            body="req_data_sample",
            properties=pika.BasicProperties(
                correlation_id=self.corr_id,
                reply_to=self.q.method.queue
            )
        )
        self.connection.process_data_events(time_limit=None)

        return int(self.response)
    

rpc_client = RPClient()

print(" [x] Requesting *** *** *** ")


response = rpc_client.call()

print(" [.] Got %r" % response)