---
layout: container
name:  "quay.io/biocontainers/rdptools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rdptools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rdptools/container.yaml"
updated_at: "2025-09-29 04:43:13.012896"
latest: "2.0.3--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/rdptools"
aliases:
 - "AbundanceStats"
 - "AlignmentTools"
 - "Clustering"
 - "FrameBot"
 - "KmerFilter"
 - "ProbeMatch"
 - "ReadSeq"
 - "SeqFilters"
 - "SequenceMatch"
 - "classifier"
 - "hmmgs"
 - "clhsdb"
 - "hsdb"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
versions:
 - "2.0.3--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for rdptools"
config: {"url": "https://biocontainers.pro/tools/rdptools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rdptools", "latest": {"2.0.3--hdfd78af_1": "sha256:51d6fc5c033c4a7713b92e343c91589884999b1851f046784f4fd5098381c803"}, "tags": {"2.0.3--hdfd78af_1": "sha256:51d6fc5c033c4a7713b92e343c91589884999b1851f046784f4fd5098381c803"}, "docker": "quay.io/biocontainers/rdptools", "aliases": {"AbundanceStats": "/usr/local/bin/AbundanceStats", "AlignmentTools": "/usr/local/bin/AlignmentTools", "Clustering": "/usr/local/bin/Clustering", "FrameBot": "/usr/local/bin/FrameBot", "KmerFilter": "/usr/local/bin/KmerFilter", "ProbeMatch": "/usr/local/bin/ProbeMatch", "ReadSeq": "/usr/local/bin/ReadSeq", "SeqFilters": "/usr/local/bin/SeqFilters", "SequenceMatch": "/usr/local/bin/SequenceMatch", "classifier": "/usr/local/bin/classifier", "hmmgs": "/usr/local/bin/hmmgs", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rdptools.
shpc-registry automated BioContainers addition for rdptools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rdptools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rdptools:2.0.3--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rdptools/2.0.3--hdfd78af_1
$ module help quay.io/biocontainers/rdptools/2.0.3--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rdptools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rdptools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rdptools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rdptools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rdptools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rdptools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AbundanceStats

```bash
$ singularity exec <container> /usr/local/bin/AbundanceStats
$ podman run --it --rm --entrypoint /usr/local/bin/AbundanceStats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AbundanceStats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AlignmentTools

```bash
$ singularity exec <container> /usr/local/bin/AlignmentTools
$ podman run --it --rm --entrypoint /usr/local/bin/AlignmentTools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AlignmentTools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Clustering

```bash
$ singularity exec <container> /usr/local/bin/Clustering
$ podman run --it --rm --entrypoint /usr/local/bin/Clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FrameBot

```bash
$ singularity exec <container> /usr/local/bin/FrameBot
$ podman run --it --rm --entrypoint /usr/local/bin/FrameBot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FrameBot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerFilter

```bash
$ singularity exec <container> /usr/local/bin/KmerFilter
$ podman run --it --rm --entrypoint /usr/local/bin/KmerFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ProbeMatch

```bash
$ singularity exec <container> /usr/local/bin/ProbeMatch
$ podman run --it --rm --entrypoint /usr/local/bin/ProbeMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProbeMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ReadSeq

```bash
$ singularity exec <container> /usr/local/bin/ReadSeq
$ podman run --it --rm --entrypoint /usr/local/bin/ReadSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ReadSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SeqFilters

```bash
$ singularity exec <container> /usr/local/bin/SeqFilters
$ podman run --it --rm --entrypoint /usr/local/bin/SeqFilters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SeqFilters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SequenceMatch

```bash
$ singularity exec <container> /usr/local/bin/SequenceMatch
$ podman run --it --rm --entrypoint /usr/local/bin/SequenceMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SequenceMatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classifier

```bash
$ singularity exec <container> /usr/local/bin/classifier
$ podman run --it --rm --entrypoint /usr/local/bin/classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmgs

```bash
$ singularity exec <container> /usr/local/bin/hmmgs
$ podman run --it --rm --entrypoint /usr/local/bin/hmmgs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmgs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### native2ascii

```bash
$ singularity exec <container> /usr/local/bin/native2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### policytool

```bash
$ singularity exec <container> /usr/local/bin/policytool
$ podman run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
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