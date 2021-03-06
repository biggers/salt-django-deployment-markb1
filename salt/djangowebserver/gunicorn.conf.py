bind = "{{ ip }}:{{ port }}"
errorlog = "{{ log }}"

import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1

preload_app = True
