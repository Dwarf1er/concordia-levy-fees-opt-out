# Concordia Levy Fees Opt Out

WARNING: As of now this script is incomplete, the form submission closed before I could finish the script, I will complete it once the next semester's form rolls over

Concordia Levy Fees Opt Out aims at automatically filling the levy fee opt out form for Concordia University students. This tool makes the process of opting out even easier! You provide the [required information](#user-content-required-information) and the form is filled automatically for you!

## Getting Started

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Dwarf1er/concordia-levy-fees-opt-out.git

# Go into the repository
$ cd concordia-levy-fees-opt-out

# Install virtualenv
$ sudo pip install virtualenv

# Create a virtual environment
$ python -m venv .venv

# Activate the virtual environment
  #Windows:
$ .venv\Scripts\Activate.bat

  #MacOS and Linux:
$ source .venv/bin/activate

# Install the dependencies
$ pip install -r requirements.txt
```

## How To Use This Project

The form requires certain information to accept your opt out request, you will have to provide this information to this tool for it to be able to fill out for you. The required information is listed below.

### Required Information

    - Your browser of choice, see the [supported browser list](#user-content-supported-browsers)
    - Your first name
    - Your last name
    - Your email address
    - Your 8 digit student ID
    - The amount of credits you are registered for during the current semester
    - The path to an image of your semester schedule where the credits are visible (see your schedule in your student portal)
    - The path to an image of your student ID card

## Supported Browsers

The following browsers are supported by this tool:

    - Chrome
    - Chromium
    - Firefox
    - Edge (chromium based)

Internet Explorer and Opera are supported by the webdriver-manager package's developer but I personally would not recommend their use and decided not to include them. If you ever want to use any of these non-included browsers I recommend you look at the [official documentation for webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager). However I only tested my tool with the aforementioned browsers, using IE or Opera might need further modifications.

### Prerequisites
 
- [Git](https://git-scm.com)
- [Python](https://www.python.org/downloads/)

## Authors

  - **Antoine Poulin**
    [Dwarf1er](https://github.com/Dwarf1er)

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE)

## Acknowledgments

  - **Billie Thompson**, this README was based on the template provided [here](https://github.com/PurpleBooth/a-good-readme-template)
  - **Sergey Pirogov**, take a look at the webdriver-manager project [here](https://github.com/SergeyPirogov/webdriver_manager)
