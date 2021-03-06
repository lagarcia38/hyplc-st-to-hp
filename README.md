# HyPLC: Hybrid Programmable Logic Controller Program Translation for Verification[1]
Programmable Logic Controllers (PLCs) provide a prominent choice of implementation platform for safety-critical industrial control systems. Formal verification provides ways of establishing correctness guarantees, which can be quite important for such safety-critical applications. But since PLC code does not include an analytic model of the system plant, their verification is limited to discrete properties. In this paper, we, thus, start the other way around with hybrid programs that include continuous plant models in addition to discrete control algorithms. Even deep correctness properties of hybrid programs can be formally verified in the theorem prover KeYmaera X that implements differential dynamic logic, dL, for hybrid programs. After verifying the hybrid program, we now present an approach for translating hybrid programs into PLC code. The new tool, **HyPLC**, implements this translation of discrete control code of verified hybrid program models to PLC controller code and, vice versa, the translation of existing PLC code into the discrete control actions for a hybrid program given an additional input of the continuous dynamics of the system to be verified. This approach allows for the generation of real controller code while preserving, by compilation, the correctness of a valid and verified hybrid program. PLCs are common cyber-physical interfaces for safety-critical industrial control applications, and HyPLC serves as a pragmatic tool for bridging formal verification of complex cyber-physical systems at the algorithmic level of hybrid programs with the execution layer of concrete PLC implementations. 

![HyPLC System Overview](./docs/figures/hyplc-overview.jpg)

##### Usage
Each translation direction has its own implementation. For the translation of structured text to hybrid programs, please visit the **hyplc-st-to-hp** directory. For the details about the hybrid program to structured text translation implementation, please see the details in the **hyplc-hp-to-st** directory.

#### Demo
You can see a demo video of both translational tools in this [Google Drive Folder](https://drive.google.com/open?id=13t1eaddGdeLXYrkVze4kzh5rHWiUlsNB) .

Publications
============
1. Luis Garcia, Stefan Mitsch, and André Platzer.
[HyPLC: Hybrid Programmable Logic Controller Program Translation for Verification]
In 2019 ACM/IEEE 10th International Conference on Cyber-Physical Systems (ICCPS). IEEE, 2019.
