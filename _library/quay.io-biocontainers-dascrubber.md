---
layout: container
name:  "quay.io/biocontainers/dascrubber"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dascrubber/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dascrubber/container.yaml"
updated_at: "2023-09-13 02:41:48.784668"
latest: "0.0.1a2--h031d066_6"
container_url: "https://biocontainers.pro/tools/dascrubber"
aliases:
 - "DASedit"
 - "DASmap"
 - "DASpatch"
 - "DASqv"
 - "DASrealign"
 - "DAStrim"
 - "REPqv"
 - "REPtrim"
versions:
 - "0.0.1a2--hec16e2b_4"
 - "0.0.1a2--h031d066_6"
description: "shpc-registry automated BioContainers addition for dascrubber"
config: {"url": "https://biocontainers.pro/tools/dascrubber", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dascrubber", "latest": {"0.0.1a2--h031d066_6": "sha256:1fe21483ca046f64c068e148ba03fe40b67999f08899f79c5b36eaff8125eabd"}, "tags": {"0.0.1a2--hec16e2b_4": "sha256:be3064ed631087420ce88b26912ae3906e48081e81941a6f0ecf566428c888e9", "0.0.1a2--h031d066_6": "sha256:1fe21483ca046f64c068e148ba03fe40b67999f08899f79c5b36eaff8125eabd"}, "docker": "quay.io/biocontainers/dascrubber", "aliases": {"DASedit": "/usr/local/bin/DASedit", "DASmap": "/usr/local/bin/DASmap", "DASpatch": "/usr/local/bin/DASpatch", "DASqv": "/usr/local/bin/DASqv", "DASrealign": "/usr/local/bin/DASrealign", "DAStrim": "/usr/local/bin/DAStrim", "REPqv": "/usr/local/bin/REPqv", "REPtrim": "/usr/local/bin/REPtrim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dascrubber.
shpc-registry automated BioContainers addition for dascrubber
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dascrubber
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dascrubber:0.0.1a2--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dascrubber/0.0.1a2--h031d066_6
$ module help quay.io/biocontainers/dascrubber/0.0.1a2--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dascrubber-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dascrubber-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dascrubber-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dascrubber-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dascrubber-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dascrubber-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DASedit

```bash
$ singularity exec <container> /usr/local/bin/DASedit
$ podman run --it --rm --entrypoint /usr/local/bin/DASedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DASedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DASmap

```bash
$ singularity exec <container> /usr/local/bin/DASmap
$ podman run --it --rm --entrypoint /usr/local/bin/DASmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DASmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DASpatch

```bash
$ singularity exec <container> /usr/local/bin/DASpatch
$ podman run --it --rm --entrypoint /usr/local/bin/DASpatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DASpatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DASqv

```bash
$ singularity exec <container> /usr/local/bin/DASqv
$ podman run --it --rm --entrypoint /usr/local/bin/DASqv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DASqv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DASrealign

```bash
$ singularity exec <container> /usr/local/bin/DASrealign
$ podman run --it --rm --entrypoint /usr/local/bin/DASrealign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DASrealign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DAStrim

```bash
$ singularity exec <container> /usr/local/bin/DAStrim
$ podman run --it --rm --entrypoint /usr/local/bin/DAStrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DAStrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### REPqv

```bash
$ singularity exec <container> /usr/local/bin/REPqv
$ podman run --it --rm --entrypoint /usr/local/bin/REPqv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REPqv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### REPtrim

```bash
$ singularity exec <container> /usr/local/bin/REPtrim
$ podman run --it --rm --entrypoint /usr/local/bin/REPtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REPtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
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