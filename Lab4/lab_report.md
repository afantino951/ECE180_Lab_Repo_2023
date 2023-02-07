# Lab 4 Hardware and IMU

## Task 1

- Below is a picture of the microcontroller working. We used the blinky example that is included in the Arduino IDE.

- Below is a screenshot of the serial monitor output from the Sparkfun 9DoF IMU that is included in the example section once the library is installed. I did not make any changes the the code.

|![rps subscriber](lab_report_files\IMU_serial_out.jpg)|
|:--:|
|*Serial monitor output of IMU readings scaled*|

## Task 2

|![Connected to WiFi](lab_report_files\Wifi_Connect.jpg)|
|:--:|
|*Serial monitor output of wifi connection proof*|

## Task 3

|![IMU from MQTT](lab_report_files\MQTT_IMU.jpg)|
|:--:|
|*Serial monitor output of IMU readings from the MQTT subcriber from Lab 2*|

There is a significant lag present, which would make sense. We are currently sending a bunch of data to an outside broker and our subscriber has to get the message from the outside broker. We don't know where this broker is, so we could be suffering ms of delay simply from that.

In addition, the Arduino script publishes the acceleration value at every iteration of the loop. This causes too much traffic through the MQTT connection.

## Task 4

1. When looking at the IMU data, it is easy to see that its orientation matches the silkscreen on the IMU. When moving the IMU, we can clearly see which axis is facing down because we can see the acceleration due to gravity. This is helpful for finding which way is down, but will become a problem when we are integrating the acceleration to find the velocity.

2. When we rotate the IMU in each direction, we can always see which way it is facing from the acceleration due to gravity. In addition, we can use the gyroscope to see the rate of rotation in all directions. A good feature to classify idle would be all gryos outputs to be close to 0 and the acceleration values constant to their previous values (eg. the derivative in each direction is ~0).

3. Here is a screenshot of our classifier. Of a jab in the X direction and a pull back of the jab in the -X direction.

    |![Classifer 2+Idle](lab_report_files\Classifier.jpg)|
    |:--:|
    |*Serial monitor output of Classifier output*|

4. Here is a picture of the classifier detecting a right movemnt by measuring the integral of the accelerometer Y-axis. This means that it considers the average instantaneous velocity from the previous 16 measurements.

    |![Classifer 4+Idle](lab_report_files\right_classifier.jpg)|
    |:--:|
    |*Serial monitor output of Classifier output of up, down, left, right detection script*|

I was not able to create an accurate circular classifier with the time that I was able to detecate to the lab. With more time to work on sensor fusion between the Z and Y axis, I think I could use the up, down, left, right classifiers to create an attempt at a circular motion.