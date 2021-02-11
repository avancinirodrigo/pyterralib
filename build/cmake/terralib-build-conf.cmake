
set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Build type" FORCE)
set(CMAKE_INSTALL_PREFIX "$ENV{_TERRALIB_INSTALL_DIR}" CACHE PATH "Where to install TerraLib?" FORCE)

if(APPLE OR UNIX)
	set(CMAKE_PREFIX_PATH "$ENV{_TERRALIB_3RDPARTY_LIBS_DIR};$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}/lib;$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}/include;$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}/gdal2;$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}/pgsql" CACHE PATH "Where are the dependencies of TerraLib?" FORCE)
	set(SWIG_EXECUTABLE "$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}/bin/swig" CACHE FILEPATH "Where are the SWIG?" FORCE)
	set(BOOST_ROOT "$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}" CACHE PATH "Boost directory" FORCE)
elseif(WIN32)
	set(CMAKE_PREFIX_PATH "$ENV{_TERRALIB_3RDPARTY_LIBS_DIR};$ENV{_TERRALIB_VLD_DIR}" CACHE PATH "Where are the dependencies of TerraLib?" FORCE)
	set(SWIG_EXECUTABLE "$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}/swig/swig.exe" CACHE FILEPATH "Where are the SWIG?" FORCE)
	set(TERRALIB_LEAK_DETECTOR_ENABLED OFF CACHE BOOL "Enable Win Visual Leak Detector?" FORCE)
	set(terralib4_DIR "$ENV{_TERRALIB_3RDPARTY_LIBS_DIR}/lib/cmake/terralib-4.2.2" CACHE PATH "TerraLib4?" FORCE)
endif()

set(TERRALIB_DIR_VAR_NAME "PYTERRALIBPATH" CACHE STRING "Name of an environment variable with the base installation path of TerraLib")

set(TERRALIB_BUILD_EXAMPLES_ENABLED OFF CACHE BOOL "Build the examples?" FORCE)
set(TERRALIB_EXAMPLE_ADO_ENABLED OFF CACHE BOOL "Build the TerraLib with ADO?" FORCE)
set(TERRALIB_BUILD_UNITTEST_ENABLED OFF CACHE BOOL "Build the unit tests?" FORCE)
set(TERRALIB_TRACK_3RDPARTY_DEPENDENCIES OFF CACHE BOOL "Track the 3rd-parties on instalation?" FORCE)
set(TERRALIB_BUILD_AS_BUNDLE OFF CACHE BOOL "If on, tells that the build will generate a bundle" FORCE)
set(BUILD_TESTING OFF CACHE BOOL "Build testing?" FORCE)
set(USE_QT5 OFF CACHE BOOL "Disabled Qt" FORCE)
set(Qt5_DIR "" CACHE PATH "Disabled Qt" FORCE)
set(TERRALIB_TRANSLATOR_ENABLED OFF CACHE BOOL "Enable translator support?" FORCE)
set(TERRALIB_EXAMPLE_BINDING_LUA_ENABLED OFF CACHE BOOL "Build TerraLib bindings example?" FORCE)
set(TERRALIB_DOXYGEN OFF CACHE BOOL  "Enable API documentation build?" FORCE)
set(TERRALIB_LOGGER_ENABLED OFF CACHE BOOL  "Logger?" FORCE)
set(TERRALIB_QTRANSLATION_ENABLED OFF CACHE BOOL "Enable translation for Qt Widgets?" FORCE)
set(TERRALIB_TERRAVIEW OFF CACHE BOOL "Build TerraView?" FORCE)
set(TERRALIB_QHELP_ENABLED OFF CACHE BOOL "QHelp?" FORCE)
set(TERRALIB_QTPROPERTYBROWSER_ENABLED OFF CACHE BOOL "Qt?" FORCE)

