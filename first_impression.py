#!/usr/bin/env python3
"""
JARVIS AI Assistant - First Impression Module
Bilingual AI Assistant with Online Design Tool
Author: Xkusursuz
Languages: English & Turkish
"""

import os
import sys
from enum import Enum
from datetime import datetime
from typing import Dict, List
import json

# Status Indicator Colors
class Status(Enum):
    """JARVIS Status Indicator"""
    SPEAKING = "\033[92m"  # Green
    LISTENING = "\033[93m"  # Yellow
    SILENT = "\033[91m"     # Red
    RESET = "\033[0m"       # Reset color

# Multilingual Messages
MESSAGES = {
    "en": {
        "greeting": "Hello! I'm JARVIS, your AI design assistant. How can I help you today?",
        "listening": "I'm listening...",
        "silent": "Standing by...",
        "design_ready": "I'm ready to help with your design project.",
        "welcome": "Welcome to JARVIS Online Design Tool",
        "features": "My capabilities include: Design suggestions, Color recommendations, Layout assistance, Creative brainstorming"
    },
    "tr": {
        "greeting": "Merhaba! Ben JARVIS, sizin AI tasarım asistanınız. Bugün sana nasıl yardımcı olabilirim?",
        "listening": "Dinliyorum...",
        "silent": "Beklemeye hazırım...",
        "design_ready": "Tasarım projenize yardımcı olmaya hazırım.",
        "welcome": "JARVIS Online Tasarım Aracına Hoş Geldiniz",
        "features": "Yeteneklerim: Tasarım önerileri, Renk önerileri, Düzen yardımı, Yaratıcı beyin fırtınası"
    }
}

class JARVISFirstImpression:
    """JARVIS Initial Configuration and Status Management"""
    
    def __init__(self, language: str = "en"):
        """
        Initialize JARVIS with language preference
        
        Args:
            language: 'en' for English or 'tr' for Turkish
        """
        self.language = language if language in ["en", "tr"] else "en"
        self.status = Status.SILENT
        self.start_time = datetime.now()
        self.config = self._load_config()
        
    def _load_config(self) -> Dict:
        """Load or create JARVIS configuration"""
        config = {
            "name": "JARVIS",
            "version": "1.0.0",
            "language": self.language,
            "status": "ready",
            "features": [
                "ai_design_assistant",
                "online_design_tool",
                "bilingual_support",
                "color_recommendations",
                "layout_suggestions",
                "asset_management"
            ],
            "created_at": self.start_time.isoformat(),
            "status_indicators": {
                "speaking": "Green",
                "listening": "Yellow",
                "silent": "Red"
            }
        }
        return config
    
    def set_status(self, status: Status) -> None:
        """Set JARVIS status and display indicator"""
        self.status = status
        status_text = {
            Status.SPEAKING: "SPEAKING",
            Status.LISTENING: "LISTENING",
            Status.SILENT: "SILENT"
        }
        print(f"{status.value}● {status_text[status]} {Status.RESET.value}")
    
    def speak(self, message_key: str) -> str:
        """Get message in current language and speak status"""
        self.set_status(Status.SPEAKING)
        message = MESSAGES[self.language].get(message_key, "")
        print(f"JARVIS: {message}")
        return message
    
    def listen(self) -> None:
        """Set listening status"""
        self.set_status(Status.LISTENING)
        print(f"JARVIS: {MESSAGES[self.language]['listening']}")
    
    def silent(self) -> None:
        """Set silent status"""
        self.set_status(Status.SILENT)
        print(f"JARVIS: {MESSAGES[self.language]['silent']}")
    
    def display_welcome(self) -> None:
        """Display welcome message and configuration"""
        print("\n" + "="*60)
        self.speak("welcome")
        print("="*60)
        print(f"\nVersion: {self.config['version']}")
        print(f"Language: {self.language.upper()}")
        print(f"Status Indicators: Green (Speaking) | Yellow (Listening) | Red (Silent)")
        print(f"\n{MESSAGES[self.language]['features']}")
        print("\n" + "="*60 + "\n")
    
    def get_config(self) -> Dict:
        """Return current configuration"""
        return self.config
    
    def export_config(self, filepath: str = "jarvis_config.json") -> None:
        """Export configuration to JSON file"""
        with open(filepath, 'w') as f:
            json.dump(self.config, f, indent=2)
        print(f"Configuration exported to {filepath}")


def main():
    """Main entry point - JARVIS First Impression"""
    # Initialize JARVIS with English and Turkish support
    print("\n" + "#"*60)
    print("# JARVIS AI ASSISTANT - ONLINE DESIGN TOOL")
    print("#"*60 + "\n")
    
    # Create JARVIS instance with English
    jarvis_en = JARVISFirstImpression(language="en")
    jarvis_en.display_welcome()
    jarvis_en.speak("greeting")
    jarvis_en.speak("design_ready")
    
    print("\n" + "-"*60 + "\n")
    
    # Create JARVIS instance with Turkish
    jarvis_tr = JARVISFirstImpression(language="tr")
    jarvis_tr.display_welcome()
    jarvis_tr.speak("greeting")
    jarvis_tr.speak("design_ready")
    
    print("\n" + "#"*60 + "\n")
    
    # Export configuration
    jarvis_en.export_config()
    jarvis_tr.export_config("jarvis_config_tr.json")


if __name__ == "__main__":
    main()
