# Relatório de Análise de Dados – Walmart Sales Data Analysis

**Autor:** Rafael  
**Objetivo:** Extrair insights estratégicos a partir dos dados de vendas da Walmart, utilizando queries SQL para responder a questões de negócio.

---

## 1️⃣ Analisar Métodos de Pagamento e Vendas  
**Query:**  
```sql
SELECT 
    payment_method, 
    COUNT(*) AS num_transacoes, 
    SUM(quantity) AS total_itens_vendidos 
FROM walmart
GROUP BY payment_method
ORDER BY num_transacoes DESC;
```  
**Resultado:**  
- Métodos identificados: *Ewallet*, *Cash* e *Credit card*.  

**Insight:**  
Os três métodos de pagamento principais foram identificados, o que possibilita entender as preferências dos clientes e orientar estratégias de otimização dos processos de pagamento.

---

## 2️⃣ Identificar a Categoria Mais Bem Avaliada em Cada Filial  
**Query:**  
```sql
SELECT *
FROM (
    SELECT 
        branch, 
        category, 
        AVG(rating) AS avg_rating, 
        RANK() OVER (PARTITION BY branch ORDER BY AVG(rating) DESC) AS ranking 
    FROM walmart 
    GROUP BY branch, category
) AS ranked
WHERE ranking = 1;
```  
**Resultado (exemplos):**  
- *WALM001*: **Electronic accessories** (avg rating: 7.45)  
- *WALM002*: **Food and beverages** (avg rating: 8.25)  
- *WALM003*: **Sports and travel** (avg rating: 7.5)  
- *(Outros resultados para demais filiais)*

**Insight:**  
A identificação das categorias com melhor avaliação por filial permite direcionar promoções e campanhas específicas para fortalecer o desempenho e a satisfação dos clientes em cada localidade.

---

## 3️⃣ Determinar o Dia Mais Movimentado em Cada Filial  
**Query:**  
```sql
SELECT *
FROM (
    SELECT 
        branch, 
        DAYNAME(STR_TO_DATE(date, '%d/%m/%y')) AS day_name, 
        COUNT(*) AS num_transacoes, 
        RANK() OVER (PARTITION BY branch ORDER BY COUNT(*) DESC) AS ranking 
    FROM walmart 
    GROUP BY branch, day_name
) AS ranked
WHERE ranking = 1;
```  
**Resultado (exemplos):**  
- *WALM001*: **Thursday** (16 transações)  
- *WALM002*: **Thursday** (15 transações)  
- *WALM003*: **Tuesday** (33 transações)  
- *(Outros resultados para demais filiais)*

**Insight:**  
Saber qual o dia da semana com maior volume de transações em cada filial permite otimizar a alocação de recursos, ajustando o gerenciamento de equipe e o controle de estoque para os períodos de pico.

---

## 4️⃣ Calcular a Quantidade Total Vendida por Método de Pagamento  
**Query:**  
```sql
SELECT
    payment_method,
    SUM(quantity) AS total_itens_vendidos 
FROM walmart
GROUP BY payment_method
ORDER BY total_itens_vendidos DESC;
```  
**Resultado:**  
- *Ewallet*: 8932 itens  
- *Cash*: 4984 itens  
- *Credit card*: 9567 itens

**Insight:**  
O acompanhamento da quantidade de itens vendidos por cada método fornece uma visão clara dos hábitos de compra dos clientes, permitindo estratégias de vendas e marketing mais direcionadas.

---

## 5️⃣ Analisar as Avaliações de Categorias por Cidade  
**Query:**  
```sql
SELECT
    city,
    category,
    MIN(rating) AS min_rating,
    MAX(rating) AS max_rating,
    AVG(rating) AS avg_rating 
FROM walmart
GROUP BY city, category
ORDER BY city, avg_rating DESC;
```  
**Resultado (exemplos):**  
- *San Antonio* – **Health and beauty**: min 5, max 9.1, avg 7.05  
- *Harlingen* – **Electronic accessories**: min, max e avg 9.6  
- *Haltom City* – **Home and lifestyle**: min 3, max 9.5, avg ≈6.23  
- *(Outros resultados para demais cidades)*

**Insight:**  
A análise das avaliações por categoria e cidade permite identificar áreas de oportunidade para promoções regionais e melhorias na experiência do cliente, ajustando estratégias de acordo com as preferências locais.

---

## 6️⃣ Calcular o Lucro Total por Categoria  
**Query (exemplo):**  
```sql
SELECT
    category,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(total * profit_margin), 2) AS total_profit 
FROM walmart
GROUP BY category
ORDER BY total_profit DESC;
```  
**Resultado (exemplos):**  
- *Fashion accessories*: total revenue ≈489480.90, profit ≈192314.89  
- *Home and lifestyle*: total revenue ≈489250.06, profit ≈192213.64  
- *Electronic accessories*: total revenue ≈78175.03, profit ≈30772.49  
- *(Outros resultados para demais categorias)*

