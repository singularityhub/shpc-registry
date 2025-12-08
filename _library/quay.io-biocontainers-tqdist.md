---
layout: container
name:  "quay.io/biocontainers/tqdist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tqdist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tqdist/container.yaml"
updated_at: "2025-12-08 05:03:58.927789"
latest: "1.0.0--h1b792b2_3"
container_url: "https://biocontainers.pro/tools/tqdist"
aliases:
 - "all_pairs_quartet_dist"
 - "all_pairs_triplet_dist"
 - "pairs_quartet_dist"
 - "pairs_triplet_dist"
 - "quartet_dist"
 - "triplet_dist"
versions:
 - "1.0.0--h1b792b2_3"
description: "shpc-registry automated BioContainers addition for tqdist"
config: {"url": "https://biocontainers.pro/tools/tqdist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tqdist", "latest": {"1.0.0--h1b792b2_3": "sha256:63599fbbe7b8ebd356b624702dc92325e916dd38526154e3e0b93aa2176d9e4a"}, "tags": {"1.0.0--h1b792b2_3": "sha256:63599fbbe7b8ebd356b624702dc92325e916dd38526154e3e0b93aa2176d9e4a"}, "docker": "quay.io/biocontainers/tqdist", "aliases": {"all_pairs_quartet_dist": "/usr/local/bin/all_pairs_quartet_dist", "all_pairs_triplet_dist": "/usr/local/bin/all_pairs_triplet_dist", "pairs_quartet_dist": "/usr/local/bin/pairs_quartet_dist", "pairs_triplet_dist": "/usr/local/bin/pairs_triplet_dist", "quartet_dist": "/usr/local/bin/quartet_dist", "triplet_dist": "/usr/local/bin/triplet_dist"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tqdist.
shpc-registry automated BioContainers addition for tqdist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tqdist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tqdist:1.0.0--h1b792b2_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tqdist/1.0.0--h1b792b2_3
$ module help quay.io/biocontainers/tqdist/1.0.0--h1b792b2_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tqdist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tqdist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tqdist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tqdist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tqdist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tqdist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### all_pairs_quartet_dist

```bash
$ singularity exec <container> /usr/local/bin/all_pairs_quartet_dist
$ podman run --it --rm --entrypoint /usr/local/bin/all_pairs_quartet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/all_pairs_quartet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### all_pairs_triplet_dist

```bash
$ singularity exec <container> /usr/local/bin/all_pairs_triplet_dist
$ podman run --it --rm --entrypoint /usr/local/bin/all_pairs_triplet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/all_pairs_triplet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairs_quartet_dist

```bash
$ singularity exec <container> /usr/local/bin/pairs_quartet_dist
$ podman run --it --rm --entrypoint /usr/local/bin/pairs_quartet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairs_quartet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairs_triplet_dist

```bash
$ singularity exec <container> /usr/local/bin/pairs_triplet_dist
$ podman run --it --rm --entrypoint /usr/local/bin/pairs_triplet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairs_triplet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quartet_dist

```bash
$ singularity exec <container> /usr/local/bin/quartet_dist
$ podman run --it --rm --entrypoint /usr/local/bin/quartet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quartet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### triplet_dist

```bash
$ singularity exec <container> /usr/local/bin/triplet_dist
$ podman run --it --rm --entrypoint /usr/local/bin/triplet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/triplet_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
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