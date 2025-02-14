# NLW Unite API

Esta é uma API desenvolvida durante o evento **NLW Unite** da Rocketseat. O projeto permite o gerenciamento de eventos e participantes. Ela oferece funcionalidades para registrar participantes, associar crachás e consultar eventos e suas informações.

## Funcionalidades

### 1. **Registrar Participante em Evento**
   - **Rota**: `POST /events/<event_id>/register`
   - **Descrição**: Permite registrar um participante em um evento específico.

### 2. **Gerar Crachá para Participante**
   - **Rota**: `POST /attendees/<attendee_id>/badge`
   - **Descrição**: Gera um crachá para um participante registrado.

### 3. **Listar Participantes de um Evento**
   - **Rota**: `GET /events/<event_id>/attendees`
   - **Descrição**: Lista todos os participantes de um evento.

### 4. **Listar Todos os Eventos**
   - **Rota**: `GET /events`
   - **Descrição**: Retorna todos os eventos disponíveis.

### 5. **Detalhes de um Evento**
   - **Rota**: `GET /events/<event_id>`
   - **Descrição**: Exibe os detalhes de um evento específico.

## Como Rodar

1. **Clone o repositório**:
     ```bash
    git clone https://github.com/MarcioLucas22/nlw_journey.git
    cd nlw_journey
    ```
    
2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use venv\Scripts\activate
    ```

4. **Instale as dependências**:
     ```bash
     pip install -r requirements.txt
     ```

5. **Execute a aplicação**:
     ```bash
     python app.py
     ```
