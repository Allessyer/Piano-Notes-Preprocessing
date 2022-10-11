# Piano-Notes-Preprocessing
A script that colors piano sheets depending on sound intensity 

## Problem Description

When you first start learning to play the piano, there is a bunch of information to know and memorize. It’s really hard to understand which keys you should press and memorize what each sign means. But you still want to play nice music and impress your friends. We want to help beginners to read notes in more easy way by coloring notes with respect to the intensity of sound.

We have collected a custom dataset using a Google search piano sheet with symbols that describe the volume of a sound, and randomly choose the 5 images. In Fig.1 in grean boxes special symbols related to sounds intensity are shown.

<p align="center">
  <img src="images/notes_with_signs.png" width="750">
</p>
<p align="center">   
   <em> Fig.1 Example of image in train set.</em>
</p>

## Solution

Overall pipeline you can see in Fig.2.

<p align="center">
  <img src="images/pipeline.png" width="750">
</p>
<p align="center">   
   <em> Fig.2 Pipeline </em>
</p>


## Result

<p align="center">
  <img src="images/return_result.jpg" width="750">
  <em> a. </em>
  <img src="images/test_6.jpg" width="750">
  <em> b. </em>
</p>
<p align="center">   
   <em> Fig.3. a. original image, b. preprocessed image.</em>
</p>


