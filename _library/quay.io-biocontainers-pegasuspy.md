---
layout: container
name:  "quay.io/biocontainers/pegasuspy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pegasuspy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pegasuspy/container.yaml"
updated_at: "2022-10-27 00:46:00.317150"
latest: "1.7.1--py39hbf8eff0_0"
container_url: "https://biocontainers.pro/tools/pegasuspy"
aliases:
 - "csv-import"
 - "demuxEM"
 - "loompy"
 - "orc-memory"
 - "orc-scan"
 - "pegasus"
 - "pegasusio"
 - "pybind11-config"
 - "timezone-dump"
 - "torchrun"
 - "wordcloud_cli"
versions:
 - "1.7.1--py39hbf8eff0_0"
description: "shpc-registry automated BioContainers addition for pegasuspy"
config: {"url": "https://biocontainers.pro/tools/pegasuspy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pegasuspy", "latest": {"1.7.1--py39hbf8eff0_0": "sha256:97d2aee83385e763406e04bfe198d6a5dd63d454e115174c16397775c9c92ce0"}, "tags": {"1.7.1--py39hbf8eff0_0": "sha256:97d2aee83385e763406e04bfe198d6a5dd63d454e115174c16397775c9c92ce0"}, "docker": "quay.io/biocontainers/pegasuspy", "aliases": {"csv-import": "/usr/local/bin/csv-import", "demuxEM": "/usr/local/bin/demuxEM", "loompy": "/usr/local/bin/loompy", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "pegasus": "/usr/local/bin/pegasus", "pegasusio": "/usr/local/bin/pegasusio", "pybind11-config": "/usr/local/bin/pybind11-config", "timezone-dump": "/usr/local/bin/timezone-dump", "torchrun": "/usr/local/bin/torchrun", "wordcloud_cli": "/usr/local/bin/wordcloud_cli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pegasuspy.
shpc-registry automated BioContainers addition for pegasuspy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pegasuspy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pegasuspy:1.7.1--py39hbf8eff0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pegasuspy/1.7.1--py39hbf8eff0_0
$ module help quay.io/biocontainers/pegasuspy/1.7.1--py39hbf8eff0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pegasuspy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pegasuspy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pegasuspy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pegasuspy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pegasuspy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pegasuspy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demuxEM

```bash
$ singularity exec <container> /usr/local/bin/demuxEM
$ podman run --it --rm --entrypoint /usr/local/bin/demuxEM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demuxEM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loompy

```bash
$ singularity exec <container> /usr/local/bin/loompy
$ podman run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pegasus

```bash
$ singularity exec <container> /usr/local/bin/pegasus
$ podman run --it --rm --entrypoint /usr/local/bin/pegasus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pegasus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pegasusio

```bash
$ singularity exec <container> /usr/local/bin/pegasusio
$ podman run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wordcloud_cli

```bash
$ singularity exec <container> /usr/local/bin/wordcloud_cli
$ podman run --it --rm --entrypoint /usr/local/bin/wordcloud_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wordcloud_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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