import subprocess
import os

class MyDisk:
    def __init__(self, partition, limit, path):
        '''
        Description:
        Checks disk storage information and show storage usage.

        Input:
        partition (str): Dash or foward dash to specify the path.
        soft_limit(int): Percentage used to represent the softcap of the disk.
        path (str): Path to the show folder.

        Output:
        None
        '''

        # Store the variables into the object.
        self.partition = partition
        self.soft_limit = limit
        self.path = path
        self.util_perc = None
        self.report_data = []
        self.all_folders = []

    def check_volume_health(self):
        '''
        Description:
        Checks the total storage of the system and compares it based on the amouhnt used.

        Input:
        None

        Output:
        self.data_line (int): Percentage used of the system.
        '''
        # Attempts to run subprocess using the df (disk space usage) into text.
        try:
            result = subprocess.check_output(
                ["df", "-h", self.partition], text=True, stderr=subprocess.PIPE
            )
        
        # Prints the exact error produced in the try and prints it using stderr.
        except subprocess.CalledProcessError as e:
            print(f"Error running checking storage: {e.stderr}")
            return

        # Grabst the result output text into different elements.
        lines = result.strip().split("\n")

        # Splits the results to grab the data_line.
        data_line = lines[1].split()
        print(f'data_line {data_line}')

        #Stores the percentage used produced by the data_line.
        self.util_perc = int(data_line[4].strip("%"))

        #Checks if the percentage is higher than the soft limit.
        if self.util_perc > self.soft_limit:
            print(
                f"Storage is at: {self.util_perc} EXCEEDS THE LIMIT of {self.soft_limit}"
            )
        else:
            print(f"Storage is good at {self.util_perc}%")

        return data_line


    def check_show_usage(self):
        '''
        Description:
        Checks the path and list of shows to get their usage.

        Input:
        None

        Output:
        None
        '''
        # Stores the values into the folder.
        all_folders = os.listdir(self.path)

        # For loop to check the list of shows.
        for show in all_folders:
            show_path = os.path.join(self.path, show)

            # Gathers all the storage and path for each directory.
            try:
                result = subprocess.check_output(
                    ["du", "-sh", show_path], text=True, stderr=subprocess.PIPE
                )
                print(result)

                #Stores the directory path, name and size into a dictionary.
                show_size = result.split()[0]
                self.report_data.append(
                    {"Show Name": show, "Usage": show_size, "Path": show_path}
                )

            # Prints the error.
            except subprocess.CalledProcessError:
                print(f"Show directory for {show} not found.")

        # Prints the result of the usage.
        print("--Top Show Disk Usage:--")
        for data in self.report_data:
            print(f"\n{data['Show Name']}: {data['Usage']}")


if __name__ == "__main__":
    #Runs the main path and seths the path.
    path = "/home/alex/code/projects/"
    disk = MyDisk("/", 85, path)
    disk.check_volume_health()
    disk.check_show_usage()
