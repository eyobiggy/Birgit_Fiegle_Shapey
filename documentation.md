Project Documentation: Shapey – Fun Background Generator

🧠 Idea to Execution
The idea started from a simple goal:
"Can I build a creative tool that generates abstract art based on mood?"

Initially, the concept was about drawing shapes randomly. From there, it expanded:

Add user interaction

Provide meaningful visual variation (color palettes and complexity)

Enable saving images

Build a clean, vintage-style UI

🎨 Features Implemented
Custom palette generation based on HSV color space

Mood-based art generation using geometric shape functions

Pygame interface with a start and display screen

Interactive UI: buttons, slider, dropdown

Save function that exports art to user’s ~/Pictures/GeneratedArt folder

"Surprise me" mode for random moods

Several visual vibes: sunshine, ocean, pastel, forest, etc.

Display of save confirmation box with file path (shortened neatly)

⚙️ General Framework
UI Framework: Built entirely in Pygame, using custom buttons, backgrounds, and fonts.

Artwork Generation: Delegated to art_generator.py, which combines shapes, randomness, and user-defined complexity.

Color Management: Done through HSV color space using Python’s colorsys, ensuring better perceptual control than plain RGB.

Saving Art: Images are saved using Pillow, converted to Pygame surfaces via a BytesIO bridge.

🔍 Key Difficult Functions (Where I Used AI)
I wrote and designed much of the project structure, interface, and idea myself. However, I made good use of AI assistance (ChatGPT) in solving specific, more technical problems or when trying to implement something outside my comfort zone. Here are examples:

Function / Part	Why AI Helped
draw_worm()	Complex math (parametric sine curves) for smooth organic movement
draw_star()	Geometry for drawing rotated 5-point stars in polar coordinates
Custom Button class	Event handling and hover/click feedback were difficult to design from scratch
Palette generation in HSV space	I knew what I wanted visually but wasn't fluent with HSV → RGB conversion math
ask_save_path_safe()	Needed a safe, cross-platform way to choose a save path in the Pictures folder
Text clipping in message box	Truncating file paths to fit in a UI box without cutting mid-word was tricky

These were either beyond my current level, too time-consuming to trial-and-error, or required unfamiliar techniques. I asked for code help, then tweaked the results to fit my visual and structural goals.

🧗‍♂️ Challenges and Solutions
Challenge	How I Overcame It
Not familiar with Pygame UI design	Studied examples online, adapted layout logic, and consulted AI
Tricky shape math (rotation, curves)	Asked AI for help, then visualized and adjusted values until it worked
Preventing file path overflow in UI	Researched pygame.font.size() and used it to dynamically clip strings
Deciding project structure	Iteratively separated UI, shape logic, and color logic into files
Making slider interactive	Followed logic from tutorials, then asked AI to help fix drag behavior
Naming main.py misleadingly	Renamed it to something like shapey_runner.py to avoid confusion

🧪 Lessons Learned
Even a seemingly “simple” app becomes complex fast with UI and randomness.

Planning color generation properly (with HSV) makes a huge difference visually.

Writing reusable classes (like Button) early saves you from copy-pasting logic later.

Breaking the project into modules (art_generator, palettes, ui, etc.) kept me sane.

🔮 Future Development Ideas
Add background music or sound effects

Export high-resolution versions for printing

Let users upload palettes or draw shapes themselves

Add animation or GIF export

Generate titles or mood names for each artwork

Package it as a standalone app using PyInstaller

🤝 References and Tools
Pygame Documentation

Pillow Documentation

Stack Overflow for small bug-fixes

OpenAI’s ChatGPT (used as a tutor, debugger, and co-designer for complex logic)

Some inspiration from generative artists and palette tools like Coolors and Adobe Color

👋 Final Thoughts
I learned a lot about randomness, design, structure, and user experience from building Shapey. While I used AI for challenging functions, the vision, direction, visual style, and architecture were all mine. I feel proud of combining creativity and code into something that is fun to use and visually engaging.

Let me know if you’d like this formatted as a PDF or submitted in a different format.