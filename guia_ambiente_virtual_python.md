
# Guia para Criar e Gerenciar um Ambiente Virtual em Python

Este guia descreve os passos para criar, ativar e desativar um ambiente virtual em Python. O uso de ambientes virtuais ajuda a manter as dependências de cada projeto isoladas e evita conflitos entre pacotes.

## 1. Criando o Ambiente Virtual

Para criar um novo ambiente virtual, siga os passos abaixo:

1. Abra o terminal e navegue até o diretório onde deseja criar o ambiente virtual.
2. Execute o comando abaixo, substituindo `myenv` pelo nome que deseja dar ao ambiente virtual:

   ```bash
   python3 -m venv myenv
   ```

   Isso cria uma pasta chamada `myenv` (ou o nome que você escolheu), contendo o ambiente isolado.

## 2. Ativando o Ambiente Virtual

Para ativar o ambiente virtual, execute o seguinte comando no terminal:

```bash
source myenv/bin/activate
```

Após a ativação, você verá o nome do ambiente (por exemplo, `(myenv)`) no início do prompt do terminal, indicando que o ambiente virtual está ativo. Todos os pacotes instalados agora serão isolados para esse ambiente.

## 3. Instalando Pacotes no Ambiente Virtual

Enquanto o ambiente virtual estiver ativo, você pode instalar pacotes sem afetar o sistema global. Por exemplo:

```bash
pip install nome-do-pacote
```

Esses pacotes estarão disponíveis apenas no ambiente virtual que você criou.

## 4. Desativando o Ambiente Virtual

Quando terminar de trabalhar no ambiente virtual, desative-o com o comando:

```bash
deactivate
```

Isso retorna o terminal ao estado padrão, saindo do ambiente virtual.

---

**Nota:** Sempre que iniciar um novo trabalho ou projeto em Python, é recomendado criar um novo ambiente virtual para manter as dependências isoladas.
