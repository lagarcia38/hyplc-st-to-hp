# Hybrid Program to Structured Text Translation
This repo simply is a placeholder until we integrate the the HP to ST command line option into the Github repo. Right now, you can download the jar file from this [Google Drive Folder](https://drive.google.com/open?id=13t1eaddGdeLXYrkVze4kzh5rHWiUlsNB) and see the usage options (see --genSTL).  The tool takes as input the hybrid program in scan cycle normal form and generates a structured text program that preserves the semantics as well as any safety guarantees.


##### Usage
You can refer to the command line KeYmaera X  usage information from the [KeYmaera X repo page.](https://github.com/LS-Lab/KeYmaeraX-release). The input will be a kyx file and hte output will

java -jar ./keymaerax.jar -genSTFile <model-file.kyx> -out file.st

The out file will be a structured text program.
