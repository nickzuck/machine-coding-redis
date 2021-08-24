from core.redisStore import RedisStore

if __name__ == '__main__':
    keyValueStore = RedisStore()
    while(True):
        command = input()
        if command == "exit":
            break
        cmdList = command.split()
        actualCmd = cmdList[0]
        cmdKey = None
        if len(cmdList) > 1 :
            cmdKey = cmdList[1]
        if actualCmd == "get":
            print (keyValueStore.get(cmdKey))
        if actualCmd == "put":
            try :
                keyValueStore.set(cmdKey, cmdList[2:])
            except Exception as e:
                print ("error : ", e)
                print ("Data Type Error")
        if actualCmd == "delete":
            keyValueStore.delete(cmdKey)
        if actualCmd == "search":
            values = cmdList[1:]
            search_dict = {}
            for i in range(0, len(values), 2):
                search_dict[values[i]] = values[i+1]
            print (keyValueStore.search(search_dict))
        if actualCmd == "keys":
            print (keyValueStore.keys())