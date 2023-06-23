from src.connection import CVALConnection

if __name__ == '__main__':
    api_key = 'a42a3a750b2dfab2f90ef64e75ba99a7c49a6c3f427d762236459d87e6766af1'
    cval = CVALConnection(api_key)
    print(cval.result().get_results())
    cval.result().get_result(cval.result().get_results()[0].result_id)
