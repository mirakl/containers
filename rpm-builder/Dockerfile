FROM centos:7

RUN yum update -y && yum install -y rpm-build

ENV SOURCE_DIR /source
RUN mkdir -p ${SOURCE_DIR}
ENV RPM_DIR /rpm
RUN mkdir -p ${RPM_DIR}

ENV WORK_DIR /tmp/build
WORKDIR ${WORK_DIR}

COPY rpmmacros /root/.rpmmacros

COPY run.sh /

CMD ["/run.sh"]
