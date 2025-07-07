[app]

# (str) Title of your application
title = FaceApp Attendance

# (str) Package name
package.name = faceappattendance

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy

# (str) Application versioning (method 1)
version = 0.1

# (list) Requirements (must be separated by comma):
# python3, kivy, flask, flask-cors, numpy, opencv, requests.
# Note: 'opencv' is the correct requirement for Buildozer, not 'opencv-python'.
requirements = python3, kivy==2.2.1, flask, flask-cors, numpy, opencv, requests

# (str) Kivy version if you use a specific one
# kivy.version = 2.2.1

# (str) Source code where the main.py lives
source.dir = .

# (list) List of inclusions for packaging (comma separated).
# These are files/directories that should be included in the APK.
source.include_exts = py, png, jpg, xml, json, mp3
source.include_patterns = haarcascade_frontalface_default.xml, known_faces/*, user_emails.json, daily_attendance.json

# (list) Android permissions (comma separated)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API level (e.g., 27, 28, 29, 30, 31, 32, 33)
# It is recommended to use a recent API level for security and compatibility.
android.api = 33

# (int) Minimum Android API level (e.g., 21, 24)
android.minapi = 24

# (list) Android archs to build for (comma separated)
# arm64-v8a is for newer 64-bit devices, armeabi-v7a for older 32-bit devices.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable/disable fullscreen mode
fullscreen = 0

# (str) The orientation of the app (portrait, landscape, sensor)
orientation = portrait

# (str) Path to the Android SDK (optional, Buildozer will download if not set)
# android.sdk = /home/user/android-sdk

# (str) Path to the Android NDK (optional, Buildozer will download if not set)
# android.ndk = /home/user/android-ndk

# (str) Path to the Java JDK (optional, Buildozer will download if not set)
# java.home = /usr/lib/jvm/java-8-openjdk-amd64

# (list) Add a list of Java or Python files to delete from the APK
# android.blacklist = jni/armeabi/libcurl.so, jni/armeabi/libz.so

# (bool) If you want to use a Google Play Store key for signing the APK, set this to 1
# android.release_keystore = 0
# android.keystore.path = ~/.android/debug.keystore
# android.keystore.alias = androiddebugkey
# android.keystore.passphrase = android
# android.keystore.keypassword = android

# (list) Custom buildozer commands (optional)
# You can add custom commands to be run before/after specific build steps.
# For example:
# android.add_build_commands =
#    (before-package) echo "Running custom command before packaging"
#    (after-package) echo "Running custom command after packaging"

[buildozer]

# (int) Log level (0 = error, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# (str) Path to the Buildozer data directory
data_dir = ./.buildozer

# (str) Path to the Buildozer global data directory
global_data_dir = ~/.buildozer

# (list) Add a list of recipes to use for building (comma separated)
# p4a.recipes = hostpython3, kivy, openssl, requests

# (str) Path to the Python for Android toolchain
# p4a.path = /home/user/python-for-android
