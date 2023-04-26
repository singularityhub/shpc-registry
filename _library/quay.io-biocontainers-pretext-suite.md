---
layout: container
name:  "quay.io/biocontainers/pretext-suite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pretext-suite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pretext-suite/container.yaml"
updated_at: "2023-04-26 03:15:05.472712"
latest: "0.0.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/pretext-suite"
aliases:
 - "PretextGraph"
 - "PretextGraph.avx"
 - "PretextGraph.avx2"
 - "PretextGraph.sse41"
 - "PretextGraph.sse42"
 - "PretextMap"
 - "PretextMap.avx"
 - "PretextMap.avx2"
 - "PretextMap.noext"
 - "PretextMap.sse41"
 - "PretextMap.sse42"
 - "PretextSnapshot"
 - "PretextSnapshot.avx"
 - "PretextSnapshot.avx2"
 - "PretextSnapshot.sse41"
 - "PretextSnapshot.sse42"
versions:
 - "0.0.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for pretext-suite"
config: {"url": "https://biocontainers.pro/tools/pretext-suite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pretext-suite", "latest": {"0.0.2--hdfd78af_1": "sha256:d08476ded98692b50f998effcef1d62c3e080cac340b47ca2482542b30123ad5"}, "tags": {"0.0.2--hdfd78af_1": "sha256:d08476ded98692b50f998effcef1d62c3e080cac340b47ca2482542b30123ad5"}, "docker": "quay.io/biocontainers/pretext-suite", "aliases": {"PretextGraph": "/usr/local/bin/PretextGraph", "PretextGraph.avx": "/usr/local/bin/PretextGraph.avx", "PretextGraph.avx2": "/usr/local/bin/PretextGraph.avx2", "PretextGraph.sse41": "/usr/local/bin/PretextGraph.sse41", "PretextGraph.sse42": "/usr/local/bin/PretextGraph.sse42", "PretextMap": "/usr/local/bin/PretextMap", "PretextMap.avx": "/usr/local/bin/PretextMap.avx", "PretextMap.avx2": "/usr/local/bin/PretextMap.avx2", "PretextMap.noext": "/usr/local/bin/PretextMap.noext", "PretextMap.sse41": "/usr/local/bin/PretextMap.sse41", "PretextMap.sse42": "/usr/local/bin/PretextMap.sse42", "PretextSnapshot": "/usr/local/bin/PretextSnapshot", "PretextSnapshot.avx": "/usr/local/bin/PretextSnapshot.avx", "PretextSnapshot.avx2": "/usr/local/bin/PretextSnapshot.avx2", "PretextSnapshot.sse41": "/usr/local/bin/PretextSnapshot.sse41", "PretextSnapshot.sse42": "/usr/local/bin/PretextSnapshot.sse42"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pretext-suite.
shpc-registry automated BioContainers addition for pretext-suite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pretext-suite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pretext-suite:0.0.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pretext-suite/0.0.2--hdfd78af_1
$ module help quay.io/biocontainers/pretext-suite/0.0.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pretext-suite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pretext-suite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pretext-suite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pretext-suite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pretext-suite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pretext-suite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PretextGraph

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.avx

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.avx
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.avx2

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.sse41

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.sse42

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap

```bash
$ singularity exec <container> /usr/local/bin/PretextMap
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.avx

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.avx
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.avx2

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.noext

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.noext
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.noext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.noext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.sse41

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.sse42

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.avx

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.avx
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.avx2

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.sse41

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.sse42

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
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