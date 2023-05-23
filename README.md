<h1>Number Base Converter</h1>
  <p>This Python script allows you to convert numbers between different bases, including bases with decimal points. It provides a user-friendly interface for entering the number, the base to convert from, and the base to convert to. The script also includes checks for input validity and ensures the bases are "friends" for certain conversions.</p>

  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3.x</li>
  </ul>

  <h2>How to Use</h2>
  <ol>
    <li>Clone the repository or download the script file.</li>
    <li>Open a terminal or command prompt and navigate to the directory where the script is located.</li>
    <li>Run the script by executing the following command:<br>
      <code>python base_converter.py</code></li>
    <li>Follow the on-screen instructions to enter the number, the base to convert from (FromB), and the base to convert to (ToB).</li>
    <li>The script will perform the conversion and display the result.</li>
  </ol>

  <h2>Functionality</h2>
  <ul>
    <li><code>make_int(char)</code>: Converts a character 'A' to 'F' to its corresponding integer value from 10 to 15. Returns False for invalid characters.</li>
    <li><code>make_num(char)</code>: Converts an integer value from 10 to 15 to its corresponding character 'A' to 'F'. Returns False for invalid integers.</li>
    <li><code>if_Friend(Fb, Tb)</code>: Checks if two bases, Fb and Tb, are "friends" (one can be obtained by raising the other to a power between 1 and 8).</li>
    <li><code>This_regal(num, B)</code>: Checks if a given number <code>num</code> is valid in a given base <code>B</code>.</li>
    <li><code>To_B10(num, Fb, Tb)</code>: Converts a number <code>num</code> from base Fb to base 10 or from a base with a decimal point to base 10.</li>
    <li><code>From_B10(numS, Fb, Tb)</code>: Converts a number <code>numS</code> from base 10 to base Tb.</li>
  </ul>

  <h2>Examples</h2>
  <p>Here are some example conversions that you can perform with this script:</p>
  <ul>
    <li>Convert a number from base 2 to base 10: <code>10101<sub>2</sub> = 21<sub>10</sub></code></li>
    <li>Convert a number from base 10 to base 16: <code>42<sub>10</sub> = 2A<sub>16</sub></code></li>
    <li>Convert a number from base 16 to base 8: <code>2A<sub>16</sub> = 52<sub>8</sub></code></li>
    <li>Convert a number from base 8 to base 5: <code>123<sub>8</sub> = 443<sub>5</sub></code></li>
  </ul>
  
  <code>Enter a num: 1010 
  From B-> 2 
  To B-> 10 
  (1010)2 = (10)10</code>
  
  

  
  

  <h2>Notes</h2>
  <ul>
    <li>The script supports bases from 2 to 16.</li>
    <li>If the entered number is not valid for the specified base, the script will display an error message.</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

  <h2>Acknowledgments</h2>
  <ul>
    <li>This script was inspired by the need to convert numbers between different bases.</li>
    <li>The concept of "friends" bases was introduced to enhance the conversion capabilities.</li>
    <li>Special thanks to <a href="https://openai.com/">OpenAI</a> for providing the GPT-3.5 model that assisted in generating this README.</li>
  </ul>
