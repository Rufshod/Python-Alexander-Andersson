# Weekly Journal

## Week 1

### Day 1, 2023-09-25
First day did not start until 14:00 in the afternoon so we just had time for a simple onboarding, we were shown were we would sit during our internship.

We had time to start our sprintplanning for our project and called it a day at around 18:30

### Day 2, 2023-09-26
Spent a good chunk of the day getting the anodet repo to work.  
Once that was done I tested the PaDiM model in the repo.  
Here is an example of how I noted down how the model behaved.
```
resnet18
- Image scores: tensor([26.2478, 21.5471, 23.0032, 10.2540,  9.6295])
  Image classifications: tensor([0., 0., 0., 1., 1.])  

wide_resnet50
- Image scores: tensor([32.4158, 28.3042, 28.7167, 12.9971, 17.5561])
  Image classifications: tensor([0., 0., 0., 1., 0.])  

- Bottle:
  Image scores: tensor([26.2478, 21.5471, 23.0032, 10.2540,  9.6295])  
  Image classifications: tensor([0., 0., 0., 1., 1.])  

- Capsule:
  Image scores: tensor([35.6994, 17.5745, 23.3754, 10.9613,  6.1606])  
  Image classifications: tensor([0., 0., 0., 1., 1.])
  ```


I also fixed some old dependencies.  
I started researching a tool to create a UML for the project. 

### Day 3, 2023-09-27
I used PlantUML to create a UML which uses a proprietary "programming language" to create UML's through text. I had to install Graphviz and Java to make it work.  
  
Read through the PaDiM research paper to get a better understanding how padim actually works and took extensive notes to better remember. 

#### For example:
##### Model Training for PaDiM: 

MVTec AD class with 10,000 images using the following data augmentation operations: random rotation ($-2^\circ$, $+2^\circ$) degrees, resize to 292x292, random crop to 282x282, and finally center crop to 256x256. The training is performed during 100 epochs with the Adam optimizer with an initial learning rate of $10^{-4}$.

Got several cameras to work on my computer simultaneously through Williams camera script.

### Day 4, 2023-09-28
First day of problem solving. We had issues with William who uses macOS and myself using Windows.  
The camera script was extremely slow on windows and could only display a max of 2 cameras.  
  
  I started with trouble shooting and created a new script that opened every camera one at a time to check that Python could find all of them, which it could. 

  Finally found a fix later in the day:
  ```py
          cap = (
            cv2.VideoCapture(idx, cv2.CAP_DSHOW)
            if os_name == "Windows"
            else cv2.VideoCapture(idx)
        )
  ```
  cv2.CAP_DSHOW allows opencv2 to get backend access to the Windows operating system, increasing the speed.

### Day 5, 2023-09-28
Finally a day full of coding!
I wrote two scripts, one for creating a folder structure to house our images. It uses args for the anomalies to make it more flexible which I was very happy with.
#### create_warehouse_directory.py:
```py
def build(self, object_name: str = "object", anomalies: List[str] = []):

if __name__ == "__main__":
    builder = WarehouseBuilder()
    builder.build()

```
#### ↑ - code snippet

The other script was to actually take the images and store them in the folders so that we can use the images to train and test our model.
#### camera.py
```py
if __name__ == "__main__":
    warehouse = WarehouseBuilder()
    warehouse.build("object_name", ["anomaly1", "anomaly2"])
    camera_manager = CameraManager(warehouse)
    camera_manager.run()
```

## Conclusion
Week 1 has been a rollercoaster of onboarding, coding, and problem-solving. From setting up our workstations to diving deep into PaDiM and UMLs, every day was a learning curve. I tackled issues head-on, like the camera script's OS compatibility, and even got multiple cameras to work simultaneously. I also managed to write scripts that not only build a data warehouse but also populate it with images for our model training. Looking forward to more coding and fewer issues in the coming weeks.

## Week 2

### Day 6, 2023-10-02
#### Summary
- Developed **camera_identifier.py** and integrated it with camera.py

- Explored multi-threading for camera.py but opted for optimization
- Investigated USB information for all cameras


