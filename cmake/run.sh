conan install . -s build_type=Release

cmake . -DCMAKE_MODULE_PATH=. -DCMAKE_VERBOSE_MAKEFILE:BOOL=True -DCMAKE_CONFIGURATION_TYPES=Release 

cmake --build .