from gensim.models import KeyedVectors

caminho = "/Users/caiobarreto/Desktop/faculdade/Projetos/Verbalyst/verbalyst/cbow_s50.txt"

# Carregar o modelo (formato texto)
print("Carregando o modelo...")
modelo = KeyedVectors.load_word2vec_format(caminho, binary=False)
print("Modelo carregado!")

# Testar similaridades
palavra1 = "gato"
palavra2 = "cachorro"

sim = modelo.similarity(palavra1, palavra2)
print(f"Similaridade entre '{palavra1}' e '{palavra2}': {sim:.4f}")

# Encontrar palavras parecidas
print("\nPalavras mais próximas de 'brasil':")
for palavra, score in modelo.most_similar("brasil", topn=5):
    print(f"{palavra}: {score:.4f}")