set(TERRALIB_MOD_MNT_CORE_ENABLED ON CACHE BOOL "Build MNT Processing Core module?" FORCE)
set(TERRALIB_MOD_BINDING_PYTHON_ENABLED ON CACHE BOOL "Build TerraLib bindings?" FORCE)
set(TERRALIB_MOD_BINDING_LUA_ENABLED OFF CACHE BOOL "Build TerraLib bindings?" FORCE)
set(TERRALIB_MOD_ADO_ENABLED OFF CACHE BOOL "Build the TerraLib with ADO?" FORCE)
set(TERRALIB_MOD_WMS_QT_ENABLED OFF CACHE BOOL "Build the TerraLib Qt Web Map Service?" FORCE)
set(TERRALIB_MOD_STATISTICS_QT_ENABLED OFF CACHE BOOL "Build Qt support for Statistics module?" FORCE)
set(TERRALIB_MOD_VP_QT_ENABLED OFF CACHE BOOL "Build Vector Processing Qt module?" FORCE)
set(TERRALIB_MOD_SA_QT_ENABLED OFF CACHE BOOL "Build Spatial Analysis Qt module?" FORCE)
set(TERRALIB_MOD_TERRALIB4_ENABLED OFF CACHE BOOL "Build TerraLib4 module?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_LAYOUT_ENABLED OFF CACHE BOOL "Build Layout plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_ADO_ENABLED OFF CACHE BOOL "Build ADO Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_GDAL_ENABLED OFF CACHE BOOL "Build GDAL Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_OGR_ENABLED OFF CACHE BOOL "Build OGR Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_POSTGIS_ENABLED OFF CACHE BOOL "Build PostGIS Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_TERRALIB4_ENABLED OFF CACHE BOOL "Build TerraLib4 Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_WCS_ENABLED OFF CACHE BOOL "Build WCS Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_WFS_ENABLED OFF CACHE BOOL "Build WFS Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_DATASOURCE_WMS_ENABLED OFF CACHE BOOL "Build WMS Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_VP_ENABLED OFF CACHE BOOL "Build Vector Processing Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_RP_ENABLED OFF CACHE BOOL "Build Raster Processing Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_SA_ENABLED OFF CACHE BOOL "Build Spatial Analysis Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_APF_ENABLED OFF CACHE BOOL "Build Spatial Analysis Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_ST_ENABLED OFF CACHE BOOL "Build Spatial Analysis Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_QT_WIDGETS_ENABLED OFF CACHE BOOL "Build Terralib Qt Widgets module?" FORCE)
set(TERRALIB_MOD_BINDING_JAVA_ENABLED OFF CACHE BOOL "Build TerraLib bindings?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_CELLSPACE_ENABLED OFF CACHE BOOL "Build Cellular Spaces Qt Plugin?" FORCE)
set(TERRALIB_MOD_ATTRIBUTEFILL_QT_ENABLED OFF CACHE BOOL "Build Attribute Fill Qt module?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_ADDRESSGEOCODING OFF CACHE BOOL "Build Address Geocoding Driver Qt plugin?" FORCE)
set(TERRALIB_MOD_EDIT_QT_ENABLED OFF CACHE BOOL "Build Edit Qt module?" FORCE)
set(TERRALIB_MOD_QT_PLUGINS_EDIT_ENABLED OFF CACHE BOOL "Build Edit Qt plugin?" FORCE)
set(TERRALIB_MOD_WS_OGC_WMS_QT_ENABLED OFF CACHE BOOL "Build Qt Components for OGC WMS?" FORCE)
set(TERRALIB_MOD_WS_OGC_WCS_CLIENT_ENABLED OFF CACHE BOOL "Build OGC WCS Client Support?" FORCE)
set(TERRALIB_MOD_METADATA_ENABLED OFF CACHE BOOL "Build Metadata?" FORCE)
set(TERRALIB_MOD_PROCESS_QT_ENABLED OFF CACHE BOOL "Build Process Qt module?" FORCE)
set(TERRALIB_MOD_PROCESS_ENABLED OFF CACHE BOOL "Build Process module?" FORCE)
