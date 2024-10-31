
# Guia para Criar e Gerenciar um Ambiente Virtual em Python

Este guia descreve os passos para criar, ativar e desativar um ambiente virtual em Python. O uso de ambientes virtuais ajuda a manter as dependências de cada projeto isoladas e evita conflitos entre pacotes. Além disso, o guia inclui instruções para configurar o ambiente tanto em sistemas Linux (como Ubuntu) quanto em Windows.

## 1. Requisitos do Sistema

Antes de começar, certifique-se de ter o Python instalado na máquina. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/downloads/).

**Nota:** Durante a instalação do Python no Windows, selecione a opção "Add Python to PATH" para que o Python seja acessível a partir do prompt de comando.

## 2. Criando o Ambiente Virtual

### No Ubuntu (Linux)
1. Abra o terminal e navegue até o diretório do projeto.
2. Execute o comando para criar um ambiente virtual:
   ```bash
   python3 -m venv myenv
   ```
   Isso cria uma pasta chamada `myenv` contendo o ambiente isolado.

### No Windows
1. Abra o `cmd` ou o `PowerShell` e navegue até o diretório do projeto.
2. Execute o comando para criar um ambiente virtual:
   ```bash
   python -m venv myenv
   ```
   Isso cria uma pasta chamada `myenv` contendo o ambiente isolado.

## 3. Ativando o Ambiente Virtual

### No Ubuntu (Linux)
Para ativar o ambiente virtual, execute:
```bash
source myenv/bin/activate
```

### No Windows
Para ativar o ambiente virtual, execute:
- No `cmd`:
  ```bash
  myenv\Scripts\activate
  ```
- No `PowerShell`:
  ```bash
  .\myenv\Scripts\Activate
  ```

Após a ativação, você verá o nome do ambiente (por exemplo, `(myenv)`) no início do prompt, indicando que o ambiente virtual está ativo. Todos os pacotes instalados agora serão isolados para esse ambiente.

## 4. Instalando Dependências

Com o ambiente virtual ativo, você pode instalar todas as dependências necessárias usando o `pip`. Para este projeto, crie ou atualize um arquivo `requirements.txt` com as dependências:

```bash
pip freeze > requirements.txt
```

Para instalar as dependências em outra máquina:
```bash
pip install -r requirements.txt
```

**Nota:** Se o projeto usa bibliotecas que requerem `ffmpeg` (como `yt-dlp` para baixar vídeos do YouTube), certifique-se de instalar o `ffmpeg`:

### Instalando `ffmpeg`

- **Ubuntu (Linux):**
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **Windows:**
  1. Baixe o `ffmpeg` em [ffmpeg.org](https://ffmpeg.org/download.html).
  2. Extraia o arquivo baixado e adicione o diretório `bin` do `ffmpeg` ao PATH do sistema.

## 5. Desativando o Ambiente Virtual

Para sair do ambiente virtual, use o comando:
```bash
deactivate
```

Isso retorna o terminal ao estado padrão, fora do ambiente virtual.

## 6. Executando o Projeto

Certifique-se de que o ambiente virtual esteja ativo e execute o script Python desejado. Por exemplo:
```bash
python video_download.py
```

**Nota:** Se você estiver usando bibliotecas que requerem configuração específica (como `yt-dlp`), siga as instruções adicionais fornecidas na documentação da biblioteca.

---

**Dica:** Sempre que mover o projeto para uma nova máquina, recrie o ambiente virtual e instale as dependências usando o `requirements.txt` para garantir que tudo funcione corretamente.
