import os


def index_tasks():
    task_list = open('files.txt', 'w')
    os.chdir('../tasks')
    print('->', os.getcwd())
    for dir in os.listdir(os.getcwd())[1:]:
        with open(os.path.join(dir, 'handover.txt')) as ho:
            for filename in ho:
                file = os.path.join(os.getcwd(), dir, filename)

                print('+ ', file)
                task_list.write(file + '\n')


if __name__ == '__main__':
    index_tasks()
