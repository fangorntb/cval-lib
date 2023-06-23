from src.connection import CVALConnection

if __name__ == '__main__':
    api_key = '425da17cea5c6573e3614ae938a594787aa130fd70531c6ff3618a85c637156f'
    cval = CVALConnection(api_key)
    ds = cval.dataset()
    ds.create()
    ds.result.get_results()
