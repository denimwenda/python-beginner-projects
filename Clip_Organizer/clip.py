import json

class ClipOrganizer:
    def __init__(self, filename='clips.json'):
        self.clips = {}
        self.filename = filename
        self.load_clips()

    def add_clip(self, clip, tags):
        for tag in tags:
            if tag not in self.clips:
                self.clips[tag] = []
            self.clips[tag].append(clip)
        self.save_clips()

    def get_clips_by_tag(self, tag):
        return self.clips.get(tag, [])

    def list_tags(self):
        return list(self.clips.keys())

    def delete_clip(self, clip, tag):
        if tag in self.clips and clip in self.clips[tag]:
            self.clips[tag].remove(clip)
            if not self.clips[tag]:  # remove the tag if no clips are left
                del self.clips[tag]
            self.save_clips()

    def save_clips(self):
        with open(self.filename, 'w') as f:
            json.dump(self.clips, f)

    def load_clips(self):
        try:
            with open(self.filename, 'r') as f:
                self.clips = json.load(f)
        except FileNotFoundError:
            self.clips = {}

# Example usage
organizer = ClipOrganizer()

# Add some clips
organizer.add_clip("This is a sample clip about Python.", ["python", "programming"])
organizer.add_clip("Another clip about machine learning.", ["machine learning", "AI"])

# Retrieve clips by tag
print("Clips tagged with 'python':", organizer.get_clips_by_tag("python"))

# List all tags
print("All tags:", organizer.list_tags())

# Delete a clip
organizer.delete_clip("This is a sample clip about Python.", "python")

# Check clips again after deletion
print("Clips tagged with 'python' after deletion:", organizer.get_clips_by_tag("python"))
