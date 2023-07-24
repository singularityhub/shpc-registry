---
layout: container
name:  "quay.io/biocontainers/relocate2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/relocate2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/relocate2/container.yaml"
updated_at: "2023-07-24 05:22:32.376915"
latest: "2.0.1--hdfd78af_6"
container_url: "https://biocontainers.pro/tools/relocate2"
aliases:
 - "characterizer.pl"
 - "clean_false_positive.py"
 - "clean_pairs_memory.py"
 - "faToNib"
 - "fastq_split.pl"
 - "gfClient"
 - "gfServer"
 - "nibFrag"
 - "pslPretty"
 - "pslReps"
 - "pslSort"
 - "relocaTE2.py"
 - "relocaTE2_temp.py"
 - "relocaTE_absenceFinder.py"
 - "relocaTE_align.py"
 - "relocaTE_insertionFinder.py"
 - "relocaTE_trim.py"
 - "utility.py"
 - "varfilter.py"
 - "twoBitToFa"
 - "blat"
 - "twoBitInfo"
 - "faToTwoBit"
 - "seqtk"
 - "perl5.32.0"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
versions:
 - "2.0.1--hdfd78af_6"
description: "shpc-registry automated BioContainers addition for relocate2"
config: {"url": "https://biocontainers.pro/tools/relocate2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for relocate2", "latest": {"2.0.1--hdfd78af_6": "sha256:900d3dd35c324f03f328839ce134df937a9f5b0b4b122cbc4cd431eb66c7e109"}, "tags": {"2.0.1--hdfd78af_6": "sha256:900d3dd35c324f03f328839ce134df937a9f5b0b4b122cbc4cd431eb66c7e109"}, "docker": "quay.io/biocontainers/relocate2", "aliases": {"characterizer.pl": "/usr/local/bin/characterizer.pl", "clean_false_positive.py": "/usr/local/bin/clean_false_positive.py", "clean_pairs_memory.py": "/usr/local/bin/clean_pairs_memory.py", "faToNib": "/usr/local/bin/faToNib", "fastq_split.pl": "/usr/local/bin/fastq_split.pl", "gfClient": "/usr/local/bin/gfClient", "gfServer": "/usr/local/bin/gfServer", "nibFrag": "/usr/local/bin/nibFrag", "pslPretty": "/usr/local/bin/pslPretty", "pslReps": "/usr/local/bin/pslReps", "pslSort": "/usr/local/bin/pslSort", "relocaTE2.py": "/usr/local/bin/relocaTE2.py", "relocaTE2_temp.py": "/usr/local/bin/relocaTE2_temp.py", "relocaTE_absenceFinder.py": "/usr/local/bin/relocaTE_absenceFinder.py", "relocaTE_align.py": "/usr/local/bin/relocaTE_align.py", "relocaTE_insertionFinder.py": "/usr/local/bin/relocaTE_insertionFinder.py", "relocaTE_trim.py": "/usr/local/bin/relocaTE_trim.py", "utility.py": "/usr/local/bin/utility.py", "varfilter.py": "/usr/local/bin/varfilter.py", "twoBitToFa": "/usr/local/bin/twoBitToFa", "blat": "/usr/local/bin/blat", "twoBitInfo": "/usr/local/bin/twoBitInfo", "faToTwoBit": "/usr/local/bin/faToTwoBit", "seqtk": "/usr/local/bin/seqtk", "perl5.32.0": "/usr/local/bin/perl5.32.0", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/relocate2.
shpc-registry automated BioContainers addition for relocate2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/relocate2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/relocate2:2.0.1--hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/relocate2/2.0.1--hdfd78af_6
$ module help quay.io/biocontainers/relocate2/2.0.1--hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### relocate2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### relocate2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### relocate2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### relocate2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### relocate2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### relocate2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### characterizer.pl

```bash
$ singularity exec <container> /usr/local/bin/characterizer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/characterizer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/characterizer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clean_false_positive.py

```bash
$ singularity exec <container> /usr/local/bin/clean_false_positive.py
$ podman run --it --rm --entrypoint /usr/local/bin/clean_false_positive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clean_false_positive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clean_pairs_memory.py

```bash
$ singularity exec <container> /usr/local/bin/clean_pairs_memory.py
$ podman run --it --rm --entrypoint /usr/local/bin/clean_pairs_memory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clean_pairs_memory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToNib

```bash
$ singularity exec <container> /usr/local/bin/faToNib
$ podman run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_split.pl

```bash
$ singularity exec <container> /usr/local/bin/fastq_split.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_split.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_split.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfClient

```bash
$ singularity exec <container> /usr/local/bin/gfClient
$ podman run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nibFrag

```bash
$ singularity exec <container> /usr/local/bin/nibFrag
$ podman run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslPretty

```bash
$ singularity exec <container> /usr/local/bin/pslPretty
$ podman run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslReps

```bash
$ singularity exec <container> /usr/local/bin/pslReps
$ podman run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslSort

```bash
$ singularity exec <container> /usr/local/bin/pslSort
$ podman run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### relocaTE2.py

```bash
$ singularity exec <container> /usr/local/bin/relocaTE2.py
$ podman run --it --rm --entrypoint /usr/local/bin/relocaTE2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/relocaTE2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### relocaTE2_temp.py

```bash
$ singularity exec <container> /usr/local/bin/relocaTE2_temp.py
$ podman run --it --rm --entrypoint /usr/local/bin/relocaTE2_temp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/relocaTE2_temp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### relocaTE_absenceFinder.py

```bash
$ singularity exec <container> /usr/local/bin/relocaTE_absenceFinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/relocaTE_absenceFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/relocaTE_absenceFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### relocaTE_align.py

```bash
$ singularity exec <container> /usr/local/bin/relocaTE_align.py
$ podman run --it --rm --entrypoint /usr/local/bin/relocaTE_align.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/relocaTE_align.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### relocaTE_insertionFinder.py

```bash
$ singularity exec <container> /usr/local/bin/relocaTE_insertionFinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/relocaTE_insertionFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/relocaTE_insertionFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### relocaTE_trim.py

```bash
$ singularity exec <container> /usr/local/bin/relocaTE_trim.py
$ podman run --it --rm --entrypoint /usr/local/bin/relocaTE_trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/relocaTE_trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### utility.py

```bash
$ singularity exec <container> /usr/local/bin/utility.py
$ podman run --it --rm --entrypoint /usr/local/bin/utility.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/utility.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varfilter.py

```bash
$ singularity exec <container> /usr/local/bin/varfilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blat

```bash
$ singularity exec <container> /usr/local/bin/blat
$ podman run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitInfo

```bash
$ singularity exec <container> /usr/local/bin/twoBitInfo
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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