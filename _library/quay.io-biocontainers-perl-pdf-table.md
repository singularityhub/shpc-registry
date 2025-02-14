---
layout: container
name:  "quay.io/biocontainers/perl-pdf-table"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-pdf-table/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-pdf-table/container.yaml"
updated_at: "2025-02-14 03:07:24.643640"
latest: "1.005--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-pdf-table"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.003--pl5321hdfd78af_0"
 - "1.004--pl5321hdfd78af_0"
 - "1.005--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-pdf-table"
config: {"url": "https://biocontainers.pro/tools/perl-pdf-table", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-pdf-table", "latest": {"1.005--pl5321hdfd78af_0": "sha256:2964a8b5f1a40ea21dca907fecff369e41031fe47df34299e0e8f0ac593a8833"}, "tags": {"1.003--pl5321hdfd78af_0": "sha256:3d375ceba785d65dbe09b802eb715b8e829573f2b38c9c396ba1362b131b3344", "1.004--pl5321hdfd78af_0": "sha256:70c31a7d263169e218464b613d46e7e4e9c10c5c00572ec2f950891ecdd7005f", "1.005--pl5321hdfd78af_0": "sha256:2964a8b5f1a40ea21dca907fecff369e41031fe47df34299e0e8f0ac593a8833"}, "docker": "quay.io/biocontainers/perl-pdf-table", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-pdf-table.
shpc-registry automated BioContainers addition for perl-pdf-table
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-pdf-table
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-pdf-table:1.005--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-pdf-table/1.005--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-pdf-table/1.005--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-pdf-table-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-pdf-table-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-pdf-table-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-pdf-table-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-pdf-table-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-pdf-table-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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