#### Details

    I considered using multi-threading to speed up camera.py. However, after some research, I realized that multi-threading was not the best fit for this project. Instead, I found that the code was inefficient because it was opening and checking every camera before each capture.

    I also spent time researching how to identify the specific USB device number for each camera, aiming for more precise control over the hardware. 

### Day 7, 2023-10-03
#### Summary
- Upgraded the the flexibility of camera.py to allow for capturing test or training images, or both
- Cleaned up the code in main and utils/camera_identifier
- Achieved a capture speed of 250 images in less than 8 seconds with camera.py

#### Details
    I managed to make camera.py faster by addressing the inefficiency issue identified on Day 6. The code is now optimized to avoid unnecessary camera checks, resulting in a significant speed boost. **→ → →**


### Day 8, 2023-10-04
#### Summary

- Created a CameraIdentifier class
- Restructured utils and added an exposure test
- Fixed a bug that caused camera.py to break
- Assisted in an extra lesson for the AI23 class at school

#### Details

    The CameraIdentifier class allows us to determine the order of each camera and save this information to camera_config.json. This enables the program to use the cameras in the user-defined order, providing more control over the capture process.

    I restructured the utils directory to make the code more modular and easier to maintain. This also paved the way for adding new features like the exposure test.

    Lastly, I joined Andreas in assisting the AI23 class with their Python lessons. This was not only helpful for the class but also an excellent opportunity for my own personal growth.

### Day 9, 2023-10-05
#### Summary
- Added 'CameraConfigurator' Class to change White Balance (WB) and Color Temperature  

- Began restructuring the MCCP repository to comply with PyPI standards

- Moved CameraIdentifier and Configurator classes to the utils directory
 
- Fixed a bug related to saving to the same configuration file

#### Details
    Continuing from Day 8 I added a new class called CameraConfigurator. This class is designed to handle White Balance and Color Temperature settings, offering more control over the camera's output.  
    I started aligning the MCCP repo with PyPI standards for easier installation and use. Moved the new CameraIdentifier and Configurator classes to utils.py to simplify our codebase.  
    Also fixed a bug that prevented saving to the same JSON config file, allowing for easier updates.


### Day 10, 2023-10-06
#### Summary

- :boot: **Bug Squashing day!**
- :bug: Fixed four bugs
#### Details

Initially, when an image was captured, it would "lag" behind, displaying the previous image. This issue was resolved by implementing a frame buffer. The first few frames are now discarded before saving an image, ensuring that an outdated picture is not saved.

Here are the bug descriptions:

    BUG 🐛: In CameraManager, observed after adding a pause between pictures
    BUG 🐛: The first image taken contained exposure data from the previous camera_config
    BUG 🐛: CameraConfigurator always runs, even when Camera Exposure and Color Temperature already exist in camera_config.json
    BUG 🐛: clean_file_names creates two subdirectories if there is a space in the anomaly name—one with a space and one with an underscore. It should only create one.


### Conclusion: 
The second week was focused on refining and expanding the MCCP project. I tackled performance issues in camera.py, introduced new classes for better camera control, and started the process of making the repository PyPI-compliant.  

Alongside these technical improvements, I also took the opportunity to assist in an AI class, which was a rewarding experience. Despite encountering several bugs, solutions were promptly found and implemented. Overall, it was a week of substantial progress, I am already looking forward to next week!


## Week 3
### Day 11, 2023-10-09
#### Summary

    Initiated MCCP's transformation into a PyPI package with unit tests creation.
    Configured PyPI account settings.
    Conducted in-depth research on PyPI build processes.

#### Details

Today was dedicated to fixing the MCCP project's maintainability and accessibility. I added type hints and comprehensive docstrings to some key files, ensuring clarity and ease of use for future contributors. one achievement was the successful configuration of pyproject.toml and setup.py, setting the stage for our project's deployment on PyPI. Overcoming a tricky configuration error in pyproject.toml was particularly satisfying, clearing the path for our project's public release.
### Day 12, 2023-10-10
#### Summary

    Attended GBG Tech Week, featuring Nvidia.
    Engaged in networking and learning opportunities.

#### Details

