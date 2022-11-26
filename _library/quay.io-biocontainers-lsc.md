---
layout: container
name:  "quay.io/biocontainers/lsc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lsc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lsc/container.yaml"
updated_at: "2022-11-25 23:40:53.265252"
latest: "2.0--2"
container_url: "https://biocontainers.pro/tools/lsc"
aliases:
 - "AlignmentBasics.py"
 - "CorrectFromMapBasics.py"
 - "FileBasics.py"
 - "NavToMapBasics.py"
 - "SamToNavBasics.py"
 - "SequenceBasics.py"
 - "SequenceCompressionBasics.py"
 - "explode_fasta.pl"
 - "fasta_to_tsv.pl"
 - "fastq_to_tsv.pl"
 - "filter_corrected_reads.py"
 - "runLSC.py"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
 - "python2-config"
versions:
 - "2.0--2"
description: "shpc-registry automated BioContainers addition for lsc"
config: {"url": "https://biocontainers.pro/tools/lsc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lsc", "latest": {"2.0--2": "sha256:df78b2f0f3eaa400f7e7e7faa43de902f2995894c110b318cef0d38f8da248ab"}, "tags": {"2.0--2": "sha256:df78b2f0f3eaa400f7e7e7faa43de902f2995894c110b318cef0d38f8da248ab"}, "docker": "quay.io/biocontainers/lsc", "aliases": {"AlignmentBasics.py": "/usr/local/bin/AlignmentBasics.py", "CorrectFromMapBasics.py": "/usr/local/bin/CorrectFromMapBasics.py", "FileBasics.py": "/usr/local/bin/FileBasics.py", "NavToMapBasics.py": "/usr/local/bin/NavToMapBasics.py", "SamToNavBasics.py": "/usr/local/bin/SamToNavBasics.py", "SequenceBasics.py": "/usr/local/bin/SequenceBasics.py", "SequenceCompressionBasics.py": "/usr/local/bin/SequenceCompressionBasics.py", "explode_fasta.pl": "/usr/local/bin/explode_fasta.pl", "fasta_to_tsv.pl": "/usr/local/bin/fasta_to_tsv.pl", "fastq_to_tsv.pl": "/usr/local/bin/fastq_to_tsv.pl", "filter_corrected_reads.py": "/usr/local/bin/filter_corrected_reads.py", "runLSC.py": "/usr/local/bin/runLSC.py", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s", "python2-config": "/usr/local/bin/python2-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lsc.
shpc-registry automated BioContainers addition for lsc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lsc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lsc:2.0--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lsc/2.0--2
$ module help quay.io/biocontainers/lsc/2.0--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lsc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lsc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lsc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lsc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lsc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lsc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AlignmentBasics.py

```bash
$ singularity exec <container> /usr/local/bin/AlignmentBasics.py
$ podman run --it --rm --entrypoint /usr/local/bin/AlignmentBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AlignmentBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CorrectFromMapBasics.py

```bash
$ singularity exec <container> /usr/local/bin/CorrectFromMapBasics.py
$ podman run --it --rm --entrypoint /usr/local/bin/CorrectFromMapBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CorrectFromMapBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FileBasics.py

```bash
$ singularity exec <container> /usr/local/bin/FileBasics.py
$ podman run --it --rm --entrypoint /usr/local/bin/FileBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FileBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NavToMapBasics.py

```bash
$ singularity exec <container> /usr/local/bin/NavToMapBasics.py
$ podman run --it --rm --entrypoint /usr/local/bin/NavToMapBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NavToMapBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SamToNavBasics.py

```bash
$ singularity exec <container> /usr/local/bin/SamToNavBasics.py
$ podman run --it --rm --entrypoint /usr/local/bin/SamToNavBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SamToNavBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SequenceBasics.py

```bash
$ singularity exec <container> /usr/local/bin/SequenceBasics.py
$ podman run --it --rm --entrypoint /usr/local/bin/SequenceBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SequenceBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SequenceCompressionBasics.py

```bash
$ singularity exec <container> /usr/local/bin/SequenceCompressionBasics.py
$ podman run --it --rm --entrypoint /usr/local/bin/SequenceCompressionBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SequenceCompressionBasics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explode_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/explode_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/explode_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explode_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_to_tsv.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta_to_tsv.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_to_tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_to_tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_to_tsv.pl

```bash
$ singularity exec <container> /usr/local/bin/fastq_to_tsv.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_to_tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_to_tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_corrected_reads.py

```bash
$ singularity exec <container> /usr/local/bin/filter_corrected_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_corrected_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_corrected_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runLSC.py

```bash
$ singularity exec <container> /usr/local/bin/runLSC.py
$ podman run --it --rm --entrypoint /usr/local/bin/runLSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runLSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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