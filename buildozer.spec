[app]

# (str) Title of your application
title = Cosmic Tunnel

# (str) Package name
package.name = cosmictunnel

# (str) Package domain (needed for android/ios packaging)
package.domain = org.iraska

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let buildozer find them)
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*

# (list) List of exclusions using pattern matching
# source.exclude_patterns = tests/*,docs/*

# (str) Application versioning
version = 0.1

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Application requirements
# IMPORTANT: Python 3.10 forced for pyjnius compatibility
requirements = python3==3.10,kivy

# (str) Presplash image
presplash.filename = data/presplash.png

# (str) Icon of the application
icon.filename = data/icon.png

# (str) Entry point
entrypoint = main.py


# ------------------------------------------------------------------
# ANDROID CONFIGURATION
# ------------------------------------------------------------------

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK supports
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX
android.enable_androidx = True

# (list) Permissions
android.permissions = INTERNET

# (str) Android application theme
android.apptheme = @android:style/Theme.NoTitleBar

# (str) Build tools version (leave empty = auto)
# android.build_tools_version =

# (str) Java source compatibility
android.gradle_dependencies =

# (bool) Copy libraries instead of linking
android.copy_libs = True


# ------------------------------------------------------------------
# PYTHON FOR ANDROID
# ------------------------------------------------------------------

# (str) python-for-android branch
p4a.branch = stable

# (str) python-for-android bootstrap
p4a.bootstrap = sdl2

# (bool) Ignore setup.py of dependencies
p4a.ignore_setup_py = True


# ------------------------------------------------------------------
# LOGGING / DEBUG
# ------------------------------------------------------------------

# (int) Log level (0 = normal, 2 = very verbose)
log_level = 1

# (bool) Display debug logs
debug = False

