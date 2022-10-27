---
layout: container
name:  "quay.io/biocontainers/metaseq-all"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaseq-all/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metaseq-all/container.yaml"
updated_at: "2022-10-27 00:53:22.009285"
latest: "0.5.6--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/metaseq-all"
aliases:
 - "bigWigSummary"
 - "download_metaseq_example_data.py"
 - "metaseq-cli"
 - "speedtest.py"
versions:
 - "0.5.6--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for metaseq-all"
config: {"url": "https://biocontainers.pro/tools/metaseq-all", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaseq-all", "latest": {"0.5.6--hdfd78af_4": "sha256:da4d442077917f5badb6c12006c40439728903cc532d247e5ea1adde4ee7c8e7"}, "tags": {"0.5.6--hdfd78af_4": "sha256:da4d442077917f5badb6c12006c40439728903cc532d247e5ea1adde4ee7c8e7"}, "docker": "quay.io/biocontainers/metaseq-all", "aliases": {"bigWigSummary": "/usr/local/bin/bigWigSummary", "download_metaseq_example_data.py": "/usr/local/bin/download_metaseq_example_data.py", "metaseq-cli": "/usr/local/bin/metaseq-cli", "speedtest.py": "/usr/local/bin/speedtest.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaseq-all.
shpc-registry automated BioContainers addition for metaseq-all
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaseq-all
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaseq-all:0.5.6--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaseq-all/0.5.6--hdfd78af_4
$ module help quay.io/biocontainers/metaseq-all/0.5.6--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaseq-all-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaseq-all-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaseq-all-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaseq-all-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaseq-all-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaseq-all-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigWigSummary

```bash
$ singularity exec <container> /usr/local/bin/bigWigSummary
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_metaseq_example_data.py

```bash
$ singularity exec <container> /usr/local/bin/download_metaseq_example_data.py
$ podman run --it --rm --entrypoint /usr/local/bin/download_metaseq_example_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_metaseq_example_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaseq-cli

```bash
$ singularity exec <container> /usr/local/bin/metaseq-cli
$ podman run --it --rm --entrypoint /usr/local/bin/metaseq-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaseq-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### speedtest.py

```bash
$ singularity exec <container> /usr/local/bin/speedtest.py
$ podman run --it --rm --entrypoint /usr/local/bin/speedtest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/speedtest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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