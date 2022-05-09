# Train Calculator

## Description

The README is written in markdown and the program is written in python.

The program is made to calculate the time it takes for a train to travel a cross a line of stations, including stopping at each station.
It also compares the time with other trains or lines.

## Languages

- Python
- Markdown

## Requirements

- Python 3.7+

## Installation

This projekt is made and tested for python 3.10 +. To install python visit (https://www.python.org/downloads) for the latest version.

You also need to clone the repository do this by opening your cmd and typing "git clone https://github.com/ElliotEriksson/End-Project".

## Example

Do you want to

(1) Create new lines  

(2) Create new trains

(3) Create new trains and lines

(4) Calculate / Compare

(5) Exit the program

4

Do you want to (1) Compare one or more trains across a single line or (2) Compare one train across multiple lines? 1

-----[THE LINES]-----

(1) ['Stockholm - Uppsala', 'Stockholm C', '30000', 'Märsta', '12000', 'Knivsta', '17000', 'Uppsala C']

(2) ['Gröna Linjen', 'Gullmarsplan', '1000', 'Skanstull', '800', 'Medborgarplatsen', '450', 'Slussen', '500', 'Gamla Stan', '1000', 'T-Centralen']

Pick a line: 2

How many trains do you want to compare (1 if you just want to calculate for a single train)? 2

-----[THE TRAINS]-----

(1) ['X2000', '0.8', '56', '1.2']

(2) ['X55', '0.9', '56', '1.4']

Train nr1: 1

Gröna Linjen

Gullmarsplan

65 seconds

Skanstull

58 seconds

Medborgarplatsen

43 seconds

Slussen

46 seconds

Gamla Stan

65 seconds

T-Centralen

It takes a total of 276 seconds to travel across Gröna Linjen with the X2000.
This does not include stoppage time at the stations.

-----[THE TRAINS]-----

(1) ['X2000', '0.8', '56', '1.2']

(2) ['X55', '0.9', '56', '1.4']

Train nr2: 3

3 is not an acceptable answer.

Try again.

-----[THE TRAINS]-----

(1) ['X2000', '0.8', '56', '1.2']

(2) ['X55', '0.9', '56', '1.4']

Train nr2: 1

Gröna Linjen

Gullmarsplan

60 seconds

Skanstull

54 seconds

Medborgarplatsen

41 seconds

Slussen

43 seconds

Gamla Stan

60 seconds

T-Centralen

It takes a total of 258 seconds to travel across Gröna Linjen with the X55.
This does not include stoppage time at the stations.

X55 is the fastest and takes 258 seconds.

X2000 is the slowest and takes 276 seconds.

The fastest train (X55) is 18 seconds faster than the slowest train (X2000).

Do you want to restart the program (y/n)? n

Thank you for using the program.

## To do/Roadmap (Att göra/Plan)

- [ ] Other Languages
- [ ] GUI
- [ ] More Trains
- [ ] More Lines

## Changelog

### Version 0.1

#### Added / Changed

- Added file saving + loading for both trains and lines.
- Added the Train class.
- Added the calculations for stop and acceleration distance.

### Version 1

#### Added / Changed

- Added the calculations for the time between stops.
- Added the comparison of different trains across one line.

#### Version 1.1

#### Added / Changed

- Added the printing out of the values.
- Added reruns for invalid choices.

### Version 1.2

#### Added / Changed

- Added comparison of one train across different lines.
- Added a nicer looking print.

### Version 1.3

#### Added / Changed

- Bug Fixes.
- Added end_program function.

### Version 1.4

#### Added / Changed

- Bug Fixes.
- Added a nicer looking print.
- Added README.

#### Removed

- Removed end_program function.

### Verion 1.5

#### Added / Changed

- Bug Fixes.
- Added loading function.

#### Removed

- Removed get_stats.

### Version 1.6

#### Added / Changed

- Bug Fixes.
- Added while loops to rerun for invalid inputs.

### Version 1.7

- Added more information to the README.

## Contribution

Because this project is assessed pull request wont be allowed. After the assessment has been made they will be allowed (June 2022).

For bigger changes I wish for a issue to be open to dicuss said changes.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

Elliot Eriksson - @Okand#3437 elliot@serait.se

[Repository](https://github.com/ElliotEriksson/End-Project)

## Acknowledgements

- Sven Marnach (sven@marnach.net)
