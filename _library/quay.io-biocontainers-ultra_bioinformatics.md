---
layout: container
name:  "quay.io/biocontainers/ultra_bioinformatics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ultra_bioinformatics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ultra_bioinformatics/container.yaml"
updated_at: "2025-12-26 04:00:15.795704"
latest: "0.1--pyh7cba7a3_1"
container_url: "https://biocontainers.pro/tools/ultra_bioinformatics"
aliases:
 - "StrobeMap"
 - "edlib-aligner"
 - "slaMEM"
 - "uLTRA"
 - "gffutils-cli"
 - "activate-global-python-argcomplete"
 - "get_objgraph"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "undill"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
versions:
 - "0.0.4.1--pyh5e36f6f_0"
 - "0.0.4.2--pyh7cba7a3_0"
 - "0.1--pyh7cba7a3_0"
 - "0.1--pyh7cba7a3_1"
description: "shpc-registry automated BioContainers addition for ultra_bioinformatics"
config: {"url": "https://biocontainers.pro/tools/ultra_bioinformatics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ultra_bioinformatics", "latest": {"0.1--pyh7cba7a3_1": "sha256:2f3faeaf6bf862b5afc11dd8dceeb47bf3edf36c70eb1ef418df828889288fd1"}, "tags": {"0.0.4.1--pyh5e36f6f_0": "sha256:efe193ed72700788e40ed41cb75aaa1ec23be83438068eb052b2b5f37748ed51", "0.0.4.2--pyh7cba7a3_0": "sha256:dc72b7a871c02bf2631e46ea1444b336cd2480a34ab8460d165c81cffabc611a", "0.1--pyh7cba7a3_0": "sha256:4cd07fac26308161d0dd9c203818c8047e288fbcc6a8eb0e9f4836fa0dffa655", "0.1--pyh7cba7a3_1": "sha256:2f3faeaf6bf862b5afc11dd8dceeb47bf3edf36c70eb1ef418df828889288fd1"}, "docker": "quay.io/biocontainers/ultra_bioinformatics", "aliases": {"StrobeMap": "/usr/local/bin/StrobeMap", "edlib-aligner": "/usr/local/bin/edlib-aligner", "slaMEM": "/usr/local/bin/slaMEM", "uLTRA": "/usr/local/bin/uLTRA", "gffutils-cli": "/usr/local/bin/gffutils-cli", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "get_objgraph": "/usr/local/bin/get_objgraph", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "undill": "/usr/local/bin/undill", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ultra_bioinformatics.
shpc-registry automated BioContainers addition for ultra_bioinformatics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ultra_bioinformatics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ultra_bioinformatics:0.1--pyh7cba7a3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ultra_bioinformatics/0.1--pyh7cba7a3_1
$ module help quay.io/biocontainers/ultra_bioinformatics/0.1--pyh7cba7a3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ultra_bioinformatics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ultra_bioinformatics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ultra_bioinformatics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ultra_bioinformatics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ultra_bioinformatics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ultra_bioinformatics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### StrobeMap

```bash
$ singularity exec <container> /usr/local/bin/StrobeMap
$ podman run --it --rm --entrypoint /usr/local/bin/StrobeMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StrobeMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edlib-aligner

```bash
$ singularity exec <container> /usr/local/bin/edlib-aligner
$ podman run --it --rm --entrypoint /usr/local/bin/edlib-aligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edlib-aligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slaMEM

```bash
$ singularity exec <container> /usr/local/bin/slaMEM
$ podman run --it --rm --entrypoint /usr/local/bin/slaMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slaMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uLTRA

```bash
$ singularity exec <container> /usr/local/bin/uLTRA
$ podman run --it --rm --entrypoint /usr/local/bin/uLTRA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uLTRA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
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