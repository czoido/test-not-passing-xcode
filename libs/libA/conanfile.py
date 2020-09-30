
from conans import ConanFile

class Recipe(ConanFile):
    name = "libA"
    version = "version"

    
    requires ="header/version"

    def build(self):
        with open("lib" + self.name + ".a", "w+") as f:
            f.write("fake library content")
        with open(self.name + ".lib", "w+") as f:
            f.write("fake library content")

        
        with open("libA2.a", "w+") as f:
            f.write("fake library content")
        with open("A2.lib", "w+") as f:
            f.write("fake library content")
        

    def package(self):
        self.copy("*.a", dst="lib")
        self.copy("*.lib", dst="lib")

    def package_info(self):
        # Libraries
        self.cpp_info.libs = ["libA"]
        
        self.cpp_info.libs.append("A2")
        
        
        self.cpp_info.libs.append("system_assumed")
        

        
        self.cpp_info.system_libs = ["system_lib"]
        

        
        self.cpp_info.frameworks.extend(["Carbon"])
        