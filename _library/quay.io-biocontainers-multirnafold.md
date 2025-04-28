---
layout: container
name:  "quay.io/biocontainers/multirnafold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/multirnafold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/multirnafold/container.yaml"
updated_at: "2025-04-28 03:31:07.931663"
latest: "2.1--h9948957_1"
container_url: "https://biocontainers.pro/tools/multirnafold"
aliases:
 - "feature_description"
 - "multifold"
 - "pairfold"
 - "pairfold-web"
 - "simfold"
 - "simfold_pf"
versions:
 - "2.1--h4ac6f70_0"
 - "2.1--h9948957_1"
description: "singularity registry hpc automated addition for multirnafold"
config: {"url": "https://biocontainers.pro/tools/multirnafold", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for multirnafold", "latest": {"2.1--h9948957_1": "sha256:2b72340a430dc9f353af60838564eee5955310e64487803a1439f76312dde306"}, "tags": {"2.1--h4ac6f70_0": "sha256:76a0ed85af24bd7ff56d7022de81435d92ddc626e4ffd385fa9123e7dffbd4da", "2.1--h9948957_1": "sha256:2b72340a430dc9f353af60838564eee5955310e64487803a1439f76312dde306"}, "docker": "quay.io/biocontainers/multirnafold", "aliases": {"feature_description": "/usr/local/bin/feature_description", "multifold": "/usr/local/bin/multifold", "pairfold": "/usr/local/bin/pairfold", "pairfold-web": "/usr/local/bin/pairfold-web", "simfold": "/usr/local/bin/simfold", "simfold_pf": "/usr/local/bin/simfold_pf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/multirnafold.
singularity registry hpc automated addition for multirnafold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/multirnafold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/multirnafold:2.1--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/multirnafold/2.1--h9948957_1
$ module help quay.io/biocontainers/multirnafold/2.1--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### multirnafold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### multirnafold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### multirnafold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### multirnafold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### multirnafold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### multirnafold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### feature_description

```bash
$ singularity exec <container> /usr/local/bin/feature_description
$ podman run --it --rm --entrypoint /usr/local/bin/feature_description   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/feature_description   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multifold

```bash
$ singularity exec <container> /usr/local/bin/multifold
$ podman run --it --rm --entrypoint /usr/local/bin/multifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairfold

```bash
$ singularity exec <container> /usr/local/bin/pairfold
$ podman run --it --rm --entrypoint /usr/local/bin/pairfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairfold-web

```bash
$ singularity exec <container> /usr/local/bin/pairfold-web
$ podman run --it --rm --entrypoint /usr/local/bin/pairfold-web   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairfold-web   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simfold

```bash
$ singularity exec <container> /usr/local/bin/simfold
$ podman run --it --rm --entrypoint /usr/local/bin/simfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simfold_pf

```bash
$ singularity exec <container> /usr/local/bin/simfold_pf
$ podman run --it --rm --entrypoint /usr/local/bin/simfold_pf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simfold_pf   -v ${PWD} -w ${PWD} <container> -c " $@"
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