from conans import ConanFile, CMake
import os

class ZxingTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def imports(self):
        self.copy('*.dll', src='bin', dst='bin')
        self.copy('*.dylib*', src='lib', dst='lib')
        self.copy('*.so*', src='lib', dst='lib')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(os.path.join(os.curdir, 'bin', 'testApp'))
