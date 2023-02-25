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
    print(handlers.get_one_res(res_name))




if __name__ == '__main__':
    main()