This day was a break from coding but not from learning. The event provided valuable insights, especially regarding Llama and image generation technologies. The panel discussions were fun and informative, and the networking opportunities were abundant, offering a chance to connect with industry professionals.
Day 13, 2023-10-11
#### Summary

    Focused on refining augment.py for better integration with MCCP.
    Encountered and addressed challenges in image saving logistics.

#### Details

The day was challenging, with a focus on improving augment.py. The primary issue revolved around ensuring that augmented images were saved correctly in the designated directory, aligning with the training images. This required meticulous debugging and code adjustments to ensure seamless functionality.
### Day 14, 2023-10-12
#### Summary

    Achieved functionality for saving augmented images in the correct folder.
    Implemented a function to remove unnecessary augmented images.
    Resolved a bug causing augmented files to be re-augmented.

#### Details

Significant progress was made in optimizing augment.py. I successfully enabled the script to save augmented images in the same folder as the training images, enhancing the organization and accessibility of our data. Additionally, I developed a function to remove redundant augmented images, streamlining the dataset preparation process. A critical bug fix was also implemented, preventing the re-augmentation of already processed files.
### Day 15, 2023-10-13
#### Summary

    Had my first day working from home.
    Officially released MCCP as a PyPI package.

#### Details

Despite having a cold, We got to release MCCP as an official PyPI package. The focus was on reviewing and refining the code, ensuring that everything was in order for the release. This process involved fixing minor bugs and cleaning up unnecessary code segments.

## Week 4
### Day 16, 2023-10-16
#### Summary

    Addressed several bugs in the MCCP project.
    Participated in a project direction meeting with the automation team and Iman.

#### Details

A pivotal meeting with the automation team and Iman to discuss the project's future direction. I felt deflated afterwards due to the project not going in the direction I had invisioned. I got orders to start work with the anomaly_detection_app, a project previously developed by other students.
### Day 17, 2023-10-17
#### Summary

    Took a sick day but managed to work on the anomaly_detection_app.

#### Details

I dedicated some time to work on the anomaly_detection_app. Progress was limited due to illness, and the app's complex and disorganized JavaScript codebase was full of spaghetti code, leading to a frustrating experience.
### Day 18, 2023-10-18
#### Summary

    Continued work on the anomaly_detection_app.
    Explored Anvil through tutorials and developed a basic website.

#### Details

The focus remained on the anomaly_detection_app, but challenges persisted, particularly with saving images correctly. After exploring Anvil through several tutorials, I decided that using Anvil to create a new frontend would be more efficient than attempting to fix the existing web app's issues.

        Anvil is a framework that converts python code into JavaScript
### Day 19, 2023-10-19
#### Summary

    Attended an Open House event at school.
    Engaged with companies like Textual, Humblebee, and Stena.
    Continued learning through Anvil tutorials.

#### Details

The Open House at school was a highlight, offering opportunities to interact with various companies and discuss potential collaborations or internships. I took the initiative to reach out to several companies, exploring opportunities for a future LIA 2 placement.
### Day 20, 2023-10-20
#### Summary

    Established the anodet-anvil repository and integrated it with the Anvil app.
    Consulted with Plejd's frontend team for insights on anomaly detection functionalities.

#### Details

Significant progress was made in frontend development with the creation of the anodet-anvil repository and its successful integration with the Anvil app. A productive discussion with Plejd's frontend team, particularly with a developer experienced in computer vision systems, provided valuable insights and guidance for enhancing our anomaly detection script.
### Conclusion

Week 4 was a blend of challenges and learning opportunities. From debugging MCCP to exploring new systems with Anvil and engaging with industry professionals. Despite health setbacks and initial frustrations with existing codebases, the week ended on a high note with promising developments in frontend design and valuable networking experiences. The journey continues with a focus on innovation and collaboration.

## Week 5
### Day 21, 2023-10-23
#### Summary

    Got our local Python code to synchronize with the Anvil app.
    Implemented a function in run.py for JSON save/load functionality.

#### Details
I integrated a new function into run.py in the Anvil repository and made it possible for it to save and load data using JSON. Now our Anvil app will soon work with MCCP, streamlining our workflow and data management.
### Day 22, 2023-10-24
#### Summary

    Resolved merge conflicts and successfully merged the MCCP branch into the main branch.

