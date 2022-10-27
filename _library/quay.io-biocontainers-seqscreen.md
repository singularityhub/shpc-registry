---
layout: container
name:  "quay.io/biocontainers/seqscreen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqscreen/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/seqscreen/container.yaml"
updated_at: "2022-10-27 00:50:40.923779"
latest: "4.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/seqscreen"
aliases:
 - "centrifuge"
 - "centrifuge-BuildSharedSequence.pl"
 - "centrifuge-RemoveEmptySequence.pl"
 - "centrifuge-RemoveN.pl"
 - "centrifuge-build"
 - "centrifuge-build-bin"
 - "centrifuge-class"
 - "centrifuge-compress.pl"
 - "centrifuge-download"
 - "centrifuge-inspect"
 - "centrifuge-inspect-bin"
 - "centrifuge-kreport"
 - "centrifuge-sort-nt.pl"
 - "dataformat"
 - "datasets"
 - "gdrive"
 - "nextflow.bak"
 - "prerapsearch"
 - "rapsearch"
 - "seqscreen"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
versions:
 - "4.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for seqscreen"
config: {"url": "https://biocontainers.pro/tools/seqscreen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqscreen", "latest": {"4.0--hdfd78af_0": "sha256:8c2734117ced23268008bf5855894a922ca92a1b592e5857602c7db961f457e4"}, "tags": {"4.0--hdfd78af_0": "sha256:8c2734117ced23268008bf5855894a922ca92a1b592e5857602c7db961f457e4"}, "docker": "quay.io/biocontainers/seqscreen", "aliases": {"centrifuge": "/usr/local/bin/centrifuge", "centrifuge-BuildSharedSequence.pl": "/usr/local/bin/centrifuge-BuildSharedSequence.pl", "centrifuge-RemoveEmptySequence.pl": "/usr/local/bin/centrifuge-RemoveEmptySequence.pl", "centrifuge-RemoveN.pl": "/usr/local/bin/centrifuge-RemoveN.pl", "centrifuge-build": "/usr/local/bin/centrifuge-build", "centrifuge-build-bin": "/usr/local/bin/centrifuge-build-bin", "centrifuge-class": "/usr/local/bin/centrifuge-class", "centrifuge-compress.pl": "/usr/local/bin/centrifuge-compress.pl", "centrifuge-download": "/usr/local/bin/centrifuge-download", "centrifuge-inspect": "/usr/local/bin/centrifuge-inspect", "centrifuge-inspect-bin": "/usr/local/bin/centrifuge-inspect-bin", "centrifuge-kreport": "/usr/local/bin/centrifuge-kreport", "centrifuge-sort-nt.pl": "/usr/local/bin/centrifuge-sort-nt.pl", "dataformat": "/usr/local/bin/dataformat", "datasets": "/usr/local/bin/datasets", "gdrive": "/usr/local/bin/gdrive", "nextflow.bak": "/usr/local/bin/nextflow.bak", "prerapsearch": "/usr/local/bin/prerapsearch", "rapsearch": "/usr/local/bin/rapsearch", "seqscreen": "/usr/local/bin/seqscreen", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqscreen.
shpc-registry automated BioContainers addition for seqscreen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqscreen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqscreen:4.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqscreen/4.0--hdfd78af_0
$ module help quay.io/biocontainers/seqscreen/4.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqscreen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqscreen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqscreen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqscreen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqscreen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqscreen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centrifuge

```bash
$ singularity exec <container> /usr/local/bin/centrifuge
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-BuildSharedSequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-BuildSharedSequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveEmptySequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveEmptySequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveN.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveN.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-class

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-class
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-compress.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-compress.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-download

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-download
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-kreport

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-kreport
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-sort-nt.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-sort-nt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataformat

```bash
$ singularity exec <container> /usr/local/bin/dataformat
$ podman run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets

```bash
$ singularity exec <container> /usr/local/bin/datasets
$ podman run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdrive

```bash
$ singularity exec <container> /usr/local/bin/gdrive
$ podman run --it --rm --entrypoint /usr/local/bin/gdrive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdrive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow.bak

```bash
$ singularity exec <container> /usr/local/bin/nextflow.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerapsearch

```bash
$ singularity exec <container> /usr/local/bin/prerapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapsearch

```bash
$ singularity exec <container> /usr/local/bin/rapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqscreen

```bash
$ singularity exec <container> /usr/local/bin/seqscreen
$ podman run --it --rm --entrypoint /usr/local/bin/seqscreen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqscreen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-build

```bash
$ singularity exec <container> /usr/local/bin/sip-build
$ podman run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-distinfo

```bash
$ singularity exec <container> /usr/local/bin/sip-distinfo
$ podman run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-install

```bash
$ singularity exec <container> /usr/local/bin/sip-install
$ podman run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-module

```bash
$ singularity exec <container> /usr/local/bin/sip-module
$ podman run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-sdist

```bash
$ singularity exec <container> /usr/local/bin/sip-sdist
$ podman run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-wheel

```bash
$ singularity exec <container> /usr/local/bin/sip-wheel
$ podman run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
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