## **Project Documentation: Shapey – Your Fun Background Generator**

### **Idea to Execution**

**The idea started from a simple goal:**
"Can I build a creative tool that generates abstract art based on mood?"

Initially, the concept was about drawing shapes randomly. From there, it expanded:
- Add user interaction
- Provide meaningful visual variation (color palettes and complexity)
- Enable saving images
- Build a clean, vintage-style UI

### **Features Implemented**

- Custom palette generation based on HSV color space
- Mood-based art generation using geometric shape functions
- Pygame interface with a start and display screen
- Interactive UI: buttons, slider, dropdown
- Save function that exports art to user’s ~/Pictures/GeneratedArt folder
- "Surprise me" mode for random moods
- Several visual vibes: sunshine, ocean, pastel, forest, etc.
- Display of save confirmation box with file path (shortened neatly)

### **General Framework**

**UI Framework:** Built entirely in Pygame, using custom buttons, backgrounds, and fonts.

**Artwork Generation:** Delegated to art_generator.py, which combines shapes, randomness, and user-defined complexity.

**Color Management:** Done through HSV color space using Python’s colorsys, ensuring better perceptual control than plain RGB.

**Saving Art:** Images are saved using Pillow, converted to Pygame surfaces via a BytesIO bridge.

### **Key Difficult Functions (Where I Used AI)**

I wrote and designed much of the project structure, interface, and idea myself. However, I made good use of AI assistance (ChatGPT) in solving specific, more technical problems or when trying to implement something outside my comfort zone.

| function                        | part where AI helped                                                                              |
|---------------------------------|---------------------------------------------------------------------------------------------------|
| draw_worm()                     | complex math to make shape exactly how I wanted it to look like                                   |
| draw_raindrop()                 | -//-                                                                                              |
| draw_squiggle()                 | -//-                                                                                              |
| ask_save_path_safe()            | save, cross-platform way to choose a save path in the Pictures folder                             |
| text clipping in message box    | truncating file paths to fit in a UI box without cutting mid-word                                 |
| Custom Button Class             | event handling and hover/click feedback                                                           |
| HSV → RGB conversion            | I knew what I wanted visually but wasn't fluent with HSV to RGB conversion math                   |
| pil_to_surface()                | converting pillow image to Pygame surface                                                         |
| handling mouse actions          | checking and updating states of the buttons and letting them change color when clicked or hovered |
| for i, vibe in enumerate(vibes) | drawing vibe buttons in 2 columns                                                                 |
| main loop                       | bringing everything together and fixing tiny details I missed                                     |


These were either beyond my current level, too time-consuming to trial-and-error, or required unfamiliar techniques. I asked for code help, then tweaked the results to fit my visual and structural goals.

### **Challenges and Solutions**

| Challenge                                       | How I Overcame It                                                                    |
|-------------------------------------------------|--------------------------------------------------------------------------------------|
| not familiar with Pygame UI Design              | studied examples online, adapted layout logic, consulted AI, drew backgrounds myself |
| tricky shape math (rotation, curves)            | asked AI for help, then visualized and adjusted values until it worked               |
| deciding project structure                      | iteratively separated UI, shape logic and color logic into files                     |
| making slider interactive                       | followed logic from tutorials, then asked AI to help fix drag behaviour              |
| creating gradient effect                        | learned from reddit, tutorials                                                       |
| balancing randomness with aesthetic consistency | initially tried evenly spaced hues, but ended up fully randomizing the colors        |

### **Lessons Learned**
Even a seemingly “simple” app becomes complex fast, especially with UI. I had the Picture Generating done quite quick and lost myself in the details of the UI then. If I wanted to, I could have added feature after feature, button after button and at some point it was actually getting difficult to keep it simple. What also turned out to be extremely helpful, was to break the project into different modules. It helped so much to keep an overview over all the code. 


### **Future Development Ideas**

- Add background music or sound effects
- Let users upload palettes or draw shapes themselves 
- Package it as a standalone app using PyInstaller
- language processing model that creates artworks based on basic user input
- option for user to choose, which shapes they would like to include/exclude
- reveal artwork with a more dramatic effect

### **References and Tools**

- Pygame Documentation 
- Pillow Documentation 
- OpenAI’s ChatGPT (used as a tutor, debugger, and co-designer for complex logic)
- Reddit
- selecolor.com for exploring the HSV color system and choosing settings for the palettes

### **Final Thoughts**
I learned a lot about randomness, design, structure, and user experience from building Shapey. While I used AI for challenging functions, the vision, direction, visual style, and architecture were all mine. I found it interesting but also challenging (in a good way) to work on a bigger Python project for the first time. I feel proud of combining creativity and code into something that is fun to use and visually engaging.
