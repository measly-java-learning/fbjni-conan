# fbjni-conan

Conan 2 recipe for [fbjni](https://github.com/facebookincubator/fbjni), Facebook's C++ wrapper around JNI, built for desktop JVMs.

Upstream fbjni builds on desktop through CMake, but nobody publishes desktop binaries or a Conan recipe. This repo holds the recipe; [fbjni-runtime-dist](https://github.com/measly-java-learning/fbjni-runtime-dist) uses it to build the native libraries published to Maven Central as `org.measly:fbjni-natives`.

## Supported platforms

- Linux x86_64 and aarch64
- macOS arm64 and x86_64 (minimum macOS 11.0)
- Windows is not supported; upstream fbjni does not build there.

## Building

The recipe follows ConanCenter's layout under `recipes/fbjni/`. By default it downloads `zulu-openjdk` for `jni.h`:

```sh
conan create recipes/fbjni/all --version 0.8.1 -o "fbjni/*:shared=True"
```

To use a JDK that is already installed, set `JAVA_HOME` (or conf `user.fbjni:java_home`) and pass `-o "fbjni/*:system_java=True"`.

Consumers using `CMakeDeps` link `fbjni::fbjni`; its CMake integration runs `find_package(JNI)` to add the consumer's own `jni.h`.

## Status

Work in progress. The recipe is intended for submission to ConanCenter.

## License

Apache-2.0, matching upstream fbjni.
