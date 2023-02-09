---
layout: container
name:  "quay.io/biocontainers/kinsimriboswitch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kinsimriboswitch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kinsimriboswitch/container.yaml"
updated_at: "2023-02-09 02:56:35.037295"
latest: "0.3--pl5262r40ha325a96_3"
container_url: "https://biocontainers.pro/tools/kinsimriboswitch"
aliases:
 - "addr2line"
 - "ar"
 - "as"
 - "barriers-RNA2"
 - "c++"
 - "c++filt"
 - "cc"
 - "cpp"
 - "dwp"
 - "elfedit"
 - "f95"
 - "g++"
 - "gcc"
 - "gcc-ar"
 - "gcc-nm"
 - "gcc-ranlib"
 - "gcov"
 - "gcov-dump"
 - "gcov-tool"
 - "gfortran"
 - "gfortran.bin"
 - "gold"
 - "gprof"
 - "kinGenMacrostates"
 - "kinPlot.R"
 - "kinSimRibo_mergeRateMats"
 - "kinSimRiboswitch"
 - "ld"
 - "ld.bfd"
 - "ld.gold"
 - "nm"
 - "objcopy"
 - "objdump"
 - "qd-config"
 - "ranlib"
 - "readelf"
 - "size"
 - "stoch_genDimerRates"
 - "strings"
 - "strip"
 - "structConnect"
 - "treekin"
 - "tts"
 - "RNAdos"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
 - "RNA2Dfold"
versions:
 - "0.3--pl5262r40ha325a96_3"
