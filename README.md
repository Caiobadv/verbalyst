# 🧠 Verbalyst

Verbalyst é um jogo de adivinhação de palavras baseado em similaridade semântica usando Word2Vec em português. Jogadores tentam adivinhar a palavra secreta, recebendo feedback sobre o quão semanticamente próximas estão as palavras sugeridas.

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/verbalyst.git
cd verbalyst

python3.11 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

pip install -r requirements.txt

Baixe o modelo Word2Vec (Português)
Acesse http://nilc.icmc.usp.br/embeddings
Baixe o arquivo cbow_s50.txt e salve no seu computador. Anote o caminho completo até ele.

Crie um arquivo chamado config_local.json na raiz do projeto com o seguinte conteúdo:

{
  "modelo_path": "/CAMINHO/ATÉ/SEU/cbow_s50.txt"
}