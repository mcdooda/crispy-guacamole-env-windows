cmake_minimum_required(VERSION 2.6)

project(crispy-guacamole)

include_directories(
	crispy-guacamole/flat-engine/src
	include
)

link_directories(
	${CMAKE_SOURCE_DIR}/lib
)

file(
    GLOB_RECURSE
    src
    crispy-guacamole/src/*
    crispy-guacamole/flat-engine/src/*
)

add_executable(
    crispy-guacamole
    ${src}
)

target_link_libraries(
    crispy-guacamole
    lua5.2
	SDL2main
    SDL2
    SDL2_image
    SDL2_mixer
    SDL2_ttf
    opengl32
    glu32
    glew32
)

