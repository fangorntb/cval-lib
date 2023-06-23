from src.connection import CVALConnection
if __name__ == '__main__':
    api_key = 'a42a3a750b2dfab2f90ef64e75ba99a7c49a6c3f427d762236459d87e6766af1'
    cval = CVALConnection(api_key)
    ds = cval.dataset()
    ds_id = ds.create()
    print(ds_id)
    update = ds.update()
    print(update)
    get = ds.get()
    print(get)
    get = ds.get(ds_id)
    print(get)
    print(ds.get_all())
