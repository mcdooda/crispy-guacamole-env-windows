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
    lua5.3
    SDL2
	SDL2main
    SDL2_image
    SDL2_mixer
    SDL2_ttf
    opengl32
    glew32
)

### custom command to move dll into the build folder 
file(GLOB copySource ${CMAKE_SOURCE_DIR}/dll/*)
foreach(dependency ${copySource})
	add_custom_command(TARGET crispy-guacamole
		POST_BUILD
		COMMAND ${CMAKE_COMMAND} -E copy_if_different ${dependency} $<TARGET_FILE_DIR:crispy-guacamole>
		COMMENT "Copying dll's...\n"
	)
endforeach()

### should be done with the install target instead
#install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/dll DESTINATION ${CMAKE_BINARY_DIR})
#install(DIRECTORY ${CMAKE_SOURCE_DIR}/dll DESTINATION ${CMAKE_BINARY_DIR}/crispy-guacamole/Debug/)