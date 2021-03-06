############################################
# Project: Enlighten
# File: src\enlighten\convert.py
# By: ProgrammingIncluded
# Website: ProgrammingIncluded.com
# Description: Converts html files generated by render_html.py
#   into raw uncropped jpgs.
#############################################

# std
import os
import glob
import argparse

# ext
import imgkit

RENDER_FOLDER = "render_html"
IMG_FOLDER = os.path.join("img_render")

def get_argument_parser(parser=argparse.ArgumentParser(prog="convert", description="Converts a rendered html into png. Uses imgkit.")):
    parser.add_argument("--raw-img-output-folder", help="Output folder of the images pre-processes.", default=IMG_FOLDER)
    parser.add_argument("--convert-folder-input", 
                        help="Input location of process html files. (Should be same as --html-render-folder in render stage.)",
                        default=RENDER_FOLDER)
    return parser

def parse_args():
    return get_argument_parser().parse_args()

def convert(args):
    if not os.path.exists(args.raw_img_output_folder):
        os.mkdir(args.raw_img_output_folder)
    
    for html in glob.glob("{}/*.html".format(args.convert_folder_input)):
        raw_filename = os.path.split(html)[-1]
        filename = os.path.splitext(raw_filename)[0]
        if filename == "sample":
            continue
        print(filename + ".jpg")

        option = {
            "width": 1920,
            "encoding": "utf-8",
            "enable-local-file-access": None
        }

        imgkit.from_file(html, os.path.join(args.raw_img_output_folder, filename + ".jpg"), options=option)

if __name__ == "__main__":
    # Change CWD to script location
    script_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_path)

    args = parse_args()

    # Render the html into png
    convert(args)