import argparse
import os
import sys
import fileinput
import re


PATH = "/home/danylo/stuff/index.html"
REGEX = 'src=+"a+[\w*/]*.\w*.\w*"'
VARIABLE = 'static'
DIR = None

DESCRIPTION = \
'Link path replacer for Django v0.1 - author grizzly.drum@gmail.com. \n\n' \
'Modify all src links ("*.css", "*.js", \n' + \
'and etc) in to the local static src path like: \n' + \
'"<img class ="img-fluid "src="assets/img/about/img1.jpg" alt=""> " \n' + \
'to <img class ="img-fluid "src=" {% static \'assets/img/about/img1.jpg\'}% "alt=""> \n' \
'This script can work with pathways like: \n' \
'src="assets/img/about/img1.jpg" and\n' \
'src="assets/img/blog/img-1.jpg"\n'


def pars_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-f", "--PATH", required=False, default=PATH, type=str, help="Full path to html file.")
    parser.add_argument("-d", "--DIR", required=False, default=DIR, type=str, help="Path to directory with files")
    parser.add_argument("-r", "--REGEX", required=False, default=REGEX, type=str,
                        help="Write custom regex. By default: \n%s" % REGEX)
    parser.add_argument("-v", "--VARIABLE", required=False, default=VARIABLE, type=str,
                        help="Write custom replace variable. By default: \n%s" % VARIABLE)
    return parser.parse_args()


def main():
    if args.DIR:
        files_path = [os.path.abspath(args.DIR + i) for i in os.listdir(args.DIR) if os.path.isfile(args.DIR + i)]
        for file in files_path:
            replace(file)
    else:
        replace(args.PATH)


def replace(PATH):
    counter = 0
    for line in fileinput.input(PATH, inplace=True):
        re_line = re.search(r'%s' % args.REGEX, line)

        if re_line:
            counter += 1
            rl = re_line.group()
            line = line[:re_line.start()] + rl[:5] + '{%"' + " %s '" % args.VARIABLE + rl[5:-1] + '\' %}"' + line[re_line.end():]
            sys.stdout.write(line)
        else:
            sys.stdout.write(line)

    print('Replaced %s lines in file %s' % (counter, args.PATH))


if __name__ == '__main__':
    args = pars_args()
    print(args)
    main()
