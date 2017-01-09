from datetime import datetime
import locale

def process_file():
    with open("logfile.txt") as fin, open("logfile_proc.txt", mode='w') as fout:
        for line in fin.readlines():
            parsed_line = _parse_line(line)
            if len(parsed_line) > 1:
                fout.write(parsed_line + '\n')

def _parse_line(line):
    res = ""
    split_line = line.split(';')
    if len(split_line) == 2:
        # lun 15 ago 2016, 17.31.01, UTC;
        datetime_str = split_line[0].replace(',', '').replace('.', ':')
        try:
            datetime_obj = datetime.strptime(datetime_str, '%a %d %b %Y %X %Z')
            if split_line[1][-3:-1] == "UP":
                is_up = 1
            else:
                is_up = 0
            res = datetime_obj.strftime('%T %D') + ";" + str(is_up)
        except (ValueError, TypeError):
            #'Ignoring malformed data'
            res = ""
    return res

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "it_IT.UTF-8")
    process_file()
