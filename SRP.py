# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:17:20 2024

@author: CompuStore
"""

#follow RSP
class OrderValidator:
    def validate_order(self, order):
        pass

class InventoryManager:
    def update_inventory(self, order):
        pass

class Notifier:
    def notify_customer(self, order):
        pass


#not following RSP
class OrderProcessor:
    def validate_order(self, order):
        pass
    def update_inventory(self, order):
        pass
    def notify_customer(self, order):
        pass
