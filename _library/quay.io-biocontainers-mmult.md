---
layout: container
name:  "quay.io/biocontainers/mmult"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmult/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmult/container.yaml"
updated_at: "2024-01-15 03:09:50.119382"
latest: "0.0.0.2--r40h8b68381_0"
container_url: "https://biocontainers.pro/tools/mmult"
aliases:
 - "bbglm"
 - "cpgcdifenrich"
 - "cpgcdifenrichhist.R"
 - "vmcvmrnme"
 - "cmpfillin"
 - "gpmetis"
 - "graphchk"
 - "m2gmetis"
 - "mpmetis"
 - "ndmetis"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
versions:
 - "0.0.0.2--r40h8b68381_0"
description: "shpc-registry automated BioContainers addition for mmult"
config: {"url": "https://biocontainers.pro/tools/mmult", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mmult", "latest": {"0.0.0.2--r40h8b68381_0": "sha256:c099eb09160108f3eefb9dabe039f978bb6f1b1fba9b87bf879875de28600601"}, "tags": {"0.0.0.2--r40h8b68381_0": "sha256:c099eb09160108f3eefb9dabe039f978bb6f1b1fba9b87bf879875de28600601"}, "docker": "quay.io/biocontainers/mmult", "aliases": {"bbglm": "/usr/local/bin/bbglm", "cpgcdifenrich": "/usr/local/bin/cpgcdifenrich", "cpgcdifenrichhist.R": "/usr/local/bin/cpgcdifenrichhist.R", "vmcvmrnme": "/usr/local/bin/vmcvmrnme", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk", "m2gmetis": "/usr/local/bin/m2gmetis", "mpmetis": "/usr/local/bin/mpmetis", "ndmetis": "/usr/local/bin/ndmetis", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmult.
shpc-registry automated BioContainers addition for mmult
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmult
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmult:0.0.0.2--r40h8b68381_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmult/0.0.0.2--r40h8b68381_0
$ module help quay.io/biocontainers/mmult/0.0.0.2--r40h8b68381_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmult-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmult-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmult-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmult-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmult-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmult-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bbglm

```bash
$ singularity exec <container> /usr/local/bin/bbglm
$ podman run --it --rm --entrypoint /usr/local/bin/bbglm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbglm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpgcdifenrich

```bash
$ singularity exec <container> /usr/local/bin/cpgcdifenrich
$ podman run --it --rm --entrypoint /usr/local/bin/cpgcdifenrich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpgcdifenrich   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpgcdifenrichhist.R

```bash
$ singularity exec <container> /usr/local/bin/cpgcdifenrichhist.R
$ podman run --it --rm --entrypoint /usr/local/bin/cpgcdifenrichhist.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpgcdifenrichhist.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmcvmrnme

```bash
$ singularity exec <container> /usr/local/bin/vmcvmrnme
$ podman run --it --rm --entrypoint /usr/local/bin/vmcvmrnme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmcvmrnme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m2gmetis

```bash
$ singularity exec <container> /usr/local/bin/m2gmetis
$ podman run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpmetis

```bash
$ singularity exec <container> /usr/local/bin/mpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndmetis

```bash
$ singularity exec <container> /usr/local/bin/ndmetis
$ podman run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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