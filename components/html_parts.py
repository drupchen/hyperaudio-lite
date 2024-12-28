from textwrap import dedent

head = dedent("""\
    <!-- Last updated for Version 2.1 -->
    
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>ལྗགས་ཁྲིད་ཐོས་ཀློག་གཉིས་ལྡན།</title>
        <link rel="stylesheet" href="css/hyperaudio-lite-player.css">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
        <style>
          /* uncomment the following CSS for active parent / word indicator */ 
          
          
          .hyperaudio-transcript .active{
            background-color: #efefef;
          }
      
          .hyperaudio-transcript .active > .active {
            background-color: #ccf;
            text-decoration:  #00f underline;
            text-decoration-thickness: 3px;
          }
          
          #popover {
          position: absolute;
          background-color: #f9f9f9;
          
          border: 1px solid #ccc;
          padding: 10px;
          border-radius: 4px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.2);
          display: none;
          z-index: 1;
          font-size: small;
          font-family: Jomolhari, Arial,Helvetica Neue,Helvetica,sans-serif;
        }
    
        #popover a {
          text-decoration: none; 
          color: #303030;
          cursor: pointer;
        }
    
        #clipboard-text {
          font-family: Jomolhari, Courier New,Courier,Lucida Sans Typewriter,Lucida Typewriter,monospace; 
        }
    
        #clipboard-confirm {
          font-size: medium;
        }
        </style>
      </head>""")

