import random
import threading
import time
import concurrent.futures

# ThreadPoolExecutor submit
# def div(divisor, limit):
#     print(f'started dividing={divisor}')
    
#     result = 0
    
#     for x in range(1, limit):
#         if x % divisor ==0:
#             result += x
#             # print(f'divisor={divisor}, x={x}')
#         time.sleep(0.2)
#     print(f'ended div={divisor}', end="\n")
#     return result
    
# if __name__ == "__main__":
#     print('Started main')
# # Выполняется все последовательно

#     futures = []
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         futures.append(executor.submit(div,3,25))
#         futures.append(executor.submit(div,5,25))
        
#         while futures[0].running() and futures[1].running():
#             print('.', end='')
#             time.sleep(0.5)
            
            
#         for f in futures:
#             print(f'{f.result()}')
        
#         print('Immediately printed out after submit')

#     print('After with block')
    
# # Выводится сначала все, а потом уже исполняются таски (Это из-за shutdown(wait=False))
#     # executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
#     # executor.submit(div,3,25)
#     # executor.submit(div,5,25)
    
#     # executor.shutdown(wait=False)
    
#     # print('\nmain ended')

#ThreadPoolExecutor map

# if __name__ == '__main__':
#     pass

# Race condition & Lock

# class BankAccount:
    
#     def __init__(self):
#         self.balance = 100 # Разделяемый ресурс
#         self.lock_obj = threading.Lock() # Создаю Lock, чтобы пото объявить его в нужно месте
        
#     def update(self, transaction, amount):
#         print(f'{transaction} started')
        
#         with self.lock_obj: # Так прописывается, что процесс залочивается. Один из потоков первым придет сюда и залочит переменную, а второй поток получит переменную уже после того, как первый ее закончит независимо от context switch
#             tmp_amount = self.balance
#             tmp_amount += amount
#             time.sleep(1)
#             self.balance = tmp_amount
        
#         print(f'{transaction} ended')
    
    
# if __name__=='__main__':
    # При таком исполнении получается неправильная работа, потомуч то проимходит context switch и данные в переменной записываются неправильно
    # acc = BankAccount()
    # print(f'Main started. acc.balance={acc.balance}')
    
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
    #     ex.map(acc.update, ('refill', 'withdraw'), (100, -200))
        
        
    # print(f'Enf of main. Balance = {acc.balance}')
    
    # Здесь прописывается Lock, чтобы потоки отработали корректно
    
    # lock_obj = threading.Lock() # Так объявляется Lock
        
    # lock_obj.acquire() # А вот так лочится объект
    
    # lock_obj.release() # Так lock отпускается
    # Дальше нужно объявить в самом классе, что локать и где
    
    # Теперь этот код будет выдавать правильный результат, сколько бы его не выполняли
    # acc = BankAccount()
    # print(f'Main started. acc.balance={acc.balance}')
    
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
    #     ex.map(acc.update, ('refill', 'withdraw'), (100, -200))
    
    # print(f'Enf of main. Balance = {acc.balance}')
    
# Семафор 

def work(semaphore):
    time.sleep(random.randint(5, 10))
    print('Releasing 1 connection')
    semaphore.release()

def connect(semaphore, reached_max_connections):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        while True:
            connections_counter = 0
            while not reached_max_connections.is_set():
                print(f'\nConnection n = {connections_counter}')
                semaphore.acquire()
                connections_counter += 1
                
                ex.submit(work, semaphore)
                
                time.sleep(0.8)
                
            time.sleep(5)


def connections_guard(semaphore, reached_max_connections):
    while True:
        print(f'[guard] semaphore = {semaphore.value} ')
        time.sleep(1.5)
        
        if semaphore.value == 0:
            reached_max_connections.set()
            print(f'[guard] Reached max connections')
            time.sleep(2)
            reached_max_connections.clear()

if __name__ == '__main__':
    max_connections = 10
    reached_max_connections = threading.Event()
    
    semaphore = threading.Semaphore(value=max_connections)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(connections_guard, semaphore, reached_max_connections)
        executor.submit(connect, semaphore, reached_max_connections)
    