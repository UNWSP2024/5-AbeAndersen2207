#UNWSP Programming PythonCos2005DEsp25
#Week#5_Program#1_Kilometer Converter
#02/20/2025
#Abraham. N. Andersen

#Write a program that asks the user to enter a distance in kilometers, then converts
#that distance to miles.  The conversion formula is as follows:  Miles = kilometers x 0.6214.
#The conversion must be done is a function with input and output.

# Define a function to convert kilometers to miles.
# The function takes one argument, kilometers, which is the distance in kilometers.
# The function returns the distance in miles.
def convert_km_to_miles(kilometers):
  """Converts kilometers to miles.

  Aruments:
    kilometers: The distance in kilometers.

  Returns:
    The distance in miles.
  """

  # Multiply the distance in kilometers by 0.6214 to get the distance in miles.
  miles = kilometers * 0.6214

  # Return the distance in miles.
  return miles


# Get the distance in kilometers from the user.
kilometers = float(input("Enter the distance in kilometers: "))

# Convert the distance to miles.
miles = convert_km_to_miles(kilometers)

# Print the distance in miles.
print("The distance in miles is:", miles)