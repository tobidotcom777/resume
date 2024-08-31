from agency_swarm.tools import BaseTool
from pydantic import Field
from transformers import pipeline

# Initialize the text generation pipeline globally
text_generator = pipeline("text-generation", model="gpt-3.5-turbo")

class EbookContentGenerator(BaseTool):
    """
    This tool generates engaging ebook content based on a given topic or outline.
    It structures the content into chapters, sections, and paragraphs, ensuring coherence
    and readability. The tool also allows for customization of writing style and tone.
    """

    topic: str = Field(
        ..., description="The main topic or outline for the ebook content."
    )
    chapters: int = Field(
        ..., description="The number of chapters to generate."
    )
    sections_per_chapter: int = Field(
        ..., description="The number of sections per chapter."
    )
    paragraphs_per_section: int = Field(
        ..., description="The number of paragraphs per section."
    )
    writing_style: str = Field(
        ..., description="The desired writing style (e.g., 'formal', 'informal', 'technical')."
    )
    tone: str = Field(
        ..., description="The desired tone (e.g., 'serious', 'humorous', 'inspirational')."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method generates the ebook content based on the provided parameters.
        """
        ebook_content = f"Title: {self.topic}\n\n"
        
        for chapter_num in range(1, self.chapters + 1):
            ebook_content += f"Chapter {chapter_num}: {self.topic} - Part {chapter_num}\n\n"
            
            for section_num in range(1, self.sections_per_chapter + 1):
                ebook_content += f"Section {chapter_num}.{section_num}: {self.topic} - Section {section_num}\n\n"
                
                for paragraph_num in range(1, self.paragraphs_per_section + 1):
                    prompt = (
                        f"Write a {self.writing_style} and {self.tone} paragraph about {self.topic} "
                        f"for Chapter {chapter_num}, Section {section_num}, Paragraph {paragraph_num}."
                    )
                    generated_text = text_generator(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
                    ebook_content += f"{generated_text}\n\n"
        
        return ebook_content