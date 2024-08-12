# Daytrade Market Emulator API

Este projeto é uma API simples construída com Flask que simula o comportamento de preços de mercado de ações em tempo real.
A API oferece endpoints para obter dados de mercado atualizados e para acessar dados históricos de preços.

<br>

## Funcionalidades

- Atualização de Preços em Tempo Real: A cada solicitação ao endpoint de dados de mercado, o preço da ação é atualizado aleatoriamente em um intervalo definido.
- Dados Históricos: A API armazena os preços históricos para cada símbolo e permite acessá-los.

<br>

## Endpoints

### 1. `GET /market-data/<symbol>`

Este endpoint retorna o preço atualizado de uma ação específica.

- **Parâmetros**:
  - `symbol`: O símbolo da ação (por exemplo, `AZUL4F`, `PETR4`).

- **Resposta**:
  - Sucesso (200 OK):
    ```json
    {
      "symbol": "AZUL4F",
      "price": 81.45,
      "timestamp": 1691070123000
    }
    ```
  - Erro (404 Not Found):
    ```json
    {
      "error": "Invalid symbol"
    }
    ```

### 2. `GET /historical-data/<symbol>`

Este endpoint retorna os dados históricos de preços para uma ação específica.

- **Parâmetros**:
  - `symbol`: O símbolo da ação (por exemplo, `AZUL4F`, `PETR4`).

- **Resposta**:
  - Sucesso (200 OK):
    ```json
    [
      {
        "price": 81.45,
        "timestamp": 1691070123000
      },
      ...
    ]
    ```
  - Erro (404 Not Found):
    ```json
    {
      "error": "Invalid symbol"
    }
    ```
