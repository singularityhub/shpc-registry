---
layout: container
name:  "quay.io/biocontainers/crass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crass/container.yaml"
updated_at: "2024-04-25 02:33:59.389832"
latest: "1.0.1--h43eeafb_5"
container_url: "https://biocontainers.pro/tools/crass"
aliases:
 - "crass"
 - "crass-assembler"
 - "crisprtools"
 - "CreateDOMDocument"
 - "DOMCount"
 - "DOMPrint"
 - "EnumVal"
 - "MemParse"
 - "PParse"
 - "PSVIWriter"
 - "Redirect"
 - "SAX2Count"
 - "SAX2Print"
versions:
 - "1.0.1--h5b5514e_3"
 - "1.0.1--h43eeafb_5"
description: "shpc-registry automated BioContainers addition for crass"
config: {"url": "https://biocontainers.pro/tools/crass", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crass", "latest": {"1.0.1--h43eeafb_5": "sha256:73b1688d71dd97b2ea0fd00bc8e6b312d3f507ff5d7ebc63d162e9e612e9d2ef"}, "tags": {"1.0.1--h5b5514e_3": "sha256:62a56fe76ea875d720f6c57627c61769198ab2c479d22f0bf8f1f8b70fbe3632", "1.0.1--h43eeafb_5": "sha256:73b1688d71dd97b2ea0fd00bc8e6b312d3f507ff5d7ebc63d162e9e612e9d2ef"}, "docker": "quay.io/biocontainers/crass", "aliases": {"crass": "/usr/local/bin/crass", "crass-assembler": "/usr/local/bin/crass-assembler", "crisprtools": "/usr/local/bin/crisprtools", "CreateDOMDocument": "/usr/local/bin/CreateDOMDocument", "DOMCount": "/usr/local/bin/DOMCount", "DOMPrint": "/usr/local/bin/DOMPrint", "EnumVal": "/usr/local/bin/EnumVal", "MemParse": "/usr/local/bin/MemParse", "PParse": "/usr/local/bin/PParse", "PSVIWriter": "/usr/local/bin/PSVIWriter", "Redirect": "/usr/local/bin/Redirect", "SAX2Count": "/usr/local/bin/SAX2Count", "SAX2Print": "/usr/local/bin/SAX2Print"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crass.
shpc-registry automated BioContainers addition for crass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crass:1.0.1--h43eeafb_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crass/1.0.1--h43eeafb_5
$ module help quay.io/biocontainers/crass/1.0.1--h43eeafb_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crass

```bash
$ singularity exec <container> /usr/local/bin/crass
$ podman run --it --rm --entrypoint /usr/local/bin/crass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crass-assembler

```bash
$ singularity exec <container> /usr/local/bin/crass-assembler
$ podman run --it --rm --entrypoint /usr/local/bin/crass-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crass-assembler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crisprtools

```bash
$ singularity exec <container> /usr/local/bin/crisprtools
$ podman run --it --rm --entrypoint /usr/local/bin/crisprtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crisprtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateDOMDocument

```bash
$ singularity exec <container> /usr/local/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount

```bash
$ singularity exec <container> /usr/local/bin/DOMCount
$ podman run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint

```bash
$ singularity exec <container> /usr/local/bin/DOMPrint
$ podman run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal

```bash
$ singularity exec <container> /usr/local/bin/EnumVal
$ podman run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse

```bash
$ singularity exec <container> /usr/local/bin/MemParse
$ podman run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse

```bash
$ singularity exec <container> /usr/local/bin/PParse
$ podman run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter

```bash
$ singularity exec <container> /usr/local/bin/PSVIWriter
$ podman run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Redirect

```bash
$ singularity exec <container> /usr/local/bin/Redirect
$ podman run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Count

```bash
$ singularity exec <container> /usr/local/bin/SAX2Count
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Print

```bash
$ singularity exec <container> /usr/local/bin/SAX2Print
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
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