#### Details

The focus of the day was on resolving several merge conflicts that emerged while integrating my MCCP branch with the main branch. This task required a thorough understanding of the codebase, ensuring that all conflicts were resolved. 
### Day 23, 2023-10-25
#### Summary

    Began the initial setup of our Anvil app.

#### Details

The day was dedicated to laying the groundwork for our Anvil app. This involved planning the best approach to create an effective and user-friendly frontend using Anvil. The planning phase is crucial as it sets the direction for the development and design of the app.
### Day 24, 2023-10-26
#### Summary

    Initiated the main Anvil app.
    Started developing a method to fetch JSON data from our local system using a Python script.

#### Details

Significant progress was made in the development of our Anvil app. The main application was created, marking the beginning of its actual development. A key focus was on devising a method to efficiently fetch JSON data from our local system using a Python script.
### Day 25, 2023-10-27
#### Summary

    Enhanced MCCP for proper JSON format saving.
    Merged Identifier and Configurator into a single class.
    Updated tests, imports, and version name.
    Improved threading in utils.
    Updated the MCCP package.

#### Details

I refined the MCCP's functionality to save JSON in the correct format, enhancing data handling and storage. In an effort to streamline our codebase, the Identifier and Configurator classes were merged into a single class. Additionally, I updated various tests and imports to align with these changes and incremented the version name to reflect the new state of the project. 

## Conclusion

I was happy with the new repository for local Python code and the the work with  JSON handling  that helped with our project's backend. MCCP project saw substantial improvements, from streamlining classes to enhancing threading mechanisms. The week was a testament to focused effort and strategic planning.

## Week 6
### Day 26, 2023-10-30
#### Summary

    Refactored camera capture code, removing threading from utils.
    Updated CameraConfigurator to function without threading.
    Modified setup.py to list both myself and William as separate authors.

#### Details

The day was focused on enhancing the efficiency and simplicity of our code. I refactored the camera capture code, specifically removing the use of threading from the utils module. This decision was driven by the realization that threading was not necessary for the CameraConfigurator to function effectively. Additionally, I updated setup.py to accurately reflect our contributions, listing both William and myself as separate authors. This change clarifies our individual contributions to the project.
### Day 27, 2023-10-31
#### Summary

    Continued development in Anvil, focusing on multiple camera streams.
    Managed to display up to two camera streams simultaneously in the Anvil app.

#### Details

The day's work was centered around enhancing the Anvil app's capability to handle multiple camera streams. Despite the challenges, we achieved some success in displaying up to two camera streams at once within the app. This development is a significant step towards our goal of having a more dynamic and versatile camera monitoring system in the browser.
### Day 28, 2023-11-01
#### Summary

    Celebrated my birthday!
    Made small fixes on MCCP.
    Began working on documentation and docstrings.

#### Details

I dedicated time to refining the MCCP project. I implemented small fixes to improve its functionality and started working on the documentation and docstrings. Ensuring that our project is not only functional but also understandable and accessible to others.
### Day 29, 2023-11-02
#### Summary

    Successfully integrated MCCP into run.py.

#### Details

This integration means that our camera application can now be operated through the Anvil app, enhancing user interaction and streamlining the process of managing camera feeds.
### Day 30, 2023-11-03
#### Summary

    Implemented a user input parameter in camera.py.

#### Details

To further enhance the usability of MCCP with the Anvil app, I added a user input parameter to camera.py. This addition eliminates the need for manual input in the terminal for capturing images, thereby simplifying the process and making it more user-friendly.

## Conclusion

The week saw significant progress in the MCCP project, with key refinements in the camera capture code and the successful integration of MCCP into run.py. The introduction of a user input parameter in camera.py streamlined the image capture process, aligning it more closely with the Anvil app's functionality. Overall, Week 6 was both productive and memorable, pushing the boundaries of our project.

## Week 7
### Day 33, 2023-11-06
#### Summary

    Refined the future strategy for the Anvil app.
    Decided against hosting live camera streams in Anvil.
    Developed a Flask app to serve images to Anvil.

#### Details

