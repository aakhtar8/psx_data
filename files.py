def exists():

    import os
    from datetime import date
    files = os.listdir()
    requied_files = []
    for file in files:
        if file[0:4] == "data":
            requied_files.append(file)
    today = str(date.today())
    existance = False
    for file in requied_files:
        if file[5:15] == today:
            existance = True

    return existance
