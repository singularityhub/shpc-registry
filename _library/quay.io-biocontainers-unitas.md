---
layout: container
name:  "quay.io/biocontainers/unitas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unitas/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/unitas/container.yaml"
updated_at: "2022-10-27 00:38:22.216042"
latest: "1.6.1--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/unitas"
aliases:
 - "dnapi.py"
 - "qual_offset.py"
 - "qual_trim.py"
 - "seqmap"
 - "to_fasta.py"
 - "unitas.pl"
versions:
 - "1.6.1--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for unitas"
config: {"url": "https://biocontainers.pro/tools/unitas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unitas", "latest": {"1.6.1--hdfd78af_2": "sha256:eeea61e95455abc79b45fc704cb96cb3f8a65ee2da5b80a79e0b7df53165b14d"}, "tags": {"1.6.1--hdfd78af_2": "sha256:eeea61e95455abc79b45fc704cb96cb3f8a65ee2da5b80a79e0b7df53165b14d"}, "docker": "quay.io/biocontainers/unitas", "aliases": {"dnapi.py": "/usr/local/bin/dnapi.py", "qual_offset.py": "/usr/local/bin/qual_offset.py", "qual_trim.py": "/usr/local/bin/qual_trim.py", "seqmap": "/usr/local/bin/seqmap", "to_fasta.py": "/usr/local/bin/to_fasta.py", "unitas.pl": "/usr/local/bin/unitas.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unitas.
shpc-registry automated BioContainers addition for unitas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unitas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unitas:1.6.1--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unitas/1.6.1--hdfd78af_2
$ module help quay.io/biocontainers/unitas/1.6.1--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unitas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unitas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unitas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unitas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unitas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unitas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnapi.py

```bash
$ singularity exec <container> /usr/local/bin/dnapi.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnapi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnapi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qual_offset.py

```bash
$ singularity exec <container> /usr/local/bin/qual_offset.py
$ podman run --it --rm --entrypoint /usr/local/bin/qual_offset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qual_offset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qual_trim.py

```bash
$ singularity exec <container> /usr/local/bin/qual_trim.py
$ podman run --it --rm --entrypoint /usr/local/bin/qual_trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qual_trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqmap

```bash
$ singularity exec <container> /usr/local/bin/seqmap
$ podman run --it --rm --entrypoint /usr/local/bin/seqmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unitas.pl

```bash
$ singularity exec <container> /usr/local/bin/unitas.pl
$ podman run --it --rm --entrypoint /usr/local/bin/unitas.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unitas.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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