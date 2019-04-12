from conans import ConanFile, CMake, tools


class ScopeguardConan(ConanFile):
    name = "scope_guard"
    version = "0.2.3"
    license = "The Unlicense"
    url = "https://github.com/Lawrencemm/scope_guard_conan"
    description = "A modern C++ scope guard that is easy to use but hard to misuse. https://ricab.github.io/scope_guard/"
    topics = ("scope guard", "RAII", "resource management")

    def source(self):
        self.run("git clone https://github.com/ricab/scope_guard.git")
        self.run("cd scope_guard && git checkout v0.2.3")

    def package(self):
        self.copy("*scope_guard.hpp", dst="include")

