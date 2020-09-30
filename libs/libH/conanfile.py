
from conans import ConanFile

class HeaderOnly(ConanFile):
    name = "header"
    version = "version"

    
    requires ="header2/version", "libZ/version"

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        # It may declare system libraries
        
        self.cpp_info.libs.append("header_system_assumed")
        

        
        self.cpp_info.system_libs = ["header_system_lib"]
        

        
        self.cpp_info.frameworks.extend(["CoreAudio"])
        