The day was marked by a strategic pivot in our approach to the Anvil app. After careful consideration, we decided to move away from hosting live camera streams within Anvil due to various complexities. Instead, we opted for a more feasible solution – using a Flask app to host static images. This approach, while less dynamic than live streaming, still effectively meets our project's needs by providing a reliable way to serve images to Anvil.
### Day 34, 2023-11-07
#### Summary

    Successfully displayed images in Anvil served by the Flask app.

#### Details
Today was a good day. After all the headache trying to get camera streams to work for a week straight. Seeing real progress was a burden lifted from my shoulders.
### Day 35, 2023-11-08
#### Summary

    Conducted a thorough cleanup of the code in both Anvil and Anodet-Anvil repositories.

#### Details

Dedicated the day to cleaning up and organizing the code in both the Anvil and Anodet-Anvil repositories.
### Day 36, 2023-11-09
#### Summary

    Achieved functionality for a camera preview script with run.py and Anvil.

#### Details
This allows us to display images from all connected cameras on the Anvil app, significantly improving the user interface and interaction.
### Day 37, 2023-11-10
#### Summary

    Initiated the development of new pages in Anvil for dataset creation and model testing/predicting.

#### Details

The focus shifted towards enhancing the Anvil app's functionality by starting the development of new pages. These pages are designed to enable users to create datasets and utilize our anomaly detection model for testing and prediction purposes.
## Conclusion

The shift from live streaming to using static images served by a Flask app was a change in our approach, the successful integration of image display in Anvil and the development of a camera preview script were key milestones, enhancing the app's functionality and user experience. 
## Week 8
### Day 40, 2023-11-13
#### Summary

    Implemented an 'overwrite original' function in Anodet-Anvil and MCCP for enhanced image database creation.

#### Details

The update was made to MCCP by adding a function that allows overwriting original images. This feature is crucial for the TrainPage on our Anvil app, enabling users to generate multiple images for training purposes, rather than being limited to a single image as per the initial design.
### Day 41, 2023-11-14
#### Summary

    Enhanced the TrainPage with interactive features, including a 'Capture' button to display the latest images from all cameras.

#### Details

The TrainPage on the Anvil app received a major upgrade for user interaction. A new 'Capture' button was added, which, upon activation, displays the most recent picture taken by each camera. This feature significantly improves the user experience by providing immediate visual feedback.
### Day 42, 2023-11-15
#### Summary

    Felt the pressure of impending project deadlines.
    Began the process of serving test images through our Flask app.

#### Details

The day was marked by a heightened sense of urgency to meet project deadlines. Efforts were focused on setting up the Flask app to serve test images, a crucial step in ensuring the functionality and completeness of our project.
### Day 43, 2023-11-16
#### Summary

    Intense day of finalizing major components: serving Train, Test, and Plots via the Flask app.
    Completed the webpage design and integrated all settings and buttons with the backend.
    Focused on writing the remaining documentation.

#### Details

Me and William worked hard together to fit all aspects of our code and frontend together. Despite the complexity of integrating various elements, we successfully enabled the Flask app to serve Train, Test, and Plot images. The webpage design was finalized, ensuring that every setting and button was fully functional and linked to the backend. Additionally, considerable time was devoted to completing the project documentation, a vital aspect for future reference and understanding.
### Day 44, 2023-11-17
#### Summary

    The final day of the internship brought a mix of emotions and accomplishments.
    Engaged in a productive meeting with the Data team regarding a potential second internship.
    Focused on minor fixes and creating a list of unresolved 'issues' for future attention.

#### Details

The last day of the internship was both surreal and fulfilling. A key highlight was the meeting with the Data team, where discussions about a possible second internshipt. The remainder of the day was spent on fine-tuning the project, addressing minor issues, and documenting 'issues' or unfinished tasks that could serve as a roadmap for future development.
## Conclusion

Implementing crucial features in Anodet-Anvil and MCCP to fixing the user interaction on the TrainPage, the week was filled with significant achievements. The successful integration of various components, finalizing the webpage design, and completing documentation were key milestones. The opportunity to discuss a potential second internship and the successful demonstration to Iman were the cherries on top of a fruitful experience. This final week not only showcased the technical skills and dedication of the team but also set the stage for future developments and personal growth in the field of AI and machine learning.