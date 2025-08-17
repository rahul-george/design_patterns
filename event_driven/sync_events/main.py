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
                print(f"Handler {handler.__name__} failed with error: {err}")


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
        print("Deleted logs by document id")

class DocumentShareUrls:
    """Dependent class"""
    def __init__(self) -> None:
        pass
    
    def delete_urls_by_doc_id(self, doc_id: str):
        print("Deleted urls by document id")


def main():
    doc = Document()
    logs = Logs()
    doc_urls = DocumentShareUrls()
    doc.on_delete.register(logs.delete_logs_by_doc_id)
    doc.on_delete.register(doc_urls.delete_urls_by_doc_id)

    doc.delete_doc('1')

main()