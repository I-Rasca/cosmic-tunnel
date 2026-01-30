[app]
title = Cosmic Tunnel
package.name = cosmictunnel
package.domain = org.cosmic

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# ---------- ANDROID (ESTABLE) ----------

android.minapi = 21
android.api = 31
android.ndk = 25b

# 🔒 CLAVE ABSOLUTA
android.build_tools_version = 30.0.3

# ❌ NO pongas android.sdk_path en CI
# Buildozer gestiona su propio SDK


# Evita que intente cosas modernas raras
android.skip_update = True

# Arquitecturas comunes
android.archs = arm64-v8a,armeabi-v7a

