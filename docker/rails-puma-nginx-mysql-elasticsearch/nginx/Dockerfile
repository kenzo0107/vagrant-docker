FROM nginx:1.13.0
#ADD ./nginx/conf/nginx.conf /etc/nginx/nginx.conf
RUN rm -f /etc/nginx/conf.d/*
ADD ./nginx/conf/conf.d/default.conf /etc/nginx/conf.d/default.conf
CMD ["/usr/sbin/nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]
