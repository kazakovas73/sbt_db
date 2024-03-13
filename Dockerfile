FROM mongo

COPY drake_data.json ./

EXPOSE 27017