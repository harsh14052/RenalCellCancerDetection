import os


def change_name():
    file_path = "E:\\KidneyTumorDetection\\datasets\\no"
    count = 1
    for filename in os.listdir(file_path):
        src = file_path + "\\" + filename
        # dst = "kidney-yes-" + str(count) + ".jpg"
        dst = file_path + "kidney-no-" + str(count) + ".jpg"
        # os.rename(src, dst)
        os.rename(src, dst)
        count += 1


change_name()
