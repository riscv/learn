# Learn RISC-V

[![Check Markdown links](https://github.com/riscv/learn/actions/workflows/action.yml/badge.svg?branch=main)](https://github.com/riscv/learn/actions/workflows/action.yml)

<!-- last_verified_all:start -->
> 🔴 Links last verified: **2026-09-09** — OK: 163, Redirects: 14, Broken: 2
<!-- last_verified_all:end -->

A community-driven, continuously updated list of RISC-V learning resources: courses, books, tools, open cores, boards and papers, organized by topic and level.

**RISC-V** is an open standard Instruction Set Architecture (ISA) based on established Reduced Instruction Set Computer (RISC) principles.

---

<a id="start-here"></a>
## 🚀 Start Here

The official references from RISC-V International. Everything else on this page builds on them.

| Resource | What you get | Access |
|---|---|---|
| **RISC-V Specifications** | The ISA manual: Volume I (Unprivileged), Volume II (Privileged) and Volume III (Profiles such as RVA23), plus the other ratified specifications, as browsable HTML. | [docs.riscv.org](https://docs.riscv.org/) |
| **RISC-V ISA Explorer** | Every extension and profile with its instructions, encodings, CSRs and dependencies. Build a configuration and get a valid `-march` string, compare profiles, and jump to the spec section for each extension. | [tech.riscv.org/isa-explorer](https://tech.riscv.org/isa-explorer/) |
| **Ratified Specifications** | The list of ratified specifications and their release history. | [riscv.org](https://riscv.org/specifications/ratified/) |
| **Training and Certification** | Free and paid courses from RISC-V International and the Linux Foundation, and the RISC-V Foundational Associate (RVFA) exam. | [riscv.org](https://riscv.org/community/training/) |

---

<a id="find-resources"></a>
## 🧭 Find Resources

| I want to… | Go to | For example |
|---|---|---|
| Follow a guided path | [🗺️ Learning Paths](#learning-paths) | Hardware, Software, Systems |
| Learn RISC-V from scratch | [🟢 Beginner-Level Resources](#beginner-level-resources) | CS61C, Easy RISC-V, The RISC-V Reader |
| Go deeper into architecture, operating systems or vectors | [🔵 Intermediate-Level Resources](#intermediate-level-resources) | MIT 6.1810 (xv6), RISC-V System-on-Chip Design |
| Look up an ABI, SBI, debug or interrupt spec | [📐 Specifications and Reference](#specifications-and-reference) | ELF psABI, SBI, Vector C Intrinsics |
| Write, run and debug assembly, or emulate a machine | [🛠️ Software and Tools](#software-and-tools) | Ripes, RARS, Spike, QEMU |
| Build or port software for RISC-V | [📦 Software Ecosystem and Porting](#software-ecosystem-and-porting) | GNU Toolchain, LLVM, Debian, Zephyr |
| Study or build a CPU | [🧩 Open RISC-V Implementations](#open-risc-v-implementations) | Ibex, Rocket Chip, BOOM, XiangShan, PicoRV32 |
| Test that a core is correct | [✅ Verification and Compliance](#verification-and-compliance) | riscv-tests, Architectural Tests, Sail |
| Get a board, laptop or tablet | [💻 Boards, Dev Kits, Tablets and Laptops](#available-risc-v-boards-development-kits-tablets-and-laptops) | Raspberry Pi Pico 2, Milk-V Duo, DC Roma |
| Read papers and talks | [📄 Articles and Presentations](#articles-and-presentations) | Design of the RISC-V ISA, RISC-V for HPC |
| Meet other learners and educators | [🤝 Community](#community) | Academia and Training SIG, YouTube |

New to computer architecture? Start with **[Digital Design & Computer Architecture (RISC-V Edition)](https://www.amazon.com/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642)**, practise with **[Easy RISC-V](https://easyriscv.dram.page)**, then move on to **[RVfpga](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core)**, or follow one of the [Learning Paths](#learning-paths). Keep the [ISA Explorer](https://tech.riscv.org/isa-explorer/) open as a reference.

---

<a id="learning-paths"></a>
## 🗺️ Learning Paths

Pick the path that matches what you want to do. Each step links to a resource on this page.

**Hardware: from logic gates to your own core**
1. Foundations: *Digital Design & Computer Architecture (RISC-V Edition)* or Nand2Tetris.
2. The ISA: *The RISC-V Reader*, with the [ISA Explorer](https://tech.riscv.org/isa-explorer/) open beside it.
3. A first core: *Building a RISC-V CPU Core* (edX) or *learn-FPGA*, simulated in Ripes.
4. Check it: run riscv-tests, then the RISC-V Architectural Tests through RISCOF.
5. Go further: *RISC-V System-on-Chip Design* with CORE-V Wally, then study Ibex, Rocket Chip or BOOM.

**Software: from assembly to porting**
1. Assembly: *Introduction to RISC-V (LFD110)*, then *Easy RISC-V* or RARS.
2. How code really runs: CS61C, the ELF psABI and the Assembly Programmer's Manual.
3. Toolchains: the RISC-V GNU Toolchain or LLVM, Compiler Explorer, and QEMU to run what you build.
4. Vectors: *RISC-V Vector Primer* and the Vector C Intrinsics.
5. Porting: *Porting Software to RISC-V (LFD114)* and the Software Ecosystem Dashboard.

**Systems: firmware and operating systems**
1. Privileged architecture: Volume II of the ISA manual on docs.riscv.org.
2. A small OS: *Writing a RISC-V OS From Scratch*, then MIT 6.1810 with xv6.
3. Firmware and boot: the SBI and BRS specifications.
4. Real systems: the Debian, Fedora or Ubuntu ports on QEMU or a 64-bit board.

---

<a id="making-contributions"></a>
## ➕ Making Contributions

Anyone can contribute. Open a pull request that adds your resource to the right table, in alphabetical order and with today's date, or [open an issue](https://github.com/riscv/learn/issues/new/choose) and we'll add it. Commits need a DCO sign-off (`git commit -s`). See [contributing.md](contributing.md) for details.

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
| **CS61C: Great Ideas in Computer Architecture** | UC Berkeley | C, RISC-V assembly, and how a RISC-V datapath, caches and parallelism work. Lectures, labs and projects are public. | [Course site](https://cs61c.org/) · [Venus simulator](https://venus.cs61c.org/) | 2026-10-11 |
| **Digital Design & Computer Architecture RISC-V Edition** | Sarah L. Harris, David M. Harris | Foundational digital logic design and RISC-V processor implementation. | [Amazon](https://www.amazon.com/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642) | 2024-10-01 |
| **Easy RISC-V** | Vivian “dramforever” Wang | RISC-V assembly tutorial with interactive emulator (RV32I and some privileged arch). | [Webpage](https://easyriscv.dram.page) | 2025-10-30 |
| **Foundations of RISC-V Assembly Programming (LFD117x)** | Linux Foundation | Free self-paced course on what a RISC-V processor executes: registers, instructions, calling conventions and the toolchain. | [Course](https://training.linuxfoundation.org/training/foundations-of-risc-v-assembly-programming-lfd117x/) | 2026-10-11 |
| **Hands-on RISC-V Processor Design** | Rahul Behl | Dive into RISC-V processor design using SystemVerilog. | [QuickSilicon](https://quicksilicon.in/course/riscv) | 2024-10-01 |
| **Introduction to RISC-V (LFD110)** | Linux Foundation | Free self-paced overview of the ISA, its extensions and profiles, and the ecosystem around it. | [Course](https://training.linuxfoundation.org/training/introduction-to-riscv-lfd110/) | 2026-10-11 |
| **learn-FPGA episode I: from blinky to RISC-V** | Bruno Levy | Design an FPGA-based RISC-V softcore starting from a basic Verilog blinker. | [GitHub](https://github.com/BrunoLevy/learn-fpga) | 2024-10-01 |
| **LinuxFoundationX: Building a RISC-V CPU Core** | Steve Hoover | Free course on RISC-V microarchitecture design using open-source tools. | [edX course](https://www.edx.org/learn/design/the-linux-foundation-building-a-risc-v-cpu-core) | 2024-10-01 |
| **MIT 6.191 Computation Structures** | MIT | MIT's introductory computer architecture course (formerly 6.004): digital logic, RISC-V assembly and processor design. | [Course site](https://6191.mit.edu/) | 2026-10-11 |
| **Nand2Tetris** | Noam Nisan, Shimon Schocken | Build a computer from logic gates using a hardware simulator. | [Website](https://www.nand2tetris.org/) | 2024-10-01 |
| **RISC-V Assembly Introduction (Portuguese)** | Gabriel G. de Brito | Basics of RISC-V IM architecture with the EGG emulator. | [Course videos](https://youtube.com/playlist?list=PLFe3Zrf4uj4vlRF21jK3vzfCuSSJ5I_uB) | 2024-06-04 |
| **Step-by-step RISC-V Compiler Development** | Shao-Ce Sun | Practical guide to RISC-V C compiler development. | [Teaching resources](https://github.com/sunshaoce/rvcc-course) · [Course videos (Chinese)](https://www.bilibili.com/video/BV1gY4y1E7Ue) | 2024-03-20 |
| **Step-by-step RISC-V OS Development** | Chen Wang | Practical guide for developing RISC-V operating systems. | [Teaching resources](https://github.com/plctlab/riscv-operating-system-mooc) · [Course videos (Chinese)](https://www.bilibili.com/video/BV1Q5411w7z5) | 2024-05-03 |
| **The RISC-V Reader: An Open Architecture Atlas** | David Patterson, Andrew Waterman | Introduction to the RISC-V instruction set. | [RISC-V Reader](http://www.riscbook.com/) | 2024-05-03 |
| **Why Your Phone Is So Fast: The Sports Car vs. The Truck** | David Patterson | How do we keep making computers faster? | [Webpage](https://kids.frontiersin.org/articles/10.3389/frym.2025.1474522) | 2025-02-09 |
| **Writing a RISC-V OS From Scratch** | Seiya Nuta | Write an OS for RISC-V in about 1,000 lines of code. | [Webpage](https://operating-system-in-1000-lines.vercel.app/en/) | 2025-07-27 |

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="intermediate-level-resources"></a>
#### 🔵 Intermediate-Level Resources

Advanced materials for learners familiar with digital logic and basic architecture.

<!-- Keep this sorted alphabetically =) -->
| Resource  | Author(s) | Description | Access | Date Added |
|---|---|---|---|---|
| **Computer Architecture: A Quantitative Approach (6th Edition)** | David Patterson, John Hennessy | Advanced topics including ILP and GPU architectures, using RISC-V. | [Amazon](https://a.co/d/fuvp97D) | 2024-10-01 |
| **Computer Organization & Design (RISC-V Edition)** | David Patterson, John Hennessy | In-depth study of RISC-V ISA and processor implementation. | [Amazon](https://www.amazon.com/Computer-Organization-Design-RISC-V-Architecture/dp/0128203315) | 2024-10-01 |
| **Guide to Computer Processor Architecture** | Bernard Goossens | Open-access book that builds RISC-V processors, from a simple pipeline to multicore, with high-level synthesis. | [Springer (open access)](https://link.springer.com/book/10.1007/978-3-031-18023-1) | 2026-10-11 |
| **HaDes-V** | Tobias Scheipel | The Instruction Guide and code template (OER) for microcontroller design using the HaDes-V RISC-V-based processor. | [GitHub](https://github.com/tscheipel/HaDes-V/) · [Instruction Guide](https://repository.tugraz.at/oer/nytm4-grv34) | 2024-12-18 |
| **learn-FPGA episode II: pipelining** | Bruno Levy | Extends the basic RISC-V softcore from episode I with pipelining and performance optimizations. | [GitHub](https://github.com/BrunoLevy/learn-fpga/blob/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/PIPELINE.md) | 2024-10-01 |
| **Learn with SHAKTI** | Shakti – RISE Lab, IITM | Tutorials on RISC-V assembly programming using the RISC-V toolchain. | [Learn with Shakti](https://shakti.org.in/learn_with_shakti/intro.html) | 2023-12-21 |
| **LinuxFoundationX: RISC-V Toolchain and Compiler Optimization Techniques** | Aditya Kumar | RISC-V toolchain internals and compiler optimizations. | [edX course](https://www.edx.org/learn/computer-programming/the-linux-foundation-risc-v-toolchain-and-compiler-optimization-techniques) | 2024-10-01 |
| **MIT 6.1810: Operating System Engineering** | MIT PDOS | The standard operating systems course on RISC-V: read and extend xv6, a small Unix for RV64, through a series of labs. | [Course site](https://pdos.csail.mit.edu/6.1810/) · [xv6-riscv](https://github.com/mit-pdos/xv6-riscv) | 2026-10-11 |
| **Porting Software to RISC-V (LFD114)** | Linux Foundation | Moving and optimizing software across instruction sets, operating systems and firmware onto RISC-V platforms. | [Course](https://training.linuxfoundation.org/training/porting-software-to-risc-v-lfd114) | 2026-10-11 |
| **rCore Tutorial** | rCore OS community | Build an operating system for RISC-V in Rust, step by step, from bare metal to processes and file systems. | [Book (Chinese)](https://rcore-os.cn/rCore-Tutorial-Book-v3/) · [GitHub](https://github.com/rcore-os/rCore-Tutorial-Book-v3) | 2026-10-11 |
| **RISC-V Optimization Guide** | RISE Project | Actionable optimization recommendations for RISC-V software developers. | [GitLab](https://gitlab.com/riseproject/riscv-optimization-guide) | 2024-02-19 |
| **RISC-V System-on-Chip Design** | David Harris, James Stine, Sarah Harris, Rose Thompson | Designing a complete, Linux-capable RISC-V SoC, using the open CORE-V Wally core as the worked example. | [Elsevier](https://shop.elsevier.com/books/risc-v-system-on-chip-design/harris/978-0-323-99498-9) · [CORE-V Wally](https://github.com/openhwgroup/cvw) | 2026-10-11 |
| **RISC-V Vector Primer** | Tran, Thang Minh and Miller, Paul and McLeod, Jonah | A structured, open technical primer explaining the RISC‑V Vector Extension, with examples, diagrams, and chapter‑based documentation. | [GitHub](https://github.com/simplex-micro/riscv-vector-primer) | 2026-02-07 |
| **RV64GC Linker from Scratch in Go** | Yang Liu, PLCT Lab | Build an RV64GC linker from scratch in Go. | [GitHub](https://github.com/ksco/rvld) · [Course videos (Chinese)](https://space.bilibili.com/296494084/channel/collectiondetail?sid=857032) | 2024-04-24 |
| **RVfpga (Extended): Understanding Computer Architecture** | Sarah Harris, Daniel Chaver-Martinez | Updated RVfpga course with FPGA and simulation tools. | [RVfpga v3.0 downloads](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) | 2024-06-02 |
| **RVfpga: Computer Architecture with an Industrial RISC-V Core** | Sarah Harris, Daniel Chaver-Martinez | Hands-on learning with a commercial RISC-V SoC on FPGAs. | [edX course](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core) | 2024-10-01 |
| **Teaching experiences with RVfpga** | ARTECS Group, Complutense University of Madrid | How RVfpga and the Ripes simulator were used in two UCM courses. | [GitHub](https://github.com/artecs-group/RVfpga-sim-addons) | 2024-10-18 |
| **Tutorial: basic_RV32s** | [T410N](https://github.com/T410N) | A systematic microarchitectural roadmap for learning RISC-V processor design from scratch. | [basic_RV32s](https://github.com/RISC-KC/basic_rv32s) | 2024-07-25 |
| **Tutorial: RISC-V Vector Extension Demystified** | Thang Tran | In-depth introduction to the RISC-V vector extension. | [YouTube](https://youtu.be/oTaOd8qr53U) | 2024-10-01 |

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="specifications-and-reference"></a>
### 📐 Specifications and Reference

The specifications beyond the ISA manual that software and hardware developers reach for. The ratified ones are on [docs.riscv.org](https://docs.riscv.org/).

<!-- Keep this sorted alphabetically =) -->
| Specification | Description | Access |
|---|---|---|
| **Advanced Interrupt Architecture (AIA)** | Interrupt controllers (APLIC, IMSIC) and message-signaled interrupts for RISC-V systems. | [docs.riscv.org](https://docs.riscv.org/reference/aia/) |
| **Assembly Programmer's Manual** | Assembler syntax, directives, pseudo-instructions and relocations. | [GitHub](https://github.com/riscv-non-isa/riscv-asm-manual) |
| **Boot and Runtime Services (BRS)** | Firmware requirements (UEFI, ACPI, SBI) for booting standard operating systems. | [docs.riscv.org](https://docs.riscv.org/reference/brs/) |
| **C API** | Preprocessor macros, function attributes and builtins that C compilers provide for RISC-V. | [GitHub](https://github.com/riscv-non-isa/riscv-c-api-doc) |
| **Debug Specification** | External debug support: the debug module, triggers and the JTAG transport. | [docs.riscv.org](https://docs.riscv.org/reference/debug/) |
| **ELF psABI** | Calling convention, register usage, data layout and ELF format: what compilers, linkers and loaders agree on. | [docs.riscv.org](https://docs.riscv.org/reference/abi/) |
| **IOMMU** | Address translation and protection for devices doing DMA. | [docs.riscv.org](https://docs.riscv.org/reference/iommu/) |
| **Platform-Level Interrupt Controller (PLIC)** | The classic external interrupt controller found on most RISC-V boards. | [docs.riscv.org](https://docs.riscv.org/reference/plic/) |
| **Semihosting** | How code on a target uses the debugger host for I/O, which is handy on bare metal. | [docs.riscv.org](https://docs.riscv.org/reference/semihosting/) |
| **Supervisor Binary Interface (SBI)** | The interface between an OS kernel and machine-mode firmware such as OpenSBI. | [docs.riscv.org](https://docs.riscv.org/reference/sbi/) |
| **Vector C Intrinsics** | The C intrinsics for programming the Vector extension directly. | [docs.riscv.org](https://docs.riscv.org/reference/vector-c-intrinsics/) |

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="software-and-tools"></a>
### 🛠️ Software and Tools

Tools to enhance understanding or visualize the RISC-V ISA.

<!-- Keep this sorted alphabetically =) -->
| Tool | Author(s) | Description | Access | Date Added |
|---|---|---|---|---|
| **ASM Editor** | specy | ASM Editor is a Webapp IDE to write, run, debug and learn RISC-V (64 and 32) assembly. | [Website](https://asm-editor.specy.app/) | 2026-09-14 |
| **Compiler Explorer** | Matt Godbolt | Online compiler explorer supporting GCC/LLVM for RV64. | [Website](https://godbolt.org/) | 2024-10-18 |
| **CREATOR** | Diego Camarmas Alonso, Félix García Carballeira, Alejandro Calderón Mateos, Elías del Pozo Puñal | Didactic simulator for RISC-V assembly programs. | [Website](https://creatorsim.github.io/creator/) | 2023-12-20 |
| **emulsiV** | Guillaume Savaton | Visual simulator for a minimal 32-bit RISC processor. | [Website](https://eseo-tech.github.io/emulsiV/) | 2023-12-20 |
| **Go RISC-V Emulator** | Lucas Teske | A Go implementation of RV32I+M that can run Doom. | [GitHub](https://github.com/racerxdl/riscv-emulator) | 2024-10-18 |
| **Online RISC-V Assembler** | Lucas Teske | Online RISC-V assembler using GNU assembler in WebAssembly. | [Website](https://riscvasm.lucasteske.dev/), [GitHub](https://github.com/racerxdl/riscv-online-asm) | 2024-10-18 |
| **Piscado** | Gustavo N. Martins | RISC-V simulator written in Python during Twitch live coding. | [GitHub](https://github.com/gustavonmartins/piscado) | 2024-10-18 |
| **QEMU** | QEMU project | Full-system and user-mode emulator; boots Linux and other OSes on emulated RISC-V machines. | [Documentation](https://www.qemu.org/docs/master/system/target-riscv.html) | 2026-10-11 |
| **QtRvSim** | CTU Prague | RISC-V simulator with cache and pipeline visualization. | [GitHub](https://github.com/cvut/qtrvsim/) | 2023-12-20 |
| **RARS** | Benjamin Landers | RISC-V Assembler and Runtime Simulator, an IDE for writing and stepping through assembly (RV32/RV64 IMFD). | [GitHub](https://github.com/TheThirdOne/rars) | 2026-10-11 |
| **Renode** | Antmicro | Simulation framework for running unmodified embedded software on simulated RISC-V boards and SoCs. | [Website](https://renode.io/) | 2026-10-11 |
| **Ripes** | Morten Borup Petersen | Graphical processor simulator and assembly editor that shows single-cycle and pipelined RISC-V datapaths and caches. | [GitHub](https://github.com/mortbopet/Ripes) | 2026-10-11 |
| **Risco-5S** | Julio Nunes Avelar | RISC-V simulator with RV32IM, built during a few days off. | [GitHub](https://github.com/JN513/Risco-5S) | 2023-11-04 |
| **RISC-V ALE** | Antonio Guimarães | RISC-V Assembly Learning Environment. | [Website](https://riscv-programming.org/ale/) | 2024-10-18 |
| **RISC-V Instruction Encoder/Decoder** | LupLab | Online tool for encoding/decoding RISC-V instructions. | [Website](https://luplab.gitlab.io/rvcodecjs/) | 2023-12-20 |
| **RVV Intrinsics Viewer** | dzaima | Documentation for RISC-V vector extension intrinsics. | [Website](https://dzaima.github.io/intrinsics-viewer/) | 2023-12-20 |
| **Spike** | RISC-V International | The reference RISC-V ISA simulator, used to check implementations and to try new extensions. | [GitHub](https://github.com/riscv-software-src/riscv-isa-sim) | 2026-10-11 |
| **Venus** | Keyhan Vakil | Browser-based RISC-V simulator built for teaching; the version used in Berkeley CS61C. | [Website](https://venus.cs61c.org/) · [GitHub](https://github.com/kvakil/venus) | 2026-10-11 |
| **WebRISC-V** | Roberto Giorgi, Gianfranco Mariotti | Web-based graphical simulation with pipeline visualization for RV32IM/RV64IM. | [GitHub](https://github.com/Mariotti94/WebRISC-V/) | 2025-08-14 |

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="software-ecosystem-and-porting"></a>
### 📦 Software Ecosystem and Porting

Toolchains, operating systems and projects for building and running software on RISC-V.

<!-- Keep this sorted alphabetically =) -->
| Resource | Maintainer | Description | Access | Date Added |
|---|---|---|---|---|
| **Debian RISC-V port** | Debian | Status, installation images and porting notes for Debian on riscv64. | [Wiki](https://wiki.debian.org/RISC-V) | 2026-10-11 |
| **Fedora RISC-V** | Fedora | Fedora on RISC-V: images, supported boards and how to help. | [Wiki](https://fedoraproject.org/wiki/Architectures/RISC-V) | 2026-10-11 |
| **FreeRTOS on RISC-V** | FreeRTOS | Running the FreeRTOS kernel on RISC-V microcontrollers. | [Documentation](https://www.freertos.org/Using-FreeRTOS-on-RISC-V.html) | 2026-10-11 |
| **LLVM RISC-V User Guide** | LLVM project | Which extensions and profiles Clang and LLVM support, and how to target them. | [Documentation](https://llvm.org/docs/RISCVUsage.html) | 2026-10-11 |
| **RISC-V GNU Toolchain** | RISC-V collaboration | Build GCC, binutils, glibc/newlib and GDB cross-compilers for RISC-V. | [GitHub](https://github.com/riscv-collab/riscv-gnu-toolchain) | 2026-10-11 |
| **RISC-V Software Ecosystem Dashboard** | RISC-V International | Where RISC-V support stands across key open-source projects. | [Dashboard](https://riscv.github.io/adm-riscv-software-ecosystem/) | 2026-10-11 |
| **RISE Project** | RISE | Industry project accelerating RISC-V support in compilers, kernels, runtimes and distributions. | [Website](https://riseproject.dev/) | 2026-10-11 |
| **Ubuntu for RISC-V** | Canonical | Ubuntu images for RISC-V boards and QEMU. | [Download](https://ubuntu.com/download/risc-v) | 2026-10-11 |
| **Zephyr on RISC-V** | Zephyr Project | The Zephyr RTOS on RISC-V: supported features and boards. | [Documentation](https://docs.zephyrproject.org/latest/hardware/arch/risc-v.html) | 2026-10-11 |

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="open-risc-v-implementations"></a>
### 🧩 Open RISC-V Implementations

Explore open RISC-V implementations for hands-on learning.

<!-- Keep this sorted alphabetically =) -->
| Name | Description | Access | Date Added |
|---|---|---|---|
| **AUK-V-Aethia** | AUK-V RV32I CPU. | [GitHub](https://github.com/veeYceeY/AUK-V-Aethia) | 2024-10-18 |
| **BOOM** | Berkeley Out-of-Order Machine: a superscalar out-of-order RV64GC core in Chisel. | [GitHub](https://github.com/riscv-boom/riscv-boom) | 2026-10-11 |
| **Chipyard** | Framework for building full RISC-V SoCs (Rocket, BOOM and accelerators) through simulation, FPGA and tape-out. | [GitHub](https://github.com/ucb-bar/chipyard) | 2026-10-11 |
| **CORE-V Wally** | Configurable RV32/RV64 5-stage core in SystemVerilog that boots Linux; the companion to *RISC-V System-on-Chip Design*. | [GitHub](https://github.com/openhwgroup/cvw) | 2026-10-11 |
| **CV32E40P** | In-order 4-stage RISC-V RV32IMFCXpulp CPU based on RI5CY (PULP-Platform). | [GitHub](https://github.com/openhwgroup/cv32e40p) | 2024-10-18 |
| **CVA6** | CORE-V CVA6, an application-class 6-stage RISC-V CPU capable of booting Linux. | [GitHub](https://github.com/openhwgroup/cva6) | 2024-10-18 |
| **DarkRISCV** | Small RV32-E/I soft-core CPU optimized for FPGAs. | [GitHub](https://github.com/darklife/darkriscv) | 2024-10-18 |
| **Didactic-RISC-V** | Didactic RV32I Zmmul Zicsr implementation with 3-stage pipeline, in Logisim Evolution and SystemVerilog. | [GitHub](https://github.com/Diogo-Valadares/Didactic-RISC-V/) | 2026-03-24 |
| **Entropic R32-P5** | 5-stage pipelined RV32I CPU in Verilog with dynamic branch prediction (64-entry BTB), verified with cocotb, taped out on SKY130 with OpenLane2 and synthesized for FPGA. | [GitHub](https://github.com/Entropify/Entropic_R32-P5_RISC-V) | 2026-10-11 |
| **Grande Risco-5** | RV32I multi-cycle processor with a 5-stage pipeline for education. | [GitHub](https://github.com/JN513/Grande-Risco-5) | 2024-11-06 |
| **Hazard3** | 3-stage RV32IMACZb* processor with debug. | [GitHub](https://github.com/Wren6991/Hazard3) | 2024-12-19 |
| **Ibex** | Small, production-quality RV32 core in SystemVerilog from lowRISC, used in OpenTitan. | [GitHub](https://github.com/lowRISC/ibex) | 2026-10-11 |
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
| **RISCV-CPU** | 6-stage pipelined RV32IM+Zicsr+Zifencei processor in SystemVerilog on Xilinx Zynq-7020 FPGA, with branch prediction (BHT/BTB/RAS), hardware multiplier/divider, UART subsystem, and full hazard handling. 263.7 CoreMark / 91.0 DMIPS at 100 MHz. | [GitHub](https://github.com/gws8820/RISCV-CPU) | 2026-03-24 |
| **RISC-V Steel** | RV32I + Zicsr + Machine mode. | [GitHub](https://github.com/riscv-steel/riscv-steel) | 2024-10-18 |
| **Riskow** | Toy RV32-E from scratch during livestreams; runs on low-cost FPGAs. | [GitHub](https://github.com/racerxdl/riskow) | 2024-10-18 |
| **Rocket Chip** | SoC generator for the in-order Rocket RV64 core, written in Chisel. | [GitHub](https://github.com/chipsalliance/rocket-chip) | 2026-10-11 |
| **RPU** | Basic RISC-V CPU in VHDL. | [GitHub](https://github.com/Domipheus/RPU) | 2024-10-18 |
| **RSD** | RISC-V out-of-order superscalar processor. | [GitHub](https://github.com/rsd-devel/rsd) | 2024-10-18 |
| **SARV** | synthesizable in-order RV32 Verilog core | [GitHub](https://github.com/Sarst04/SARV) | 2026-07-30 |
| **SERV** | The SErial RISC-V CPU. | [GitHub](https://github.com/olofk/serv) | 2024-10-18 |
| **SGDH-RVSoC** | Tiny 32-bit RISC-V rv32acim CPU capable of running Linux on FPGA and in simulation. | [GitHub](https://github.com/semisgdh/SGDH-RVSoC) | 2025-10-08 |
| **TinyRiscv** | Very simple and easy-to-understand RISC-V core. | [GitHub](https://github.com/liangkangnan/tinyriscv) | 2024-10-18 |
| **VestaRV** | RV32IMACZb* synthesizable mixed-signal MCU SoC for ASIC and FPGA. Includes HDL sources, User Guide, RISC-V ISA verification suite, and simulation instructions. Fabricated and silicon-verified as the 'Myshkin' ASIC (TSMC 65nm, Nov 2025). | [GitHub](https://github.com/maxxseminario/VestaRV) | 2026-03-24 |
| **VexRiscv** | FPGA-friendly 32-bit RISC-V CPU (SpinalHDL). | [GitHub](https://github.com/SpinalHDL/VexRiscv) | 2024-10-18 |
| **XiangShan** | High-performance out-of-order RV64 processor in Chisel, developed in the open. | [GitHub](https://github.com/OpenXiangShan/XiangShan) | 2026-10-11 |

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="verification-and-compliance"></a>
### ✅ Verification and Compliance

How to check that a core really implements RISC-V correctly.

<!-- Keep this sorted alphabetically =) -->
| Resource | Maintainer | Description | Access | Date Added |
|---|---|---|---|---|
| **CORE-V-VERIF** | OpenHW Foundation | Industrial UVM verification environments for the CORE-V cores. | [GitHub](https://github.com/openhwgroup/core-v-verif) | 2026-10-11 |
| **RISC-V Architectural Tests** | RISC-V International | The official architectural tests that check an implementation against the specification. | [GitHub](https://github.com/riscv-non-isa/riscv-arch-test) | 2026-10-11 |
| **RISCOF** | RISC-V International | Framework that runs the architectural tests on your core and compares the results with a reference model. | [GitHub](https://github.com/riscv-software-src/riscof) | 2026-10-11 |
| **riscv-dv** | CHIPS Alliance | Random instruction generator for stress-testing RISC-V processors. | [GitHub](https://github.com/chipsalliance/riscv-dv) | 2026-10-11 |
| **riscv-tests** | RISC-V International | Small self-checking unit tests per instruction, a good first test suite for a student core. | [GitHub](https://github.com/riscv-software-src/riscv-tests) | 2026-10-11 |
| **Sail RISC-V Model** | RISC-V International | The formal, executable specification of the ISA, written in Sail. | [GitHub](https://github.com/riscv/sail-riscv) | 2026-10-11 |

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="available-risc-v-boards-development-kits-tablets-and-laptops"></a>
### 💻 Available RISC-V Boards, Development Kits, Tablets, and Laptops

<a id="32-bit-hardware"></a>
#### 🟢 32-bit Hardware

Popular hardware with RV32 based processors.

<!-- Keep this sorted alphabetically =) -->
| Board or Dev Kit | Company | SoC | RISC-V Core | Frequency | Date Added |
|---|---|---|---|---|---|
| [**CH32V003 Devkit**](https://www.aliexpress.com/item/1005004895791296.html) | WCH | CH32V003 | Single-core QingKe V2A | 48 MHz | 2025-07-25 |
| [**Dabao Evaluation Board**](https://www.crowdsupply.com/baochip/dabao) | Baochip | Baochip-1x | Single-core VexRiscv RV32-IMAC | 350 MHz | 2026-04-13 |
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

Popular hardware with RV64 based processors.

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

<sub>[↑ Back to top](#find-resources)</sub>

---

<a id="articles-and-presentations"></a>
### 📄 Articles and Presentations

<!-- Keep this sorted alphabetically =) -->
| Resource | Author(s) | Description | Access |
|---|---|---|---|
| **32-Bit RISC-V CPU Core on Logisim** | Siddesh D. Patil et al. | Beginner-friendly walkthrough of building a 32-bit RISC-V CPU core in the Logisim digital-logic simulator. | [arXiv](https://arxiv.org/abs/2312.01455) |
| **An Educational RISC-V-Based 16-Bit Processor** | Jecel Mattos de Assumpção, Oswaldo Hideo Ando, Hugo Puertas de Araújo, Mario Gazziro | Peer-reviewed paper (MDPI Chips, 2024) describing a simplified 16-bit processor based on the RISC-V ISA, developed as a teaching platform for computer architecture and digital design. | [Article](https://www.mdpi.com/2674-0729/3/4/20) · [DOI](https://doi.org/10.3390/chips3040020) |
| **A RISC-V SystemC-TLM Simulator** | Màrius Montón | Introduction to modeling a RISC-V system using SystemC and Transaction-Level Modeling. | [arXiv](https://arxiv.org/abs/2010.10119) |
| **A Survey on RISC-V Security: Hardware and Architecture** | Tao Lu | Survey of security research across RISC-V hardware and architecture. | [arXiv](https://arxiv.org/abs/2107.04175) |
| **Croc: An End-to-End Open-Source Extensible RISC-V MCU Platform to Democratize Silicon** | Philippe Sauter et al. | A complete open-source RISC-V microcontroller platform and design flow, from RTL toward tapeout. | [arXiv](https://arxiv.org/abs/2502.05090) |
| **Design of the RISC-V Instruction Set Architecture** | Andrew Waterman | PhD dissertation on the structure of the RISC-V ISA. | [PDF](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-1.pdf) |
| **Enabling Heterogeneous, Multicore SoC Research with RISC-V and ESP** | Joseph Zuckerman et al. | Hands-on platform for building heterogeneous multicore RISC-V systems-on-chip with ESP. | [arXiv](https://arxiv.org/abs/2206.01901) |
| **FREESS: A Web-Based Educational Simulator for a RISC-V-Inspired Superscalar Processor** | Roberto Giorgi et al. | Browser-based simulator that teaches superscalar execution on a RISC-V-inspired processor. | [arXiv](https://arxiv.org/abs/2605.30377) |
| **Is RISC-V the Future?** | Roddy Urquhart | Examination of RISC-V’s future potential. | [Article](https://semiengineering.com/is-risc-v-the-future) |
| **Past, Present and Future of RISC-V** | Krste Asanović | Overview of RISC-V’s evolution. | [YouTube](https://www.youtube.com/watch?v=RrVRMFjYti0) |
| **PERI: A Posit Enabled RISC-V Core** | Sugandha Tiwari et al. | Extends a RISC-V core with posit arithmetic; a good advanced ISA-extension study. | [arXiv](https://arxiv.org/abs/1908.01466) |
| **Return-Oriented Programming in RISC-V** | Garrett Gu et al. | Security case study demonstrating return-oriented programming on RISC-V. | [arXiv](https://arxiv.org/abs/2007.14995) |
| **RISC-V for HPC: Where We Are and Where We Need to Go** | Nick Brown | Accessible overview of the state of RISC-V for high-performance computing. | [arXiv](https://arxiv.org/abs/2406.12398) |
| **WebRISC-V: A 64-bit RISC-V Pipeline Simulator for Computer Architecture Classes** | Roberto Giorgi et al. | Browser-based 64-bit RISC-V pipeline simulator designed for computer-architecture courses. | [arXiv](https://arxiv.org/abs/2504.03722) |
| **x264 SAD Optimization with RISC-V Vector** | Fernando Mendoza V., Thomas Kolman | Optimizing the Sum of Absolute Differences (SAD) function in x264 using the RISC-V Vector 1.0 extension for the RVA23 profile, achieving up to 4x speedup over scalar C code. | [PDF](articles/x264-SAD-Optimization-with-RISC-V-Vector.pdf) |

> 🔎 Explore more RISC-V research on [arXiv](https://arxiv.org/search/?query=RISC-V&searchtype=all).

<sub>[↑ Back to top](#find-resources)</sub>


---

<a id="community"></a>
## 🤝 Community

| Where | What | Access |
|---|---|---|
| **Academia and Training SIG** | RISC-V International's group for educators and students: course material, curricula and training. | [Mailing list](https://lists.riscv.org/g/sig-academia-training) |
| **Ambassadors and Advocates** | Community members who teach, speak and help others get started with RISC-V. | [riscv.org](https://riscv.org/developers/ambassadors-advocates/) |
| **Mailing lists** | Public RISC-V International lists, including technical groups and announcements. | [lists.riscv.org](https://lists.riscv.org/) |
| **RISC-V International on YouTube** | Summit talks, webinars and technical presentations. | [YouTube](https://www.youtube.com/@RISCVInternational) |

<sub>[↑ Back to top](#find-resources)</sub>
