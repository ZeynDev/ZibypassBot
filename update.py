from os import path as opath, getenv
from logging import FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info
from logging.handlers import RotatingFileHandler
from subprocess import run as srun
from dotenv import load_dotenv

basicConfig(
    level=INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=50000000, backupCount=10),
        StreamHandler(),
    ],
)
load_dotenv()
##ENV
GDTot_Crypt = os.environ.get("CRYPT","b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D")
Laravel_Session = os.environ.get("Laravel_Session","")
XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")
DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","cnhXOGVQNVlpeFZlM2lvTmN6Z2FPVWJiSjVBbWdVN0dWOEpvR3hHbHFLVT0%3D")
KCRYPT = os.environ.get("KOLOP_CRYPT","a1V1ZWllTnNNNEZtbkU4Y0RVd3pkRG5UREFJZFlUaC9GRko5NUNpTHNFcz0%3D")
HCRYPT = os.environ.get("HUBDRIVE_CRYPT","N25hV1pxMXZWUTdFWEh6L2Q2WFJyQWo2NGJEcWN6R2E5ci91aG8zSFF5Zz0%3D")
KATCRYPT = os.environ.get("KATDRIVE_CRYPT","bzQySHVKSkY0bEczZHlqOWRsSHZCazBkOGFDak9HWXc1emRTL1F6Rm9ubz0%3D")


UPSTREAM_REPO = getenv('UPSTREAM_REPO', "https://github.com/SilentDemonSD/FZBypassBot")
UPSTREAM_BRANCH = getenv('UPSTREAM_BRANCH', "main")

if UPSTREAM_REPO is not None:
    if opath.exists('.git'):
        srun(["rm", "-rf", ".git"])
        
    update = srun([f"git init -q \
                     && git config --global user.email drxxstrange@gmail.com \
                     && git config --global user.name SilentDemonSD \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

    if update.returncode == 0:
        log_info('Successfully updated with latest commit from UPSTREAM_REPO')
    else:
        log_error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')
