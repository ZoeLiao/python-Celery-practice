# python_Celery_practice
Practice celery on toturial: http://docs.celeryproject.org/en/latest/getting-started/index.html

How to use?
---
1.vietualenv --python=python3 venv  
2.source venv/bin/activate  
3.pip intall -r requiretments.txt  
4.Use tmux and open 4 windows  
5.window 0: redis-server  
6.window 1: redis-cli  
7.window 2: celery -A proj worker -l info  
8.window 3: run python3 and import proj.tasks
