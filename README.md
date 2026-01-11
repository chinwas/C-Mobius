C-Mobius 🌀
C-Mobius is a lightweight C++ terminal application that renders a dynamic, flowing ASCII Möbius strip. Instead of a static image, the characters on the surface of the strip shift continuously, creating the illusion of a liquid or "river-like" flow along its non-orientable surface.

✨ Features
Dynamic ASCII Flow: The characters within the strip are not static; they rotate through a character queue to simulate motion.

Flicker-Free Animation: Uses ANSI escape sequences to clear the screen and reset the cursor position, ensuring a smooth visual experience.

Zero Dependencies: Built entirely with the C++ Standard Library (iostream, vector, chrono, and thread).

Minimalist Design: Focuses on the "retro-hacker" terminal aesthetic.

⚙️ How It Works
The animation logic is divided into three main parts:

The Character Queue: A sequence of 66 ASCII symbols (ranging from space to dense @) is stored in a std::vector.

Cyclic Rotation: In every frame, the program moves the first character of the vector to the back. This "shifts" the entire texture of the strip by one unit.

The Geometry Map: The Möbius strip shape is hard-coded into a frame buffer. Each point on the strip references a specific index in the character vector. Because the vector is rotating but the indices stay the same, the symbols appear to flow through the shape.

🕹️ Why This Project?
Mathematical Art: It translates the complex topology of a Möbius strip into a simple terminal visual.

Performance Testing: It demonstrates how to handle 30 FPS terminal updates efficiently using std::ostringstream to prevent screen tearing.

Visual Interest: It serves as a great "screen saver" or background process for terminal enthusiasts.

🚀 Getting Started
Prerequisites
A C++ compiler (GCC, Clang, or MSVC).

A terminal that supports ANSI Escape Sequences (default on Linux/macOS; supported on Windows 10/11).
