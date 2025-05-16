[app]

title = Takviye Takip
package.name = takviyetakip
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 23
android.ndk = 25.1.8937393
android.ndk_path = /Users/builder/Library/Android/sdk/ndk/25.1.8937393
android.sdk_path = /Users/builder/Library/Android/sdk
android.build_tools_version = 36.0.0
android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0
android.arch = arm64-v8a
# Eğer x86_64 de istiyorsan aşağıdaki satırı uncomment et:
# android.archs = armeabi-v7a,arm64-v8a,x86_64

# Eğer icon kullanıyorsan:
# icon.filename = %(source.dir)s/icon.png

[buildozer]

log_level = 2
warn_on_root = 1

[android]

# Eğer başka Java bağımlılığı gerekiyorsa:
# android.add_jars = path/to/your.jar

# Eğer native modüller kullanıyorsan:
# android.permissions = INTERNET, CAMERA

# Modern Android destekleri için
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.1

# OpenGL ES 2 zorunluysa:
# android.opengl_es = 2
