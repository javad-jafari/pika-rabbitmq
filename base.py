import pika
from dataclasses import dataclass



@dataclass
class Setting:

    username:str= "username"
    password:str= "password"
    


setting = Setting()





class BaseRabbitMQ:

    def __init__(self) -> None:
        

        self.pk_url_params = pika.URLParameters(
            url="amqps://{}:{}@rabbit.lmq.cloudamqp.com/{}".format(
                setting.username,
                setting.password,
                setting.username
            )
            )

        self.connection  = pika.BlockingConnection(
            parameters=self.pk_url_params
        )

        self.channel = self.connection.channel()