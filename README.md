#  This is a simle CLI to download pages from network

[![Build Status](https://travis-ci.org/Topolun/python-project-lvl3.svg?branch=master)](https://travis-ci.org/Topolun/python-project-lvl3)
[![Maintainability](https://api.codeclimate.com/v1/badges/5fbfcf4562ffe7192ba0/maintainability)](https://codeclimate.com/github/Topolun/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5fbfcf4562ffe7192ba0/test_coverage)](https://codeclimate.com/github/Topolun/python-project-lvl3/test_coverage)

**To install this CLI please enter in the command line:**

    pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple topolun_page_loader

## How it is works:

- To download a page just run: '`page_loader page_adress(http://...)`'. It will save page in current directory.
To save page in othe place, please add '`--output path_to_save_file`'.


[![asciicast](https://asciinema.org/a/Fa0Q6wvTF6Xm7iQ6Y6q5JztCa.svg)](https://asciinema.org/a/Fa0Q6wvTF6Xm7iQ6Y6q5JztCa)


- All local resources from page tags like '`link`', '`script`' and '`img`' are downloaded to a local directory in the same place as the main file.

[![asciicast](https://asciinema.org/a/hjCvkV962YxwEb0GrOA2tQxAr.svg)](https://asciinema.org/a/hjCvkV962YxwEb0GrOA2tQxAr)

- You may set a level of logging in the cli. just add '`-L`' or '`--log`' ang choose a level of logging. You can choose from `CRITICAL`, `ERROR`, `WARNING`, `INFO` and `DEBUG` levels. 
**Example:**

    page_loader https://hexlet.io/courses --log INFO

[![asciicast](https://asciinema.org/a/UoEl5SuNZWzS1IFDcuyAlYsDZ.svg)](https://asciinema.org/a/UoEl5SuNZWzS1IFDcuyAlYsDZ)

- If something goes wrong, this cli inform you about that.

[![asciicast](https://asciinema.org/a/jsFhZG0UHxd15pNeIMym8SbXY.svg)](https://asciinema.org/a/jsFhZG0UHxd15pNeIMym8SbXY)


- You can see a progress of the download as progress bar

[![asciicast](https://asciinema.org/a/6yU7WvspOpyNKpXCHzx8lAWlV.svg)](https://asciinema.org/a/6yU7WvspOpyNKpXCHzx8lAWlV)
