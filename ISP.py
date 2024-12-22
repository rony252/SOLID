#follow ISP
class PrinterInterface:
    def print_document(self, document):
        pass

class ScannerInterface:
    def scan_document(self, document):
        pass


class Printer(PrinterInterface):
    def print_document(self, document):
        print(f"Printing: {document}")


class Scanner(ScannerInterface):
    def scan_document(self, document):
        print(f"Scanning: {document}")
        
        
#not following ISP

class PrinterInterface:
    def print_document(self, document):
        pass
    def scan_document(self, document):
        pass


class Printer(PrinterInterface):
    def print_document(self, document):
        print(f"Printing: {document}")


class Scanner(PrinterInterface):
    def scan_document(self, document):
        print(f"Scanning: {document}")