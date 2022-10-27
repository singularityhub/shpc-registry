---
layout: container
name:  "quay.io/biocontainers/bftools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bftools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bftools/container.yaml"
updated_at: "2022-10-27 00:35:24.775895"
latest: "6.7.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bftools"
aliases:
 - "bf.sh"
 - "bfconvert"
 - "bioformats_package.jar"
 - "config.sh"
 - "domainlist"
 - "formatlist"
 - "ijview"
 - "logback.xml"
 - "mkfake"
 - "showinf"
 - "xmlindent"
 - "xmlvalid"
versions:
 - "6.7.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bftools"
config: {"url": "https://biocontainers.pro/tools/bftools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bftools", "latest": {"6.7.0--hdfd78af_0": "sha256:4f7e54cd1366910cb03f41efec6e83373a50d2e17724f049e05deb87bcd86fba"}, "tags": {"6.7.0--hdfd78af_0": "sha256:4f7e54cd1366910cb03f41efec6e83373a50d2e17724f049e05deb87bcd86fba"}, "docker": "quay.io/biocontainers/bftools", "aliases": {"bf.sh": "/usr/local/bin/bf.sh", "bfconvert": "/usr/local/bin/bfconvert", "bioformats_package.jar": "/usr/local/bin/bioformats_package.jar", "config.sh": "/usr/local/bin/config.sh", "domainlist": "/usr/local/bin/domainlist", "formatlist": "/usr/local/bin/formatlist", "ijview": "/usr/local/bin/ijview", "logback.xml": "/usr/local/bin/logback.xml", "mkfake": "/usr/local/bin/mkfake", "showinf": "/usr/local/bin/showinf", "xmlindent": "/usr/local/bin/xmlindent", "xmlvalid": "/usr/local/bin/xmlvalid"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bftools.
shpc-registry automated BioContainers addition for bftools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bftools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bftools:6.7.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bftools/6.7.0--hdfd78af_0
$ module help quay.io/biocontainers/bftools/6.7.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bftools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bftools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bftools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bftools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bftools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bftools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bf.sh

```bash
$ singularity exec <container> /usr/local/bin/bf.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bfconvert

```bash
$ singularity exec <container> /usr/local/bin/bfconvert
$ podman run --it --rm --entrypoint /usr/local/bin/bfconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bfconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioformats_package.jar

```bash
$ singularity exec <container> /usr/local/bin/bioformats_package.jar
$ podman run --it --rm --entrypoint /usr/local/bin/bioformats_package.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioformats_package.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config.sh

```bash
$ singularity exec <container> /usr/local/bin/config.sh
$ podman run --it --rm --entrypoint /usr/local/bin/config.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### domainlist

```bash
$ singularity exec <container> /usr/local/bin/domainlist
$ podman run --it --rm --entrypoint /usr/local/bin/domainlist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/domainlist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatlist

```bash
$ singularity exec <container> /usr/local/bin/formatlist
$ podman run --it --rm --entrypoint /usr/local/bin/formatlist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatlist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ijview

```bash
$ singularity exec <container> /usr/local/bin/ijview
$ podman run --it --rm --entrypoint /usr/local/bin/ijview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ijview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### logback.xml

```bash
$ singularity exec <container> /usr/local/bin/logback.xml
$ podman run --it --rm --entrypoint /usr/local/bin/logback.xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/logback.xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkfake

```bash
$ singularity exec <container> /usr/local/bin/mkfake
$ podman run --it --rm --entrypoint /usr/local/bin/mkfake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkfake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### showinf

```bash
$ singularity exec <container> /usr/local/bin/showinf
$ podman run --it --rm --entrypoint /usr/local/bin/showinf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/showinf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlindent

```bash
$ singularity exec <container> /usr/local/bin/xmlindent
$ podman run --it --rm --entrypoint /usr/local/bin/xmlindent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlindent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlvalid

```bash
$ singularity exec <container> /usr/local/bin/xmlvalid
$ podman run --it --rm --entrypoint /usr/local/bin/xmlvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
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