# Structured Text to Hybrid Program Translation
============
This is the half of the HyPLC tool that translates the IEC61131-3 standard structured text programming language for PLCs to a hybrid program specified in differential dynamic logic. This makes up one half of the HyPLC tool presented in [1]. For the converse translation, please visit the project link page. The tool has been directly integrated into the KeYmaera X command-line tool.
*README TODO: Add usage examples 
##### Usage
You can use the hyplc-st-to-hp.py script to perform the translation for a given st file as follows:
</br>
* python3 ./hyplc-st-to-hp.py st-file [hp-file]

where <st-file> is a structured text program file that conforms to the subset of the IEC61131-3 standard defined in our paper, and <hp-file> is an option for providing a hybrid program where the ctrl can be replaced. This can be done by essentially writing a hybrid program as usual and including a placeholder "ctrl" variable where the  ctrl of the system should reside.


