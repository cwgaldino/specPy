The **specPy** python package contains different modules providing functionality related 
with the **spec** software (by Certified Scientific Software).

**This is forked from: https://github.com/certified-spec/specPy.** The **filespec** module was modified to work on pyhthon 3.7. This version might also work with python 2.7, but it was not fully tested!

**spec** is an application by *Certified Scientific Software* 
(http://www.certif.com/) specialized in instrument control and data 
acquisition in X-Ray diffraction experiments and it is largely used 
and many synchrotrons, universities and laboratories around the
world.

Modules in this package include:

filespec
-----------
This module gives full access to scans recorded in files writing with 
the spec file format.

The spec file format organizes scans (data from experimental acquisitions 
sequences) in blocks inside a file.  Each block of data if preceded by a 
header block containing the metadata associated with the acquisition.

For a full description of the format and the description of its organization 
and keywords refer to the documentation distributed with this package.

