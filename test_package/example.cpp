#include <iostream>

#include <scope_guard/scope_guard.hpp>

int main() {
    auto guard = sg::make_scope_guard([]()noexcept { std::cout << "It Works!" << std::endl; });
}
