# BikeShare Interactive Data Tool (IDT)
> The bikeshare IDT is an interactive tool to aid in the understanding U.S. bikeshare data. This tool provides the user with a filtered dataset based on the user's choices.

### Getting Started
It is necessary for users to install [Python and Anaconda](https://www.datacamp.com/community/tutorials/installing-anaconda-windowsshould) to run the script.

#### Required Files
The following data files _must_ be used with the program:
- [chicago.csv](chicago.csv)
- [new_york_city.csv](new_york_city.csv)
- [washington.csv](washington.csv)

The following libraries and their versions used when writing the script for the program are:
- `v3.7.1` [time](https://docs.python.org/3/library/time.html)
- `v1.15.1` [NumPy](https://docs.scipy.org/doc/numpy-1.15.1/reference/index.html#reference)
- `v0.23.4` [Pandas](https://pandas.pydata.org/pandas-docs/version/0.23.4/index.html)

### How to use the program?
1. Ensure that the required files and python script is in the current working directory.
2. Run the script in the terminal with:
`python bikshare.py`
3. The script will prompt the user for an input based on these questions:

   * Would you like to see data for Chicago, New York, or Washington?
   * Would you like to filter by month, day, both, or none at all?
   * _(If they chose month)_ Which month - January, February, March, April, May, or June?
   * _(If they chose day)_ Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?


4. Depending on the user input, the data will be _filtered_ accordingly and statistical results of the filtered dataset will be displayed.
5. When requested, the user is able to see five rows of raw data until otherwise communicated.
6. Finally, the user can choose to either restart or terminate the program.

### Credits
Special thanks to the following for making this project possible:
* [Udacity](https://www.udacity.com/) for providing the materials and knowledge to build the project
* [RomchyFCC's Repo](https://github.com/RomchyFCC/GitHub-Practice-For-All) for providing a repo setup to practice git skills
***
### Version Control
`20/11/2018` This project was created on 20th November 2018.
***
