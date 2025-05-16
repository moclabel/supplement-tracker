[app]
title = Supplement Tracker
package.name = supplementtracker
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.api = 33
android.minapi = 21
android.sdk_path = $HOME/Library/Android/sdk
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r25b
android.permissions = INTERNET
android.arch = armeabi-v7a

# buildozer automatically uses latest tools unless this is pinned:
# (Zorunlu değilse kaldırdık)
# android.build_tools_version = 33.0.2

[app.android.ndk]
# Gerekli değilse boş bırakıyoruz

[app.android.logcat]
# Gerekli değilse boş bırak

[app.android.p4a]
# Gerekli değilse boş bırak

[app.android.extra]
# Gerekli değilse boş bırak

[app.android.gradle_dependencies]
# Gerekli değilse boş bırak

[app.android.add_src]
# Gerekli değilse boş bırak

[app.android.add_jars]
# Gerekli değilse boş bırak

[app.android.replace_presplash]
# Gerekli değilse boş bırak

[app.android.add_presplash]
# Gerekli değilse boş bırak

[app.android.add_resources]
# Gerekli değilse boş bırak

[app.android.add_assets]
# Gerekli değilse boş bırak

[app.android.runnable]
# Gerekli değilse boş bırak

[app.android.copy_libs]
# Gerekli değilse boş bırak

[app.ios]
# iOS hedeflemiyoruz

[buildozer]
build_dir = .buildozer
bin_dir = bin
