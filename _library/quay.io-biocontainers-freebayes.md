---
layout: container
name:  "quay.io/biocontainers/freebayes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/freebayes/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/freebayes/container.yaml"
updated_at: "2022-10-29 05:48:24.157505"
latest: "1.3.3--py36hc088bd4_0"
container_url: "https://biocontainers.pro/tools/freebayes"
aliases:
 - "2to3-3.6"
 - "bamleftalign"
 - "bgzip"
 - "coverage_to_regions.py"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
 - "env_parallel.dash"
 - "env_parallel.fish"
versions:
 - "1.3.3--py36hc088bd4_0"
description: "shpc-registry automated BioContainers addition for freebayes"
config: {"url": "https://biocontainers.pro/tools/freebayes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for freebayes", "latest": {"1.3.3--py36hc088bd4_0": "sha256:da103b362206e7eea33b2bafad20198113f72de445b3c1fe4fdd87ea552a59e7"}, "tags": {"1.3.3--py36hc088bd4_0": "sha256:da103b362206e7eea33b2bafad20198113f72de445b3c1fe4fdd87ea552a59e7"}, "docker": "quay.io/biocontainers/freebayes", "aliases": {"2to3-3.6": "/usr/local/bin/2to3-3.6", "bamleftalign": "/usr/local/bin/bamleftalign", "bgzip": "/usr/local/bin/bgzip", "coverage_to_regions.py": "/usr/local/bin/coverage_to_regions.py", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/freebayes.
shpc-registry automated BioContainers addition for freebayes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/freebayes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/freebayes:1.3.3--py36hc088bd4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/freebayes/1.3.3--py36hc088bd4_0
$ module help quay.io/biocontainers/freebayes/1.3.3--py36hc088bd4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### freebayes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### freebayes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### freebayes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### freebayes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### freebayes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### freebayes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamleftalign

```bash
$ singularity exec <container> /usr/local/bin/bamleftalign
$ podman run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_to_regions.py

```bash
$ singularity exec <container> /usr/local/bin/coverage_to_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.csh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.csh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.dash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.dash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.fish

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.fish
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
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