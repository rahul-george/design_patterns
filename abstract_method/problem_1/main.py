"""
My initial implementation. 
- WriterBase implements the common interface.
- Each of it's subclass implements the concrete implementation. 
- The creater class chooses the type of writer and returns it. 
- export function has the export workflow. 

My analysis: 
- This implementation is good but can we combine the export function and the creator?
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


class Creator:
    @classmethod
    def create(cls, writer_type) -> WriterBase:
        if writer_type == "CSV":
            return CsvWriter()
        elif writer_type == "XLSX":
            return XlsxWriter()
        else:
            raise NotImplementedError(f"Unknown writer type")



def export(export_type, data, target, metadata, stats):
    exporter = Creator.create(export_type)
    exporter.open(target)
    exporter.writeHeader(metadata)
    for row in data:
        exporter.writeRow(row)
    exporter.writeFooter(stats)
    exporter.close()