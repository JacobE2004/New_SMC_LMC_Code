import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Object Info Class
class ObjectInfo:
    def __init__(self, file_path, target=None):
        """
        Initialize the object with the file path and target name.
        :param file_path: Full path to the CSV file (including the file name).
        :param target: Name of the target (optional).
        """
        self.file_path = file_path  # Full path to the file (copied and pasted)
        self.target = target  # Optional target name

# Analysis Code
class LightCurveAnalysis:
    def __init__(self, object_info):
        """
        Initialize with ObjectInfo instance that contains file path and target.
        :param object_info: ObjectInfo instance.
        """
        self.file_path = object_info.file_path
        self.target = object_info.target
        self.data = self._process_data()

    def _process_data(self):
        try:
            # Read the CSV file
            df = pd.read_csv(self.file_path)
            # Ensure the file has the expected columns (JD, mag, mag error)
            if len(df.columns) < 2:
                raise ValueError("The CSV file should have at least two columns: JD and mag.")
            
            time = df.iloc[:, 0].to_numpy()  # First column: JD
            mag = df.iloc[:, 1].to_numpy()   # Second column: mag
            
            return np.array(list(zip(time, mag)), dtype=[('time', 'f4'), ('mag', 'f4')])

        except Exception as e:
            print(f"An error occurred while loading the file {self.file_path}: {e}")
            return np.array([])  # Return an empty array on error

    def get_time_flux(self):
        return self.data['time'], self.data['mag']

    def plot(self):
        time, flux = self.get_time_flux()
        if len(time) == 0 or len(flux) == 0:
            print("No valid data to plot.")
            return
        
        plt.figure(figsize=(18.5, 10.5))
        plt.scatter(time, flux, color='darkblue', s=3)
        plt.xlabel("Time (JD)")
        plt.ylabel("Magnitude")
        plt.title(f"Light Curve of {self.target}" if self.target else "Light Curve")
        plt.gca().invert_yaxis()  # Invert the y-axis
        plt.show()  # Display the plot

# Example usage:

# Step 1: Copy and paste the full file path here (use raw string to avoid issues with backslashes)
file_path = input(r"C:\Users\Jmell\research folder\FILE.csv")

# Step 2: Initialize ObjectInfo with the file path and target name
object_info = ObjectInfo(file_path, target="Sample Target")

# Step 3: Perform the analysis by passing the ObjectInfo to the analysis class
light_curve_analysis = LightCurveAnalysis(object_info)

# Step 4: Plot the data
light_curve_analysis.plot()


