[app]

# (str) Title of your application
title = Cosmic Tunnel

# (str) Package name
package.name = cosmictunnel

# (str) Package domain (needed for android)
package.domain = org.iraska

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash image
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape / portrait)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1


# -------------------------
# ANDROID CONFIG
# -------------------------

# (int) Android API to build against
android.api = 33

# (int) Minimum API your app supports
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Use AndroidX
android.enable_androidx = 1

# (list) Permissions
android.permissions = INTERNET

# (bool) Copy libs instead of linking
android.copy_libs = 1

# (str) Logcat filters
android.logcat_filters = *:S python:D


# -------------------------
# BUILD OPTIONS
# -------------------------

# (bool) Enable debug symbols
android.debuggable = 1

# (bool) Enable OpenGL ES 2
android.opengl_es = 2


# -------------------------
# KIVY CONFIG
# -------------------------

# (str) Kivy version
kivy.version = stable

# (bool) Include SDL2
android.include_sdl2 = 1


# -------------------------
# OTHER
# -------------------------

# (str) Path to main python file
entrypoint = main.py

# (bool) Use legacy packaging
android.use_legacy_packaging = 0


