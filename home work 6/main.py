def total_salary(path):
    fh = open(path)
    while True:
        salary = 0.000
        lines = fh.readline()
        if not lines:
            break
        for elem in lines:
            salary += float(elem.split(","))
            print(salary)
            