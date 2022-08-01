FROM centos 

COPY employees_script employees_script 

RUN   sed -i -e "s|mirrorlist=|#mirrorlist=|g" /etc/yum.repos.d/CentOS-* 

RUN sed -i -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" /etc/yum.repos.d/CentOS-* 

RUN dnf clean all && dnf swap centos-linux-repos centos-stream-repos -y

RUN dnf install python3 -y

RUN curl "https://bootstrap.pypa.io/pip/3.6/get-pip.py" -o "get-pip.py"

RUN python3 get-pip.py

RUN pip3 install -r employees_script/requirements.txt

CMD [ "python3", "employees_script/run.py" ]
