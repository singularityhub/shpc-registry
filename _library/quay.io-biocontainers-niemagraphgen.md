---
layout: container
name:  "quay.io/biocontainers/niemagraphgen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/niemagraphgen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/niemagraphgen/container.yaml"
updated_at: "2024-11-09 03:29:43.185540"
latest: "1.0.6--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/niemagraphgen"
aliases:
 - "ngg_barabasi_albert"
 - "ngg_barbell"
 - "ngg_complete"
 - "ngg_cycle"
 - "ngg_empty"
 - "ngg_erdos_renyi"
 - "ngg_newman_watts_strogatz"
 - "ngg_path"
 - "ngg_ring_lattice"
versions:
 - "1.0.6--hdbdd923_0"
description: "singularity registry hpc automated addition for niemagraphgen"
config: {"url": "https://biocontainers.pro/tools/niemagraphgen", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for niemagraphgen", "latest": {"1.0.6--hdbdd923_0": "sha256:45cffe05712fc95f2cdb26ee44d598af7d602ec79920a081d592650cd4c60a2f"}, "tags": {"1.0.6--hdbdd923_0": "sha256:45cffe05712fc95f2cdb26ee44d598af7d602ec79920a081d592650cd4c60a2f"}, "docker": "quay.io/biocontainers/niemagraphgen", "aliases": {"ngg_barabasi_albert": "/usr/local/bin/ngg_barabasi_albert", "ngg_barbell": "/usr/local/bin/ngg_barbell", "ngg_complete": "/usr/local/bin/ngg_complete", "ngg_cycle": "/usr/local/bin/ngg_cycle", "ngg_empty": "/usr/local/bin/ngg_empty", "ngg_erdos_renyi": "/usr/local/bin/ngg_erdos_renyi", "ngg_newman_watts_strogatz": "/usr/local/bin/ngg_newman_watts_strogatz", "ngg_path": "/usr/local/bin/ngg_path", "ngg_ring_lattice": "/usr/local/bin/ngg_ring_lattice"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/niemagraphgen.
singularity registry hpc automated addition for niemagraphgen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/niemagraphgen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/niemagraphgen:1.0.6--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/niemagraphgen/1.0.6--hdbdd923_0
$ module help quay.io/biocontainers/niemagraphgen/1.0.6--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### niemagraphgen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### niemagraphgen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### niemagraphgen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### niemagraphgen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### niemagraphgen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### niemagraphgen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngg_barabasi_albert

```bash
$ singularity exec <container> /usr/local/bin/ngg_barabasi_albert
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_barabasi_albert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_barabasi_albert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_barbell

```bash
$ singularity exec <container> /usr/local/bin/ngg_barbell
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_barbell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_barbell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_complete

```bash
$ singularity exec <container> /usr/local/bin/ngg_complete
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_complete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_complete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_cycle

```bash
$ singularity exec <container> /usr/local/bin/ngg_cycle
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_empty

```bash
$ singularity exec <container> /usr/local/bin/ngg_empty
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_empty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_empty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_erdos_renyi

```bash
$ singularity exec <container> /usr/local/bin/ngg_erdos_renyi
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_erdos_renyi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_erdos_renyi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_newman_watts_strogatz

```bash
$ singularity exec <container> /usr/local/bin/ngg_newman_watts_strogatz
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_newman_watts_strogatz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_newman_watts_strogatz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_path

```bash
$ singularity exec <container> /usr/local/bin/ngg_path
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngg_ring_lattice

```bash
$ singularity exec <container> /usr/local/bin/ngg_ring_lattice
$ podman run --it --rm --entrypoint /usr/local/bin/ngg_ring_lattice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngg_ring_lattice   -v ${PWD} -w ${PWD} <container> -c " $@"
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