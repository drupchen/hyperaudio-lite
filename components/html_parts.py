from textwrap import dedent

head = dedent("""\
    <!-- Last updated for Version 2.1 -->
    
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>ལམ་རིམ་བདུད་རྩི་སྙིང་པོ་དང་། དེའི་འགྲེལ་ཆུང་ཚིག་དོན་རབ་གསལ་གྱི་ལྗགས་ཁྲིད། རྗེ་བླ་མ་དིལ་མཁྱེན་རྡོ་རྗེ་འཆང་གི་གསུང་།</title>
        <link rel="stylesheet" href="css/hyperaudio-lite-player.css">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
        <style>
          /* uncomment the following CSS for active parent / word indicator */ 
          
          /*
          .hyperaudio-transcript .active{
            background-color: #efefef;
          }
      
          .hyperaudio-transcript .active > .active {
            background-color: #ccf;
            text-decoration:  #00f underline;
            text-decoration-thickness: 3px;
          }
          */
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
          <p style="font-size: 26pt; text-align: center;">༄༅། །ལམ་རིམ་བདུད་རྩི་སྙིང་པོ་དང་། དེའི་འགྲེལ་ཆུང་ཚིག་དོན་རབ་གསལ་གྱི་ལྗགས་ཁྲིད། རྗེ་བླ་མ་དིལ་མཁྱེན་རྡོ་རྗེ་འཆང་གི་གསུང་བཞུགས།།</p>
          <p style="font-size: 10pt;"> Work in progress. Will be regularly updated. Please check the instructions at the bottom.</p>
          <iframe  id="hyperplayer" data-player-type="soundcloud" width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1928781707%3Fsecret_token%3Ds-k7KAfbcdtzf&color=%23ff5500&auto_play=false&hide_related=false&show_comments=false&show_user=false&show_reposts=false&show_teaser=false"></iframe>
    
          <div id="popover"><a id="popover-btn">Copy to clipboard <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="-130 -110 600 600"><path d="m161,152.9h190c0.1,0 0.1,0 0.2,0 10.8,0 19.6-7.1 19.6-16 0-1.5-14.1-82.7-14.1-82.7-1.3-7.9-9.6-13.8-19.4-13.8l-61.7,.1v-13.5c0-8.8-8.8-16-19.6-16-10.8,0-19.6,7.1-19.6,16v13.6l-61.8,.1c-9.8,0-18,5.9-19.4,13.8l-13.7,80.3c-1.2,14.3 13.5,18.1 19.5,18.1z" fill="currentcolor"/><path d="m427.5,78.9h-26.8c0,0 9.3,53.5 9.3,58 0,30.4-26.4,55.2-58.8,55.2h-190.2c-19.6,0.4-63.3-14.7-58.1-63.9l8.4-49.2h-26.8c-10.8,0-19.6,8.8-19.6,19.6v382.9c0,10.8 8.8,19.6 19.6,19.6h343c10.8,0 19.6-8.8 19.6-19.6v-383c0-10.8-8.8-19.6-19.6-19.6zm-76.5,320.1h-190c-10.8,0-19.6-8.8-19.6-19.6 0-10.8 8.8-19.6 19.6-19.6h190c10.8,0 19.6,8.8 19.6,19.6 0,10.8-8.7,19.6-19.6,19.6zm0-110.3h-190c-10.8,0-19.6-8.8-19.6-19.6 0-10.8 8.8-19.6 19.6-19.6h190c10.8,0 19.6,8.8 19.6,19.6 0,10.8-8.7,19.6-19.6,19.6z" fill="currentcolor"/></svg></a></div>
    
          <dialog id="clipboard-dialog">
              <h3>The following text has been copied to the clipboard</h3>
              <p id=clipboard-text></p>
              <div style="text-align: right;">
                <button id="clipboard-confirm">ok</button>
              </div>
          </dialog>""")

transcript_start = dedent("""\
          <div id="hypertranscript" class="hyperaudio-transcript" style="overflow-y:scroll; height:600px; position:relative; border-style:dashed; border-width: 1px; border-color:#999; padding: 8px">
          <article><section>""")

transcrip_end = dedent("""\
          </section></article>
          </div>""")

body_end = dedent("""\
            <p style="font-size: 50%;">
              Press the "Play" button to start playing the audio. The transcription will follow the audio.
              <br><br>You can also click anywhere on the text (except where there is a background color) to bring the audio to that point.
              <br><br>
              Legend: <br>
              "<font class="unsure">༺transcription I'm unsure about༻</font>"<br>
              "<font class="hesit">༼hesitations or repetitions that can be ignored༽</font>"<br>
              "<font class="changed">changed-syllable࿏་</font>"
            </p>
          <script src="https://w.soundcloud.com/player/api.js"></script>
          <script src="js/hyperaudio-lite.js"></script>
          <script src="js/hyperaudio-lite-extension.js"></script>
          <script>
          // minimizedMode is still experimental - it aims to show the current words in the title, which can be seen on the browser tab.
          let minimizedMode = false;
          let autoScroll = true;
          let doubleClick = false;
          let webMonetization = false;
    
          new HyperaudioLite("hypertranscript", "hyperplayer", minimizedMode, autoScroll, doubleClick, webMonetization);
          </script>
      </body>
    </html>""")