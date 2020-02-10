FROM python:3
MAINTAINER josh@joshhighet.com
ADD cyberdyne.py /
CMD [ "python", "./cyberdyne.py" ]
