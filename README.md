# Learn RISC-V

[![Check Markdown links](https://github.com/riscv/learn/actions/workflows/action.yml/badge.svg?branch=main)](https://github.com/riscv/learn/actions/workflows/action.yml)

A community-driven, continuously updated compilation of RISC-V learning resources. Content is organized by topic and experience level to help you discover courses, software, documentation, and articles efficiently.

**RISC-V** is an open standard Instruction Set Architecture (ISA) based on established Reduced Instruction Set Computer (RISC) principles.

👋 **Want to learn about RISC-V?** Check out the [Beginner-Level](#beginner-level-resources) or [Intermediate-Level](#intermediate-level-resources) learning resources.

<a id="star-history"></a>
## Star History

[![Star History for riscv/learn](https://api.star-history.com/svg?repos=riscv/learn&type=Date)](https://www.star-history.com/#riscv/learn&Date)

---

<a id="table-of-contents"></a>
## 👉 Table of Contents

- [Learn RISC-V](#learn-risc-v)
  - [Star History](#star-history)
  - [👉 Table of Contents](#-table-of-contents)
  - [➕ Making Contributions](#-making-contributions)
  - [📙 Resources](#-resources)
    - [Learning Resources for RISC-V](#learning-resources-for-risc-v)
      - [🟢 Beginner-Level Resources](#-beginner-level-resources)
      - [🔵 Intermediate-Level Resources](#-intermediate-level-resources)
    - [Software and Tools](#software-and-tools)
    - [Open RISC-V Implementations](#open-risc-v-implementations)
    - [Available RISC-V Boards, Development Kits, Tablets, and Laptops](#available-risc-v-boards-development-kits-tablets-and-laptops)
      - [🟢 32-bit Hardware](#-32-bit-hardware)
      - [🔵 64-bit Hardware](#-64-bit-hardware)
    - [Articles and Presentations](#articles-and-presentations)

---

<a id="making-contributions"></a>
## ➕ Making Contributions

We love contributions! Check out [contributing.md](contributing.md) for more info. Thank you for your interest in contributing to our RISC-V tutorial compilation.

<!--
---
<a id="learning-roadmap"></a>
## 📚 Learning Roadmap

A roadmap to help beginners select materials to familiarize themselves with RISC-V. Your contributions are welcome.

![Learning Roadmap](roadmap/roadmap_v1.png)

[View the roadmap web version](https://roadmap.sh/r?id=662706c3351f8e69e690e740)
-->

---

<a id="resources"></a>
## 📙 Resources

<a id="learning-resources-for-risc-v"></a>
### Learning Resources for RISC-V

<a id="beginner-level-resources"></a>
#### 🟢 Beginner-Level Resources

For those with little or no knowledge of digital logic design. Consider starting with **[Digital Design & Computer Architecture (RISC-V Edition)](https://www.amazon.com/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642)** and then progressing to intermediate-level courses like **[RVfpga](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core)**.

<!-- Keep this sorted alphabetically =) -->
| Resource  | Author(s) | Description  | Access | Date Added |
|---|---|---|---|---|
| **An Introduction to Assembly Programming with RISC-V** | Prof. Edson Borin | Teaches RISC-V assembly programming concepts. | [Webpage](https://www.ic.unicamp.br/~edson/riscv-book.html) | 2024-05-03 |
| **Architecture 1005: RISC-V Assembly** | OpenSecurityTraining | Security-focused exploration of RISC-V ISAs and extensions. | [Course videos](https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+Arch1005_IntroRISCV+2024_v1/course/) | 2024-04-15 |
| **Basic Computer Architecture** | Smruti R. Sarangi | Computer architecture fundamentals. | [Website](https://www.cse.iitd.ac.in/~srsarangi/archbooksoft.html) | 2024-12-27 |
| **Computer Architecture Basics** | CTU Prague – FEE (Pavel Piša) | Course covering computer architecture basics, including CPU design and speculative execution. | [Course videos](https://cw.fel.cvut.cz/wiki/courses/b35apo/en/lectures/start) | 2024-04-16 |
| **Creating a RISC-V from scratch!** | Lucas Teske (Teske's Lab) | Learning livestream series focused on creating an RV32E that runs on FPGAs. | [YouTube (Portuguese)](https://www.youtube.com/playlist?list=PLEP_M2UAh9q52a-w3ZUEChEoG_ROeMa88) | 2024-10-18 |
| **Digital Design & Computer Architecture RISC-V Edition** | Sarah L. Harris, David M. Harris | Foundational digital logic design and RISC-V processor implementation. | [Amazon](https://www.amazon.com/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642) | 2024-10-01 |
| **Easy RISC-V** | Vivian “dramforever” Wang | RISC-V assembly tutorial with interactive emulator (RV32I and some privileged arch). | [Webpage](https://easyriscv.dram.page) | 2025-10-30 |
| **Hands-on RISC-V Processor Design** | Rahul Behl | Dive into RISC-V processor design using SystemVerilog. | [QuickSilicon](https://quicksilicon.in/course/riscv) | 2024-10-01 |
| **learn-FPGA episode I: from blinky to RISC-V** | Bruno Levy | Design an FPGA-based RISC-V softcore starting from a basic Verilog blinker. | [GitHub](https://github.com/BrunoLevy/learn-fpga) | 2024-10-01 |
| **LinuxFoundationX: Building a RISC-V CPU Core** | Steve Hoover | Free course on RISC-V microarchitecture design using open-source tools. | [edX course](https://www.edx.org/learn/design/the-linux-foundation-building-a-risc-v-cpu-core) | 2024-10-01 |
| **Nand2Tetris** | Noam Nisan, Shimon Schocken | Build a computer from logic gates using a hardware simulator. | [Website](https://www.nand2tetris.org/) | 2024-10-01 |
| **RISC-V Assembly Introduction (Portuguese)** | Gabriel G. de Brito | Basics of RISC-V IM architecture with the EGG emulator. | [Course videos](https://youtube.com/playlist?list=PLFe3Zrf4uj4vlRF21jK3vzfCuSSJ5I_uB) | 2024-06-04 |
| **Step-by-step RISC-V Compiler Development** | Shao-Ce Sun | Practical guide to RISC-V C compiler development. | [Teaching resources](https://github.com/sunshaoce/rvcc-course) · [Course videos (Chinese)](https://www.bilibili.com/video/BV1gY4y1E7Ue) | 2024-03-20 |
| **Step-by-step RISC-V OS Development** | Chen Wang | Practical guide for developing RISC-V operating systems. | [Teaching resources](https://github.com/plctlab/riscv-operating-system-mooc) · [Course videos (Chinese)](https://www.bilibili.com/video/BV1Q5411w7z5) | 2024-05-03 |
| **The RISC-V Reader: An Open Architecture Atlas** | David Patterson, Andrew Waterman | Introduction to the RISC-V instruction set. | [RISC-V Reader](http://www.riscbook.com/) | 2024-05-03 |
| **Writing a RISC-V OS From Scratch** | Seiya Nuta | Write an OS for RISC-V in about 1,000 lines of code. | [Webpage](https://operating-system-in-1000-lines.vercel.app/en/) | 2025-07-27 |
| **Why Your Phone Is So Fast: The Sports Car vs. The Truck** | David Patterson | How do we keep making computers faster? | [Webpage](https://kids.frontiersin.org/articles/10.3389/frym.2025.1474522) | 2025-02-09 |

---

<a id="intermediate-level-resources"></a>
#### 🔵 Intermediate-Level Resources

Advanced materials for learners familiar with digital logic and basic architecture.

<!-- Keep this sorted alphabetically =) -->
| Resource  | Author(s) | Description | Access | Date Added |
|---|---|---|---|---|
| **Computer Architecture: A Quantitative Approach (6th Edition)** | David Patterson, John Hennessy | Advanced topics including ILP and GPU architectures, using RISC-V. | [Amazon](https://a.co/d/fuvp97D) | 2024-10-01 |
| **Computer Organization & Design (RISC-V Edition)** | David Patterson, John Hennessy | In-depth study of RISC-V ISA and processor implementation. | [Amazon](https://www.amazon.com/Computer-Organization-Design-RISC-V-Architecture/dp/0128203315) | 2024-10-01 |
| **HaDes-V** | Tobias Scheipel | The Instruction Guide and code template (OER) for microcontroller design using the HaDes-V RISC-V-based processor. | [GitHub](https://github.com/tscheipel/HaDes-V/) · [Instruction Guide](https://repository.tugraz.at/oer/nytm4-grv34) | 2024-12-18 |
| **Learn with SHAKTI** | Shakti – RISE Lab, IITM | Tutorials on RISC-V assembly programming using the RISC-V toolchain. | [Learn with Shakti](https://shakti.org.in/learn_with_shakti/intro.html) | 2023-12-21 |
| **learn-FPGA episode II: pipelining** | Bruno Levy | Extends the basic RISC-V softcore from episode I with pipelining and performance optimizations. | [GitHub](https://github.com/BrunoLevy/learn-fpga/blob/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/PIPELINE.md) | 2024-10-01 |
| **LinuxFoundationX: RISC-V Toolchain and Compiler Optimization Techniques** | Aditya Kumar | RISC-V toolchain internals and compiler optimizations. | [edX course](https://www.edx.org/learn/computer-programming/the-linux-foundation-risc-v-toolchain-and-compiler-optimization-techniques) | 2024-10-01 |
| **RISC-V Optimization Guide** | RISE Project | Actionable optimization recommendations for RISC-V software developers. | [GitLab](https://gitlab.com/riseproject/riscv-optimization-guide) | 2024-02-19 |
| **RV64GC Linker from Scratch in Go** | Yang Liu, PLCT Lab | Build an RV64GC linker from scratch in Go. | [GitHub](https://github.com/ksco/rvld) · [Course videos (Chinese)](https://space.bilibili.com/296494084/channel/collectiondetail?sid=857032) | 2024-04-24 |
| **RVfpga (Extended): Understanding Computer Architecture** | Sarah Harris, Daniel Chaver-Martinez | Updated RVfpga course with FPGA and simulation tools. | [RVfpga v3.0 downloads](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) | 2024-06-02 |
| **RVfpga: Computer Architecture with an Industrial RISC-V Core** | Sarah Harris, Daniel Chaver-Martinez | Hands-on learning with a commercial RISC-V SoC on FPGAs. | [edX course](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core) | 2024-10-01 |
| **Teaching experiences with RVfpga** | ARTECS Group, Complutense University of Madrid | How RVfpga and the Ripes simulator were used in two UCM courses. | [GitHub](https://github.com/artecs-group/RVfpga-sim-addons) | 2024-10-18 |
| **Tutorial: RISC-V Vector Extension Demystified** | Thang Tran | In-depth introduction to the RISC-V vector extension. | [YouTube](https://youtu.be/oTaOd8qr53U) | 2024-10-01 |
| **Tutorial: basic_RV32s** | [T410N](https://github.com/T410N) | A systematic microarchitectural roadmap for learning RISC-V processor design from scratch. | [basic_RV32s](https://github.com/RISC-KC/basic_rv32s) | 2024-07-25 |
| **RISC-V Vector Primer** | Tran, Thang Minh and Miller, Paul and McLeod, Jonah | A structured, open technical primer explaining the RISC‑V Vector Extension, with examples, diagrams, and chapter‑based documentation. | [GitHub](https://github.com/simplex-micro/riscv-vector-primer) | 2026-02-07 |

---

<a id="software-and-tools"></a>
### Software and Tools

Tools to enhance understanding or visualize the RISC-V ISA.

<!-- Keep this sorted alphabetically =) -->
| Tool | Author(s) | Description | Access | Date Added |
|---|---|---|---|---|
| **CREATOR** | Diego Camarmas Alonso, Félix García Carballeira, Alejandro Calderón Mateos, Elías del Pozo Puñal | Didactic simulator for RISC-V assembly programs. | [Website](https://creatorsim.github.io/creator/) | 2023-12-20 |
| **emulsiV** | Guillaume Savaton | Visual simulator for a minimal 32-bit RISC processor. | [Website](https://eseo-tech.github.io/emulsiV/) | 2023-12-20 |
| **Go RISC-V Emulator** | Lucas Teske | A Go implementation of RV32I+M that can run Doom. | [GitHub](https://github.com/racerxdl/riscv-emulator) | 2024-10-18 |
| **Compiler Explorer** | Matt Godbolt | Online compiler explorer supporting GCC/LLVM for RV64. | [Website](https://godbolt.org/) | 2024-10-18 |
| **Online RISC-V Assembler** | Lucas Teske | Online RISC-V assembler using GNU assembler in WebAssembly. | [Website](https://riscvasm.lucasteske.dev/), [GitHub](https://github.com/racerxdl/riscv-online-asm) | 2024-10-18 |
| **Piscado** | Gustavo N. Martins | RISC-V simulator written in Python during Twitch live coding. | [GitHub](https://github.com/gustavonmartins/piscado) | 2024-10-18 |
| **QtRvSim** | CTU Prague | RISC-V simulator with cache and pipeline visualization. | [GitHub](https://github.com/cvut/qtrvsim/) | 2023-12-20 |
| **RISC-V ALE** | Antonio Guimarães | RISC-V Assembly Learning Environment. | [Website](https://riscv-programming.org/ale/) | 2024-10-18 |
| **RISC-V Instruction Encoder/Decoder** | LupLab | Online tool for encoding/decoding RISC-V instructions. | [Website](https://luplab.gitlab.io/rvcodecjs/) | 2023-12-20 |
| **Risco-5S** | Julio Nunes Avelar | RISC-V simulator with RV32IM, built during a few days off. | [GitHub](https://github.com/JN513/Risco-5S) | 2023-11-04 |
| **RVV Intrinsics Viewer** | dzaima | Documentation for RISC-V vector extension intrinsics. | [Website](https://dzaima.github.io/intrinsics-viewer/) | 2023-12-20 |
| **WebRISC-V** | Roberto Giorgi, Gianfranco Mariotti | Web-based graphical simulation with pipeline visualization for RV32IM/RV64IM. | [GitHub](https://github.com/Mariotti94/WebRISC-V/) | 2025-08-14 |

---

<a id="open-risc-v-implementations"></a>
### Open RISC-V Implementations

Explore open RISC-V implementations for hands-on learning.

<!-- Keep this sorted alphabetically =) -->
| Name | Description | Access | Date Added |
|---|---|---|---|
| **AUK-V-Aethia** | AUK-V RV32I CPU. | [GitHub](https://github.com/veeYceeY/AUK-V-Aethia) | 2024-10-18 |
| **CV32E40P** | In-order 4-stage RISC-V RV32IMFCXpulp CPU based on RI5CY (PULP-Platform). | [GitHub](https://github.com/openhwgroup/cv32e40p) | 2024-10-18 |
| **CVA6** | CORE-V CVA6, an application-class 6-stage RISC-V CPU capable of booting Linux. | [GitHub](https://github.com/openhwgroup/cva6) | 2024-10-18 |
| **DarkRISCV** | Small RV32-E/I soft-core CPU optimized for FPGAs. | [GitHub](https://github.com/darklife/darkriscv) | 2024-10-18 |
| **Grande Risco-5** | RV32I multi-cycle processor with a 5-stage pipeline for education. | [GitHub](https://github.com/JN513/Grande-Risco-5) | 2024-11-06 |
| **Hazard3** | 3-stage RV32IMACZb* processor with debug. | [GitHub](https://github.com/Wren6991/Hazard3) | 2024-12-19 |
| **KianV** | SV32 (MMU) RV32IMA Zicntr Zicsr Zifencei SSTC Linux/XV6 ASIC/FPGA SoC. | [GitHub](https://github.com/splinedrive/kianRiscV) | 2025-09-30 |
| **Kronos** | 3-stage in-order RISC-V RV32I_Zicsr_Zifencei core geared towards FPGA. | [GitHub](https://github.com/SonalPinto/kronos) | 2024-10-18 |
| **Leaf** | Small RV32I SoC in VHDL for portable applications; FPGA and ASIC. | [GitHub](https://github.com/britovski/leaf) | 2024-10-23 |
| **Maestro** | 5-stage pipeline RV32I implementation in VHDL. | [GitHub](https://github.com/Artoriuz/maestro) | 2024-10-18 |
| **Mriscv** | 32-bit microcontroller featuring a RISC-V core. | [GitHub](https://github.com/onchipuis/mriscv) | 2024-10-18 |
| **NEORV32** | MCU-class RISC-V soft-core CPU, customizable and extensible. | [GitHub](https://github.com/stnolting/neorv32) | 2024-11-01 |
| **NERV** | Naive Educational RISC-V processor. | [GitHub](https://github.com/YosysHQ/nerv) | 2024-10-18 |
| **NoX** | Small RISC-V (RV32I) core written in SystemVerilog. | [GitHub](https://github.com/aignacio/nox) | 2024-10-21 |
| **Pequeno** | Pipelined in-order RISC-V CPU core compliant with RV32I. | [GitHub](https://github.com/iammituraj/pequeno_riscv) | 2023-12-20 |
| **PicoRV32** | Size-optimized RISC-V CPU. | [GitHub](https://github.com/YosysHQ/picorv32) | 2024-10-18 |
| **ReonV** | Modified LEON3 (SPARC V8) to RISC-V ISA, VHDL. | [GitHub](https://github.com/lcbcFoo/ReonV) | 2024-10-18 |
| **Riscado-V** | Simple RISC-V (RV32I) implementation in Verilog. | [GitHub](https://github.com/zxmarcos/riscado-v) | 2024-10-18 |
| **Risco-5** | Multi-cycle RISC-V processor with RV32I/E[M]. | [GitHub](https://github.com/JN513/Risco-5) | 2024-10-18 |
| **RISC-V Steel** | RV32I + Zicsr + Machine mode. | [GitHub](https://github.com/riscv-steel/riscv-steel) | 2024-10-18 |
| **RPU** | Basic RISC-V CPU in VHDL. | [GitHub](https://github.com/Domipheus/RPU) | 2024-10-18 |
| **RSD** | RISC-V out-of-order superscalar processor. | [GitHub](https://github.com/rsd-devel/rsd) | 2024-10-18 |
| **SERV** | The SErial RISC-V CPU. | [GitHub](https://github.com/olofk/serv) | 2024-10-18 |
| **SGDH-RVSoC** | Tiny 32-bit RISC-V rv32acim CPU capable of running Linux on FPGA and in simulation. | [GitHub](https://github.com/semisgdh/SGDH-RVSoC) | 2025-10-08 |
| **TinyRiscv** | Very simple and easy-to-understand RISC-V core. | [GitHub](https://github.com/liangkangnan/tinyriscv) | 2024-10-18 |
| **VexRiscv** | FPGA-friendly 32-bit RISC-V CPU (SpinalHDL). | [GitHub](https://github.com/SpinalHDL/VexRiscv) | 2024-10-18 |
| **Riskow** | Toy RV32-E from scratch during livestreams; runs on low-cost FPGAs. | [GitHub](https://github.com/racerxdl/riskow) | 2024-10-18 |

---

<a id="available-risc-v-boards-development-kits-tablets-and-laptops"></a>
### Available RISC-V Boards, Development Kits, Tablets, and Laptops

<a id="32-bit-hardware"></a>
#### 🟢 32-bit Hardware

Popular hardware based on RV32 processors.

<!-- Keep this sorted alphabetically =) -->
| Board or Dev Kit | Company | SoC | RISC-V Core | Frequency | Date Added |
|---|---|---|---|---|---|
| [**CH32V003 Devkit**](https://www.aliexpress.com/item/1005004895791296.html) | WCH | CH32V003 | Single-core QingKe V2A | 48 MHz | 2025-07-25 |
| [**ESP32C2 Devkit**](https://www.espressif.com/en/products/devkits) | Espressif | ESP32C2 | Single-core 32-bit | 120 MHz | 2025-07-25 |
| [**ESP32C3 Devkit**](https://www.espressif.com/en/products/devkits) | Espressif | ESP32C3 | Single-core 32-bit | 160 MHz | 2025-07-25 |
| [**ESP32C5 Devkit**](https://www.espressif.com/en/products/devkits) | Espressif | ESP32C5 | Single-core 32-bit | 240 MHz | 2025-07-25 |
| [**ESP32C6 Devkit**](https://www.espressif.com/en/products/devkits) | Espressif | ESP32C6 | Single-core 32-bit | 160 MHz | 2025-07-25 |
| [**ESP32H2 Devkit**](https://www.espressif.com/en/products/devkits) | Espressif | ESP32H2 | Single-core 32-bit | 96 MHz | 2025-07-25 |
| [**ESP32P4 EV Board**](https://www.espressif.com/en/products/devkits) | Espressif | ESP32P4 | Dual-core 32-bit | 360 MHz | 2025-07-25 |
| [**Longan Nano**](https://wiki.sipeed.com/hardware/en/longan/Nano/Longan_nano.html) | Sipeed | GD32VF103CBT6 | Single-core 32-bit | 108 MHz | 2025-07-25 |
| [**M0sense**](https://wiki.sipeed.com/hardware/en/maixzero/sense/maix_zero_sense.html) | Sipeed | BL702 | Single-core 32-bit | 144 MHz | 2025-08-24 |
| [**Raspberry Pi Pico 2**](https://www.raspberrypi.com/products/raspberry-pi-pico-2) | Raspberry Pi | RP2350 | Dual-core Hazard3 | 150 MHz | 2024-12-19 |

Following are no longer available:

| Board or Dev Kit | Company | SoC | RISC-V Core | Frequency | Date Added |
|---|---|---|---|---|---|
| [**HiFive1**](https://www.sifive.com/boards/hifive1) | SiFive | FE310-G000 | 32-bit E31 | 256 MHz | 2024-10-31 |
| [**HiFive1 Rev B**](https://www.sifive.com/boards/hifive1-rev-b) | SiFive | FE310-G002 | 32-bit E31 | 256 MHz | 2024-10-31 |

<a id="64-bit-hardware"></a>
#### 🔵 64-bit Hardware

Popular hardware based on RV64 processors.

<!-- Keep this sorted alphabetically =) -->
| Board or Dev Kit | Company | SoC | RISC-V Core | Date Added |
|---|---|---|---|---|
| [**Banana Pi F3**](https://docs.banana-pi.org/en/BPI-F3/BananaPi_BPI-F3) | Banana Pi | SpacemiT K1 | Octa-core X60 | 2024-11-01 |
| [**BeagleV-Ahead**](https://www.beagleboard.org/boards/beaglev-ahead) | BeagleBoard.org | TH1520 | T-HEAD quad-core Xuantie C910 | 2025-07-26 |
| [**BeagleV-Fire**](https://www.beagleboard.org/boards/beaglev-fire) | BeagleBoard.org | Microchip PolarFire MPFS025T | 4× RV64GC + 1× RV64IMAC | 2025-07-26 |
| [**DC Roma Laptop I**](https://deepcomputing.io/product/dc-roma-risc-v-laptop/) | DeepComputing | StarFive JH7110 | Quad-core | 2025-11-03 |
| [**DC Roma Laptop II**](https://deepcomputing.io/product/dc-roma-risc-v-laptop-ii/) | DeepComputing | SpacemiT K1 | Octa-core X60™ | 2024-10-31 |
| [**DC Roma Mainboard I**](https://deepcomputing.io/product/dc-roma-risc-v-mainboard/) | DeepComputing | StarFive JH7110 | Quad-core | 2025-11-03 |
| [**DC Roma Mainboard II (AI PC)**](https://deepcomputing.io/product/dc-roma-risc-v-ai-pc/) | DeepComputing | ESWIN EIC7702X | SiFive octa-core P550 | 2025-07-25 |
| [**HiFive Premier P550**](https://www.sifive.com/boards/hifive-premier-p550) | SiFive | ESWIN EIC7700X | SiFive quad-core P550 | 2024-10-31 |
| [**HiFive Unmatched**](https://www.sifive.com/boards/hifive-unmatched) | SiFive | SiFive U74-MC | 64-bit S7 | 2024-10-31 |
| [**Kendryte K230**](https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html) | Canaan Technology | K230 | Dual-core T-HEAD C908 | 2024-11-01 |
| [**LicheeBook 4A**](https://wiki.sipeed.com/hardware/en/lichee/th1520/lbook4a/lbook4a.html) | Sipeed | TH1520 | Quad-core T-HEAD C910 | 2024-10-31 |
| [**LicheePi 3A**](https://wiki.sipeed.com/hardware/en/lichee/K1/lpi3a/1_intro.html) | Sipeed | SpacemiT K1 | Octa-core X60 | 2024-10-31 |
| [**LicheePi 4A**](https://wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/1_intro.html) | Sipeed | TH1520 | Quad-core T-HEAD C910 | 2024-10-31 |
| [**LicheePi Console 4A**](https://wiki.sipeed.com/hardware/en/lichee/th1520/lcon4a/lcon4a.html) | Sipeed | TH1520 | Quad-core T-HEAD C910 | 2024-10-31 |
| [**LicheeRV D1**](https://wiki.sipeed.com/hardware/en/lichee/RV/Dock.html) | Sipeed | AllWinner D1 | Single-core T-HEAD C906 | 2024-10-31 |
| [**LicheeRV Nano**](https://wiki.sipeed.com/hardware/en/lichee/RV_Nano/1_intro.html) | Sipeed | SG2002 | Single-core T-HEAD C906 | 2024-10-31 |
| [**MangoPi MQ-Pro**](https://mangopi.org/mqpro) | MangoPi | D1 | Single-core T-HEAD C906 | 2025-07-28 |
| [**Milk-V Duo**](https://milkv.io/docs/duo/getting-started/duo) | Milk-V | CV1800B | T-HEAD C906 | 2024-10-31 |
| [**Milk-V Duo256M**](https://milkv.io/docs/duo/getting-started/duo256m) | Milk-V | SG2002 | T-HEAD C906 | 2024-10-31 |
| [**Milk-V Duo S**](https://milkv.io/docs/duo/getting-started/duos) | Milk-V | SG2000 | T-HEAD C906 | 2024-10-31 |
| [**Milk-V Jupiter**](https://milkv.io/jupiter) | Milk-V | SpacemiT K1 | Octa-core X60 | 2024-10-31 |
| [**Milk-V Mars**](https://milkv.io/mars) | Milk-V | JH7110 | Quad-core SiFive U74 | 2024-10-31 |
| [**Milk-V Meles**](https://milkv.io/meles) | Milk-V | TH1520 | Quad-core T-HEAD C910 | 2024-10-31 |
| [**Milk-V Pioneer**](https://milkv.io/pioneer) | Milk-V | SG2042 | 64 cores T-HEAD C910 | 2024-10-31 |
| [**Milk-V Vega**](https://milkv.io/vega) | Milk-V | FSL1030M | UX608 core | 2024-10-31 |
| [**OK7110-C**](https://www.forlinx.net/product/jh7110-single-board-computer-riscv-142.html) | Forlinx | JH7110 | Quad-core SiFive U74 | 2024-10-31 |
| [**Ox64**](https://pine64.com/product/star64-model-a-8gb-single-board-computer/) | Pine64 | BL808 | T-HEAD C906, E907, E902 | 2024-10-31 |
| [**PineTab-V**](https://pine64.com/product/pinetab-v-10-1-8gb-128gb-risc-v-based-linux-tablet-with-detached-backlit-keyboard/) | Pine64 | JH7110 | Quad-core SiFive U74 | 2024-10-31 |
| [**SpacemiT MUSE Book**](https://www.spacemit.com/spacemit-muse/) | SpacemiT | SpacemiT K1 | Octa-core X60 | 2025-09-04 |
| [**SpacemiT MUSE Box**](https://www.spacemit.com/spacemit-muse-box/) | SpacemiT | SpacemiT K1 | Octa-core X60 | 2025-09-04 |
| [**SpacemiT MUSE Card**](https://www.spacemit.com/spacemit-muse-card/) | SpacemiT | SpacemiT M1 | Octa-core X60 | 2025-09-02 |
| [**SpacemiT MUSE Pi**](https://www.spacemit.com/spacemit-muse-pi/) | SpacemiT | SpacemiT M1 | Octa-core X60 | 2024-11-01 |
| [**SpacemiT MUSE Pi Pro**](https://www.spacemit.com/spacemit-muse-pi-pro/) | SpacemiT | SpacemiT M1 | Octa-core X60 | 2025-09-02 |
| [**Star 64**](https://pine64.com/product/star64-model-a-8gb-single-board-computer/) | Pine64 | JH7110 | Quad-core SiFive U74 | 2024-10-31 |
| [**VisionFive 2**](https://www.starfivetech.com/en/site/boards) | StarFive Technology | JH7110 | Quad-core SiFive U74 | 2024-10-31 |

---

<a id="articles-and-presentations"></a>
### Articles and Presentations

<!-- Keep this sorted alphabetically =) -->
| Resource | Author(s) | Description | Access |
|---|---|---|---|
| **Design of the RISC-V Instruction Set Architecture** | Andrew Waterman | PhD dissertation on the structure of the RISC-V ISA. | [PDF](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-1.pdf) |
| **Is RISC-V the Future?** | Roddy Urquhart | Examination of RISC-V’s future potential. | [Article](https://semiengineering.com/is-risc-v-the-future) |
| **Past, Present and Future of RISC-V** | Krste Asanović | Overview of RISC-V’s evolution. | [YouTube](https://www.youtube.com/watch?v=RrVRMFjYti0) |
