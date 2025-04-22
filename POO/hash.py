import hashlib

texto = "Minha mensagem secreta"
hash_gerado = hashlib.sha256(texto.encode()).hexdigest()

print("Hash SHA-256:", hash_gerado)
