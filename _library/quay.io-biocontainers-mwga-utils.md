---
layout: container
name:  "quay.io/biocontainers/mwga-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mwga-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mwga-utils/container.yaml"
updated_at: "2023-12-15 02:51:16.736190"
latest: "0.1.6--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/mwga-utils"
aliases:
 - "metrics"
 - "missing_regions"
 - "single_cov"
 - "stats"
versions:
 - "0.1.4--h9f5acd7_1"
 - "0.1.6--h9f5acd7_0"
 - "0.1.6--h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for mwga-utils"
config: {"url": "https://biocontainers.pro/tools/mwga-utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mwga-utils", "latest": {"0.1.6--h4ac6f70_2": "sha256:72347643ba7d2208078cf35dd29c6cc6d8dbdde10a5fe2c7d2fa4906db8ff115"}, "tags": {"0.1.4--h9f5acd7_1": "sha256:ca2a396654fba41221c11e51d2d93badd69836bc605f9e634e600e69532e93f5", "0.1.6--h9f5acd7_0": "sha256:5959aac716b40fdd522cd6e7ac37333e17c1b269537902f370a552e7a7c9dc0d", "0.1.6--h4ac6f70_2": "sha256:72347643ba7d2208078cf35dd29c6cc6d8dbdde10a5fe2c7d2fa4906db8ff115"}, "docker": "quay.io/biocontainers/mwga-utils", "aliases": {"metrics": "/usr/local/bin/metrics", "missing_regions": "/usr/local/bin/missing_regions", "single_cov": "/usr/local/bin/single_cov", "stats": "/usr/local/bin/stats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mwga-utils.
shpc-registry automated BioContainers addition for mwga-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mwga-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mwga-utils:0.1.6--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mwga-utils/0.1.6--h4ac6f70_2
$ module help quay.io/biocontainers/mwga-utils/0.1.6--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mwga-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mwga-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mwga-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mwga-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mwga-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mwga-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metrics

```bash
$ singularity exec <container> /usr/local/bin/metrics
$ podman run --it --rm --entrypoint /usr/local/bin/metrics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metrics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### missing_regions

```bash
$ singularity exec <container> /usr/local/bin/missing_regions
$ podman run --it --rm --entrypoint /usr/local/bin/missing_regions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/missing_regions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_cov

```bash
$ singularity exec <container> /usr/local/bin/single_cov
$ podman run --it --rm --entrypoint /usr/local/bin/single_cov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_cov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stats

```bash
$ singularity exec <container> /usr/local/bin/stats
$ podman run --it --rm --entrypoint /usr/local/bin/stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stats   -v ${PWD} -w ${PWD} <container> -c " $@"
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