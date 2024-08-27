---
layout: container
name:  "quay.io/biocontainers/perl-excel-writer-xlsx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-excel-writer-xlsx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-excel-writer-xlsx/container.yaml"
updated_at: "2024-08-27 06:42:23.007733"
latest: "1.11--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-excel-writer-xlsx"
aliases:
 - "crc32"
 - "extract_vba"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.09--pl5321hdfd78af_0"
 - "1.10--pl5321hdfd78af_0"
 - "1.11--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-excel-writer-xlsx"
config: {"url": "https://biocontainers.pro/tools/perl-excel-writer-xlsx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-excel-writer-xlsx", "latest": {"1.11--pl5321hdfd78af_0": "sha256:3e18c2ffb31edcf85e1451957d433a02d36daa0ce8a4f3e8e16cf00a3d57d03e"}, "tags": {"1.09--pl5321hdfd78af_0": "sha256:4642b1f4c6f70520ed697d085abed0be8560b1eb31ccb865bc4b9aca418eef76", "1.10--pl5321hdfd78af_0": "sha256:d560b3b4bc83250005bcc7eb1ca188f955a0d64c14f932c03e64b29fbe41f818", "1.11--pl5321hdfd78af_0": "sha256:3e18c2ffb31edcf85e1451957d433a02d36daa0ce8a4f3e8e16cf00a3d57d03e"}, "docker": "quay.io/biocontainers/perl-excel-writer-xlsx", "aliases": {"crc32": "/usr/local/bin/crc32", "extract_vba": "/usr/local/bin/extract_vba", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-excel-writer-xlsx.
shpc-registry automated BioContainers addition for perl-excel-writer-xlsx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-excel-writer-xlsx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-excel-writer-xlsx:1.11--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-excel-writer-xlsx/1.11--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-excel-writer-xlsx/1.11--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-excel-writer-xlsx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-excel-writer-xlsx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-excel-writer-xlsx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-excel-writer-xlsx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-excel-writer-xlsx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-excel-writer-xlsx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_vba

```bash
$ singularity exec <container> /usr/local/bin/extract_vba
$ podman run --it --rm --entrypoint /usr/local/bin/extract_vba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_vba   -v ${PWD} -w ${PWD} <container> -c " $@"
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