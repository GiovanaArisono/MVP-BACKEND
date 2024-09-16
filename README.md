# PetAdote - Backend

Bem-vindo ao backend da **PetAdote**, a API que suporta nossa plataforma de adoção de animais. Desenvolvido com Flask, este backend gerencia operações relacionadas aos animais disponíveis para adoção.

## Funcionalidades

- **Adicionar Animalzinho**: Permite adicionar um novo animalzinho à base de dados.
- **Consultar Animalzinho**: Recupera informações detalhadas de um animalzinho específico.
- **Listar Animalzinhos**: Obtém uma lista de todos os animais disponíveis para adoção.
- **Remover Animalzinho**: Remove um animalzinho da base de dados.

## Como Executar

### Instalação das Dependências

Certifique-se de ter as bibliotecas Python listadas no `requirements.txt` instaladas. É recomendado usar um ambiente virtual para gerenciar suas dependências.

    (env)$ pip install -r requirements.txt

### Execução da Aplicação

Para iniciar a aplicação, navegue até o diretório raiz do projeto e execute o seguinte comando:

    (env)$ python app.py

Para desenvolvimento, você pode usar o parâmetro `--reload` no Flask para reiniciar automaticamente o servidor após alterações no código. No entanto, este método pode variar dependendo da configuração do seu projeto.

### Acesso à Documentação

Abra [http://localhost:5000](http://localhost:5000) no navegador para acessar a documentação da API gerada pelo Swagger.