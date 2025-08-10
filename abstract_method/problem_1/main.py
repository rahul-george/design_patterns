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
        pass

    @abstractmethod
    def open(self, target):
        pass

    @abstractmethod
    def writeHeader(self, metadata):
        pass
    
    @abstractmethod
    def writeRow(self, row):
        pass
    
    @abstractmethod
    def writeFooter(self, stats):
        pass

    @abstractmethod
    def close(self):
        pass

class CsvWriter(WriterBase):
    def open(self, target):
        raise NotImplementedError

    def writeHeader(self, metadata):
        raise NotImplementedError

    def writeRow(self, row):
        raise NotImplementedError

    def writeFooter(self, stats):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class XlsxWriter(WriterBase):
    def open(self, target):
        raise NotImplementedError

    def writeHeader(self, metadata):
        raise NotImplementedError

    def writeRow(self, row):
        raise NotImplementedError

    def writeFooter(self, stats):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class ExporterBase(ABC):
    @abstractmethod
    def create_writer(self) -> WriterBase
        pass

    def export(self, target, data, metadata, stats) -> None:
        exporter = self.create_writer()
        exporter.open(target)
        exporter.writeHeader(metadata)
        for row in data:
            exporter.writeRow(row)
        exporter.writeFooter(stats)
        exporter.close()

class CsvExporter(ExporterBase):
    def create_writer(self) -> WriterBase:
        return CsvWriter()
    
class XlsxExporter(ExporterBase):
    def create_writer(self) -> WriterBase:
        return XlsxWriter()


def main():
    exporter = CsvExporter()
    exporter.export("", [], [], [])


if __name__ == "__main__":
    main()