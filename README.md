# fbjni-conan

Conan 2 recipe for [fbjni](https://github.com/facebookincubator/fbjni), Facebook's C++ wrapper around JNI, built for desktop JVMs.

Upstream fbjni builds on desktop through CMake, but nobody publishes desktop binaries or a Conan recipe. This repo holds the recipe; [fbjni-runtime-dist](https://github.com/measly-java-learning/fbjni-runtime-dist) uses it to build the native libraries published to Maven Central as `org.measly:fbjni-natives`.

## Supported platforms

- Linux x86_64 and aarch64
- macOS arm64 and x86_64 (minimum macOS 11.0)
- Windows is not supported; upstream fbjni does not build there.

## Status

Work in progress. The recipe is intended for submission to ConanCenter.

## License

Apache-2.0, matching upstream fbjni.
