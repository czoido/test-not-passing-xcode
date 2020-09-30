
from conans import ConanFile

class HeaderOnly(ConanFile):
    name = "header2"
    version = "version"

    

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        # It may declare system libraries
        
        self.cpp_info.libs.append("header2_system_assumed")
        

        
        self.cpp_info.system_libs = ["header2_system_lib"]
        

        
        self.cpp_info.frameworks.extend(["Security"])
        