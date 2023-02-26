import handlers 


def begin() -> str:
    resourses = handlers.get_all_resources()
    # print(resourses)
    print('Select the resourse :')
    for i, name in enumerate(resourses):
        print(f'{i+1}. {name["res_name"]}')
    try:
        res_id = int(input())
        return resourses[res_id-1]
    except:
        print('Provide integer value')

def main():
    res_name = begin()
    print(res_name)
    params = handlers.get_one_res(res_name['res_name'])
    # print(params)
    handlers.parce_resource(params, res_name["id"])




if __name__ == '__main__':
    main()