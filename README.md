# No Cap, Thank You
#### Video Demo: <URL HERE>
#### Description:
No Cap, Thank You is a dynamic and user-friendly web application designed to cultivate gratitude and positivity in your daily life. This application serves as a digital gratitude diary, enabling you to reflect on and document the moments, people, and experiences that bring joy and meaning to your life. Whether it’s appreciating the small things, celebrating significant achievements, or recognizing acts of kindness, No Cap, Thank You provides a dedicated space for self-reflection and personal growth.

With features like a Gratitude Journal for recording daily reflections, a Good Deeds Tracker to document and review your acts of kindness, and a collection of inspiring Daily Prompts to guide your thoughts, this app encourages mindfulness and positivity. By using No Cap, Thank You, you can develop a habit of gratitude, foster emotional well-being, and discover new ways to appreciate the world around you.

Whether you’re starting your gratitude journey or looking for a creative outlet to enhance your perspective, No Cap, Thank You offers an engaging and meaningful experience. Embrace the habit of gratitude and see how it transforms your mindset, one reflection at a time.


#### Files and Functionality:
- `app.py`: The main application file containing Flask routes, database initialization, and helper functions for time zone conversion.
- `gratitude_journal.html`: Displays the gratitude journal form and entries.
- `good_deeds.html`: Provides a form to log good deeds and displays the list of deeds.
- `daily_prompt.html`: Shows a randomly selected prompt and allows users to reflect.
- `styles.css`: Contains the styling for all pages, ensuring a clean and consistent UI.
- `gratitude.db`: SQLite database storing user entries, deeds, and prompts.

#### Features:
1. **Gratitude Journal**:
   - Allows users to log daily gratitude entries.
   - Displays entries with timestamps converted to the user's local time.

2. **Good Deeds Tracker**:
   - Enables users to record and view their acts of kindness.

3. **Daily Prompts**:
   - Provides inspirational prompts to guide users in their reflections.

4. **User-Friendly Interface**:
   - Responsive design for desktop and mobile users.
   - Flash messages for feedback after actions.

#### Design Choices:
- **Frameworks**: Flask for the backend due to its simplicity and robust templating engine.
- **Database**: SQLite, as it's lightweight and easy to integrate with Flask.
- **Time Zone Handling**: Used `pytz` to ensure timestamps match the user's local time.
- **Frontend**: Designed a minimalist UI with CSS for better usability and aesthetics.

#### Challenges and Learning:
- Implementing time zone conversion for accurate timestamps.
- Handling flash messages effectively without duplication.
- Designing a scalable structure for adding more features in the future.

### How to Run:
1. Clone the repository:
   ```bash
   git clone <https://github.com/choihyerin/no-cap-thank-you.git>
   cd <no-cap-thank-you>
