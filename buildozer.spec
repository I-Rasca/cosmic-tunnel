[buildozer]
# Log level (0 = error only, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# Buildozer build directory
build_dir = .buildozer

# If yes, buildozer will attempt to use ccache
use_ccache = True


[app]
# (str) Title of your application
title = Cosmic Tunnel

# (str) Package name
package.name = cosmictunnel

# (str) Package domain (reverse DNS)
package.domain = org.iraska

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv

# (list) Source files to exclude
source.exclude_exts = spec

# (str) Application version
version = 0.1

# (str) Application requirements
requirements = python3,kivy

# (str) Entry point
entrypoint = main.py

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1


[graphics]
# (str) Supported orientations:
# portrait, landscape, landscape-reverse, portrait-reverse
orientation = portrait


[android]
# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (list) Architectures to build for
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Extra Gradle dependencies
android.gradle_dependencies = androidx.core:core-ktx:1.12.0

# (bool) Allow application backup
android.allow_backup = True

# (bool) Copy libraries instead of symlinking
android.copy_libs = True

# (str) Android application theme
android.apptheme = @android:style/Theme.NoTitleBar

# (list) Permissions
android.permissions = INTERNET

# (str) Icon and presplash (optional but recommended)
icon.filename = data/icon.png
presplash.filename = data/presplash.png


[buildozer:android]
# This section is intentionally left minimal and stable

