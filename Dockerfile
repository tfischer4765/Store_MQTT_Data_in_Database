FROM python

WORKDIR /mqtt-app
ADD mqtt_Listen_Sensor_Data.py /mqtt-app
ADD store_Sensor_Data_to_DB.py /mqtt-app
ADD UnknownTopicError.py /mqtt-app

RUN pip install mysqlclient
RUN pip install paho-mqtt

CMD ["python",  "mqtt_Listen_Sensor_Data.py"]

