# YoutubeToStems
Convert a youtube (musical) video into 5 audio stems (Vocals, Bass, Piano, Drums and Everything_else)

Credits:
90% of the credits and the magic goes to [Spleeter](https://github.com/deezer/spleeter) for their awesome ML algorithm.<br>
5% goes to [Youtube_dl](https://pypi.org/project/youtube_dl/) for the youtube download package.

## Setup:

1. Run <code>pip3 install requirements.txt</code>
2. install [Spleeter](https://github.com/deezer/spleeter)

## Usage:

Parameters:

<code>-s</code> or <code>--stems</code> (Quantity of stems:2,4 or 5. default: 5)<br>
<code>--input</code>       (Select file to read links. default: inputFile.txt)

1. paste all the youtube's url you want to convert to the desired input file, one below the other (I do not take any responsability for copyright infringments)
2. Select number of stems: 2 (vocals and arrangement), 4(vocal, bass, drums, everyhing else) or 5(4 + piano)
3. Run <code>python3 youtubeToStems.py </code>
4. enjoy!!
