import time, logging, random, hashlib, os, requests, json


class AccountManager:
    def __init__(self, engine):
        self.engine = engine
        print('init done')

    def create_new_account(self):
        ...

    def generate_hash(self):
        ...

    def create_session(self):
        ...

    def get_account_id(self, hash_value):
        ...

    def create_account_folder(self, hash_value):
        ...

    def choose_proxy(self):
        ...

    def get_ip_address(self):
        ...

    def push_db_using_acc(self):
        ...

    def end_using_account(self):
        ...

    def reboot_proxy(self):
        ...

    def get_number(self):
        ...

    def get_code(self, tzid):
        ...


    def resolve_captcha(self, cpt_el):
        ...

    
    def register_account(self):
        ...
