<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/KSU-AI-Club/BusyBee">
    
  </a>

<h3 align="center">BusyBee 🐝</h3>

  <p align="center">
BusyBee 🐝 is an object detection system for detecting and classifying bees on the tribe level 
<br />
    ![](/demo/bee_vid_annotated.gif)



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The goal of project Busy Bee is to create a lightweight object detection model capable of identifying Bees and tracking their movements. The classifications are done at the [tribe](https://en.wikipedia.org/wiki/Tribe_(biology)) level (as opposed to "Bee or No Bee"). To do this, we had to leverage foundation vision models (Grounding-DINO) to create a [novel dataset](https://huggingface.co/datasets/nicholicaron/Bees_SE_USA) of over 45,000 research-grade bee images from throughout the South Eastern United States, sourced from iNaturalist. The end goal is to create a model that is both performant and effective enough to be run on a Raspberry Pi Trail Camera. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][python]][python-url]
* [![MatplotLib][matplotlib]][matplotlib-url]
* [![Numpy][numpy]][numpy-url]
* [![Pytorch][pytorch]][pytorch-url]
* [![Ultralytics][ultralytics]][ultralytics-url]
* [![iNaturalist][inaturalist]][inaturalist-url]
* [![HuggingFace][huggingface]][huggingface-url]
* [![Streamlit][streamlit]][streamlit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

If you'd like to play around with the Model, it's hosted [here, on HuggingFace](https://huggingface.co/spaces/nicholicaron/BusyBee)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/KSU-AI-Club/BusyBee.svg?style=for-the-badge
[contributors-url]: https://github.com/KSU-AI-Club/BusyBee/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/KSU-AI-Club/BusyBee.svg?style=for-the-badge
[forks-url]: https://github.com/KSU-AI-Club/BusyBee/network/members
[stars-shield]: https://img.shields.io/github/stars/KSU-AI-Club/BusyBee.svg?style=for-the-badge
[stars-url]: https://github.com/KSU-AI-Club/BusyBee/stargazers
[issues-shield]: https://img.shields.io/github/issues/KSU-AI-Club/BusyBee.svg?style=for-the-badge
[issues-url]: https://github.com/KSU-AI-Club/BusyBee/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge 
[licnse-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: [https://linkedin.com/in/nicholicaron](https://www.linkedin.com/groups/14303678/)
[product-screenshot]: images/screenshot.png
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[matplotlib-url]: https://matplotlib.org/
[numpy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[numpy-url]: https://numpy.org/
[pytorch]: https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white
[pytorch-url]: https://pytorch.org/
[ultralytics]: https://img.shields.io/badge/ultralytics-red
[ultralytics-url]: https://www.ultralytics.com/
[inaturalist]: https://img.shields.io/badge/iNaturalist-green
[inaturalist-url]: https://www.inaturalist.org/
[huggingface]: https://img.shields.io/badge/HuggingFace-orange
[huggingface-url]: https://huggingface.co/
[streamlit]: https://img.shields.io/badge/Streamlit-maroon
[streamlit-url]: https://streamlit.io/
