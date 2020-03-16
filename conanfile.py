from conans import ConanFile, CMake, tools


class ZxingConan(ConanFile):
    name = 'zxing'
    lib_version = '3.3.3'
    revision = '8'
    version = '{}-{}'.format(lib_version, revision)
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'Zxing recipe'
    url = 'git@github.com:Pix4D/zxing.git'
    license = 'GNU LESSER GENERAL PUBLIC LICENSE'
    generators = 'cmake'
    exports_sources = ('CMakeLists.txt', 'source_files.cmake', 'cmake/*', 'core/*')

    def build(self):
        cmake_args = {
           'CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS': 'TRUE',
           'BUILD_SHARED_LIBS': 'TRUE',
           'WITH_OPENCV': 'OFF',
        }

        cmake = CMake(self, parallel=True)

        if(tools.cross_building(self.settings) and
           str(self.settings.os).lower() == 'android'):
            # this is a workaround for the lack of proper Android support from Conan
            # see https://github.com/conan-io/conan/issues/2856#issuecomment-421036768
            cmake.definitions["CONAN_LIBCXX"] = ""

        cmake.configure(build_dir='build', defs=cmake_args)
        cmake.build(target='install')

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libdirs = ['lib']
        self.cpp_info.bindirs = ['bin']
        self.cpp_info.libs = ['zxing']

        self.cpp_info.builddirs += ['.']