body_beginning = dedent("""\
      <body>
          <p style="font-size: 32pt; text-align: center; color: brown;">༄༅། །རྗེ་བླ་མ་དིལ་མཁྱེན་རྡོ་རྗེ་འཆང་གི་ལྗགས་ཁྲིད་ཐོས་ཀློག་སྦྲགས་མར་བསྒྲིགས་པ་བཞུགས།།</p>
          <button type="button" class="collapsible"><span style="color:blue;"><font face="Jomolhari" size="4">འགྲེལ་བརྗོད་ཕྱིར་འདིར་སྣུན།</font> Click for instructions.</span> (Work in progress, will be regularly updated.)</button>
          <div class="content">
              Press the "Play" button to start playing the audio. The transcription will follow the audio.
              <br><br>You can also click anywhere on the text (except where there is a background color) to bring the audio to that point.
              <br>You can resize the text area vertically.
              <br><br>
              <font face="Jomolhari" size="3">ཡིག་ནོར་རམ། སྒྲ་ཇི་བཞིན་མ་ཕབས་པ་གཟིགས་ཚེ། གཤམ་གྱི་དྲྭ་ཐག་འདིར་བསྣུན་ནས། མཆན་འགོད་པའི་བཀའ་དྲིན་གནང་བར་ཞུ། གང་མགྱོགས་ཀྱིས་ནོར་བཅོས་བྱེད་ངེས་ཡིན།</font>
              <br><a href="https://docs.google.com/document/d/1NE32WPpIsZMqHPH529EZb7JNW848hwPQKZ74CdUNujI/edit?usp=sharing" target="_blank" rel="noopener noreferrer">ལམ་རིམ་བདུད་རྩི་སྙིང་པོའི་ལྗགས་ཁྲིད། སྒྲ་དང་པོ།</a>
              <br><a href="https://docs.google.com/document/d/1hdEhUVutoZhDGROR1wM7GzIl3cg3fCpMiB3t4gPTFyQ/edit?usp=sharing" target="_blank" rel="noopener noreferrer">ལམ་རིམ་བདུད་རྩི་སྙིང་པོའི་ལྗགས་ཁྲིད། སྒྲ་གཉིས་པ།</a>
              <br><a href="https://docs.google.com/document/d/1AHqgSmalajDM1W6f0N-2JPNVct5otDJLtjvSBekXNho/edit?usp=sharing" target="_blank" rel="noopener noreferrer">ལམ་རིམ་བདུད་རྩི་སྙིང་པོའི་ལྗགས་ཁྲིད། སྒྲ་གསུམ་པ།</a>
              <br><a href="https://docs.google.com/document/d/1K63bd_z6we4CjFOABsKIuADlvvA4DFRA54ny2D2U3YI/edit?usp=sharing" target="_blank" rel="noopener noreferrer">མན་ངག་མཛོད་ཀྱི་དོན་ཁྲིད་རབ་གསལ་ཟླ་བའི་བདུད་རྩི། སྒྲ་དང་པོ།</a>
              
              <br>If you see any mistakes, please add a comment in the corresponding links. I'll correct the transcription as soon as possible.
              <br><br>
              Legend:
              <ul>
                <li>"<font class="unsure">༺དོགས་པ་ཡོད་ས།༻</font>" "<font class="unsure">༺&#60;transcription I'm unsure about&#62;༻</font>"</li>
                <li>"<font class="hesit">༼བཞག་ན་ཆོག་པའི་གསུངས་།༽</font>" "<font class="hesit">༼&#60;hesitations or repetitions that can be ignored&#62;༽</font>"</li>
                <li>"<font class="changed">ཚེག་བར་࿏ རྟགས་ཅན་ནི་སྒྲ་ཇི་བཞིན་མེད།</font>" "<font class="changed">&#60;changed-syllable&#62;࿏་</font>"</li>
              </ul>

              In the images, 
              <ul>
                <li><font color="firebrick">root text is in red</font></li>
                <li><font color="steelblue">sapche is in blue</font></li>
              </ul>
              
          </div>
          <p style="font-size: 20pt;">
                <a href="#dutsi-nyingpo-1">ལམ་རིམ་བདུད་རྩི་སྙིང་པོ། སྒྲ་དང་པོ།</a><br>
                <a href="#dutsi-nyingpo-2">ལམ་རིམ་བདུད་རྩི་སྙིང་པོ། སྒྲ་གཉིས་པ།</a><br>
                <a href="#dutsi-nyingpo-3">ལམ་རིམ་བདུད་རྩི་སྙིང་པོ། སྒྲ་གསུམ་པ།</a><br>
                <a href="#mengag-dzo-1">མན་ངག་མཛོད། སྒྲ་དང་པོ།</a><br>
                <a href="#mengag-dzo-2">མན་ངག་མཛོད། སྒྲ་གཉིས་པ།</a><br>
                <a href="#mengag-dzo-3">མན་ངག་མཛོད། སྒྲ་གསུམ་པ།</a><br>
                <a href="#mengag-dzo-4">མན་ངག་མཛོད། སྒྲ་བཞི་པ།</a><br>
                <a href="#mengag-dzo-5">མན་ངག་མཛོད། སྒྲ་ལྔ་པ།</a><br>
                <a href="#mengag-dzo-6">མན་ངག་མཛོད། སྒྲ་དྲུག་པ།</a><br>
                <a href="#mengag-dzo-7">མན་ངག་མཛོད། སྒྲ་བདུན་པ།</a><br>
                <a href="#mengag-dzo-8">མན་ངག་མཛོད། སྒྲ་བརྒྱད་པ།</a><br>
                <a href="#mengag-dzo-9">མན་ངག་མཛོད། སྒྲ་དགུ་པ།</a><br>
                <a href="#mengag-dzo-10">མན་ངག་མཛོད། སྒྲ་བཅུ་པ།</a><br>
                <a href="#mengag-dzo-11">མན་ངག་མཛོད། སྒྲ་བཅུ་གཅིག་པ།</a><br>
                <a href="#mengag-dzo-12">མན་ངག་མཛོད། སྒྲ་བཅུ་གཉིས་པ།</a><br>
                <a href="#mengag-dzo-13">མན་ངག་མཛོད། སྒྲ་བཅུ་གསུམ་པ།</a><br>
                <a href="#mengag-dzo-14">མན་ངག་མཛོད། སྒྲ་བཅུ་བཞི་པ།</a><br>
                <a href="#mengag-dzo-15">མན་ངག་མཛོད། སྒྲ་བཅོ་ལྔ་པ།</a><br>
                <a href="#mengag-dzo-16">མན་ངག་མཛོད། སྒྲ་བཅུ་དྲུག་པ།</a><br>
                <a href="#mengag-dzo-17">མན་ངག་མཛོད། སྒྲ་བཅུ་བདུན་པ།</a><br>
                <a href="#mengag-dzo-18">མན་ངག་མཛོད། སྒྲ་བཅོ་བརྒྱད་པ།</a><br>
                <a href="#yeshe-drupa-1">རྡོ་རྗེ་ཐོལ་གླུ་ཡེ་ཤེས་གྲུབ་པ། སྒྲ་དང་པོ།</a><br>
                <a href="#yeshe-drupa-2">རྡོ་རྗེ་ཐོལ་གླུ་ཡེ་ཤེས་གྲུབ་པ། སྒྲ་གཉིས་པ།</a><br>
                <a href="#yeshe-drupa-3">རྡོ་རྗེ་ཐོལ་གླུ་ཡེ་ཤེས་གྲུབ་པ། སྒྲ་གསུམ་པ།</a><br>
                <a href="#tsiksum-nedek-1">ཚིག་གསུམ་གནད་རྡེག །སྒྲ་དང་པོ།</a><br>
                <a href="#tsiksum-nedek-2">ཚིག་གསུམ་གནད་རྡེག །སྒྲ་གཉིས་པ།</a><br>
          </p>
          """)

