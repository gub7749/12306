# -*- coding=utf-8 -*-

from init import login, select_ticket_info
from concurrent.futures import ThreadPoolExecutor
import sys

pool = ThreadPoolExecutor(max_workers=1)

def run(ticket_config):
    #login.go_login(ticket_config).login()
    select_ticket_info.select(ticket_config).main()



f1 = pool.submit(run(sys.argv[1]))
