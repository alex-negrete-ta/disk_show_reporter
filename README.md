# disk_show_reporter
Grabs the path to the disk and publishes the total amount of storage each folder has, with the percentage it has. It also publishes if any storage exceeds the softcap limit.

# The problem.
To get a better idea of the size of each project and notify production if any project is over the percentage softcap for clean up or archival.

# Tools 
Python script using in a linux enviroment to reinforce linux cli management with object oriented code.

#  The solution
Using Linux paths and subprocess commands to grab the total storage, and each project total.


# Sample how to use.

This object-oriented programming uses __main__ to run the software when you automatically run the disk_management.py
The variable it needs is a Linux path to your show's root directory, for example
'/home/user/shows/'
