---
layout: container
name:  "quay.io/biocontainers/htstream"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/htstream/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/htstream/container.yaml"
updated_at: "2024-12-01 04:00:34.195029"
latest: "1.3.3--hf5e1c6e_5"
container_url: "https://biocontainers.pro/tools/htstream"
aliases:
 - "hts_AdapterTrimmer"
 - "hts_CutTrim"
 - "hts_LengthFilter"
 - "hts_NTrimmer"
 - "hts_Overlapper"
 - "hts_PolyATTrim"
 - "hts_Primers"
 - "hts_QWindowTrim"
 - "hts_SeqScreener"
 - "hts_Stats"
 - "hts_SuperDeduper"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.3.3--h39f6147_2"
 - "1.3.3--he82b154_4"
 - "1.3.3--hf5e1c6e_5"
description: "shpc-registry automated BioContainers addition for htstream"
config: {"url": "https://biocontainers.pro/tools/htstream", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for htstream", "latest": {"1.3.3--hf5e1c6e_5": "sha256:8b2f45de7711e0d3ea896bb07b2caf7edaec0206ef769a1d4a3b05fbb32c3996"}, "tags": {"1.3.3--h39f6147_2": "sha256:9a6dfe01cf8c656645abb2c430c529cab66cd9652ba3d1c5f4d1bfc1d9b4f650", "1.3.3--he82b154_4": "sha256:77d16606afea262612acc312bb3d08f2a8cfbc80d1de3ac8aac73edc5a0a7e8b", "1.3.3--hf5e1c6e_5": "sha256:8b2f45de7711e0d3ea896bb07b2caf7edaec0206ef769a1d4a3b05fbb32c3996"}, "docker": "quay.io/biocontainers/htstream", "aliases": {"hts_AdapterTrimmer": "/usr/local/bin/hts_AdapterTrimmer", "hts_CutTrim": "/usr/local/bin/hts_CutTrim", "hts_LengthFilter": "/usr/local/bin/hts_LengthFilter", "hts_NTrimmer": "/usr/local/bin/hts_NTrimmer", "hts_Overlapper": "/usr/local/bin/hts_Overlapper", "hts_PolyATTrim": "/usr/local/bin/hts_PolyATTrim", "hts_Primers": "/usr/local/bin/hts_Primers", "hts_QWindowTrim": "/usr/local/bin/hts_QWindowTrim", "hts_SeqScreener": "/usr/local/bin/hts_SeqScreener", "hts_Stats": "/usr/local/bin/hts_Stats", "hts_SuperDeduper": "/usr/local/bin/hts_SuperDeduper", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/htstream.
shpc-registry automated BioContainers addition for htstream
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/htstream
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/htstream:1.3.3--hf5e1c6e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/htstream/1.3.3--hf5e1c6e_5
$ module help quay.io/biocontainers/htstream/1.3.3--hf5e1c6e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htstream-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htstream-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htstream-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htstream-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htstream-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htstream-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hts_AdapterTrimmer

```bash
$ singularity exec <container> /usr/local/bin/hts_AdapterTrimmer
$ podman run --it --rm --entrypoint /usr/local/bin/hts_AdapterTrimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_AdapterTrimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_CutTrim

```bash
$ singularity exec <container> /usr/local/bin/hts_CutTrim
$ podman run --it --rm --entrypoint /usr/local/bin/hts_CutTrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_CutTrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_LengthFilter

```bash
$ singularity exec <container> /usr/local/bin/hts_LengthFilter
$ podman run --it --rm --entrypoint /usr/local/bin/hts_LengthFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_LengthFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_NTrimmer

```bash
$ singularity exec <container> /usr/local/bin/hts_NTrimmer
$ podman run --it --rm --entrypoint /usr/local/bin/hts_NTrimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_NTrimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_Overlapper

```bash
$ singularity exec <container> /usr/local/bin/hts_Overlapper
$ podman run --it --rm --entrypoint /usr/local/bin/hts_Overlapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_Overlapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_PolyATTrim

```bash
$ singularity exec <container> /usr/local/bin/hts_PolyATTrim
$ podman run --it --rm --entrypoint /usr/local/bin/hts_PolyATTrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_PolyATTrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_Primers

```bash
$ singularity exec <container> /usr/local/bin/hts_Primers
$ podman run --it --rm --entrypoint /usr/local/bin/hts_Primers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_Primers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_QWindowTrim

```bash
$ singularity exec <container> /usr/local/bin/hts_QWindowTrim
$ podman run --it --rm --entrypoint /usr/local/bin/hts_QWindowTrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_QWindowTrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_SeqScreener

```bash
$ singularity exec <container> /usr/local/bin/hts_SeqScreener
$ podman run --it --rm --entrypoint /usr/local/bin/hts_SeqScreener   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_SeqScreener   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_Stats

```bash
$ singularity exec <container> /usr/local/bin/hts_Stats
$ podman run --it --rm --entrypoint /usr/local/bin/hts_Stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_Stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hts_SuperDeduper

```bash
$ singularity exec <container> /usr/local/bin/hts_SuperDeduper
$ podman run --it --rm --entrypoint /usr/local/bin/hts_SuperDeduper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hts_SuperDeduper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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