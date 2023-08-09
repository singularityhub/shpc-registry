---
layout: container
name:  "quay.io/biocontainers/cogclassifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cogclassifier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cogclassifier/container.yaml"
updated_at: "2023-08-09 03:04:37.624908"
latest: "1.0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cogclassifier"
aliases:
 - "COGclassifier"
 - "plot_cog_classifier_barchart"
 - "plot_cog_classifier_piechart"
 - "jsonschema"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.0.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for cogclassifier"
config: {"url": "https://biocontainers.pro/tools/cogclassifier", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cogclassifier", "latest": {"1.0.5--pyhdfd78af_0": "sha256:4b3368fae3d9807167a9d3f59d0c81e9ec2661db833f60e48744da0dd7851476"}, "tags": {"1.0.5--pyhdfd78af_0": "sha256:4b3368fae3d9807167a9d3f59d0c81e9ec2661db833f60e48744da0dd7851476"}, "docker": "quay.io/biocontainers/cogclassifier", "aliases": {"COGclassifier": "/usr/local/bin/COGclassifier", "plot_cog_classifier_barchart": "/usr/local/bin/plot_cog_classifier_barchart", "plot_cog_classifier_piechart": "/usr/local/bin/plot_cog_classifier_piechart", "jsonschema": "/usr/local/bin/jsonschema", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cogclassifier.
singularity registry hpc automated addition for cogclassifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cogclassifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cogclassifier:1.0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cogclassifier/1.0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/cogclassifier/1.0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cogclassifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cogclassifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cogclassifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cogclassifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cogclassifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cogclassifier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### COGclassifier

```bash
$ singularity exec <container> /usr/local/bin/COGclassifier
$ podman run --it --rm --entrypoint /usr/local/bin/COGclassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COGclassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_cog_classifier_barchart

```bash
$ singularity exec <container> /usr/local/bin/plot_cog_classifier_barchart
$ podman run --it --rm --entrypoint /usr/local/bin/plot_cog_classifier_barchart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_cog_classifier_barchart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_cog_classifier_piechart

```bash
$ singularity exec <container> /usr/local/bin/plot_cog_classifier_piechart
$ podman run --it --rm --entrypoint /usr/local/bin/plot_cog_classifier_piechart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_cog_classifier_piechart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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