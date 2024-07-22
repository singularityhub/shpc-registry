---
layout: container
name:  "quay.io/biocontainers/dragonflye"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dragonflye/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dragonflye/container.yaml"
updated_at: "2024-07-22 02:49:09.938686"
latest: "1.2.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/dragonflye"
aliases:
 - "assembly-scan"
 - "check_compression"
 - "compress_fast5"
 - "demux_fast5"
 - "dragonflye"
 - "fast5_subset"
 - "flye"
 - "flye-minimap2"
 - "flye-modules"
 - "flye-samtools"
 - "hdf2tf.py"
 - "medaka"
 - "medaka_consensus"
 - "medaka_counts"
 - "medaka_data_path"
 - "medaka_haploid_variant"
 - "medaka_version_report"
 - "mini_align"
 - "miniasm"
 - "minidot"
 - "multi_to_single_fast5"
 - "nanoq"
 - "porechop"
 - "rasusa"
 - "raven"
 - "single_to_multi_fast5"
 - "whatshap"
 - "fastp"
 - "pilon"
 - "minimap2.py"
 - "samclip"
 - "any2fasta"
 - "kmc"
 - "kmc_dump"
 - "kmc_tools"
 - "racon"
 - "rampler"
versions:
 - "1.0.9--hdfd78af_0"
 - "1.0.13--hdfd78af_0"
 - "1.0.14--hdfd78af_0"
 - "1.1.0--hdfd78af_0"
 - "1.1.1--hdfd78af_0"
 - "1.1.2--hdfd78af_0"
 - "1.2.0--hdfd78af_0"
 - "1.2.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for dragonflye"
