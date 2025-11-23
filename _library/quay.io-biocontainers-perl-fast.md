---
layout: container
name:  "quay.io/biocontainers/perl-fast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-fast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-fast/container.yaml"
updated_at: "2025-11-23 03:59:05.578781"
latest: "1.06--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-fast"
aliases:
 - "alncut"
 - "alnpi"
 - "fascodon"
 - "fascomp"
 - "fasconvert"
 - "fascut"
 - "fasfilter"
 - "fasgrep"
 - "fashead"
 - "faslen"
 - "faspaste"
 - "fasrc"
 - "fassort"
 - "fassub"
 - "fastail"
 - "fastax"
 - "fastaxsort"
 - "fastr"
 - "fasuniq"
 - "faswc"
 - "fasxl"
 - "gbfalncut"
 - "gbfcut"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.06--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-fast"
config: {"url": "https://biocontainers.pro/tools/perl-fast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-fast", "latest": {"1.06--pl5321hdfd78af_2": "sha256:a70f6b76df634023945351362d020147151d1add9e4fbd7309596928f20f1577"}, "tags": {"1.06--pl5321hdfd78af_2": "sha256:a70f6b76df634023945351362d020147151d1add9e4fbd7309596928f20f1577"}, "docker": "quay.io/biocontainers/perl-fast", "aliases": {"alncut": "/usr/local/bin/alncut", "alnpi": "/usr/local/bin/alnpi", "fascodon": "/usr/local/bin/fascodon", "fascomp": "/usr/local/bin/fascomp", "fasconvert": "/usr/local/bin/fasconvert", "fascut": "/usr/local/bin/fascut", "fasfilter": "/usr/local/bin/fasfilter", "fasgrep": "/usr/local/bin/fasgrep", "fashead": "/usr/local/bin/fashead", "faslen": "/usr/local/bin/faslen", "faspaste": "/usr/local/bin/faspaste", "fasrc": "/usr/local/bin/fasrc", "fassort": "/usr/local/bin/fassort", "fassub": "/usr/local/bin/fassub", "fastail": "/usr/local/bin/fastail", "fastax": "/usr/local/bin/fastax", "fastaxsort": "/usr/local/bin/fastaxsort", "fastr": "/usr/local/bin/fastr", "fasuniq": "/usr/local/bin/fasuniq", "faswc": "/usr/local/bin/faswc", "fasxl": "/usr/local/bin/fasxl", "gbfalncut": "/usr/local/bin/gbfalncut", "gbfcut": "/usr/local/bin/gbfcut", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-fast.
shpc-registry automated BioContainers addition for perl-fast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-fast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-fast:1.06--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-fast/1.06--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-fast/1.06--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-fast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-fast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-fast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-fast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-fast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-fast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alncut

```bash
$ singularity exec <container> /usr/local/bin/alncut
$ podman run --it --rm --entrypoint /usr/local/bin/alncut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alncut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alnpi

```bash
$ singularity exec <container> /usr/local/bin/alnpi
$ podman run --it --rm --entrypoint /usr/local/bin/alnpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alnpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fascodon

```bash
$ singularity exec <container> /usr/local/bin/fascodon
$ podman run --it --rm --entrypoint /usr/local/bin/fascodon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fascodon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fascomp

```bash
$ singularity exec <container> /usr/local/bin/fascomp
$ podman run --it --rm --entrypoint /usr/local/bin/fascomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fascomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasconvert

```bash
$ singularity exec <container> /usr/local/bin/fasconvert
$ podman run --it --rm --entrypoint /usr/local/bin/fasconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fascut

```bash
$ singularity exec <container> /usr/local/bin/fascut
$ podman run --it --rm --entrypoint /usr/local/bin/fascut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fascut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasfilter

```bash
$ singularity exec <container> /usr/local/bin/fasfilter
$ podman run --it --rm --entrypoint /usr/local/bin/fasfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasgrep

```bash
$ singularity exec <container> /usr/local/bin/fasgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fasgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fashead

```bash
$ singularity exec <container> /usr/local/bin/fashead
$ podman run --it --rm --entrypoint /usr/local/bin/fashead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fashead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faslen

```bash
$ singularity exec <container> /usr/local/bin/faslen
$ podman run --it --rm --entrypoint /usr/local/bin/faslen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faslen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faspaste

```bash
$ singularity exec <container> /usr/local/bin/faspaste
$ podman run --it --rm --entrypoint /usr/local/bin/faspaste   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faspaste   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasrc

```bash
$ singularity exec <container> /usr/local/bin/fasrc
$ podman run --it --rm --entrypoint /usr/local/bin/fasrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasrc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fassort

```bash
$ singularity exec <container> /usr/local/bin/fassort
$ podman run --it --rm --entrypoint /usr/local/bin/fassort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fassort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fassub

```bash
$ singularity exec <container> /usr/local/bin/fassub
$ podman run --it --rm --entrypoint /usr/local/bin/fassub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fassub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastail

```bash
$ singularity exec <container> /usr/local/bin/fastail
$ podman run --it --rm --entrypoint /usr/local/bin/fastail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastax

```bash
$ singularity exec <container> /usr/local/bin/fastax
$ podman run --it --rm --entrypoint /usr/local/bin/fastax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastax   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaxsort

```bash
$ singularity exec <container> /usr/local/bin/fastaxsort
$ podman run --it --rm --entrypoint /usr/local/bin/fastaxsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaxsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastr

```bash
$ singularity exec <container> /usr/local/bin/fastr
$ podman run --it --rm --entrypoint /usr/local/bin/fastr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasuniq

```bash
$ singularity exec <container> /usr/local/bin/fasuniq
$ podman run --it --rm --entrypoint /usr/local/bin/fasuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faswc

```bash
$ singularity exec <container> /usr/local/bin/faswc
$ podman run --it --rm --entrypoint /usr/local/bin/faswc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faswc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasxl

```bash
$ singularity exec <container> /usr/local/bin/fasxl
$ podman run --it --rm --entrypoint /usr/local/bin/fasxl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasxl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbfalncut

```bash
$ singularity exec <container> /usr/local/bin/gbfalncut
$ podman run --it --rm --entrypoint /usr/local/bin/gbfalncut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbfalncut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbfcut

```bash
$ singularity exec <container> /usr/local/bin/gbfcut
$ podman run --it --rm --entrypoint /usr/local/bin/gbfcut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbfcut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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