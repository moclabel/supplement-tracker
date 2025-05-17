[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (reverse DNS style)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Android API to target
android.api = 33

# (str) Minimum Android API your APK will support
android.minapi = 21

# (str) Android SDK build tools version
android.build_tools_version = 36.0.0

# (int) Target SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (bool) Use Android arch armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a, arm64-v8a

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, choose from "import", "black", "white"
android.theme = import

# (bool) Copy assets as is
copy_assets = True

# (list) Permissions
android.permissions = INTERNET

# (bool) Use androidX libraries
android.use_androidx = True
