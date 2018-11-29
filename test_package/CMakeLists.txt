cmake_minimum_required(VERSION 3.10)
project(ZxingTest)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

if (UNIX)
    conan_set_find_paths()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
else()
    conan_basic_setup()
endif()

find_package(zxing REQUIRED)
find_library(ZXING_LIBRARY NAMES zxing PATHS ${CONAN_LIB_DIRS_ZXING})

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_executable(testApp main.cpp)
target_link_libraries(testApp PRIVATE ${ZXING_LIBRARY})
target_include_directories(testApp PRIVATE ${CONAN_INCLUDE_DIRS_ZXING})
