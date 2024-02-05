from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}


'''
Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 425, in main
    run(app, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 447, in run
    server.run()
  File "/usr/local/lib/python3.10/site-packages/uvicorn/server.py", line 68, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/local/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/local/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/usr/local/lib/python3.10/site-packages/uvicorn/server.py", line 76, in serve
    config.load()
  File "/usr/local/lib/python3.10/site-packages/uvicorn/config.py", line 448, in load
    self.loaded_app = import_from_string(self.app)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/hcpdocker/data/fastapi/hcp_py-core/./src/hcpcore/restapi.py", line 34, in <module>
    mqtt_client.connect()
  File "/usr/local/lib/python3.10/site-packages/tb_device_mqtt.py", line 254, in connect
    self._client.connect(self.__host, self.__port, keepalive=keepalive)
  File "/usr/local/lib/python3.10/site-packages/paho/mqtt/client.py", line 915, in connect
    return self.reconnect()
  File "/usr/local/lib/python3.10/site-packages/paho/mqtt/client.py", line 1057, in reconnect
    sock = self._create_socket_connection()
  File "/usr/local/lib/python3.10/site-packages/paho/mqtt/client.py", line 3731, in _create_socket_connection
    return socket.create_connection(addr, timeout=self._connect_timeout, source_address=source)
  File "/usr/local/lib/python3.10/socket.py", line 845, in create_connection
    raise err
  File "/usr/local/lib/python3.10/socket.py", line 833, in create_connection
    sock.connect(sa)
TimeoutError: timed out

'''
