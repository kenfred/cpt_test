from conans import ConanFile, CMake, tools

class CptTestConan(ConanFile):
    name = "cpt_test"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    scm = {
        "type": "git",
        "subfolder": ".",
        "url": "auto",         #this will be replaced with the true url during `conan create`
        "revision": "auto"     #this will be replaced with the current git hash during `conan create`
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=".")
        self.copy("**.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cpt_test"]

