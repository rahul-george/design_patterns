"""
This version: 
1. Writer and Exporter Bases implement the structure for the concrete classes. 
2. CsvExporter and XlsxExporter should initialize the CsvWriter and XlsxWriter classes. 
3. These classes can either implement their own export workflow or keep the base export algorithm. 
4. Assume in the future the user wants to print on screen, I can implement a screen writer.
"""

from abc import ABC, abstractmethod


class WriterBase(ABC):
    def __init__(self) -> None:
        print("WriterBase initialized")

    @abstractmethod
    def open(self, target):
        print("WriterBase opened")

    @abstractmethod
    def writeHeader(self, metadata):
        print("WriterBase header written")
    
    @abstractmethod
    def writeRow(self, row):
        print("WriterBase row written")
    
    @abstractmethod
    def writeFooter(self, stats):
        print("WriterBase footer written")

    @abstractmethod
    def close(self):
        print("WriterBase closed")

class CsvWriter(WriterBase):
    def open(self, target):
        print("CSV Writer opened target")

    def writeHeader(self, metadata):
        print("CSV Writer written header")

    def writeRow(self, row):
        print("CSV Writer row written")

    def writeFooter(self, stats):
        print("CSV Writer footer written")

    def close(self):
        print("CSV Writer closed")


class XlsxWriter(WriterBase):
    def open(self, target):
        print("XLSX Writter opened")

    def writeHeader(self, metadata):
        print("XLSX Writer written header")

    def writeRow(self, row):
        print("XLSX Writer row written")

    def writeFooter(self, stats):
        print("XLSX Writer footer written")

    def close(self):
        print("XLSX Writer closed")


class ExporterBase(ABC):
    @abstractmethod
    def create_writer(self) -> WriterBase:
        pass

    def export(self, target, data, metadata, stats) -> None:
        exporter = self.create_writer()
        try:
            exporter.open(target)
            exporter.writeHeader(metadata)
            for row in data:
                exporter.writeRow(row)
            exporter.writeFooter(stats)
        except Exception as e:
            print(e)
            print("Exporter ran into error")
        finally:
            exporter.close()

class CsvExporter(ExporterBase):
    def create_writer(self) -> WriterBase:
        return CsvWriter()
    
class XlsxExporter(ExporterBase):
    def create_writer(self) -> WriterBase:
        return XlsxWriter()


def main():
    exporter = CsvExporter()
    exporter.export("", ['a', 'b'], [], [])


if __name__ == "__main__":
    main()