# python-geoservices
The purpose of this package is to provide an easy way to call NYC Planning's geoservices API from python and add in functionality to accomodate typical geocoding workflows. Additionally this package includes documentation that is scraped and compiled for use within the package.

# Functionality
- Call one or more geoservices functions
- Validate the input arguments supplied for each function
- Allow the workflow of chaining together multiple geoservice functions, using the outputs of one as the inputs of another
- Provide human readable names for all columns (and maybe map them back to the C names/types)
