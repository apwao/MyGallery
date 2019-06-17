# MyGallery
### June 15th 2019
#### By **[Purity Sowayi]** (https://github.com/apwao)
## Description
This is a Django application that allows users to upload their images and add a description, location and category. Other users can view these images.
## Setup/Installation Requirements
* Ensure git is intalled in your computer
* Use 'git clone' command to Clone and then unzip the repository from github, https://github.com/apwao/MyGallery.git
* Navigate to the cloned project through the terminal
* Create a virtual environment and install all dependencies in the requirements.txt file
* Run the command 'python3.6 manage.py runserver' to run the application
## BDD
|Behavior                      |Input                       |Output
|------------------------------|----------------------------|----------------------------------------
|User opens an image           | Clicks on Image            | Displays a modal with the image and its details
|User copies link              | Clicks copy link           | Copies image link to the clip board
|User navigates to admin       | Inputs Admin Url           | Admin panel to allow adding an image
|User Adds a location          | Creates location in Admin  |  Adds the location to the database
|User Adds a category          | Creates category in Admin  | Adds the category to the database
|User Adds an image            | Creates image in Admin     | Adds the image to the database
|User Searches images          | Submits search term in form| Displays images from searched category
## Known Bugs
* No known bugs
## Technologies Used
* HTML
* CSS
* Git
* Django
* Bootstrap
* Heroku
## Support and contact details
Incase of any issues, ideas, questions or concerns, contact contributor at pasowayi@gmail.com.
In order to contribute to the code: Fork a copy of the repository, push changes to a branch called contributions. Issue a pull request to the contributor.
### License
Copyright (c) 2019 **Purity Sowayi**
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
