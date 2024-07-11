# Instale 

~~~
pip install fastapi uvicorn sqlalchemy pydantic
~~~

## organizando  
Crie o diretorio  `workout_api`, dentro dele vamos criar os arquivos `__init__.py` e `main.py`

No `main.py`:

~~~ python
from fastapi import FastAPI 
import uvicorn

app = FastAPI(title='workoutApi')


if __name__ == 'main':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)

~~~

Para facilita rodar, vamos criar um `Makefile`:

~~~
run: 
	@uvicorn workout_api.main:app --reload
~~~

