---
layout: container
name:  "quay.io/biocontainers/ultraplex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ultraplex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ultraplex/container.yaml"
updated_at: "2025-08-26 03:20:39.033036"
latest: "1.2.10--py39hbcbf7aa_0"
container_url: "https://biocontainers.pro/tools/ultraplex"
aliases:
 - "ultraplex"
 - "igzip"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "pigz"
 - "unpigz"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
versions:
 - "1.2.5--py38hbff2b2d_1"
 - "1.2.5--py38he5da3d1_2"
 - "1.2.9--py39hf95cd2a_0"
 - "1.2.9--py39hf95cd2a_1"
 - "1.2.9--py38he5da3d1_1"
 - "1.2.9--py39hff71179_2"
 - "1.2.9--py39hbcbf7aa_3"
 - "1.2.10--py39hbcbf7aa_0"
description: "shpc-registry automated BioContainers addition for ultraplex"
config: {"url": "https://biocontainers.pro/tools/ultraplex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ultraplex", "latest": {"1.2.10--py39hbcbf7aa_0": "sha256:c80685ca250cb7f9253a576a911017a8335a134b2c14c02f6470ad05f2cb7844"}, "tags": {"1.2.5--py38hbff2b2d_1": "sha256:ddbad5d727fc973a41af1ea912875d0d5dae098ced96529579f0f9d467b14ec6", "1.2.5--py38he5da3d1_2": "sha256:91534aea10a0522397d4484bb47300c79cb96ffe41aada57b7055ead51a8e08a", "1.2.9--py39hf95cd2a_0": "sha256:88d3f865faa1e5d6aa1e05b3225ecce809242dd126d66e7f2d68db086482942b", "1.2.9--py39hf95cd2a_1": "sha256:77f0cfcb4722107bf607726eed2379c4bbf81fff98cd1442801eb33f4a28efa7", "1.2.9--py38he5da3d1_1": "sha256:78c493b940bd7bfb2b24851210c189c2fae9fe8575df5a67cd20031b309657ca", "1.2.9--py39hff71179_2": "sha256:b67e3cbc9f72f71872b5dc994f3ff8319f10e0d673c6b40f1bf70598869a60f5", "1.2.9--py39hbcbf7aa_3": "sha256:90b4c9f8abc0ccbf20117ee503d39080c207524bb9cc23bb69d1014a0724393e", "1.2.10--py39hbcbf7aa_0": "sha256:c80685ca250cb7f9253a576a911017a8335a134b2c14c02f6470ad05f2cb7844"}, "docker": "quay.io/biocontainers/ultraplex", "aliases": {"ultraplex": "/usr/local/bin/ultraplex", "igzip": "/usr/local/bin/igzip", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ultraplex.
shpc-registry automated BioContainers addition for ultraplex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ultraplex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ultraplex:1.2.10--py39hbcbf7aa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ultraplex/1.2.10--py39hbcbf7aa_0
$ module help quay.io/biocontainers/ultraplex/1.2.10--py39hbcbf7aa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ultraplex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ultraplex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ultraplex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ultraplex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ultraplex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ultraplex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ultraplex

```bash
$ singularity exec <container> /usr/local/bin/ultraplex
$ podman run --it --rm --entrypoint /usr/local/bin/ultraplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ultraplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
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