import time
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import busio
import adafruit_scd30
import adafruit_veml6075
import adafruit_mlx90614

# Set up I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensors for different parameters
ads = ADS.ADS1115(i2c)
ph_channel = AnalogIn(ads, ADS.P0)
hardness_channel = AnalogIn(ads, ADS.P1)
conductivity_channel = AnalogIn(ads, ADS.P2)
organic_carbon_channel = AnalogIn(ads, ADS.P3)

scd = adafruit_scd30.SCD30(i2c)
mlx = adafruit_mlx90614.MLX90614(i2c)
uv = adafruit_veml6075.VEML6075(i2c)

# Set up the data collection loop
while True:
    # Read data from the pH sensor
    ph_voltage = ph_channel.voltage
    ph = -5.7 * ph_voltage + 21.34

    # Read data from the hardness sensor
    hardness_voltage = hardness_channel.voltage
    hardness = 0.0028 * hardness_voltage + 47.833

    # Read data from the conductivity sensor
    conductivity_voltage = conductivity_channel.voltage
    conductivity = 0.6 * conductivity_voltage

    # Read data from the organic carbon sensor
    organic_carbon_voltage = organic_carbon_channel.voltage
    organic_carbon = 67.088 * organic_carbon_voltage - 33.536

    # Read data from the SCD30 sensor
    co2 = scd.CO2

    # Read data from the MLX90614 sensor
    temperature = mlx.object_temperature
    ambient_temperature = mlx.ambient_temperature

    # Read data from the UV sensor
    uv_index = uv.index

    # Print the collected data to the console
    print("pH: ", ph)
    print("Hardness: ", hardness)
    print("Conductivity: ", conductivity)
    print("Organic Carbon: ", organic_carbon)
    print("CO2: ", co2)
    print("Temperature: ", temperature)
    print("Ambient Temperature: ", ambient_temperature)
    print("UV Index: ", uv_index)

    # Wait for 1 second before taking the next reading
    time.sleep(1)
