[app]
title = Cosmic Tunnel
package.name = cosmictunnel
package.domain = org.irascadev

source.dir = .
source.include_exts = py,png,jpg,kv,mp3

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

icon.filename = data/icon.png
presplash.filename = data/presplash.png

log_level = 2

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.minapi = 21
android.api = 33
android.ndk = 25b

android.arch = arm64-v8a,armeabi-v7a

android.permissions = INTERNET
android.enable_androidx = True
