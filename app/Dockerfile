FROM django:1.9.4
RUN pip install djangorestframework
RUN mkdir -p app
WORKDIR /app
ADD . /app




RUN cd /app/InvestmentAdvisorAPI && ls

EXPOSE 8000

CMD ["python3","/app/InvestmentAdvisorAPI/manage.py","createsuperuser"]
CMD ["admin3"]
CMD ["admin3@gmail.com"]
CMD ["songlingbing"]
CMD ["songlingbing"]

CMD ["python3", "/app/InvestmentAdvisorAPI/manage.py", "runserver", "0.0.0.0:8000"]
