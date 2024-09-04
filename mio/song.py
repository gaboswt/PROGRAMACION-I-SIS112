import time

# Función para imprimir texto en cursiva
def print_italic(text):
    print(f"\033[3m{text}\033[0m", end=' ', flush=True)

# Añadir 10 líneas en blanco
print("\n" * 10)

# Lista de letras con los tiempos (en segundos)
lyrics = [
    ("If", 0.4), ("the", 0.4), ("sun", 0.8), ("refused", 1), ("to", 0.4), ("shine", 2),
    ("\nBaby,", 0.5), ("would", 0.6), ("I", 0.6), ("still", 0.4), ("be", 0.4), ("your", 0.4), ("lover?", 0.9),
    ("\nWould", 0.6), ("you", 0.4), ("want", 0.4), ("me", 0.4), ("there?", 0.4),
    ("\nIf", 0.4), ("the", 0.4), ("moon", 1), ("went", 0.4), ("dark", 1), ("tonight", 2),
    ("\nAnd", 0.4), ("if", 0.4), ("it", 0.2), ("all", 0.9), ("ended", 0.6), ("tomorrow", 1.1),
    ("\nWould", 0.8), ("I", 0.4), ("be", 0.35), ("the", 0.35), ("one", 0.35), ("on", 0.5), ("your", 0.5), ("mind?", 0.8),
    ("\nYour", 0.5), ("mind?", 0.8), ("Your", 0.5), ("mind?", 1.7),
    ("\nAnd", 0.4), ("if", 0.4), ("it", 0.3), ("all", 0.9), ("ended", 0.6), ("tomorrow", 1.1),
    ("\nWould", 0.8), ("you", 0.4), ("be", 0.4), ("the", 0.5), ("one", 0.4), ("on", 0.4), ("mine?", 0.3), ("<3", 8)
]

for word, delay in lyrics:
    print_italic(word)
    time.sleep(delay)

print("\n")  


