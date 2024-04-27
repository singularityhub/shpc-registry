---
layout: container
name:  "quay.io/biocontainers/smartmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smartmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smartmap/container.yaml"
updated_at: "2024-04-27 02:44:00.031814"
latest: "1.0.0--hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/smartmap"
aliases:
 - "SmartMap"
 - "SmartMapPrep"
 - "SmartMapRNAPrep"
 - "extract_exons.py"
 - "extract_splice_sites.py"
 - "hisat2"
 - "hisat2-align-l"
 - "hisat2-align-s"
 - "hisat2-build"
 - "hisat2-build-l"
 - "hisat2-build-s"
 - "hisat2-inspect"
 - "hisat2-inspect-l"
 - "hisat2-inspect-s"
 - "hisat2_extract_exons.py"
 - "hisat2_extract_snps_haplotypes_UCSC.py"
 - "hisat2_extract_snps_haplotypes_VCF.py"
 - "hisat2_extract_splice_sites.py"
 - "hisat2_read_statistics.py"
 - "hisat2_simulate_reads.py"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
 - "fasta-sanitize.pl"
versions:
 - "1.0.0--hd03093a_2"
 - "1.0.0--hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for smartmap"
config: {"url": "https://biocontainers.pro/tools/smartmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smartmap", "latest": {"1.0.0--hdcf5f25_3": "sha256:1d2e90ecb69447900dbd85a34ba6c56905e14aca059ad48c5494da7d384f1837"}, "tags": {"1.0.0--hd03093a_2": "sha256:0b02eb2278c16528f05dea773b489bb7ba9b72becf42db11e437e44e8e68a201", "1.0.0--hdcf5f25_3": "sha256:1d2e90ecb69447900dbd85a34ba6c56905e14aca059ad48c5494da7d384f1837"}, "docker": "quay.io/biocontainers/smartmap", "aliases": {"SmartMap": "/usr/local/bin/SmartMap", "SmartMapPrep": "/usr/local/bin/SmartMapPrep", "SmartMapRNAPrep": "/usr/local/bin/SmartMapRNAPrep", "extract_exons.py": "/usr/local/bin/extract_exons.py", "extract_splice_sites.py": "/usr/local/bin/extract_splice_sites.py", "hisat2": "/usr/local/bin/hisat2", "hisat2-align-l": "/usr/local/bin/hisat2-align-l", "hisat2-align-s": "/usr/local/bin/hisat2-align-s", "hisat2-build": "/usr/local/bin/hisat2-build", "hisat2-build-l": "/usr/local/bin/hisat2-build-l", "hisat2-build-s": "/usr/local/bin/hisat2-build-s", "hisat2-inspect": "/usr/local/bin/hisat2-inspect", "hisat2-inspect-l": "/usr/local/bin/hisat2-inspect-l", "hisat2-inspect-s": "/usr/local/bin/hisat2-inspect-s", "hisat2_extract_exons.py": "/usr/local/bin/hisat2_extract_exons.py", "hisat2_extract_snps_haplotypes_UCSC.py": "/usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py", "hisat2_extract_snps_haplotypes_VCF.py": "/usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py", "hisat2_extract_splice_sites.py": "/usr/local/bin/hisat2_extract_splice_sites.py", "hisat2_read_statistics.py": "/usr/local/bin/hisat2_read_statistics.py", "hisat2_simulate_reads.py": "/usr/local/bin/hisat2_simulate_reads.py", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smartmap.
shpc-registry automated BioContainers addition for smartmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smartmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smartmap:1.0.0--hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smartmap/1.0.0--hdcf5f25_3
$ module help quay.io/biocontainers/smartmap/1.0.0--hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smartmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smartmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smartmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smartmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smartmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smartmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SmartMap

```bash
$ singularity exec <container> /usr/local/bin/SmartMap
$ podman run --it --rm --entrypoint /usr/local/bin/SmartMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SmartMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SmartMapPrep

```bash
$ singularity exec <container> /usr/local/bin/SmartMapPrep
$ podman run --it --rm --entrypoint /usr/local/bin/SmartMapPrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SmartMapPrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SmartMapRNAPrep

```bash
$ singularity exec <container> /usr/local/bin/SmartMapRNAPrep
$ podman run --it --rm --entrypoint /usr/local/bin/SmartMapRNAPrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SmartMapRNAPrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_exons.py

```bash
$ singularity exec <container> /usr/local/bin/extract_exons.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_splice_sites.py

```bash
$ singularity exec <container> /usr/local/bin/extract_splice_sites.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2

```bash
$ singularity exec <container> /usr/local/bin/hisat2
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect

```bash
$ singularity exec <container> /usr/local/bin/hisat2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/hisat2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/hisat2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_exons.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_exons.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_snps_haplotypes_UCSC.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_UCSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_snps_haplotypes_VCF.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_snps_haplotypes_VCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_splice_sites.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_extract_splice_sites.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_read_statistics.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_read_statistics.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/hisat2_simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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