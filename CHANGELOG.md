# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.0.0] - 2021-01-10
> ![Breaking Changes](./static/warning_icon_small.png "Warning")  
> **BREAKING CHANGES**
### Changes
 - Reads configurations from `config.json`, including source and destination folders.
 - Added `config.py` to parse configuration file and setup directories. 
 - Only selects files with dimensions set in `device_properties` set in `config.json`.
 - Saves to appropriate folder depending on `device_properties` set in `config.json`.
 - Saves to alternate location `/data` if config location not valid.
 - Checks if file exists before copying over.

## [0.0.1] - 2020-04-22
 - Initial setup.
 - General progress.
