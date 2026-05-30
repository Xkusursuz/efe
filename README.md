# JARVIS - AI Design Assistant

## Overview

JARVIS is a bilingual AI assistant (English & Turkish) designed to help with online design work. It features intelligent design suggestions, color recommendations, layout assistance, and creative support.

### Key Features

- 🎨 **Online Design Tool** - Web-based design interface
- 🤖 **AI Assistant** - Intelligent design recommendations
- 🌐 **Bilingual Support** - English & Turkish
- 🎯 **Status Indicators**
  - 🟢 **Green** - JARVIS is speaking
  - 🟡 **Yellow** - JARVIS is listening
  - 🔴 **Red** - JARVIS is silent
- 💡 **Design Features**
  - Color palette recommendations
  - Layout suggestions
  - Asset management
  - Creative brainstorming

## Project Structure

```
efe/
├── first_impression.py      # Main JARVIS initialization
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── config/
│   └── jarvis_config.json   # Configuration file
├── src/
│   ├── jarvis_core.py       # Core JARVIS engine
│   ├── design_tool.py       # Online design tool backend
│   ├── ai_engine.py         # AI and NLP engine
│   └── languages.py         # Language support
├── web/
│   ├── index.html           # Frontend interface
│   ├── css/
│   │   └── style.css        # Styling
│   └── js/
│       └── app.js           # Frontend logic
└── tests/
    └── test_jarvis.py       # Unit tests
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Xkusursuz/efe.git
cd efe
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the first impression:
```bash
python first_impression.py
```

## Usage

### Starting JARVIS

```python
from first_impression import JARVISFirstImpression

# Initialize with English
jarvis = JARVISFirstImpression(language="en")
jarvis.display_welcome()
jarvis.speak("greeting")

# Or initialize with Turkish
jarvis_tr = JARVISFirstImpression(language="tr")
jarvis_tr.display_welcome()
```

## Status Indicators

JARVIS communicates its status through color indicators:

| Status | Color | Meaning |
|--------|-------|----------|
| Speaking | 🟢 Green | JARVIS is providing information or suggestions |
| Listening | 🟡 Yellow | JARVIS is waiting for user input |
| Silent | 🔴 Red | JARVIS is in standby mode |

## Multilingual Support

JARVIS supports both English and Turkish. Switch languages by passing the language parameter:

```python
# English
jarvis = JARVISFirstImpression(language="en")

# Turkish
jarvis = JARVISFirstImpression(language="tr")
```

## Development

Contributions are welcome! Please follow these guidelines:

1. Create a new branch for features
2. Write tests for new functionality
3. Submit a pull request

## License

MIT License - See LICENSE file for details

## Author

Xkusursuz

## Support

For issues or questions, please open an issue on GitHub.