config: {"url": "https://biocontainers.pro/tools/dragonflye", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dragonflye", "latest": {"1.2.1--hdfd78af_0": "sha256:b0a68f02ebd1e3b150d64553f8572966846ff105b595412c3d6b20d69998d294"}, "tags": {"1.0.9--hdfd78af_0": "sha256:3ee956287ddd0abcc4db884b12cbdec1c1233de50304468e6677c8d0b28659aa", "1.0.13--hdfd78af_0": "sha256:ccd80cb057e8003ae7ddbbf9c00189ccded4b30ad7b57980e2c9abcf96ad7fd6", "1.0.14--hdfd78af_0": "sha256:c04524b05166dd1587b4bda1bc11e9479c23a223f77bc467501157efea21fe09", "1.1.0--hdfd78af_0": "sha256:d698e110c4590c10d9dc21c955dfad00d4a1a5c55242394ea439f8f5821fa04b", "1.1.1--hdfd78af_0": "sha256:169cb709b4bde4d7e06192bbab466d77e987b92aa2ccc59cdb8eb2dbe2b6ed86", "1.1.2--hdfd78af_0": "sha256:ad1a180d2b5433e295ac160fba4a5a3d717367d91c0b085c646a46a2166dcdea", "1.2.0--hdfd78af_0": "sha256:7c4b1d85397e6ee8ca8fb426cbf182558588ceac84843536aee6f19143f4dfd7", "1.2.1--hdfd78af_0": "sha256:b0a68f02ebd1e3b150d64553f8572966846ff105b595412c3d6b20d69998d294"}, "docker": "quay.io/biocontainers/dragonflye", "aliases": {"assembly-scan": "/usr/local/bin/assembly-scan", "check_compression": "/usr/local/bin/check_compression", "compress_fast5": "/usr/local/bin/compress_fast5", "demux_fast5": "/usr/local/bin/demux_fast5", "dragonflye": "/usr/local/bin/dragonflye", "fast5_subset": "/usr/local/bin/fast5_subset", "flye": "/usr/local/bin/flye", "flye-minimap2": "/usr/local/bin/flye-minimap2", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "hdf2tf.py": "/usr/local/bin/hdf2tf.py", "medaka": "/usr/local/bin/medaka", "medaka_consensus": "/usr/local/bin/medaka_consensus", "medaka_counts": "/usr/local/bin/medaka_counts", "medaka_data_path": "/usr/local/bin/medaka_data_path", "medaka_haploid_variant": "/usr/local/bin/medaka_haploid_variant", "medaka_version_report": "/usr/local/bin/medaka_version_report", "mini_align": "/usr/local/bin/mini_align", "miniasm": "/usr/local/bin/miniasm", "minidot": "/usr/local/bin/minidot", "multi_to_single_fast5": "/usr/local/bin/multi_to_single_fast5", "nanoq": "/usr/local/bin/nanoq", "porechop": "/usr/local/bin/porechop", "rasusa": "/usr/local/bin/rasusa", "raven": "/usr/local/bin/raven", "single_to_multi_fast5": "/usr/local/bin/single_to_multi_fast5", "whatshap": "/usr/local/bin/whatshap", "fastp": "/usr/local/bin/fastp", "pilon": "/usr/local/bin/pilon", "minimap2.py": "/usr/local/bin/minimap2.py", "samclip": "/usr/local/bin/samclip", "any2fasta": "/usr/local/bin/any2fasta", "kmc": "/usr/local/bin/kmc", "kmc_dump": "/usr/local/bin/kmc_dump", "kmc_tools": "/usr/local/bin/kmc_tools", "racon": "/usr/local/bin/racon", "rampler": "/usr/local/bin/rampler"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dragonflye.
shpc-registry automated BioContainers addition for dragonflye
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dragonflye
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dragonflye:1.2.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dragonflye/1.2.1--hdfd78af_0
$ module help quay.io/biocontainers/dragonflye/1.2.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dragonflye-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dragonflye-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dragonflye-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dragonflye-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dragonflye-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dragonflye-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assembly-scan

```bash
$ singularity exec <container> /usr/local/bin/assembly-scan
$ podman run --it --rm --entrypoint /usr/local/bin/assembly-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assembly-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_compression

```bash
$ singularity exec <container> /usr/local/bin/check_compression
$ podman run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress_fast5

```bash
$ singularity exec <container> /usr/local/bin/compress_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demux_fast5

```bash
$ singularity exec <container> /usr/local/bin/demux_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dragonflye

```bash
$ singularity exec <container> /usr/local/bin/dragonflye
$ podman run --it --rm --entrypoint /usr/local/bin/dragonflye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dragonflye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast5_subset

```bash
$ singularity exec <container> /usr/local/bin/fast5_subset
$ podman run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye

```bash
$ singularity exec <container> /usr/local/bin/flye
$ podman run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-minimap2

```bash
$ singularity exec <container> /usr/local/bin/flye-minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2tf.py

```bash
$ singularity exec <container> /usr/local/bin/hdf2tf.py
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka

```bash
$ singularity exec <container> /usr/local/bin/medaka
$ podman run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_consensus

```bash
$ singularity exec <container> /usr/local/bin/medaka_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_counts

```bash
$ singularity exec <container> /usr/local/bin/medaka_counts
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_data_path

```bash
$ singularity exec <container> /usr/local/bin/medaka_data_path
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_haploid_variant

```bash
$ singularity exec <container> /usr/local/bin/medaka_haploid_variant
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_version_report

```bash
$ singularity exec <container> /usr/local/bin/medaka_version_report
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mini_align

```bash
$ singularity exec <container> /usr/local/bin/mini_align
$ podman run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniasm

```bash
$ singularity exec <container> /usr/local/bin/miniasm
$ podman run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minidot

```bash
$ singularity exec <container> /usr/local/bin/minidot
$ podman run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi_to_single_fast5

```bash
$ singularity exec <container> /usr/local/bin/multi_to_single_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanoq

```bash
$ singularity exec <container> /usr/local/bin/nanoq
$ podman run --it --rm --entrypoint /usr/local/bin/nanoq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanoq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### porechop

```bash
$ singularity exec <container> /usr/local/bin/porechop
$ podman run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rasusa

```bash
$ singularity exec <container> /usr/local/bin/rasusa
$ podman run --it --rm --entrypoint /usr/local/bin/rasusa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rasusa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raven

```bash
$ singularity exec <container> /usr/local/bin/raven
$ podman run --it --rm --entrypoint /usr/local/bin/raven   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raven   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_to_multi_fast5

```bash
$ singularity exec <container> /usr/local/bin/single_to_multi_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whatshap

```bash
$ singularity exec <container> /usr/local/bin/whatshap
$ podman run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilon

```bash
$ singularity exec <container> /usr/local/bin/pilon
$ podman run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samclip

```bash
$ singularity exec <container> /usr/local/bin/samclip
$ podman run --it --rm --entrypoint /usr/local/bin/samclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_dump

```bash
$ singularity exec <container> /usr/local/bin/kmc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rampler

```bash
$ singularity exec <container> /usr/local/bin/rampler
$ podman run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
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