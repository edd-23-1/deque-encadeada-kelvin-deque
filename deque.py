# -*- coding:UTF-8 -*-
from no import No

class Deque:
    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__fim = None
        self.__capacidade = capacidade
        self.__qtdElementos = 0
        print(f"Criada EDD Fila com capacidade: {capacidade}")


    # Verifica se a deque está vazia
    # Retorna True se a deque estiver vazia e False caso contrário
    def is_empty(self) -> bool:
        # implementação do método
       return self.__qtdElementos == 0


    # Verifica se a deque está cheia
    # Retorna True se a deque estiver cheia e False caso contrário
    def is_full(self) -> bool:
        # implementação do método
        return self.__qtdElementos == self.__capacidade
    

    # Insere um elemento no início da deque e retorna True
    # Se a fila estiver cheia, lança uma exceção 
    def add_front(self, valor) -> bool:
        # implementação do método
        if self.is_full():
            raise Exception("Deque cheia")
        novoNo = No(valor)

        if self.is_empty():
            self.__inicio = novoNo
            self.__fim = novoNo

        else:
            novoNo.prox = self.__inicio
            self.__inicio = novoNo
            self.__inicio = novoNo
        
        self.__qtdElementos += 1
        return True


    # Insere um elemento no final da deque e retorna True
    # Se a deque estiver cheia, lança uma exceção 
    def add_rear(self, valor) -> bool:
        # implementação do método
        if self.is_full():
            raise Exception("Deque cheia")
        novoNo = No(valor)

        if self.is_empty():
            self.__inicio = novoNo
            self.__fim = novoNo

        else:
            self.__fim.prox = novoNo
            self.__fim = novoNo
        
        self.__qtdElementos += 1
        return True


    # Remove um elemento do início da deque e retorna esse elemento
    # Se a deque estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove_front(self) -> No:
        # implementação do método
        if self.is_empty():
            raise Exception("Deque vazia")
        noRemovido = self.__inicio

        if self.__inicio == self.__fim:
            self.__inicio = None
            self.__fim = None

        else:
            self.__inicio = self.__inicio.prox
        
        self.__qtdElementos -= 1
        return noRemovido
    

    # Remove um elemento do início da deque e retorna esse elemento
    # Se a deque estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove_rear(self) -> No:
        # implementação do método
        if self.is_empty():
            raise Exception("Deque vazia")
        noRemovido = self.__fim
        
        if self.__inicio == self.__fim:
            self.__inicio = None
            self.__fim = None

        else:
            noAtual = self.__inicio
            while noAtual.prox != self.__fim:
                noAtual = noAtual.prox
            
            noAtual .prox = None
            self.__fim = noAtual

        self.__qtdElementos -= 1
        return noRemovido
    

    # Retorna o primeiro elemento da deque sem removê-lo
    # Se a deque estiver vazia retorna None
    def peek_front(self) -> No:
        # implementação do método
        return self.__inicio


    # Retorna o último elemento da deque sem removê-lo
    # Se a deque estiver vazia retorna None
    def peek_rear(self) -> No:
        # implementação do método
        return self.__fim
    

    # Retorna uma lista com os valores do atributo dado de cada No
    # da deque na ordem em que os elementos da foram inseridos.
    # Imprime os elementos da deque do primeiro para o último.
    # Caso a deque esteja vazia, imprime uma mensagem informando
    # que a deque está vazia e retorna uma lista vazia
    def display(self) -> list():
        # implementação do método
        pass
    

    # Retorna a quantidade de elementos na deque
    # Se a deque estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        return self.__qtdElementos
