
# Projeto Feriados (Holidays)

O objetivo é montar uma classe para ter a lista de [feriados da ANBIMA](https://www.anbima.com.br/feriados/feriados.asp) e funçãoes de dias úteis em python.



## Funções

- **holidays**: 
Retorna uma lista datetime com todos os feriados ANBIMA.

- **isNotDU**: 
Verifica se o dia é um dia útil por meio da lista de feriados e finais de semana.

- **returnDayUtil**: 
Retorna o próximo dia útil levando em consideração os feriados da ANBIMA e finais de semana.



  ## Chamada da classe

```
from holidays import Holidays

hd = Holidays()
```

### Função holidays
Retorna a lista de feriados ANBIMA.

```
listaFeriados = hd.holidays()
```
### Função holidays
Retorno booleano (True ou False) se a data passada é um dia útil.

```
dia = '2021-08-10'
isNotDU(dia, listaFeriados)
```
### Função holidays
Retorno o próximo dia útil para o dia que foi passada.

```
dia = '2021-08-10'
returnDayUtil(dia, listaFeriados)
```
