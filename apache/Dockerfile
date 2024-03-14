FROM httpd:latest

RUN apt-get update

# Expose the default Apache port
EXPOSE 80

# Run httpd in the foreground
CMD ["httpd", "-D", "FOREGROUND"]