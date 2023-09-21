if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg_list = student_marks.get(query_name)
    cnt_list = len(avg_list)
    avg = 0
    for value in avg_list:
        avg += value
        
    print('%.2f' % (avg/3))
