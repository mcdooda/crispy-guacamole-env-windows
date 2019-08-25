cmake_minimum_required(VERSION 3.6)

project(crispy-guacamole)

include_directories(
    crispy-guacamole/src/game
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

#black magic, ask Tom
foreach(_source IN ITEMS ${src})
    if (IS_ABSOLUTE "${_source}")
        file(RELATIVE_PATH _source_rel "${CMAKE_CURRENT_SOURCE_DIR}" "${_source}")
    else()
        set(source_rel "${_source}")
    endif()
    get_filename_component(_source_path "${_source_rel}" PATH)
    string(REPLACE "/" "\\" _source_path_msvc "${_source_path}")
    source_group("${_source_path_msvc}" FILES "${_source}")
endforeach()

add_definitions(-DFLAT_DEBUG)
add_definitions(-DFLAT_PROFILER_ENABLED)

add_executable(
    crispy-guacamole
    ${src}
)

target_link_libraries(
    crispy-guacamole
    lua5.3
	SDL2main
    SDL2
    SDL2_image
    SDL2_mixer
    SDL2_ttf
    opengl32
    glew32
)

set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT crispy-guacamole)
set_property(TARGET crispy-guacamole PROPERTY CXX_STANDARD 17)

if(MSVC)
    target_compile_options(crispy-guacamole PRIVATE "/MP")
endif()