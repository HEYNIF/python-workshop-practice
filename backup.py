import shutil
import datetime
import os

def backup_file(source, destination):
    today = datetime.date.today()
    back_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(back_file_name.replace('.tar.gz',''),'gztar',source)

source = "/Users/hanifshaikh/Desktop/program/python-workshop-practice"

destination = "/Users/hanifshaikh/Desktop/program/python-workshop-practice/backups"

backup_file(source,destination)