**Insight:**  
A classificação das categorias com base no lucro total fornece uma base para focar esforços de expansão e ajustes de precificação, priorizando os segmentos mais rentáveis.

---

## 7️⃣ Determinar o Método de Pagamento Mais Utilizado em Cada Filial  
**Query:**  
```sql
WITH cte AS (
    SELECT
        branch,
        payment_method,
        COUNT(*) AS total_trans,
        RANK() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS ranking
    FROM walmart 
    GROUP BY branch, payment_method
)
SELECT * FROM cte WHERE ranking = 1;
```  
**Resultado (exemplos):**  
- *WALM001*: **Ewallet** (45 transações)  
- *WALM002*: **Ewallet** (37 transações)  
- *WALM003*: **Credit card** (115 transações)  
- *(Outros resultados para demais filiais)*

**Insight:**  
Entender qual método de pagamento é o mais popular em cada filial pode auxiliar na otimização dos sistemas de processamento e na personalização dos serviços oferecidos.

---

## 8️⃣ Analisar os Picos de Venda ao Longo do Dia  
**Query:**  
```sql
SELECT
    branch,
    CASE
        WHEN HOUR(TIME(time)) < 12 THEN 'Morning'
        WHEN HOUR(TIME(time)) BETWEEN 12 AND 17 THEN 'Afternoon'
        ELSE 'Evening'
    END AS day_time,
    COUNT(*) AS total_transacoes
FROM walmart
GROUP BY branch, day_time
ORDER BY branch, total_transacoes DESC;
```  
**Resultado (exemplos para WALM001 e WALM002):**  
- *WALM001*: Afternoon – 36 transações, Evening – 30, Morning – 8  
- *WALM002*: Afternoon – 29, Evening – 21, Morning – 15  
- *(Outros resultados para demais filiais)*

**Insight:**  
A distribuição das transações por turno revela os horários de maior movimento em cada filial, permitindo o ajuste da escala de funcionários e a reposição de estoque para melhor atender à demanda.

---

## 9️⃣ Identificar Filiais com Maior Queda de Receita Ano a Ano  
**Query:**  
```sql
WITH revenue_2022 AS (
    SELECT branch, SUM(total) AS revenue
    FROM walmart
    WHERE YEAR(STR_TO_DATE(date, '%d/%m/%y')) = 2022
    GROUP BY branch
), 
revenue_2023 AS (
    SELECT branch, SUM(total) AS revenue
    FROM walmart
    WHERE YEAR(STR_TO_DATE(date, '%d/%m/%y')) = 2023
    GROUP BY branch
)
SELECT
    ls.branch,
    ls.revenue AS lastYear_revenue,
    cs.revenue AS currentYear_revenue,
    (ls.revenue - IFNULL(cs.revenue, 0)) AS revenue_drop,
    ROUND(((ls.revenue - IFNULL(cs.revenue, 0)) / ls.revenue) * 100, 2) AS revenue_decline_ratio
FROM revenue_2022 AS ls
LEFT JOIN revenue_2023 AS cs ON ls.branch = cs.branch
WHERE ls.revenue > IFNULL(cs.revenue, 0)
ORDER BY revenue_decline_ratio DESC
LIMIT 5;
```  
**Resultado:**  
- *WALM045*: lastYear_revenue = 1731, currentYear_revenue = 647, revenue_drop = 1084, decline ≈62.62%  
- *WALM047*: lastYear_revenue = 2581, currentYear_revenue = 1069, revenue_drop = 1512, decline ≈58.58%  
- *WALM098*: lastYear_revenue = 2446, currentYear_revenue = 1030, revenue_drop = 1416, decline ≈57.89%  
- *WALM033*: lastYear_revenue = 2099, currentYear_revenue = 931, revenue_drop = 1168, decline ≈55.65%  
- *WALM081*: lastYear_revenue = 1723, currentYear_revenue = 850, revenue_drop = 873, decline ≈50.67%

**Insight:**  
A análise da queda de receita identifica as filiais que enfrentaram os maiores desafios ano a ano, permitindo uma investigação mais profunda das causas e o desenvolvimento de estratégias para reverter a tendência.

---

## Considerações Finais

Este projeto demonstrou como a combinação de Python e SQL pode ser empregada para extrair insights significativos a partir de um dataset robusto de vendas. Cada questão de negócio foi abordada com queries específicas, permitindo:

- A identificação dos métodos de pagamento e dos hábitos dos clientes.
- O reconhecimento das categorias e dias de maior desempenho em cada filial.
- A avaliação dos lucros e da performance financeira por categoria.
- A análise do comportamento de vendas por turno e a detecção de filiais com declínio de receita.

Essas análises oferecem subsídios importantes para a tomada de decisões estratégicas, otimizando operações, marketing e gestão de estoque nas filiais da Walmart.

---

**Contato:**  
Se houver dúvidas ou sugestões, entre em contato: [rafaeldutrapro@gmail.com](mailto:rafaeldutrapro@gmail.com)

