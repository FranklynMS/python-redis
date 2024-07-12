import redis

# Configuración de Redis
redis_host = 'redis-14100.c263.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 14100  # Cambia al puerto correspondiente
redis_password = 'zgC4nA1hE1N5oFEDGsdp6PHZSJNOEki1'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Suscriptor
def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()