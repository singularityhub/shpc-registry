---
layout: container
name:  "quay.io/biocontainers/fastmlst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastmlst/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fastmlst/container.yaml"
updated_at: "2022-10-29 05:45:00.573734"
latest: "0.0.9--py_0"
container_url: "https://biocontainers.pro/tools/fastmlst"
aliases:
 - "fastmlst"
 - "blast_formatter"
 - "blastdb_aliastool"
 - "blastdbcheck"
 - "blastdbcmd"
 - "blastdbcp"
 - "blastn"
 - "blastp"
 - "blastx"
 - "convert2blastmask"
 - "datatool"
versions:
 - "0.0.9--py_0"
description: "shpc-registry automated BioContainers addition for fastmlst"
config: {"url": "https://biocontainers.pro/tools/fastmlst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastmlst", "latest": {"0.0.9--py_0": "sha256:cc131ee6bc0b619e22e8ceb8bef435cf764a29f07751726b5db3f83e618cbdbf"}, "tags": {"0.0.9--py_0": "sha256:cc131ee6bc0b619e22e8ceb8bef435cf764a29f07751726b5db3f83e618cbdbf"}, "docker": "quay.io/biocontainers/fastmlst", "aliases": {"fastmlst": "/usr/local/bin/fastmlst", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool", "blastdbcheck": "/usr/local/bin/blastdbcheck", "blastdbcmd": "/usr/local/bin/blastdbcmd", "blastdbcp": "/usr/local/bin/blastdbcp", "blastn": "/usr/local/bin/blastn", "blastp": "/usr/local/bin/blastp", "blastx": "/usr/local/bin/blastx", "convert2blastmask": "/usr/local/bin/convert2blastmask", "datatool": "/usr/local/bin/datatool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastmlst.
shpc-registry automated BioContainers addition for fastmlst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastmlst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastmlst:0.0.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastmlst/0.0.9--py_0
$ module help quay.io/biocontainers/fastmlst/0.0.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastmlst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastmlst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastmlst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastmlst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastmlst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastmlst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastmlst

```bash
$ singularity exec <container> /usr/local/bin/fastmlst
$ podman run --it --rm --entrypoint /usr/local/bin/fastmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastmlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool

```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcheck

```bash
$ singularity exec <container> /usr/local/bin/blastdbcheck
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcmd

```bash
$ singularity exec <container> /usr/local/bin/blastdbcmd
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcp

```bash
$ singularity exec <container> /usr/local/bin/blastdbcp
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn

```bash
$ singularity exec <container> /usr/local/bin/blastn
$ podman run --it --rm --entrypoint /usr/local/bin/blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastp

```bash
$ singularity exec <container> /usr/local/bin/blastp
$ podman run --it --rm --entrypoint /usr/local/bin/blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastx

```bash
$ singularity exec <container> /usr/local/bin/blastx
$ podman run --it --rm --entrypoint /usr/local/bin/blastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert2blastmask

```bash
$ singularity exec <container> /usr/local/bin/convert2blastmask
$ podman run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datatool

```bash
$ singularity exec <container> /usr/local/bin/datatool
$ podman run --it --rm --entrypoint /usr/local/bin/datatool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datatool   -v ${PWD} -w ${PWD} <container> -c " $@"
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