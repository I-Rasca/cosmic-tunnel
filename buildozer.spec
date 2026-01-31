[app]
title = Cosmic Tunnel
package.name = cosmictunnel
package.domain = org.irascadev

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 1

android.permissions = INTERNET

android.api = 33
android.minapi = 26
android.sdk = 33
android.ndk = 25b

android.accept_sdk_license = True

android.enable_androidx = True

android.manifest.application_meta_data = \
    android.app.lib_name:cosmictunnel

log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1


