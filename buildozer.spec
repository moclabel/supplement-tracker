[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let's include everything)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (str) Requirements
requirements = python3==3.10.13, kivy, cython==0.29.36

# (str) Presplash image
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Android API to compile against (latest stable)
android.api = 33

# (str) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK build tools version
android.build_tools_version = 36.0.0

# (str) Android NDK version to use
android.ndk = 25.1.8937393

# (int) Target API level (recommended to keep as android.api)
android.target = 33

# (bool) Use AndroidX libraries (should be true for modern Android builds)
android.use_androidx = True

# (bool) Whether to include the Python stdlib inside the APK
android.include_stdlib = true

# (str) Android entry point, default is ok for Kivy apps
android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported architectures, usually armeabi-v7a and arm64-v8a
android.archs = armeabi-v7a, arm64-v8a

# (bool) Use SDL2 window provider (recommended)
android.window = sdl2

# (int) Presplash animation duration in seconds
presplash.duration = 3

# (bool) Enable or disable debug symbols in the APK
android.debug = False

# (int) Number of concurrent processes during build
num_parallel_builds = 4

# (str) Log level: info, debug, error, warning
log_level = info
