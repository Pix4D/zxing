from conans import ConanFile, CMake, tools

class ZxingConan(ConanFile):
    name = 'zxing'
    lib_version = '3.3.3'
    revision = '2'
    version = '{}-{}'.format(lib_version, revision)
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'Zxing recipe'
    url = 'git@bitbucket.org:pix4d/zxing.git'
    license = 'GNU LESSER GENERAL PUBLIC LICENSE'
    generators = 'cmake'
    scm = {
        'type': 'git',
        'revision': 'auto',
        'url': 'auto',
    }

    def build(self):
        cmake_args = {
           'CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS': 'TRUE',
           'BUILD_SHARED_LIBS': 'TRUE',
           'WITH_OPENCV': 'OFF',
        }
        cmake = CMake(self, parallel=True)
        cmake.configure(build_dir='build', defs=cmake_args)
        cmake.build(target='install')

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libdirs = ['lib']
        self.cpp_info.bindirs = ['bin']
        self.cpp_info.libs = ['zxing']
