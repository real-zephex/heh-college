from spire.doc import Document
from spire.doc.common import *
import markdown

# Your Markdown string
markdown_string = """
Operating in mode: Comprehensive Mode

# The Significance of Past Revolutions:  Transforming Societies

Revolutions, by their very nature, are periods of radical social, political, and often violent upheaval that fundamentally reshape societies.  While each revolution has its unique context and characteristics, several common themes emerge regarding their broader significance.  Let's explore the impact of major revolutions like the French and Russian Revolutions, highlighting their lasting effects on the world.

---

## 1. The French Revolution (1789-1799):  Liberty, Equality, Fraternity

The French Revolution dramatically altered the course of European and world history.  Its significance lies primarily in:

- **The Rise of Nationalism:** The revolution fostered a strong sense of French national identity and inspired similar nationalist movements across Europe.

- **The Spread of Enlightenment Ideals:** The revolution championed Enlightenment principles of liberty, equality, and fraternity, significantly influencing political thought and movements for democracy and human rights globally. The Declaration of the Rights of Man and of the Citizen, though flawed in its application, served as a blueprint for many subsequent declarations of rights.

- **The End of Feudalism:** The revolution effectively dismantled the feudal system in France, replacing it with a more centralized state and paving the way for modern nation-states.

- **Social and Political Upheaval:** The revolution triggered significant social and political changes, including the abolition of aristocratic privileges, the rise of the bourgeoisie, and the establishment of a republic (albeit temporarily).

- **Economic conditions:**  The state of the economy often plays a significant role in triggering revolutionary movements.

- **Political structures:**  Existing political systems and their responsiveness to demands for change are crucial.

- **Social structures:**  Existing social hierarchies and inequalities influence the likelihood and dynamics of revolution.

- **Leadership and organization:**  Effective leadership and organization are vital for the success of revolutionary movements.

- **International context:**  Global political events and relationships often shape the course of revolutions.

By understanding these factors, we can better grasp the complexity and long-term significance of past revolutions and their continuing relevance to contemporary issues.
"""

# Convert Markdown to HTML
html_string = markdown.markdown(markdown_string)

# Create a Document object
document = Document()

# Load HTML string
document.LoadFromHTML(html_string)

# Save it as a PDF file
document.SaveToFile("output/ToPdf.pdf", FileFormat.PDF)

# Dispose resources
document.Dispose()