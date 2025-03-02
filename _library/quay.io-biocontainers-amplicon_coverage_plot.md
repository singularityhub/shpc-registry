---
layout: container
name:  "quay.io/biocontainers/amplicon_coverage_plot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amplicon_coverage_plot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/amplicon_coverage_plot/container.yaml"
updated_at: "2025-03-02 03:15:54.193798"
latest: "0.3.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/amplicon_coverage_plot"
aliases:
 - "amplicov"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.3.2--pyhdfd78af_0"
 - "0.3.3--pyhdfd78af_0"
 - "0.3.3--pyhdfd78af_1"
 - "0.3.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for amplicon_coverage_plot"
config: {"url": "https://biocontainers.pro/tools/amplicon_coverage_plot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for amplicon_coverage_plot", "latest": {"0.3.4--pyhdfd78af_0": "sha256:f5714f8b7b19037fd1250538349e6f3627a85678d448cbd680410acb2718d596"}, "tags": {"0.3.2--pyhdfd78af_0": "sha256:e491e3cd75d973764f62829479bd1a69fe55778406d3eb7e716f226ffdebc27c", "0.3.3--pyhdfd78af_0": "sha256:79030441e6ca3b023758ca099a81855ba7c8d94202c6edad0cc3b8c355d7c9da", "0.3.3--pyhdfd78af_1": "sha256:f7cdd96b7dfac35da028a3196b2bc2dbb6026bd5cffbf2f3a6f1a7f1a149ee62", "0.3.4--pyhdfd78af_0": "sha256:f5714f8b7b19037fd1250538349e6f3627a85678d448cbd680410acb2718d596"}, "docker": "quay.io/biocontainers/amplicon_coverage_plot", "aliases": {"amplicov": "/usr/local/bin/amplicov", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amplicon_coverage_plot.
shpc-registry automated BioContainers addition for amplicon_coverage_plot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amplicon_coverage_plot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amplicon_coverage_plot:0.3.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amplicon_coverage_plot/0.3.4--pyhdfd78af_0
$ module help quay.io/biocontainers/amplicon_coverage_plot/0.3.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amplicon_coverage_plot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amplicon_coverage_plot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amplicon_coverage_plot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amplicon_coverage_plot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amplicon_coverage_plot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amplicon_coverage_plot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amplicov

```bash
$ singularity exec <container> /usr/local/bin/amplicov
$ podman run --it --rm --entrypoint /usr/local/bin/amplicov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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