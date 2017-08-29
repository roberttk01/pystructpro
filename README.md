# PyStructPro
A new python project structural organizer used to generate and organize the directories of a simple Python application 
at the beginning of a project for the user. The organization is based on Matt Bachmann's 2016 talk at the Boston Python
User Group. The Youtube video of the lecture may be found [here](https://youtu.be/RKHMnevITF0) and the slide may be
found [here](https://speakerdeck.com/bachmann1234/structuring-your-python-project).

## Preface
I wanted to make clear that this project was put together as a personal project to learn the basics of Python packaging,
distribution, and Github, along with an implementation of the best practices when it comes to organizing my projects and
standardizing how to go from project initialization to its ultimate distribution. That said, I am eager to learn from my
mistakes and invite any feedback and criticism the community may have as that community is one of the pillars that
lends itself to the strength and popularity of Python.  

## Getting Started
These are the steps that I had envisioned while creating this project, which is not to say that there is not another,
possibly better, implementation that you can find.

### Environment
The system specifications used for development were:
* Windows 10
* Python 3.5.2
* PyInstaller 3.2.1

### Installing
Follow these steps to install PyStructPro locally.
1) After the environment is installed, clone project to local machine
2) Open cmd.exe and navigate to the *pystructpro* directory
3) Use PyInstaller to generate the source distribution to a directory you wish. For instance,
```
C:\...\pystructpro>pyinstaller pystructpro.py --distpath C:\pystructpro 

```
4) Add the directory to your local %PATH% variable.

You should now be able to run PyStructPro from the command line.

### Usage
The following example is a basic usage example.

PyStructPro has only one required variable, **name**, and one optional variable, **directory** (unless you count help
as an optional variable). **directory** should be entered when the user wants to create the project directory somewhere
other than the current working directory they are currently in.

**The only rule that the program has currently is that the specificied directory *must* be empty before the PyStructPro 
is ran. If that is not the case, PyStructPro will inform the user and exit.**

##### Example 1: Excluding **--directory** option
    
Project Name: foo

Project Directory: *None*

This example would create a project called **foo** in the current directory.
```
C:\empty_directory>dir
 Volume in drive C has no label.
 Volume Serial Number is ####-####
 
 Directory of C:\empty_directory
 
8/29/2017   12:00 AM     <DIR>      .
8/29/2017   12:00 AM     <DIR>      ..
                0 File(s)          0 bytes
                2 Dir(s) 999,999,999,999 bytes free
C:\empty_directory>pystructpro foo
Project directory does not exist. Would you like to create it at this time? Y/N
y
Populating project directory.

```

When we look now, we can see the PyStructPro has created a project directory called *foo* in our current working 
directory with the project structure outlines in Matt Bachmann's talk.

```
C:\empty_directory>dir
 Volume in drive C has no label.
 Volume Serial Number is ####-####
 
 Directory of C:\empty_directory
 
8/29/2017   12:01 AM     <DIR>      .
8/29/2017   12:01 AM     <DIR>      ..
8/29/2017   12:01 AM     <DIR>      foo
                0 File(s)          0 bytes
                3 Dir(s) 9,999,998,892 bytes free
C:\empty_directory>cd foo
C:\empty_directory\foo>dir
 Volume in drive C has no label.
 Volume Serial Number is ####-####
 
 Directory of C:\empty_directory\foo
 
8/29/2017   12:01 AM     <DIR>      .
8/29/2017   12:01 AM     <DIR>      ..
8/29/2017   12:01 AM     <DIR>      docs
8/29/2017   12:01 AM     <DIR>      foo
8/29/2017   12:01 AM          1,107 LICENSE
8/29/2017   12:01 AM              0 README.md
8/29/2017   12:01 AM              0 requirements.txt
8/29/2017   12:01 AM              0 setup.py
8/29/2017   12:01 AM              0 test-requirements.txt
8/29/2017   12:01 AM     <DIR>      tests
                5 File(s)      1,107 bytes
                5 Dir(s) 9,999,998,892 bytes free
```

Further exploration of the project directories generated will show that it resembles 
[this structure](https://speakerdeck.com/bachmann1234/structuring-your-python-project?slide=4).


##### Example 2: Including **--directory** option

Project name: bar

Project directory: C:\projects\foo

This example will create the project directory **bar** in the directory **C:\projects\foo**.

**NOTE 1:** Currently, PyStructPro will only be able to create the singular root directory, so the directory tree needs to 
exist prior to running or else it will return error and quit.

**NOTE 2:** Directory should include no spaces.

```
C:\>pystructpro bar --directory C:\projects\bar
Project directory does not exist. Would you like to create it at this time? Y/N
y
Populating project directory.

C:\>cd projects\bar
C:\>dir
 Volume in drive C has no label.
 Volume Serial Number is ####-####
 
 Directory of C:\projects\bar
 
8/29/2017   12:01 AM     <DIR>      .
8/29/2017   12:01 AM     <DIR>      ..
8/29/2017   12:01 AM     <DIR>      docs
8/29/2017   12:01 AM     <DIR>      bar
8/29/2017   12:01 AM          1,107 LICENSE
8/29/2017   12:01 AM              0 README.md
8/29/2017   12:01 AM              0 requirements.txt
8/29/2017   12:01 AM              0 setup.py
8/29/2017   12:01 AM              0 test-requirements.txt
8/29/2017   12:01 AM     <DIR>      tests
                5 File(s)      1,107 bytes
                5 Dir(s) 9,999,998,892 bytes free
```

As you can see, the project directory was generated and organized just as before in the specified directory.

### To-Do
   
- [x] Develop basic skeleton generator with optional directory parameter
- [x] Update README.md (ongoing)
- [x] Populate setup.py
- [ ] Generate tests
- [ ] Provide options for other license types (Apache, GNU, etc.)
- [ ] Include CONTRIBUTORS.md

## Authors

**Thomas Kyle Robertson** - *Creator* - [Github](https://github.com/roberttk01) [LinkedIn](https://www.linkedin.com/in/thomas-robertson-3530743b/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements
* As previously stated, this idea was derived mostly from a desire to standardize personal project structure as laid out
by Matt Bachmann's 2016 Boston Python User Group talk, *Structuring your First Python Project*.
    * [Youtube](https://youtu.be/RKHMnevITF0)
    * [Slides](https://speakerdeck.com/bachmann1234/structuring-your-python-project)
    * [Matt Bachmann's Github](https://github.com/Bachmann1234)
    * [Matt Bachmann's LinkedIn](https://www.linkedin.com/in/matt-bachmann-34b56850/)