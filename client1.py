from base import BaseRabbitMQ, pika


class RabbitClient(BaseRabbitMQ):

    def Publish_msg(self, msg,  queue="", exchange="", exchangge_type=""):

        if exchange:
            self.channel.exchange_declare(
                exchange=exchange , 
                exchange_type=exchangge_type
                )

        else :
            self.channel.queue_declare(
                queue
                )

        self.channel.basic_publish(
            exchange=exchange,
            routing_key=queue,
            body=msg
        )


        print("[+] send a new message succesfully!")

        self.connection.close()



if __name__ == "__main__":

    client = RabbitClient()

    client.Publish_msg(
        msg="hello outside the universe! from fanout@ 111111111111", 
        exchange="testy", 
        exchangge_type="fanout"
        )