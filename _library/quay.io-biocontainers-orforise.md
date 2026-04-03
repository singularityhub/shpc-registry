---
layout: container
name:  "quay.io/biocontainers/orforise"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orforise/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orforise/container.yaml"
updated_at: "2026-04-03 15:28:09.451386"
latest: "1.6.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/orforise"
aliases:
 - "Aggregate-Compare"
 - "Annotation-Compare"
 - "Annotation-Intersector"
 - "Convert-To-GFF"
 - "GFF-Adder"
 - "List-Tools"
 - "StORForise"
 - "aggregate-compare"
 - "annotation-compare"
 - "annotation-intersector"
 - "convert-to-gff"
 - "gff-adder"
 - "list-tools"
 - "storforise"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
versions:
 - "1.6.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for orforise"
config: {"url": "https://biocontainers.pro/tools/orforise", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for orforise", "latest": {"1.6.6--pyhdfd78af_0": "sha256:dab9aa067941204418dd4a671f922cfee9bdb448256b946e12c8869fb7edde2f"}, "tags": {"1.6.6--pyhdfd78af_0": "sha256:dab9aa067941204418dd4a671f922cfee9bdb448256b946e12c8869fb7edde2f"}, "docker": "quay.io/biocontainers/orforise", "aliases": {"Aggregate-Compare": "/usr/local/bin/Aggregate-Compare", "Annotation-Compare": "/usr/local/bin/Annotation-Compare", "Annotation-Intersector": "/usr/local/bin/Annotation-Intersector", "Convert-To-GFF": "/usr/local/bin/Convert-To-GFF", "GFF-Adder": "/usr/local/bin/GFF-Adder", "List-Tools": "/usr/local/bin/List-Tools", "StORForise": "/usr/local/bin/StORForise", "aggregate-compare": "/usr/local/bin/aggregate-compare", "annotation-compare": "/usr/local/bin/annotation-compare", "annotation-intersector": "/usr/local/bin/annotation-intersector", "convert-to-gff": "/usr/local/bin/convert-to-gff", "gff-adder": "/usr/local/bin/gff-adder", "list-tools": "/usr/local/bin/list-tools", "storforise": "/usr/local/bin/storforise", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orforise.
singularity registry hpc automated addition for orforise
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orforise
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orforise:1.6.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orforise/1.6.6--pyhdfd78af_0
$ module help quay.io/biocontainers/orforise/1.6.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orforise-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orforise-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orforise-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orforise-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orforise-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orforise-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Aggregate-Compare

```bash
$ singularity exec <container> /usr/local/bin/Aggregate-Compare
$ podman run --it --rm --entrypoint /usr/local/bin/Aggregate-Compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aggregate-Compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Annotation-Compare

```bash
$ singularity exec <container> /usr/local/bin/Annotation-Compare
$ podman run --it --rm --entrypoint /usr/local/bin/Annotation-Compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Annotation-Compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Annotation-Intersector

```bash
$ singularity exec <container> /usr/local/bin/Annotation-Intersector
$ podman run --it --rm --entrypoint /usr/local/bin/Annotation-Intersector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Annotation-Intersector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Convert-To-GFF

```bash
$ singularity exec <container> /usr/local/bin/Convert-To-GFF
$ podman run --it --rm --entrypoint /usr/local/bin/Convert-To-GFF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Convert-To-GFF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GFF-Adder

```bash
$ singularity exec <container> /usr/local/bin/GFF-Adder
$ podman run --it --rm --entrypoint /usr/local/bin/GFF-Adder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GFF-Adder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### List-Tools

```bash
$ singularity exec <container> /usr/local/bin/List-Tools
$ podman run --it --rm --entrypoint /usr/local/bin/List-Tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/List-Tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StORForise

```bash
$ singularity exec <container> /usr/local/bin/StORForise
$ podman run --it --rm --entrypoint /usr/local/bin/StORForise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StORForise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate-compare

```bash
$ singularity exec <container> /usr/local/bin/aggregate-compare
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotation-compare

```bash
$ singularity exec <container> /usr/local/bin/annotation-compare
$ podman run --it --rm --entrypoint /usr/local/bin/annotation-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotation-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotation-intersector

```bash
$ singularity exec <container> /usr/local/bin/annotation-intersector
$ podman run --it --rm --entrypoint /usr/local/bin/annotation-intersector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotation-intersector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-to-gff

```bash
$ singularity exec <container> /usr/local/bin/convert-to-gff
$ podman run --it --rm --entrypoint /usr/local/bin/convert-to-gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-to-gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-adder

```bash
$ singularity exec <container> /usr/local/bin/gff-adder
$ podman run --it --rm --entrypoint /usr/local/bin/gff-adder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-adder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list-tools

```bash
$ singularity exec <container> /usr/local/bin/list-tools
$ podman run --it --rm --entrypoint /usr/local/bin/list-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### storforise

```bash
$ singularity exec <container> /usr/local/bin/storforise
$ podman run --it --rm --entrypoint /usr/local/bin/storforise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/storforise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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