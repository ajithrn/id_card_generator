# ID Card generator

Python script for creating personalized event badges for attendees. The script reads attendee data from a CSV file and uses it to generate a badge image for each attendee.


## Prerequisites

- Python3+, python-pip and venv


## Instructions

- create virtual env using `python -m venv env`
- source into env using `source env/bin/activate`
- install requirements.txt using, `pip install -r requirements.txt`
- replace data_id.csv with your file (include headers) `assets/data` sample csv can be found in the folder (make sure the fields are in order, also type contains volunteer,attendee,organizer and sponsor)
- replace images in `assets/images`, fonts in `assets/fonts`
- run `python main.py` (Id cards will be saved to a folder named "output" in sub folders corresponding to the type )
