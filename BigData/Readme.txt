-----------------------------Requirements----------------------
pip install paho-mqtt
pip install pynput
pip install matplotlib
pip install pandas

-----------------------------How to Run------------------------
run each publisher then the subscriber in this order
python publisherTemperature.py
python publisherHumidity.py

before running the accelerator script one must run the phone application and connect it using the laptop ip adress as well as port 5555
python publisherAccelerator.py
python subscriber.py

to see changes in the database use a DBMS like SQLiteStudio

-----------------------------Remaining tasks-------------------
visualisation on real time 
