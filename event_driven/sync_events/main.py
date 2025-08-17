from concurrent.futures import ThreadPoolExecutor
from time import time



class SyncEvents:
    """Base class for all sync events"""
    def __init__(self):
        self._handlers = []     # We can add more information to the handlers
    def register(self, handler):
        """Method to register new handlers for an event"""
        self._handlers.append(handler)

    def dispatch(self, *event_args, **event_kwargs):
        """Method to call event handlers"""
        for handler in self._handlers:
            try:
                handler(*event_args, **event_kwargs)
                # raise ValueError("Blah")
            except Exception as err:
                # Write them to a database or a logger. 
                print(f"Handler {handler.__name__} failed with error: {err}")


class BackgroundEvents:
    """Events are executed on different threads"""
    def __init__(self):
        self._handlers = []     # We can add more information to the handlers
        self.event_executor = ThreadPoolExecutor(max_workers=5)

    def register(self, handler):
        """Method to register new handlers for an event"""
        self._handlers.append(handler)

    def dispatch(self, *event_args, **event_kwargs):
        """Different events are run on parallel threads. Making it faster than Sync events. """

        with self.event_executor as executor:
            futures = [executor.submit(handler, *event_args, **event_kwargs) for handler in self._handlers]

            # Iterate over the futures and handle exceptions or failures. 
            for future in futures:
                print(future.result())



class Document:
    """Main document or event generator"""
    def __init__(self) -> None:
        self.on_delete = SyncEvents()
    
    def delete_doc(self, doc_id: str):
        print("Document deleted")
        self.on_delete.dispatch(doc_id)


class Logs:
    """Dependent class"""
    def __init__(self) -> None:
        pass
    
    def delete_logs_by_doc_id(self, doc_id: str):
        """Long running dependency"""
        i = 0
        while i<200000000: i+=1
        print("Deleted logs by document id")
        return i

class DocumentShareUrls:
    """Dependent class"""
    def __init__(self) -> None:
        pass
    
    def delete_urls_by_doc_id(self, doc_id: str):
        """Long running dependency"""
        i = 0
        while i<200000000: i+=1
        print("Deleted urls by document id")


def main():
    doc = Document()
    logs = Logs()
    doc_urls = DocumentShareUrls()
    doc.on_delete.register(logs.delete_logs_by_doc_id)
    doc.on_delete.register(doc_urls.delete_urls_by_doc_id)

    start_time = time()
    doc.delete_doc('1')
    duration = time() - start_time

    print(f"Duration: {duration: .4f}s")

main()