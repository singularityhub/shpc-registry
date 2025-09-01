---
layout: container
name:  "quay.io/biocontainers/insurveyor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/insurveyor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/insurveyor/container.yaml"
updated_at: "2025-09-01 03:55:12.176205"
latest: "1.1.3--h077b44d_2"
container_url: "https://biocontainers.pro/tools/insurveyor"
aliases:
 - "add_filtering_info"
 - "call_insertions"
 - "clip_consensus_builder"
 - "dc_remapper"
 - "filter"
 - "normalise"
 - "random_pos_generator.py"
 - "reads_categorizer"
 - "surveyor.py"
 - "faidx"
 - "f2py3.9"
 - "htsfile"
 - "bgzip"
 - "tabix"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.0.2--h9f5acd7_0"
 - "1.1.1--h9f5acd7_0"
 - "1.1.1--h4ac6f70_1"
 - "1.1.2--h4ac6f70_0"
 - "1.1.3--hdcf5f25_1"
 - "1.1.3--h077b44d_2"
description: "singularity registry hpc automated addition for insurveyor"
config: {"url": "https://biocontainers.pro/tools/insurveyor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for insurveyor", "latest": {"1.1.3--h077b44d_2": "sha256:90d047ddcde43ed8d69a9d1efb319360579ced1b1a03a25037f5051e67aac694"}, "tags": {"1.0.2--h9f5acd7_0": "sha256:cba49eaee8f188cd994994d5eb08f9738f0ced1ef51488809ec446f216116b03", "1.1.1--h9f5acd7_0": "sha256:89f3afed826d3480ac7db1c2ca30079de7eaef38d0f2d23bbde1a77396e11cbd", "1.1.1--h4ac6f70_1": "sha256:316d19461e69e61bec2202125a26084066fcbfaa50dbb17a1d9cc5c7dd71e938", "1.1.2--h4ac6f70_0": "sha256:ae817d422576d4a4d696e80ef02ac008e8864a64192e06473ef32be4b95c2693", "1.1.3--hdcf5f25_1": "sha256:8211adb2f2f8cd2420113cbb02fd20990c9af1a98f8c65c4598c2f27442466c0", "1.1.3--h077b44d_2": "sha256:90d047ddcde43ed8d69a9d1efb319360579ced1b1a03a25037f5051e67aac694"}, "docker": "quay.io/biocontainers/insurveyor", "aliases": {"add_filtering_info": "/usr/local/bin/add_filtering_info", "call_insertions": "/usr/local/bin/call_insertions", "clip_consensus_builder": "/usr/local/bin/clip_consensus_builder", "dc_remapper": "/usr/local/bin/dc_remapper", "filter": "/usr/local/bin/filter", "normalise": "/usr/local/bin/normalise", "random_pos_generator.py": "/usr/local/bin/random_pos_generator.py", "reads_categorizer": "/usr/local/bin/reads_categorizer", "surveyor.py": "/usr/local/bin/surveyor.py", "faidx": "/usr/local/bin/faidx", "f2py3.9": "/usr/local/bin/f2py3.9", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/insurveyor.
singularity registry hpc automated addition for insurveyor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/insurveyor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/insurveyor:1.1.3--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/insurveyor/1.1.3--h077b44d_2
$ module help quay.io/biocontainers/insurveyor/1.1.3--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### insurveyor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### insurveyor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### insurveyor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### insurveyor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### insurveyor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### insurveyor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_filtering_info

```bash
$ singularity exec <container> /usr/local/bin/add_filtering_info
$ podman run --it --rm --entrypoint /usr/local/bin/add_filtering_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_filtering_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### call_insertions

```bash
$ singularity exec <container> /usr/local/bin/call_insertions
$ podman run --it --rm --entrypoint /usr/local/bin/call_insertions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/call_insertions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clip_consensus_builder

```bash
$ singularity exec <container> /usr/local/bin/clip_consensus_builder
$ podman run --it --rm --entrypoint /usr/local/bin/clip_consensus_builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clip_consensus_builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc_remapper

```bash
$ singularity exec <container> /usr/local/bin/dc_remapper
$ podman run --it --rm --entrypoint /usr/local/bin/dc_remapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc_remapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter

```bash
$ singularity exec <container> /usr/local/bin/filter
$ podman run --it --rm --entrypoint /usr/local/bin/filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalise

```bash
$ singularity exec <container> /usr/local/bin/normalise
$ podman run --it --rm --entrypoint /usr/local/bin/normalise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### random_pos_generator.py

```bash
$ singularity exec <container> /usr/local/bin/random_pos_generator.py
$ podman run --it --rm --entrypoint /usr/local/bin/random_pos_generator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/random_pos_generator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reads_categorizer

```bash
$ singularity exec <container> /usr/local/bin/reads_categorizer
$ podman run --it --rm --entrypoint /usr/local/bin/reads_categorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reads_categorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### surveyor.py

```bash
$ singularity exec <container> /usr/local/bin/surveyor.py
$ podman run --it --rm --entrypoint /usr/local/bin/surveyor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/surveyor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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