players = [
        dedent("""\
          <p style="font-size: 26pt; text-align: center; color: brown;">༈ ལམ་རིམ་བདུད་རྩི་སྙིང་པོ་དང་། དེའི་འགྲེལ་ཆུང་ཚིག་དོན་རབ་གསལ་གྱི་ལྗགས་ཁྲིད་ཐོས་ཀློག་སྦྲགས་མ།</p>
          <p id="dutsi-nyingpo-1" style="font-size: 26pt; color: brown;">སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer1" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-9-15/388135794-44100-2-4d0b90528e155.m4a" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="dutsi-nyingpo-2" style="font-size: 26pt; color: brown;">སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer2" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-9-17/182bd42d-915c-6b81-16d6-c0b0e0f61dd0.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="dutsi-nyingpo-3" style="font-size: 26pt; color: brown;">སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer3" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-10-6/389326076-44100-2-18ee3b8b57965.m4a" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p style="font-size: 26pt; text-align: center; color: brown;">༈ མན་ངག་མཛོད་ཀྱི་དོན་ཁྲིད་རབ་གསལ་ཟླ་བའི་བདུད་རྩི་ཐོས་ཀློག་སྦྲགས་མ།</p>
          <p id="mengag-dzo-1" style="font-size: 26pt; color: brown;">སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer4" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-9-15/388134785-44100-2-e4521ae64343e.m4a" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-2" style="font-size: 26pt; color: brown;">སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer5" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-11/1042aa00-5130-cc4b-2efc-d335e8113eca.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-3" style="font-size: 26pt; color: brown;">སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer6" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-11/391400879-44100-2-6239b7eb4a845.m4a" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-4" style="font-size: 26pt; color: brown;">སྒྲ་བཞི་པ།</p>         
          <audio id="hyperplayer7" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-11/f4fa6463-d894-aec3-f06c-353ea2194407.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-5" style="font-size: 26pt; color: brown;">སྒྲ་ལྔ་པ།</p>         
          <audio id="hyperplayer8" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-12/fee8e6ad-9598-f1fd-188d-f16b7df686be.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-6" style="font-size: 26pt; color: brown;">སྒྲ་དྲུག་པ།</p>         
          <audio id="hyperplayer9" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-14/b0266787-814c-9ab5-b084-4411b42e3ace.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-7" style="font-size: 26pt; color: brown;">སྒྲ་བདུན་པ།</p>         
          <audio id="hyperplayer10" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-14/34e1c358-436c-75b1-2600-38d162088162.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-8" style="font-size: 26pt; color: brown;">སྒྲ་བརྒྱད་པ།</p>         
          <audio id="hyperplayer11" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-15/30b1af0c-8d40-6e55-ca5b-42474f7c62c3.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-9" style="font-size: 26pt; color: brown;">སྒྲ་དགུ་པ།</p>         
          <audio id="hyperplayer12" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-16/03c6d45a-963c-2613-edc8-c55f6445c756.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-10" style="font-size: 26pt; color: brown;">སྒྲ་བཅུ་པ།</p>         
          <audio id="hyperplayer13" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-17/391688829-44100-2-7c7d374f39ff7.m4a" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-11" style="font-size: 26pt; color: brown;">སྒྲ་བཅུ་གཅིག་པ།</p>         
          <audio id="hyperplayer14" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-17/391722426-44100-2-5d740b2aa1fe.m4a" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-12" style="font-size: 26pt; color: brown;">སྒྲ་བཅུ་གཉིས་པ།</p>         
          <audio id="hyperplayer15" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-18/cccb767e-f700-21d6-4528-264b9b387ea4.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-13" style="font-size: 26pt; color: brown;">སྒྲ་བཅུ་གསུམ་པ།</p>         
          <audio id="hyperplayer16" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-18/4174847c-9b8d-7297-8547-4ae41340fe1f.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-14" style="font-size: 26pt; color: brown;">སྒྲ་བཅུ་བཞི་པ།</p>         
          <audio id="hyperplayer17" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-18/0bc94b93-b937-dfbc-8f08-3bf30fcb6da5.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-15" style="font-size: 26pt; color: brown;">སྒྲ་བཅོ་ལྔ་པ།</p>         
          <audio id="hyperplayer18" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-18/622f2293-956a-7037-edb2-5f378c0350de.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-16" style="font-size: 26pt; color: brown;">སྒྲ་བཅུ་དྲུག་པ།</p>         
          <audio id="hyperplayer19" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-19/ef761fe3-2419-9c0c-8834-aa11464fd7c1.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-17" style="font-size: 26pt; color: brown;">སྒྲ་བཅུ་བདུན་པ།</p>         
          <audio id="hyperplayer20" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-19/3cd7d4d4-47cb-4852-380e-a5906465500f.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="mengag-dzo-18" style="font-size: 26pt; color: brown;">སྒྲ་བཅོ་བརྒྱད་པ།</p>         
          <audio id="hyperplayer21" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-19/764eb10a-8485-ce68-ea96-eab87fbdcd05.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p style="font-size: 26pt; text-align: center; color: brown;">༈ རྡོ་རྗེ་ཐོལ་གླུ་ཡེ་ཤེས་གྲུབ་པ་ཐོས་ཀློག་སྦྲགས་མ།</p>
          <p id="yeshe-drupa-1" style="font-size: 26pt; color: brown;">སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer22" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-26/b9bd87c3-9e9f-2665-6153-569c0b63baf1.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="yeshe-drupa-2" style="font-size: 26pt; color: brown;">སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer23" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-26/ac2e8a13-6fc1-4d13-9efa-2bdc9aa50663.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="yeshe-drupa-3" style="font-size: 26pt; color: brown;">སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer24" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-26/775b61af-7ca0-6fc4-4a34-cd0af931d4f2.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p style="font-size: 26pt; text-align: center; color: brown;">༈ ཚིག་གསུམ་གནད་རྡེག་ཐོས་ཀློག་སྦྲགས་མ།</p>
          <p id="tsiksum-nedek-1" style="font-size: 26pt; color: brown;">སྒྲ་དང་པོ།</p>  
          <p style="font-size: 20pt; color: brown;">༺ ༻ གཉིས་ཀྱི་བར་ལ་ཡོད་པའི་ཡི་གེ་ནི་གསུང་ལ་དངོས་སུ་མེད་པར་ཟུར་སྣོན་གྱི་ཡི་གེ་ཡིན།<br>༼ ༽ གཉིས་ཀྱི་བར་ལ་ཡོད་པ་ནི། སྲུབ་དགོས་རྒྱུའི་ཡི་གེ་ཡིན།<br>࿏ རྟགས་མཐའ་ཅན་གྱི་ཚེག་བར་རྣམས་ནི། ཡང་ན་ནོར་བཅོས། ཡང་ན་སྔོན་ཡི་གེར་མ་ཕབས་པའི་གསུང་ཡིན།</p>       
          <audio id="hyperplayer25" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-27/c50a99be-4e63-4639-05d2-4fc04db0d048.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum-nedek-2" style="font-size: 26pt; color: brown;">སྒྲ་གཉིས་པ།</p>  
          <p style="font-size: 20pt; color: brown;">༺ ༻ གཉིས་ཀྱི་བར་ལ་ཡོད་པའི་ཡི་གེ་ནི་གསུང་ལ་དངོས་སུ་མེད་པར་ཟུར་སྣོན་གྱི་ཡི་གེ་ཡིན།<br>༼ ༽ གཉིས་ཀྱི་བར་ལ་ཡོད་པ་ནི། སྲུབ་དགོས་རྒྱུའི་ཡི་གེ་ཡིན།<br>࿏ རྟགས་མཐའ་ཅན་གྱི་ཚེག་བར་རྣམས་ནི། ཡང་ན་ནོར་བཅོས། ཡང་ན་སྔོན་ཡི་གེར་མ་ཕབས་པའི་གསུང་ཡིན།</p>       
          <audio id="hyperplayer26" style="position:relative; width:97%" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2024-11-27/2863b05e-6294-a58d-0e77-9af99548754c.mp3" type="audio/mp3" controlsList="nodownload" controls></audio>
        """),
]

