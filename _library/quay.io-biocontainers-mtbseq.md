---
layout: container
name:  "quay.io/biocontainers/mtbseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mtbseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mtbseq/container.yaml"
updated_at: "2024-03-21 02:26:08.046556"
latest: "1.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mtbseq"
aliases:
 - "GenomeAnalysisTK"
 - "MTBseq"
 - "gatk3"
 - "picard"
 - "clhsdb"
 - "hsdb"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
versions:
 - "1.0.4--hdfd78af_2"
 - "1.1.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for mtbseq"
config: {"url": "https://biocontainers.pro/tools/mtbseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mtbseq", "latest": {"1.1.0--hdfd78af_0": "sha256:c8fa7c7d24d007574cc88532ea0a8d028528a9d25682aebb2e73abfe7a2f36db"}, "tags": {"1.0.4--hdfd78af_2": "sha256:e043bc02993a7022b69f2710842108a8e3cfd87e136b252677d3e59821dd9948", "1.1.0--hdfd78af_0": "sha256:c8fa7c7d24d007574cc88532ea0a8d028528a9d25682aebb2e73abfe7a2f36db"}, "docker": "quay.io/biocontainers/mtbseq", "aliases": {"GenomeAnalysisTK": "/usr/local/bin/GenomeAnalysisTK", "MTBseq": "/usr/local/bin/MTBseq", "gatk3": "/usr/local/bin/gatk3", "picard": "/usr/local/bin/picard", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mtbseq.
shpc-registry automated BioContainers addition for mtbseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mtbseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mtbseq:1.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mtbseq/1.1.0--hdfd78af_0
$ module help quay.io/biocontainers/mtbseq/1.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mtbseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mtbseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mtbseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mtbseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mtbseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mtbseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GenomeAnalysisTK

```bash
$ singularity exec <container> /usr/local/bin/GenomeAnalysisTK
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MTBseq

```bash
$ singularity exec <container> /usr/local/bin/MTBseq
$ podman run --it --rm --entrypoint /usr/local/bin/MTBseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MTBseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk3

```bash
$ singularity exec <container> /usr/local/bin/gatk3
$ podman run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
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