# Calculadora de Rede IPv4

## Trabalho de Fundamentos de Redes de Computadores

**Professor:** CÁSSIO DAVID BORRALHO PINHEIRO

**Alunos:** Carlos Davi Gomes Pereira, Matheus de Jesus Sousa, Silvestre Bentes Cardoso

## Objetivo

Este trabalho tem como objetivo desenvolver um programa em Python que, dado um **Endereço IP** e uma **Máscara de Rede**, calcula:

1. O **Endereço da Rede**
2. O **Endereço de Broadcast**
3. A **Faixa de Endereços Válidos**

---

## Estrutura do projeto

* `calculadora_rede.py`: arquivo principal com o código Python.
* `README.md`: este arquivo, explicando o projeto e os testes.
* `casos_de_teste.txt` (opcional): lista de entradas e saídas usadas para teste.

---

## Como executar no VS Code

1. Abra o VS Code e abra a pasta do projeto.
2. Certifique-se de que a extensão Python está instalada.
3. Abra o arquivo `calculadora_rede.py`.
4. Clique em **Run Python File** ou pressione **F5**.
5. No terminal integrado do VS Code:

   * Digite o **Endereço IP**.
   * Digite a **Máscara de Rede**.
6. O programa exibirá:

   * Endereço da Rede
   * Endereço de Broadcast
   * Faixa de Endereços Válidos

Para encerrar, digite `sair` quando o programa pedir o IP.

---

## Casos de teste

### Caso 1

* **IP:** 192.168.1.10
* **Máscara:** 255.255.255.0
* **Saída esperada:**

```
Endereço da Rede: 192.168.1.0
Endereço de Broadcast: 192.168.1.255
Faixa de Endereços Válidos: 192.168.1.1 a 192.168.1.254
```

### Caso 2

* **IP:** 10.0.0.5
* **Máscara:** 255.255.255.252
* **Saída esperada:**

```
Endereço da Rede: 10.0.0.4
Endereço de Broadcast: 10.0.0.7
Faixa de Endereços Válidos: 10.0.0.5 a 10.0.0.6
```

---

## Observações

* O programa valida IP e máscara, exibindo mensagem de erro se forem inválidos.
* Funciona com qualquer endereço IPv4 válido.
* Feito para fins acadêmicos e demonstração de conceitos de redes.
