---
layout: container
name:  "quay.io/biocontainers/cath-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cath-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cath-tools/container.yaml"
updated_at: "2023-12-14 03:25:48.223200"
latest: "0.16.5--h78a066a_0"
container_url: "https://biocontainers.pro/tools/cath-tools"
aliases:
 - "cath-assign-domains"
 - "cath-cluster"
 - "cath-map-clusters"
 - "cath-refine-align"
 - "cath-resolve-hits"
 - "cath-score-align"
 - "cath-ssap"
 - "cath-superpose"
versions:
 - "0.16.5--h78a066a_0"
description: "shpc-registry automated BioContainers addition for cath-tools"
config: {"url": "https://biocontainers.pro/tools/cath-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cath-tools", "latest": {"0.16.5--h78a066a_0": "sha256:88f72ad7bccaa8a2726e1c2b064abc2651359c6677891d8d65df13de76ad1418"}, "tags": {"0.16.5--h78a066a_0": "sha256:88f72ad7bccaa8a2726e1c2b064abc2651359c6677891d8d65df13de76ad1418"}, "docker": "quay.io/biocontainers/cath-tools", "aliases": {"cath-assign-domains": "/usr/local/bin/cath-assign-domains", "cath-cluster": "/usr/local/bin/cath-cluster", "cath-map-clusters": "/usr/local/bin/cath-map-clusters", "cath-refine-align": "/usr/local/bin/cath-refine-align", "cath-resolve-hits": "/usr/local/bin/cath-resolve-hits", "cath-score-align": "/usr/local/bin/cath-score-align", "cath-ssap": "/usr/local/bin/cath-ssap", "cath-superpose": "/usr/local/bin/cath-superpose"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cath-tools.
shpc-registry automated BioContainers addition for cath-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cath-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cath-tools:0.16.5--h78a066a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cath-tools/0.16.5--h78a066a_0
$ module help quay.io/biocontainers/cath-tools/0.16.5--h78a066a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cath-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cath-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cath-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cath-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cath-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cath-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cath-assign-domains

```bash
$ singularity exec <container> /usr/local/bin/cath-assign-domains
$ podman run --it --rm --entrypoint /usr/local/bin/cath-assign-domains   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-assign-domains   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cath-cluster

```bash
$ singularity exec <container> /usr/local/bin/cath-cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cath-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cath-map-clusters

```bash
$ singularity exec <container> /usr/local/bin/cath-map-clusters
$ podman run --it --rm --entrypoint /usr/local/bin/cath-map-clusters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-map-clusters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cath-refine-align

```bash
$ singularity exec <container> /usr/local/bin/cath-refine-align
$ podman run --it --rm --entrypoint /usr/local/bin/cath-refine-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-refine-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cath-resolve-hits

```bash
$ singularity exec <container> /usr/local/bin/cath-resolve-hits
$ podman run --it --rm --entrypoint /usr/local/bin/cath-resolve-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-resolve-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cath-score-align

```bash
$ singularity exec <container> /usr/local/bin/cath-score-align
$ podman run --it --rm --entrypoint /usr/local/bin/cath-score-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-score-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cath-ssap

```bash
$ singularity exec <container> /usr/local/bin/cath-ssap
$ podman run --it --rm --entrypoint /usr/local/bin/cath-ssap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-ssap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cath-superpose

```bash
$ singularity exec <container> /usr/local/bin/cath-superpose
$ podman run --it --rm --entrypoint /usr/local/bin/cath-superpose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cath-superpose   -v ${PWD} -w ${PWD} <container> -c " $@"
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