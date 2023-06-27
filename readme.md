Pré-requisitos
Certifique-se de ter o Python 3 instalado em seu sistema. Além disso, é recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

Configuração do ambiente
Crie e ative um ambiente virtual:
```
python3 -m venv myenv
source myenv/bin/activate

```
Instale as dependências:
```
pip install -r requirements.txt
```
Carga inicial de dados
Para realizar a carga inicial de dados, siga os passos abaixo:

``` Execute o comando para enviar os dados para a fila do serviço 2:
python initial_charge.py
Isso enviará as informações dos veículos para a fila, permitindo o processamento assíncrono pelo serviço 2.
```
Aguarde o processamento assíncrono pelo serviço 2 para popular o banco de dados MongoDB.
Rodando os endpoints

Para rodar os endpoints da API-1, execute o seguinte comando:

```
uvicorn main:app --reload
```
Isso iniciará o servidor Uvicorn e carregará o aplicativo principal (main) para atender às solicitações HTTP. Certifique-se de que o serviço esteja em execução antes de realizar as chamadas aos endpoints.

Agora você pode acessar os seguintes endpoints:

````
http://127.0.0.1:8000/docs
````
```
/brands - Retorna as marcas de veículos disponíveis.

/brands/vehicles  - Retorna as informações da marca de veículo com o código especificado.
```