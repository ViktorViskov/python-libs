from time import sleep
from threading import Thread


class ThreadManager:
    """
    Class is simple representation of thread manager.
    Its must get list with thread and amount active thread in same time.
    To start at to do job must call start method
    """
    _threads: list[Thread]
    _last_thread_number: int = 0
    _pool: list[Thread]
    _active_threads: int
    _check_pause: float = 0.3
    _verbouse: bool

    def __init__(self,*, threads: list[Thread], active_threads: int = 10, verbouse: bool = True) -> None:
        self._threads = threads
        self._active_threads: int = active_threads
        self._pool = []
        self._verbouse = verbouse

    def start(self) -> None:
        """
        Method for start executing threads from gived in list.
        """

        for number, thread in enumerate(self._threads):

            # check amount of active threads and make pause whe is max
            # sleep(1) its for make pause between cheking for preevent cpu pooling
            while self._pool_cleaner() >= self._active_threads: sleep(self._check_pause)

            thread.start()
            self._pool.append(thread)
            self._last_thread_number = number

        while self._pool_cleaner(): sleep(self._check_pause)
    
    def _pool_cleaner(self) -> int:
        """
        This method created for clean up finished thread and after executing
        method return amount alive threads in threads pool. Its make to easy use 
        for controlling amount active threads in pool and make pause when its need 
        with while loop and sleep function to preevent cpu pooling
        """
        self._pool = [t for t in self._pool if t.is_alive()]
        
        tasks_in_pool = len(self._pool)

        if self._verbouse:
            self._show_status()

        return tasks_in_pool
    
    def _show_status(self) -> None:
            progress = (self._last_thread_number + 1) / len(self._threads) * 100
            pool_size = len(self._pool) / self._active_threads * 100
            
            print("Started: %d%%. In queue %d%%." % (progress, pool_size))
            print('\033[1A','\033[K','\033[1G', sep="", end='')