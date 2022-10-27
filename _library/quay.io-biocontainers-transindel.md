---
layout: container
name:  "quay.io/biocontainers/transindel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transindel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/transindel/container.yaml"
updated_at: "2022-10-27 01:00:47.657786"
latest: "1.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/transindel"
aliases:
 - "transIndel_build_DNA.py"
 - "transIndel_build_RNA.py"
 - "transIndel_call.py"
versions:
 - "1.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for transindel"
config: {"url": "https://biocontainers.pro/tools/transindel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transindel", "latest": {"1.0--hdfd78af_2": "sha256:628a19184a45264569593ef19ca163c464f4c9a968d4914504d30878f1700577"}, "tags": {"1.0--hdfd78af_2": "sha256:628a19184a45264569593ef19ca163c464f4c9a968d4914504d30878f1700577"}, "docker": "quay.io/biocontainers/transindel", "aliases": {"transIndel_build_DNA.py": "/usr/local/bin/transIndel_build_DNA.py", "transIndel_build_RNA.py": "/usr/local/bin/transIndel_build_RNA.py", "transIndel_call.py": "/usr/local/bin/transIndel_call.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transindel.
shpc-registry automated BioContainers addition for transindel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transindel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transindel:1.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transindel/1.0--hdfd78af_2
$ module help quay.io/biocontainers/transindel/1.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transindel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transindel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transindel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transindel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transindel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transindel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### transIndel_build_DNA.py

```bash
$ singularity exec <container> /usr/local/bin/transIndel_build_DNA.py
$ podman run --it --rm --entrypoint /usr/local/bin/transIndel_build_DNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transIndel_build_DNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transIndel_build_RNA.py

```bash
$ singularity exec <container> /usr/local/bin/transIndel_build_RNA.py
$ podman run --it --rm --entrypoint /usr/local/bin/transIndel_build_RNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transIndel_build_RNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transIndel_call.py

```bash
$ singularity exec <container> /usr/local/bin/transIndel_call.py
$ podman run --it --rm --entrypoint /usr/local/bin/transIndel_call.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transIndel_call.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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