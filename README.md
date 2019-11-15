SublimeLinter-gfortran
=========================


This (unofficial) linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an updated interface to [SublimeFortran](https://packagecontrol.io/packages/Fortran).  It is a bugfix on SublimeFortran to work with SublimeLinter in 2019.
It will be used with files that have the "Modern Fortran" syntax.  


## Installation

Please use [Package Control](https://packagecontrol.io) to install the SublimeLinter and SublimeFortran plugin.

Then navigate to your Sublime Text Packages folder (found via `Preferences -> Browse Packages...`) and clone this repository as
`git clone git@github.com:stanleyjs/SublimeLinter-gfortran.git SublimeLinter-gfortran`.  The folder name appears to be crucial.

You may have issues if `gfortran` is not found in your `PATH` by SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable). 

## Settings
- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

## Future
- Add support for different compilers and flags via user settings.  This is an easy extension.
- Wrap into full package for use with PackageControl and the official SublimeLinter repo.
