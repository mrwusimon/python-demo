import speedtest

test=speedtest.Speedtest()

print("Loading server list...")
# serverlist=test.get_servers()

# print(f'Given Server list: {serverlist}')
print("Choosing best server")
best=test.get_best_server()
host=best['host']
country=best['country']
print(f'Found:{host} located in {country}')

print("Performing download test...")
download_result=test.download()

print("Performing upload test...")
upload_result=test.upload()
ping_result =test.results.ping

print(f'Download speed: {download_result /1024 /1024:.2f} Mb/s')
print(f'Upload speed: {upload_result /1024 /1024:.2f} Mb/s')
print(f'Ping:{ping_result:.2f} ms')

