FROM        lcgkiller/deploy_google
MAINTAINER  dev@azelf.com

# 현재경로의 모든 파일들을 컨테이너의 /srv/google 폴더에 복사
COPY        . /srv/google
# cd /srv/deploy_eb_docker와 같은 효과
WORKDIR     /srv/google
# requirements설치
RUN         /root/.pyenv/versions/google/bin/pip install -r .requirements/deploy.txt

# 슈퍼바이저 파일 복사
COPY .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY .config/supervisor/nginx.conf /etc/supervisor/conf.d/

# nginx 파일 복사
COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

# collectstatic 실행
RUN         /root/.pyenv/versions/google/bin/python /srv/google/django_app/manage.py collectstatic --settings=config.settings.deploy --noinput

CMD         supervisord -n
EXPOSE      80 8000
