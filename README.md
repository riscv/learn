Learn RISC-V
================
[![Check Markdown links](https://github.com/riscv/learn/actions/workflows/action.yml/badge.svg?branch=main)](https://github.com/riscv/learn/actions/workflows/action.yml)

A community-driven compilation of RISC-V resources and learning material. The list is dynamically
updated by the community and categorized based on different contexts of the RISC-V scope, taking
also into account different levels of experience/knowledge, allowing anyone interested in RISC-V to
discover RISC-V resources and relevant content (courses, software, documentation, articles etc.) in
an organized fashion.
Feel free to navigate through the resources listed below with their descriptions.

**RISC-V** is an open standard Instruction Set Architecture (ISA) based on established Reduced Instruction Set Computer (RISC) principles. 

👋 **Want to learn about RISC-V?** Check out the [Beginner-Level](#-beginner-level-resources) or [Intermediate-Level](#-intermediate-level-resources) learning resources.

<b>👉 Table of Contents</b>
<br>

- [Learn RISC-V](#learn-risc-v)
  - [➕ Making Contributions](#-making-contributions)
  - [📙 Resources](#-resources)
    - [Learning Resources for RISC-V](#learning-resources-for-risc-v)
      - [🟢 Beginner-level resources](#-beginner-level-resources)
      - [🔵 Intermediate-Level resources](#-intermediate-level-resources)
      - [Softwares and Tools](#softwares-and-tools)
      - [Open RISC-V Implementations](#open-risc-v-implementations)
    - [Relevant Documentation from RISC-V International](#relevant-documentation-from-risc-v-international)
    - [Articles and presentations](#articles-and-presentations)

## ➕ Making Contributions

We love contributions! Thank you for your interest in contributing to our compilation of tutorial resources for RISC-V.

Contributing is easy, here are some steps to help get you started:

✔ Browse through the list of beginner and intermediate-level resources [here](#learning-resources-for-risc-v) to see if your resource is already included.

✔ If not, go to [Issues](https://github.com/riscv/learn/issues), click on `New issue` and select the template for adding a new RISC-V tutorial resource. 

✔ Enter the resource information in the fields provided and click `Submit new issue`.

✔ If you have a different contribution, you can select the General Request issue template from the provided <a href="https://github.com/riscv/learn/issues/new/choose" target="_blank">issue types</a>.

✔ You could also engage with an already open issue.

We may interact with you before adding your contributions.

## 📙 Resources

### Learning Resources for RISC-V

#### 🟢 Beginner-level resources

<!-- ##### Beginner to Digital Logic Design -->

For those with little or no knowledge of digital logic design. After studying the [**Digital Design**](#digital-design) book in this section, you could jump to the intermediate-level [**edx RVfpga**](#computer-architecture-rvfpga) course if you wish as it expands on concepts discussed in the book.

| Resource  |  Author(s) | Description  | Access | Date added |
|---|---|---|---|---|
|  <span id="digital-design">**Digital Design and Computer Architecture RISC-V edition**</span> (good starting point) | Sarah L. Harris, David M. Harris   | Covers the foundational knowledge of digital logic design and segues smoothly into RISC-V Processor implementation. <i><br><br><ins>Topics</ins>: Number systems and digital representation, Semiconductors and transistors, Logic gates and Digital design, C Programming, RISC-V architecture, RISC-V assembly, Memory systems, Embedded I/O systems</i> | <a href="https://www.amazon.com/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642/ref=sr_1_5?crid=1Y6VGCXHTB99I&keywords=digital+design+and+computer+architecture&qid=1659609065&sprefix=digital+design+and+computer+architecture%2Caps%2C135&sr=8-5" target="_blank">[Amazon book link]</a>| 2024-01-10 |
|  <span id="digital-design">**The RISC-V Reader: An Open Architecture Atlas**</span> | David Patterson, Andrew Waterman| A beginner-friendly introduction to the RISC-V instruction set architecture as readers can start programming after the 2nd chapter. <i><br><br><ins>Topics</ins>: Computer architecture, RISC-V Instruction Set Architecture (ISA)</i> | <a href="http://www.riscbook.com/" target="_blank">[Available in Chineses, Japanese, Spanish, Portuguese and Korean]</a>| 2024-03-05 |
| **Nand2Tetris** (optional) | Noam Nisan, Shimon Schocken | A free hands-on tutorial on building a general-purpose computer from logic gates using a hardware simulator. <i><br><br><ins>Topics</ins>: Logic gates<i>|<a href="https://www.nand2tetris.org/" target="_blank">[webpage]</a> | 2024-01-10 |
|<span id="bruno-levy-episode-1">**learn-FPGA episode I: from blinky to RISC-V**</span>|[BrunoLevy](https://github.com/BrunoLevy)|A beginner's introduction to the digital design of a RISC-V softcore on FPGAs. Episode I gently starts from a very basic blinker in Verilog and morphs it step by step into a basic yet fully functional RISC-V SoC. It also explains how to write programs in C and assembly for the SoC.<i><br><br><ins>Topics</ins>: Digital design, FPGA, C Programming, RISC-V assembly<br><ins>Requirement</ins>: Basic knowledge of Verilog</i>|<a href="https://github.com/BrunoLevy/learn-fpga/blob/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/README.md" target="_blank">[GitHub]</a>| 2024-01-10 |
|**Hands-on RISC-V Processor Design**|[Rahul Behl](https://github.com/raulbehl)|This practical tutorial offers a deep dive into the world of computer architecture and processor design, with a specific focus on the RISC-V Instruction Set Architecture (ISA).<i><br><br><ins>Topics</ins>: Computer architecture, Processor design, RISC-V Instruction Set Architecture (ISA), SystemVerilog, RISC-V assembly<br><ins>Requirements</ins>: SystemVerilog but not necessary</i>|<a href="https://quicksilicon.in/course/riscv" target="_blank">[webpage]</a> | 2024-01-10 |
|**LinuxFoundationX: Building a RISC-V CPU Core** | [Steve Hoover](https://www.edx.org/bio/steve-hoover) | This free EdX course by Steve Hoover (founder of Redwood EDA) is a great way for a beginner to get started with digital logic design and basic RISC-V microarchitecture design with the help of modern, freely available open source tools.<i><br><br><ins>Topics</ins>: Digital logic design, RISC-V Instruction Set Architecture (ISA), CPU microarchitecture, Transaction-Level Verilog, Makerchip online IDE</i>| <a href="https://www.edx.org/learn/design/the-linux-foundation-building-a-risc-v-cpu-core" target="_blank"> [edX Course Link] | 2024-01-10 |
|**An introduction to Assembly Programming with RISC-V** | [Prof. Edson Borin](https://www.ic.unicamp.br/~edson/index.html) | This book uses RISC-V ISA to teach fundamental assembly programming concepts.<i><br><br><ins>Topics</ins>: RISC-V Instruction Set Architecture (ISA), RISC-V assembly</i>| <a href="https://www.ic.unicamp.br/~edson/riscv-book.html" target="_blank"> [webpage]| 2024-03-05 |
|**RISC-V Assembly Introduction in Portuguese** | [Gabriel G. de Brito](https://github.com/gboncoffee) | This course is designed for the Teaching Assistant program at Federal University of Paraná, Brazil, focusing on the basics of RISC-V IM architecture with the [EGG](https://github.com/gboncoffee/egg) emulator.<i><br><br><ins>Topics</ins>: RISC-V Instruction Set Architecture (ISA), RISC-V assembly<br><ins>Requirements</ins>: C programming, Digital Design</i>| <a href="https://youtube.com/playlist?list=PLFe3Zrf4uj4vlRF21jK3vzfCuSSJ5I_uB&si=bx4eHYpPLBxAUTy8" target="_blank"> [Online courses video]| 2024-04-06 |
|**Step-by-step RISC-V OS development** | [Chen Wang](https://github.com/unicornx) | A practical guidance to develop RISC-V operating systems<i><br><br><ins>Topics</ins>: RISC-V Instruction Set Architecture (ISA), Operating systems<br><ins>Requirements</ins>: C programming, Data structures, Linux commands</i>| <a href="https://github.com/plctlab/riscv-operating-system-mooc" target="_blank"> [Teaching resources]<a href="https://www.bilibili.com/video/BV1Q5411w7z5" target="_blank"> [Online course videos in Chineses] | 2024-03-05 |
|**Step-by-step RISC-V Compiler development** | [Shao-Ce SUN](https://github.com/sunshaoce) | A practical guidance to develop RISC-V C compiler<i><br><br><ins>Topics</ins>: RISC-V Instruction Set Architecture (ISA), Compilier<br><ins>Requirements</ins>: C programming, Data structures</i>| <a href="https://github.com/sunshaoce/rvcc-course" target="_blank"> [Teaching resources]<a href="https://github.com/sunshaoce/rvcc" target="_blank"> [Sample code] <a href="https://www.bilibili.com/video/BV1gY4y1E7Ue" target="_blank"> [Online course videos in Chineses]| 2024-03-20 |
|**OpenSecurityTraining2 Architecture 1005: RISC-V Assembly** | [Xeno Kovah](https://www.linkedin.com/in/xenokovah/) | The class explores RISC-V RV32I/RV64I ISAs, “C” Compressed and “M” extensions from a security perspective.<i><br><br><ins>Topics</ins>: RISC-V ISA, GDB<br><ins>Requirements</ins>: C programming</i>|<a href="https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+Arch1005_IntroRISCV+2024_v1/course/" target="_blank"> [Online course videos]| 2024-04-15 |

<!-- ##### Beginner to RISC-V (w/ some background in digital logic design) -->


#### 🔵 Intermediate-Level resources 
A collection of more advanced learning resources for RISC-V

| Resource  |  Author(s) | Description  | Access | Date added |
|---|---|---|---|---|
| <span id="hardware-software-interface">**Computer Organization and Design RISC-V edition: The Hardware Software Interface (2nd edition)**</span> (good starting point)| David A. Patterson, John L. Hennesy | Covers the RISC-V Instruction Set in general and does an in-depth examination of the core RISC-V instructions. It also does a deep dive into RISC-V processor implementations. Each chapter includes real-world applications by tying concepts discussed with available modern computers. The book also highlights the interactions between hardware and software by continuously optimizing a sample software program based on the new hardware concepts introduced in each chapter.<i><br><br><ins>Topics</ins>: RISC-V ISA, Real world examples<br><ins>Requirements</ins>: <i>Logic design</i> | <a href="https://www.amazon.com/Computer-Organization-Design-RISC-V-Architecture/dp/0128203315" target="_blank">[Amazon book link]</a>| 2024-01-10 |
| <span id="computer-architecture-rvfpga">**RVfpga: Computer Architecture with an Industrial RISC-V Core**</span> | Sarah Harris, Daniel Chaver-Martinez | This free EdX course expands on topics covered in **Digital Design and Computer Architecture, RISC-V edition** with hands-on learning. This course shows how to target a commercial RISC-V Core and RISC-V system-on-chip (SoC) to FPGA, program the RISC-V SoC, and add more functionalities to the RISC-V SoC <i><br><br><ins>Topics</ins>: RVfpga SoC development<br><ins>Requirements</ins>: Digital logic design, C programming, RISC-V ISA, processor microarchitecture, Memory systems, Embedded I/O systems</i>| <a href="https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core" target="_blank">[Edx course link]</a>| 2024-01-10 |
| <span id="computer-architecture-rvfpga-extended">**RVfpga (extended): Understanding Computer Architecture**</span> | Sarah Harris, Daniel Chaver-Martinez | This is an updated and extended version of the free [edx course](#computer-architecture-rvfpga) above. The RVfpga Course in Computer Architecture provides hands-on understanding of a commercial RISC-V processor, RISC-V SoC, and the RISC-V ecosystem. Specifically, the RVfpga v3.0 course shows how to target a VeeR EL2 and a VeeR EH1 based system-on-chip (SoC) to 3 different FPGA boards: the Digilent Basys 3 board ($124 academic price), the Real Digital Boolean board ($74 academic price), and the Digilent Nexys A7 board ($262 academic price). The course can also be completed only in simulation; for that purpose, several simulation tools are provided which enable the user to simulate the system at different levels: from a Boolean/Nexys A7/Basys 3 virtual board down to the VeeR EH1/EL2 pipeline.<i><br><br><ins>Topics</ins>: RVfpga SoC development<br><ins>Requirements</ins>: It is highly recommended to read [Digital Design and Computer Architecture, RISC-V edition](#digital-design)| [RVfpga v3.0 course link](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) </i>| 2024-02-06 |
|**learn-FPGA episode II: pipelining**|[BrunoLevy](https://github.com/BrunoLevy)|This tutorial explains how to transform the basic softcore from [episode I](#bruno-levy-episode-1) into an efficient pipelined processor. The tutorial follows a step-by-step approach, starting from a 5-states processor, transforming the states into stages, and solving data and control hazards by first observing what happens in real programs thanks to the included debugger/disassembler. Then it is explained how to gain more performance using register forwarding. Finally, branch prediction is introduced, from the simplest static branch prediction to more elaborate ones (gshare). The effect of the different optimizations are demonstrated using different codes (the classical dhrystones and coremark benchmarks, and a program that computes an image using raytracing).<i><br><br><ins>Topics</ins>: Digital desgin, FPGA, C Programming, RISC-V assembly<br><ins>Requirements</ins>: It is highly recommended to read [episode I](#bruno-levy-episode-1) before episode II !</i>| <a href="https://github.com/BrunoLevy/learn-fpga/blob/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/PIPELINE.md" target="_blank">[GitHub]</a>| 2024-01-10 |
| **Computer Architecture: A Quantitative Approach(6th edition)** | David A. Patterson, John L. Hennesy | Covers advanced computer architecture concepts pertaining to high performance computing principles and domain specific architectures along with examples and exercises pertaining to the RISC-V ISA-(6th Edition onwards). This is a step-up from the first book,(Hardware-Software Interface), with advanced concepts like Instruction , Data and Thread Level Parallelism along with introduction to Vector, SIMD and GPU architectures.It also continues the tradition of using real-world examples to demonstrate the concepts, by introducing memory organizations and architectures of ARM Cortex A8, Intel Core i7, Nvidia GTX-280 GPUs and so on.<i><br><br><ins>Topics</ins>: Computer architecture, RISC-V ISA<br><ins>Requirements</ins>: It is highly recommendeded to read [Hardware Software Interface](#hardware-software-interface) before this book</i>| <a href="https://a.co/d/fuvp97D" target="_blank">[Amazon book link]</a>| 2024-01-10 |
| **Tutorial: RISC-V Vector Extension Demystified** | Thang Tran | A very in-depth, three hour long video introduction to the RISC-V Vector extension. <i><br><br><ins>Topics</ins>: RISC-V Vector extension| <a href="https://youtu.be/oTaOd8qr53U" target="_blank">[Youtube video]</a> | 2024-01-10 |
|**Learn with SHAKTI**| <a href="https://shakti.org.in/team.html" target="_blank"> [Shakti - RISE Lab, IITM] </a> | A tutorial on RISC-V assembly programming using the RISC-V toolchain (Spike, riscv-pk, OpenOCD) and basic examples and assignments. More elaborate RISC-V ASM examples can be found in the: <a href="https://shakti.org.in/docs/risc-v-asm-manual.pdf" target="_blank">[Shakti RISC-V ASM Programmer Manual Part I]</a><i><br><br><ins>Topics</ins>: RISC-V assembly<br></i>| <a href="https://shakti.org.in/learn_with_shakti/intro.html" target="_blank">[Link to: Learn with Shakti]</a>| 2023-12-21 |
|**LinuxFoundationX: RISC-V Toolchain and Compiler Optimization Techniques** | <a href="https://www.edx.org/bio/aditya-kumar" target="_blank"> Aditya Kumar  </a> | Develop a working knowledge of the internals of compiler toolchains and compiler optimization techniques with a focus on RISC-V applications. <i><br><br><ins>Topics</ins>: RISC-V Toolchain and Compiler<br><ins>Requirements</ins>: C/C++ programming, Compiler, Git</i>| <a href="https://www.edx.org/learn/computer-programming/the-linux-foundation-risc-v-toolchain-and-compiler-optimization-techniques" target="_blank"> [edX Course Link] </a> | 2024-01-10 |
|**RISC-V Optimization Guide** | <a href="https://riseproject.dev/" target="_blank"> RISE Project </a> | The intention is to give specific actionable optimization recommendations for software developers writing code for RISC-V application processors.<i><br><br><ins>Topics</ins>: RISC-V Optimization</i>| <a href="https://gitlab.com/riseproject/riscv-optimization-guide" target="_blank"> [Github] </a> | 2024-02-19 |

#### Softwares and Tools
A collection of tools that can be used along with the beginner or intermediate-level learning resources for a better understanding or visualization of the RISC-V ISA

| Resource |  Author(s) | Description  | Access | Date added |
|---|---|---|---|---|
| **emulsiV** | Guillaume Savaton, ESEO | emulsiV is a visual simulator for a simple RISC processor called Virgule. Virgule is a 32-bit RISC processor core that implements a minimal subset of the RISC-V instruction set. Here, “minimal” means that Virgule accepts only the instructions that a C compiler would generate from a pure stand-alone C program. | <a href="https://eseo-tech.github.io/emulsiV/" target="_blank">[website]</a> | 2023-20-12 |
| **RISC-V Instruction Encoder/Decoder** | LupLab @ University of California, Davis | This tool is an online encoder/decoder for RISC-V instructions. Users can input RISC-V instructions in their assembly or binary format and get the full conversion from one to the other. | <a href="https://luplab.gitlab.io/rvcodecjs/" target="_blank">[website]</a> | 2023-20-12 |
| **CREATOR** | Diego Camarmas Alonso,Félix García Carballeira,Alejandro Calderón Mateos,Elías del Pozo Puñal | CREATOR is a didactic simulator that allows the development, simulation, and debugging of RISC-V (RV32IMFD) assembly programs intuitively and interactively. It is a web application, so it can be used on any type of device (desktop, tablet, smartphone, etc.) without installing additional software. Only a modern web browser (Google Chrome, Mozilla Firefox, Apple Safari, etc.) is required. | <a href="https://creatorsim.github.io/creator/" target="_blank">[website]</a> | 2023-20-12 |
| **QtRvSim** - RISC-V CPU Simulator with Cache and Pipeline Visualization | Computer Architectures Education project at Czech Technical University | QtRvSim is educational simulator with pipeline and cache visualization (RV32IMA/RV64IMA). It supports even M-mode ecalls, ACLINT MTIMER, MSWI, SSWI, related CSR registers, serial port Rx and Tx interrupts and more. | <a href="https://github.com/cvut/qtrvsim/" target="_blank">[Github]</a> | 2023-20-12 |
| **RVV intrinsics viewer** | dzaima | A third party documentation website for the vector extension intrinsics, currently including pretty much all intrinsics variations, and fuzzy search. This can be a useful resource when writing rvv code. | <a href="https://dzaima.github.io/intrinsics-viewer/" target="_blank">[website]</a> | 2023-20-12 |

#### Open RISC-V Implementations
A list of open RISC-V Implementations

| Name | Description  | Access | Date added |
|---|---|---|---|
| **Pequeno** | Pequeno aka pqr5 is a pipelined in-order RISC-V CPU Core compliant with RV32I | <a href="https://github.com/iammituraj/pequeno_riscv" target="_blank">[Github]</a> | 2023-20-12 |
| **NEORV32** | A tiny, customizable and highly extensible MCU-class 32-bit RISC-V soft-core CPU and microcontroller-like SoC written in platform-independent VHDL. The project is highly documented, powered by a nice community, includes software examples, demo FPGA setups and targets FPGA/RISC-V starters as well as advanced users.| [[GitHub]](https://github.com/stnolting/neorv32) | 2024-01-11 |

### Relevant Documentation from RISC-V International

| Resource | Description | Access |
|---|---|---|
| **Member Benefits and Welcome deck** | A set of slides useful for new RISC-V members to familiarize themselves with the scope/organization of the RISC-V community and learn about membership benefits, as well as how to integrate into the community as a member. |  <a href="https://docs.google.com/presentation/d/1Q8gMcVwzqdqym3ugl_Q-LW0KMUApO-v8mWVdjqQE-MI/edit#slide=id.gf097992cc3_0_1819" target="_blank">[Google Doc]</a>|
| **Getting Started Guide for RISC-V Members** |This document is intended to give a member’s overview of the RISC-V technical organizations. The intended audience is both for new members as well as a reference for existing members.| <a href="https://docs.google.com/document/d/1Qjf6BwMmtqTfzftr3WWf2bRv8Cl4f0qZrWWbr0jCBSU/edit" target="_blank">[Google Doc]</a>|
| **RISC-V Technical Wiki** |This page serves as the main anchor point for the most important pieces of technical information for RISC-V. If you're looking for something technical, start here.| <a href="https://wiki.riscv.org" target="_blank">[webpage]</a> |
| **RISC-V Lifecycle Guide** |This document has been created to facilitate RISC-V member participation in the key activities involved in creating and running groups, writing of specifications, and contributing open-source software in support of RISC-V architectures.  It is a guide, not the rules. |<a href="https://docs.google.com/document/d/1Au3veNdNJQKPq-oiQRKTzdgmM72FDaqZOKeH7sOnG04/" target="_blank">[Google Doc]</a> |
|**RISC-V Repository Map** |A central point that directs to different repositories relevant to the RISC-V ecosystem. It includes the technical and non-technical, ISA and non-ISA related, software related, as well as collaboration related repositories for RISC-V available on Github. | <a href="https://wiki.riscv.org/display/HOME/GitHub+Repo+Map" target="_blank">[webpage]</a>|


### Articles and presentations

| Resource  |  Author(s) | Description  | Access |
|---|---|---|---|
| **Design of the RISC-V Instruction Set Architecture** |Andrew Waterman|Andrew Waterman’s Doctorate of Philosophy dissertation in the University of California, Berkeley, about the RISC-V ISA. It covers how RISC-V is a well structured small base ISA with a variety of optional extensions, making RISC-V convenient for a range of purposes from research and education, low-power embedded devices, to more general-purpose, high-performance computing, with the existence of these optional extensions. It provides a comparison of RISC-V to other popular ISAs as well.| <a href="https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-1.pdf" target="_blank">[pdf]</a>|
| **Past, Present and Future of RISC-V** | Krste Asanović | | <a href="https://www.youtube.com/watch?v=RrVRMFjYti0" target="_blank">[YouTube video]</a>|
| **Is RISC-V the Future** | Roddy Urquhart | |<a href="https://semiengineering.com/is-risc-v-the-future" target="_blank">[webpage]</a>|




