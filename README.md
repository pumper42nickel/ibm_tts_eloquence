# ibm_tts_eloquence
IBM TTS eloquence driver. Compatible with Python 3 versions of NVDA.

# Building
Prerequisites:
* python 3
If scons is not installed, run:
```
python3 -m pip install scons
```
Make sure that 
```
where scons
```
points to a python 3 version of scons, otherwise build will fail.
Then, run:
```
git clone https://github.com/pumper42nickel/ibm_tts_eloquence --recursive
cd ibm_tts_eloquence
git submodule update --remote
build
```
