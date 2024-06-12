all : smc600.py smc600_wrap.cxx smc600.h
	python3 setup.py build_ext --inplace

install : all smc600.h
	python3 setup.py install

smc600.py : smc600.i smc600.h
	swig -python -c++ smc600.i

smc600_wrap.cxx : smc600.i smc600.h
	swig -python -c++ smc600.i

clean:
	@rm -rf __pycache__ *.so build smc600.py *_wrap.cxx *.pyc *.pyd
