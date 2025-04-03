# python example using anaconda

capture steps

 * install anaconda via HomeBrew -- a preferred style on MacOS; this way you are not installing software directly on OS.. but doing it via SINGLE package manager which is HomeBrew
 * once you install anaconda via HomeBrew verify the installation.. try launching Anaconda Navigator -- this is the UI application/ navigator which helps to launch several tools
 * next is to check from command line.. iTerm; command to try is "conda"
 * homebrew installs anaconda in its path.. and its not visible in system-path.. verify by ```echo $PATH```
 * one way is to add the bin, sbin paths of anaconda to $PATH.. 
 * once this is done you can run basic conda commands from iTerm.. verify a few
 * for working on python project/ application that needs data science.. use conda instead of poetry
 * reason for this being, conda comes with lots of useful data science libraries and sdks and tools.. all these are available in their repo (analogus to maven-repo for java or per)