description: "shpc-registry automated BioContainers addition for kinsimriboswitch"
config: {"url": "https://biocontainers.pro/tools/kinsimriboswitch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kinsimriboswitch", "latest": {"0.3--pl5262r40ha325a96_3": "sha256:8237010fd1a5beb3cf465f262e55ec60a05839c8281fde8a092b9685dcebe59a"}, "tags": {"0.3--pl5262r40ha325a96_3": "sha256:8237010fd1a5beb3cf465f262e55ec60a05839c8281fde8a092b9685dcebe59a"}, "docker": "quay.io/biocontainers/kinsimriboswitch", "aliases": {"addr2line": "/usr/local/bin/addr2line", "ar": "/usr/local/bin/ar", "as": "/usr/local/bin/as", "barriers-RNA2": "/usr/local/bin/barriers-RNA2", "c++": "/usr/local/bin/c++", "c++filt": "/usr/local/bin/c++filt", "cc": "/usr/local/bin/cc", "cpp": "/usr/local/bin/cpp", "dwp": "/usr/local/bin/dwp", "elfedit": "/usr/local/bin/elfedit", "f95": "/usr/local/bin/f95", "g++": "/usr/local/bin/g++", "gcc": "/usr/local/bin/gcc", "gcc-ar": "/usr/local/bin/gcc-ar", "gcc-nm": "/usr/local/bin/gcc-nm", "gcc-ranlib": "/usr/local/bin/gcc-ranlib", "gcov": "/usr/local/bin/gcov", "gcov-dump": "/usr/local/bin/gcov-dump", "gcov-tool": "/usr/local/bin/gcov-tool", "gfortran": "/usr/local/bin/gfortran", "gfortran.bin": "/usr/local/bin/gfortran.bin", "gold": "/usr/local/bin/gold", "gprof": "/usr/local/bin/gprof", "kinGenMacrostates": "/usr/local/bin/kinGenMacrostates", "kinPlot.R": "/usr/local/bin/kinPlot.R", "kinSimRibo_mergeRateMats": "/usr/local/bin/kinSimRibo_mergeRateMats", "kinSimRiboswitch": "/usr/local/bin/kinSimRiboswitch", "ld": "/usr/local/bin/ld", "ld.bfd": "/usr/local/bin/ld.bfd", "ld.gold": "/usr/local/bin/ld.gold", "nm": "/usr/local/bin/nm", "objcopy": "/usr/local/bin/objcopy", "objdump": "/usr/local/bin/objdump", "qd-config": "/usr/local/bin/qd-config", "ranlib": "/usr/local/bin/ranlib", "readelf": "/usr/local/bin/readelf", "size": "/usr/local/bin/size", "stoch_genDimerRates": "/usr/local/bin/stoch_genDimerRates", "strings": "/usr/local/bin/strings", "strip": "/usr/local/bin/strip", "structConnect": "/usr/local/bin/structConnect", "treekin": "/usr/local/bin/treekin", "tts": "/usr/local/bin/tts", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kinsimriboswitch.
shpc-registry automated BioContainers addition for kinsimriboswitch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kinsimriboswitch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kinsimriboswitch:0.3--pl5262r40ha325a96_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kinsimriboswitch/0.3--pl5262r40ha325a96_3
$ module help quay.io/biocontainers/kinsimriboswitch/0.3--pl5262r40ha325a96_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kinsimriboswitch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kinsimriboswitch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kinsimriboswitch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kinsimriboswitch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kinsimriboswitch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kinsimriboswitch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addr2line

```bash
$ singularity exec <container> /usr/local/bin/addr2line
$ podman run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ar

```bash
$ singularity exec <container> /usr/local/bin/ar
$ podman run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### as

```bash
$ singularity exec <container> /usr/local/bin/as
$ podman run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barriers-RNA2

```bash
$ singularity exec <container> /usr/local/bin/barriers-RNA2
$ podman run --it --rm --entrypoint /usr/local/bin/barriers-RNA2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barriers-RNA2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c++

```bash
$ singularity exec <container> /usr/local/bin/c++
$ podman run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c++filt

```bash
$ singularity exec <container> /usr/local/bin/c++filt
$ podman run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cc

```bash
$ singularity exec <container> /usr/local/bin/cc
$ podman run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpp

```bash
$ singularity exec <container> /usr/local/bin/cpp
$ podman run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwp

```bash
$ singularity exec <container> /usr/local/bin/dwp
$ podman run --it --rm --entrypoint /usr/local/bin/dwp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elfedit

```bash
$ singularity exec <container> /usr/local/bin/elfedit
$ podman run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f95

```bash
$ singularity exec <container> /usr/local/bin/f95
$ podman run --it --rm --entrypoint /usr/local/bin/f95   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f95   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g++

```bash
$ singularity exec <container> /usr/local/bin/g++
$ podman run --it --rm --entrypoint /usr/local/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc

```bash
$ singularity exec <container> /usr/local/bin/gcc
$ podman run --it --rm --entrypoint /usr/local/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ar

```bash
$ singularity exec <container> /usr/local/bin/gcc-ar
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-nm

```bash
$ singularity exec <container> /usr/local/bin/gcc-nm
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ranlib

```bash
$ singularity exec <container> /usr/local/bin/gcc-ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov

```bash
$ singularity exec <container> /usr/local/bin/gcov
$ podman run --it --rm --entrypoint /usr/local/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-dump

```bash
$ singularity exec <container> /usr/local/bin/gcov-dump
$ podman run --it --rm --entrypoint /usr/local/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-tool

```bash
$ singularity exec <container> /usr/local/bin/gcov-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfortran

```bash
$ singularity exec <container> /usr/local/bin/gfortran
$ podman run --it --rm --entrypoint /usr/local/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gold

```bash
$ singularity exec <container> /usr/local/bin/gold
$ podman run --it --rm --entrypoint /usr/local/bin/gold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gprof

```bash
$ singularity exec <container> /usr/local/bin/gprof
$ podman run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinGenMacrostates

```bash
$ singularity exec <container> /usr/local/bin/kinGenMacrostates
$ podman run --it --rm --entrypoint /usr/local/bin/kinGenMacrostates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinGenMacrostates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinPlot.R

```bash
$ singularity exec <container> /usr/local/bin/kinPlot.R
$ podman run --it --rm --entrypoint /usr/local/bin/kinPlot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinPlot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinSimRibo_mergeRateMats

```bash
$ singularity exec <container> /usr/local/bin/kinSimRibo_mergeRateMats
$ podman run --it --rm --entrypoint /usr/local/bin/kinSimRibo_mergeRateMats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinSimRibo_mergeRateMats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinSimRiboswitch

```bash
$ singularity exec <container> /usr/local/bin/kinSimRiboswitch
$ podman run --it --rm --entrypoint /usr/local/bin/kinSimRiboswitch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinSimRiboswitch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld

```bash
$ singularity exec <container> /usr/local/bin/ld
$ podman run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld.bfd

```bash
$ singularity exec <container> /usr/local/bin/ld.bfd
$ podman run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld.gold

```bash
$ singularity exec <container> /usr/local/bin/ld.gold
$ podman run --it --rm --entrypoint /usr/local/bin/ld.gold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld.gold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nm

```bash
$ singularity exec <container> /usr/local/bin/nm
$ podman run --it --rm --entrypoint /usr/local/bin/nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### objcopy

```bash
$ singularity exec <container> /usr/local/bin/objcopy
$ podman run --it --rm --entrypoint /usr/local/bin/objcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/objcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### objdump

```bash
$ singularity exec <container> /usr/local/bin/objdump
$ podman run --it --rm --entrypoint /usr/local/bin/objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qd-config

```bash
$ singularity exec <container> /usr/local/bin/qd-config
$ podman run --it --rm --entrypoint /usr/local/bin/qd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ranlib

```bash
$ singularity exec <container> /usr/local/bin/ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readelf

```bash
$ singularity exec <container> /usr/local/bin/readelf
$ podman run --it --rm --entrypoint /usr/local/bin/readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### size

```bash
$ singularity exec <container> /usr/local/bin/size
$ podman run --it --rm --entrypoint /usr/local/bin/size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stoch_genDimerRates

```bash
$ singularity exec <container> /usr/local/bin/stoch_genDimerRates
$ podman run --it --rm --entrypoint /usr/local/bin/stoch_genDimerRates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stoch_genDimerRates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strings

```bash
$ singularity exec <container> /usr/local/bin/strings
$ podman run --it --rm --entrypoint /usr/local/bin/strings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip

```bash
$ singularity exec <container> /usr/local/bin/strip
$ podman run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### structConnect

```bash
$ singularity exec <container> /usr/local/bin/structConnect
$ podman run --it --rm --entrypoint /usr/local/bin/structConnect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/structConnect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treekin

```bash
$ singularity exec <container> /usr/local/bin/treekin
$ podman run --it --rm --entrypoint /usr/local/bin/treekin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treekin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tts

```bash
$ singularity exec <container> /usr/local/bin/tts
$ podman run --it --rm --entrypoint /usr/local/bin/tts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### popt

```bash
$ singularity exec <container> /usr/local/bin/popt
$ podman run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)