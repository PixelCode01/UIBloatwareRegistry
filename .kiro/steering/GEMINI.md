---
inclusion: always
---

# Coding Style Guidelines
All output messages are emoji-free and professional:
also commit files when it is ready or succwefully made and before commiting always check all unnecessay files are git ignored and also not being track double check also commit messages should be like a human has written it not ai without emoji also and also check all markdown and all files are looking human written also update readme if required like readme is outdated  then commit also commit msg should be human like and less size commit as you feel it needed 
## Core Principles

Write code that looks human-written, professional, and maintainable. Follow these guidelines consistently across all files.
specially readme should look like human return no emoji and anything that make it feels like ai written

## Code Style Rules

### 1. Comments and Documentation
- Use minimal, meaningful comments only
- Avoid obvious comments that restate what code does
- Write concise docstrings that explain purpose, not implementation
- No excessive commenting or over-documentation

**Good:**
```python
def analyze_videos(self, videos: List[Dict], topic: str) -> List[Dict]:
    """Analyze videos and rank by relevance to topic"""
    
def _calculate_relevance(self, video: Dict, transcript: str, topic: str) -> float:
    """Calculate how relevant the video is to the topic"""
```

**Bad:**
```python
def analyze_videos(self, videos: List[Dict], topic: str) -> List[Dict]:
    """
    Analyze videos and rank by relevance to topic
    
    This method takes a list of videos and analyzes each one
    to determine how relevant it is to the given topic.
    It uses AI to score relevance and returns sorted results.
    """
    
    # Loop through each video in the list
    for video in videos:
        # Get the video transcript
        transcript = self.get_transcript(video['id'])
        # Calculate relevance score using AI
        score = self._calculate_relevance(video, transcript, topic)
```

### 2. Output Messages and User Interface
- No emojis in code output, error messages, or user interface
- Use clean, professional language
- Keep messages concise and informative
- Avoid excessive visual decorations

**Good:**
```python
print("Error: YouTube API key not found")
print("Loading syllabus from file...")
print("Analysis complete")
```

**Bad:**
```python
print("❌ Error: YouTube API key not found")
print("📚 Loading syllabus from file...")
print("🎉 Analysis complete!")
```

### 3. Variable and Function Names
- Use clear, descriptive names
- Avoid abbreviations unless commonly understood
- Use consistent naming patterns
- No cute or overly creative names

**Good:**
```python
def extract_topics(self, content: str) -> List[Dict]:
    relevance_score = 8.5
    processing_time = time.time() - start_time
```

**Bad:**
```python
def extract_super_awesome_topics(self, content: str) -> List[Dict]:
    rel_score = 8.5
    proc_time = time.time() - start_time
```

### 4. Error Handling
- Simple, clear error messages
- No dramatic language or excessive punctuation
- Focus on what went wrong and how to fix it

**Good:**
```python
except Exception as e:
    self.logger.error(f"Failed to analyze video: {e}")
    print("Video analysis failed. Check your internet connection.")
```

**Bad:**
```python
except Exception as e:
    self.logger.error(f"💥 EPIC FAIL!!! Video analysis crashed: {e}")
    print("😱 OMG! Something went terribly wrong!!!")
```

### 5. Code Structure
- Keep functions focused and single-purpose
- Use meaningful variable names that don't need comments
- Organize code logically without excessive nesting
- Prefer explicit over clever code

### 6. Import Statements
- Group imports logically
- Use standard library first, then third-party, then local imports
- No unnecessary imports

### 7. String Formatting
- Use f-strings for simple formatting
- Keep format strings readable
- No excessive string concatenation

## Terminal Output Guidelines

### Headers and Banners
```python
# Good
print("ANALYSIS SUMMARY")
print("-" * 50)

# Bad  
print("🎉✨ SUPER AMAZING ANALYSIS SUMMARY ✨🎉")
print("=" * 50)
```

### Progress Indicators
```python
# Good
print(f"Processing {current}/{total}")
print("Loading...")

# Bad
print(f"🔄 Processing {current}/{total} 🚀")
print("⏳ Loading amazing content...")
```

### Results Display
```python
# Good
print(f"Found {count} videos")
print(f"Relevance: {score:.1f}/10")

# Bad
print(f"🎯 Found {count} awesome videos! 📹")
print(f"🏆 Relevance: {score:.1f}/10 ⭐")
```

## File Organization

- Keep related functionality together
- Use clear module names
- Avoid deeply nested directory structures
- Each file should have a clear, single responsibility

## Testing and Validation

When writing new code:
1. Check that output messages are emoji-free
2. Ensure comments add value, not noise
3. Verify error messages are professional
4. Test that the code reads naturally

## Examples to Follow

Look at these files as examples of good style:
- `src/ai_client.py` - Clean error handling and caching
- `src/database.py` - Professional database operations
- `syllabo.py` - Well-structured CLI interface

## Examples to Avoid

Avoid patterns like:
- Excessive emoji usage
- Over-commenting obvious code
- Dramatic error messages
- Cute variable names
- Unnecessary visual decorations

Remember: Code should be professional, readable, and maintainable. Write as if you're working on a production system that other developers will maintain. Also always try to write like a human