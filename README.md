DCPE-2A-04-Group1 mini project repository 
# Automated Gardening System
## The Automated Gardening System will support the monitoring and control of a hydroponics system for optimal plant growth.

The following parameters are monitored continuously:

- pH level of the solution ("Potentiometer" readings)
- Ambient temperature ("Temperature" readings)
- Relative humidity ("Humidity" readings)
- Ambient lighting intensity ("LDR" readings)
- EC level ("Moisture sensor" readings)                 

### The automated hydroponics system will be a closed loop system where the simulated EC level ("Moisture sensor" readings) is constantly adjusted to maintain the pre-set optimal level.

- When the simulated EC level is equal to 0, additional nutrient solution will be dispensed into the hydroponics solution by activating a pump based on a servo motor.

### The light intensity will also be controlled based on the measured ambient lighting intensity ("LDR" readings) to ensure that plants have optimal lighting at all times.

- When the ambient light intensity level is lower than or equal to 200, a LED (Acting as UV light) will be activated.

### Ambient temperature ("Temperature" readings) in the hydroponics system is also maintained at a constant level as much as possible.

- When the ambient temperature is higher than 20, a DC motor (Acting as a fan) is activated to reduce the ambient temperature.

### To visualise the data from the different sensors, a dashboard will also be implemented via web page. 
