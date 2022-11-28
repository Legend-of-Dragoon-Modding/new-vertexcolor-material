# New VertexColor Material
This addon for Blender (2.8 recommended) written for saving some clicks, will add Materials; linking a Surface type: Principled BSDF linked with an attribute node set up.

## Story
"Well the story goes like this, one day after doing my 1000 model re-assemble i was tired of constantly have to manually add Vertex Colour node into Blender (Attribute Node and filling the Atrribute Name), so an idea comes to my mind, there is an addon that could do this on internet?... well the answer was a partial "yes", but didn't fill my expectations on how they to work (neither my addon lol), but i think my addon is just what i needed to work with the models converted from TLoD TMD Converter".

So, New VertexColor Material is a simple addon to add automatically a Material called VC (Vertex Colour) into the materials of each object in the scene, will check for the max number of objects in the scene and going from 1 to N adding 1 Material Slot connected to an Attribute Node wich have the Atrribute name as "Coln" where n is the number of object... pretty simple yeah?.

With this addon you'll save some clicks and keyboard usages.

***NOTE: This addon is intended to be used with models converted by my tool TLoD TMD Converter.***
# TLoD TMD Converter:
*https://github.com/Legend-of-Dragoon-Modding/TLoD-TMD-Converter*

USAGE:

Download the addon
In Blender 2.8: 
>*Edit->Preferences->Add-ons->Install->"Navigate until finding the addon Script"*
after doing that you will find a tab in the Context Toggle (pressing n keyboard key)
the tab is called VertexColorMAT, click it and a simple button will be displayed Vertex Color new mat, press it.
![alt text](https://github.com/Legend-of-Dragoon-Modding/new-vertexcolor-material/blob/main/Images/Pref_Blend.png)
![alt text](https://github.com/Legend-of-Dragoon-Modding/new-vertexcolor-material/blob/main/Images/Addons_Blend.png)
![alt text](https://github.com/Legend-of-Dragoon-Modding/new-vertexcolor-material/blob/main/Images/Install_Blend.png)
![alt text](https://github.com/Legend-of-Dragoon-Modding/new-vertexcolor-material/blob/main/Images/NewSelect_Blend.png)
![alt text](https://github.com/Legend-of-Dragoon-Modding/new-vertexcolor-material/blob/main/Images/Tab_Button.png)

**__IMPORTANT:__ NO object must be selected or the addon will raise an error, be sure of all the objects being de-selected. Also keep in mind, this tool will not automatically select the vertex coloured and applying the Surface settings, that must be done manually.**

<sub>Maybe in a model with very few objects and even if you work only with few models the tool help is not so noticeable, but when you do almost one thousand models you are saving around three thousand clicks (not counting the each object but the single model, so are way much more than three thousand), Mouse are not cheap lol.</sub>
