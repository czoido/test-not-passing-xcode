
from conans import ConanFile

class Recipe(ConanFile):
    name = "libB"
    version = "version"

    
    requires ="libA/version"

    def build(self):
        with open("lib" + self.name + ".a", "w+") as f:
            f.write("fake library content")
        with open(self.name + ".lib", "w+") as f:
            f.write("fake library content")

        
        with open("libB2.a", "w+") as f:
            f.write("fake library content")
        with open("B2.lib", "w+") as f:
            f.write("fake library content")
        

    def package(self):
        self.copy("*.a", dst="lib")
        self.copy("*.lib", dst="lib")

    def package_info(self):
        # Libraries
        self.cpp_info.libs = ["libB"]
        
        self.cpp_info.libs.append("B2")
        
        
        self.cpp_info.libs.append("system_assumed")
        

        
        self.cpp_info.system_libs = ["system_lib"]
        

        
        self.cpp_info.frameworks.extend(["Carbon"])
        