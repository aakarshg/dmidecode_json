import re as _re
from subprocess import call,Popen,PIPE, check_output
import json
import argparse

def _parse(dmide_fullinput):
    output_data = {}
    #  Each record is separated by double newlines
    dmide_fullinput = dmide_fullinput.replace('\n\t\t',' ')
    split_output = dmide_fullinput.replace('\t','').split('\n\n')
    for record in split_output:
        #print record
        #print "/////"
        #split_lines = record.replace(':','\":\"').split('\n')
        split_lines = record.split('\n')
        for x in range(len(split_lines)):
            split_lines[x] = split_lines[x].encode('ascii', 'ignore')
            split_lines[x] = _re.sub(r":\s\s+",": ", split_lines[x])
            split_lines[x] = _re.sub(r"\s\s+","", split_lines[x])
        if split_lines[0]!="" and len(split_lines)>=2:
            split_lines[0] = split_lines[0].replace(' ','_')
            if split_lines[0] not in output_data:
                output_data[split_lines[0]] = []
            current_dict = {}
            # splitting only on first occurence as some fields can have multiple
            # example
            # OEM Strings
        	# String 1: PSF:
        	# String 2: Product ID: 670635-S01
            for s in split_lines[1:]:
                if ': ' in s:
                    key_val = s.split(': ',1)
                else:
                    continue
                if len(key_val) <= 1:
                    key_val.append("None")
                current_dict[key_val[0].replace(' ','_')]=key_val[1]
            #current_dict = dict(s.split(': ') for s in split_lines[1:])
            output_data[split_lines[0]].append(current_dict)
    print json.dumps(output_data, indent=1)
    return output_data

def parse(input_args):
    args = ["dmidecode"]
    if input_args:
        args.append("--type")
        args.append(",".join(input_args))
    args.append("--quiet")
    args = " ".join(args)
    data_output = _execute_cmd(args)
    _data = _parse(data_output)
    return _data

def _execute_cmd(args):
    p1 = check_output(args, shell=True).decode("utf-8")
    return p1

def main():
    parser = argparse.ArgumentParser(
        description="Dmidecode output in json")
    parser.add_argument(
        '-t', '--type', dest="types", nargs='+'
    )
    type_args = parser.parse_args()

    if type_args:
        parse(type_args.types)
    else:
        parse()

if __name__ == '__main__':
    main()