transcript_start = """\
          <div id="hypertranscript###" class="hyperaudio-transcript" style="resize: vertical; overflow-y:scroll; height:800px; width: 97%; scrollbar-gutter: stable; position:relative; border-style:dashed; border-width: 1px; border-color:#999; padding: 8px">
          <article><section>"""


transcript_end = dedent("""\
          </section></article>
          </div>""")

body_end = dedent("""\
          <script src="https://w.soundcloud.com/player/api.js"></script>
          <script src="js/hyperaudio-lite.js"></script>
          <script src="js/hyperaudio-lite-extension.js"></script>
          <script>
          // minimizedMode is still experimental - it aims to show the current words in the title, which can be seen on the browser tab.
          let minimizedMode = false;
          let autoScroll = true;
          let doubleClick = false;
          let webMonetization = false;
    
          new HyperaudioLite("hypertranscript1", "hyperplayer1", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript2", "hyperplayer2", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript3", "hyperplayer3", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript4", "hyperplayer4", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript5", "hyperplayer5", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript6", "hyperplayer6", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript7", "hyperplayer7", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript8", "hyperplayer8", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript9", "hyperplayer9", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript10", "hyperplayer10", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript11", "hyperplayer11", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript12", "hyperplayer12", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript13", "hyperplayer13", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript14", "hyperplayer14", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript15", "hyperplayer15", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript16", "hyperplayer16", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript17", "hyperplayer17", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript18", "hyperplayer18", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript19", "hyperplayer19", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript20", "hyperplayer20", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript21", "hyperplayer21", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript22", "hyperplayer22", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript23", "hyperplayer23", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript24", "hyperplayer24", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript25", "hyperplayer25", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript26", "hyperplayer26", minimizedMode, autoScroll, doubleClick, webMonetization);
          </script>
          <script>
            var coll = document.getElementsByClassName("collapsible");
            var i;
            
            for (i = 0; i < coll.length; i++) {
              coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.display === "block") {
                  content.style.display = "none";
                } else {
                  content.style.display = "block";
                }
              });
            }
          </script>
      </body>
    </html>""")