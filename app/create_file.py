import os
import sys
import datetime


datetime_now = datetime.datetime.now()
str_num = 1
if "-d" in sys.argv and "-f" in sys.argv:
    if sys.argv.index("-f") < sys.argv.index("-d"):
        path = (f"C:\\Users\\igor1\\PycharmProjects"
                f"\\py-create-file-from-terminal\\"
                f"{'\\'.join(sys.argv[sys.argv.index("-d") + 1:])}")
        os.makedirs(path, exist_ok=True)

        with open(f"{path}\\{''.join(sys.argv[sys.argv.index('-f') + 1:
                  sys.argv.index('-d')])}", "a") as file:
            content_file = input("Enter content line: ")
            file.write(datetime_now.strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                if content_file != "stop":
                    file.write(f"{str_num} {content_file}\n")
                    content_file = input("Enter content line: ")
                    str_num += 1
                else:
                    break

    else:
        path = (f"C:\\Users\\igor1\\PycharmProjects"
                f"\\py-create-file-from-terminal\\"
                f"{'\\'.join(sys.argv[sys.argv.index('-d') + 1:
                                      sys.argv.index('-f')])}")
        os.makedirs(path, exist_ok=True)

        with open(f"{path}\\{''.join(sys.argv[sys.argv.index('-f') + 1:])}",
                  "a") as file:
            content_file = input("Enter content line: ")
            file.write(datetime_now.strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                if content_file != "stop":
                    file.write(f"{str_num} {content_file}\n")
                    content_file = input("Enter content line: ")
                    str_num += 1
                else:
                    break

elif "-d" in sys.argv and "-f" not in sys.argv:
    path = (f"C:\\Users\\igor1\\PycharmProjects"
            f"\\py-create-file-from-terminal\\"
            f"{'\\'.join(sys.argv[sys.argv.index('-d') + 1:])}")
    os.makedirs(path, exist_ok=True)


elif "-f" in sys.argv and "-d" not in sys.argv:
    if os.path.exists(f"{''.join(sys.argv[sys.argv.index('-f') + 1:])}"):
        with open(f"{''.join(sys.argv[sys.argv.index('-f') + 1:])}",
                  "a") as file:
            content_file = input("Enter content line: ")
            file.write("\n")
            file.write(datetime_now.strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                if content_file != "stop":
                    file.write(f"{str_num} {content_file}\n")
                    content_file = input("Enter content line: ")
                    str_num += 1
                else:
                    break
    else:
        with open(f"{''.join(sys.argv[sys.argv.index("-f") + 1:])}",
                  "w") as file:
            content_file = input("Enter content line: ")
            file.write(datetime_now.strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                if content_file != "stop":
                    file.write(f"{str_num} {content_file}\n")
                    content_file = input("Enter content line: ")
                    str_num += 1
                else:
                    break
