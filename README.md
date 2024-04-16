# Searchify

Get Web Result, AI Generated Answer through your terminal 😎

<!-- <div align="center"> -->
<!--   <video src="https://user-images.githubusercontent.com/48545987/178679494-c7d58bdd-d8ca-4802-a01c-a9444b8b882f.mp4" type="video/mp4"></video> -->
<!-- </div> -->
<!---->
## :sparkles: Features
- Search and get the results from the Google Search API.
- Preview the results, by seeing title, snippet and link.
- Get the result by your choice of having all at once or any particular.
    - Copy the link to the clipbopard.
    - Paginate the results(For any screen size). Especially helpfull while live coding in a text editor or IDE.
    - Freedom of displaying the result by only links , title or snippets.
- Easy Setup
- Get the ai-generated answer for your questions.
- Good for the basic and medium level questions.
    - Helps in reducing distraction as no need to open Google or other Browser for your basic level queries.
- More focused coding envirnoment.
- Control the AI-Generated answer's sampling parameter(topk or top_p, temperature) and output token.


## :lock: Requirements
- Python 3.XX and Pip 3.XX
- Works on Windows, Linux and Mac.

## :package: Installation
This tool is platform independent, hence it could be installed at any OS that is capable of running Python 3 programs or application.
- ### Recommended
    ```
    pip install searchify-cli
    ```
    You might need to restart your system after installation especially in case of cloud system.
    
    Visit for more [searchify-cli](https://pypi.org/project/searchify-cli/) pypi page for more information.

This is the one way of installation, other way to install is by manually clonning this repo and register this as a command.

- ### Manual Installation
    <b> For Linux or Mac </b>
    
    1. Clone this repository.
    ```
    git clone -b manual-installation https://github.com/reactVishnu/Searchify.git
    ```
    2. Install the requirements.
    ```
    pip install -r requirements.txt
    ```
    3. Register it as a command.

        If you want to make an alias permanent, you can add it to your shell's configuration file.
        For example:
        - For <b>Bash</b>, you can add aliases to ~/.bashrc or ~/.bash_aliases.
        - For <b>Zsh</b>, you can add aliases to ~/.zshrc.
        - For <b>Fish</b>, you can add aliases to ~/.config/fish/config.fish
    ```
    alias search='python3 /home/ec2-user/Searchify/Web/main.py'
    alias search-config='python3 /home/ec2-user/Searchify/install.py'
    alias ai-search='python3 /home/ec2-user/Searchify/AI_Search/ai_search.py'
    ```
    For unalias purposes
    ```
    unalias search
    ```

    <b> For Windows </b>
    1. Clone this repository.
    ```
    git clone -b manual-installation https://github.com/reactVishnu/Searchify.git
    ```
    2. Go to the downloaded folder and Install the requirements.
    ```
    pip install -r requirements.txt
    ```
    3. Register it as a command using doskey.
    Mostly doskey is preinstalled in Windows CMD or Powershell.
    ```
    doskey search = python C:\Users\path\Searchify\Web\main.py
    doskey search-config = python C:\Users\path\Searchify\install.py
    doskey ai-search = python C:\Users\path\Searchify\AI_Search\ai_search.py
    ```
    Unregister it  as a command.
    ```
    doskey /D search
    ```

## 🚀 Usage 
- ### Web Search through terminal
    All web search can be done through "search" command.

    - <b>`search`</b>: Syntax for most basic search.

        ```
        search "your_query"
        ```
        This one will show the top result(number 1) snippet.
    - <b>`-h`</b>: Show's help for search.
        ```
        search -h
        ```
    - <b>`--all`</b>: Display the top 10 result.
        ```
        search "your query" --all
        ```
    - <b>`--no`</b> : Select the specific result.
        ```
        search "your_query" --no=4
        ```
    - <b>`--link`</b>: Show's the link and snippet.
        ```
        search "your_query" --link
        ```
    - <b>`--title`</b>: Show's the title and snippet.
        ```
        search "your_query" --title
        ```
    - <b>`--copy` </b>: Copy the link to the clipboard.
        ```
        search "your_query" --no=3 --link --copy
        ```
        It will copy the 3rd results link.

    <b>Overall Usage for `search`:</b>

    ```
    usage: main.py [-h] [--no NO] [--link] [--title] [--copy]
               [--all]
               query

    Search the web from the command line
    ```
- ### 🤖AI-Search through terminal
    Get the answers of your query through Google Generative AI Palm.
    - <b>`ai-search`</b>: Syntax for most basic ai search.

        ```
        ai-search "your_query"
        ```

    - <b>`--temp`</b>: Controls the randomness of the output. Must be positive. Typical values are in between [0,1]
    
        Higher values produce a more random and varied response. A temperature of zero will be deterministic.
        ```
        ai-search "your_query" --temp=0.3
        ```

    - <b>`--max_output_tokens`</b>: The maximum number of output token [Default : 250]
        
        ```
        ai-search "your_query" --max_output_tokens=800
        ```

    - <b>`--top_p`</b>: top_p configures the nucleus sampling. It sets the maximum cumulative probability of tokens to sample from.

        For example, if the sorted probabilities are [0.5, 0.2, 0.1, 0.1, 0.05, 0.05] a top_p of 0.8 will sample as [0.625, 0.25, 0.125, 0, 0, 0].
        ```
        ai-search "your_query"  --top_p=0.1
         ```

    - <b>`--top_k`</b>: top_k sets the maximum number of tokens to sample from on each step.
        ```
        ai-search "your_query" -- top_k=0.2
        ```
    - <b>`--page`</b>: Paginate the output. [Default: False]
        ```
        ai-search "your_query" --page
        ```
