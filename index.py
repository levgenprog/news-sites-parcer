import handlers 


def begin() -> str:
    # get the list of all resourses available

    resourses = handlers.get_all_resources()
    print('Select the resourse :')
    for i, name in enumerate(resourses):
        print(f'{i+1}. {name["res_name"]}')
    try:
        res_id = int(input())
        if res_id > len(resourses):
           raise AttributeError
        return resourses[res_id-1]
    except :
        print('Provide correct integer value')

def main():
    res_data = begin()
    # get the parameters to create a resourse for parcing

    params = handlers.get_one_res(res_data['res_name'])

    # Converting params into a Res object
    resourse = handlers.create_resource(params, res_data)

    # Perform parcing
    handlers.parce_resource(resourse=resourse)


if __name__ == '__main__':
    main()