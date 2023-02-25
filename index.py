import handlers 


def begin() -> str:
    resourses = handlers.get_all_resources()
    print('Select the resourse :')
    for i, name in enumerate(resourses):
        print(f'{i+1}. {name}')
    try:
        res_id = int(input())
        return resourses[res_id-1]
    except:
        print('Provide integer value')

def main():
    res_name = begin()
    params = handlers.get_one_res(res_name)
    # print(params)
    handlers.parce_resource(params)




if __name__ == '__main__':
    main()