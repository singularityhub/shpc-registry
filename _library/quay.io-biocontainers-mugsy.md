---
layout: container
name:  "quay.io/biocontainers/mugsy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mugsy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mugsy/container.yaml"
updated_at: "2024-01-15 02:43:45.090832"
latest: "1.2.3--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/mugsy"
aliases:
 - "delta-dups.sh"
 - "fixMAFnames.pl"
 - "maf2fasta.pl"
 - "mugsy"
 - "mugsyWGA"
 - "mugsyenv.sh"
 - "plot.pl"
 - "splitmaf.pl"
 - "synchain-mugsy"
 - "xmfa2maf.pl"
 - "perl5.32.0"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "streamzip"
versions:
 - "1.2.3--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for mugsy"
config: {"url": "https://biocontainers.pro/tools/mugsy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mugsy", "latest": {"1.2.3--hdfd78af_4": "sha256:5764b6bc25ed1a6ba912154db34db2d2d5d260df3903a7327d4b3ad418475810"}, "tags": {"1.2.3--hdfd78af_4": "sha256:5764b6bc25ed1a6ba912154db34db2d2d5d260df3903a7327d4b3ad418475810"}, "docker": "quay.io/biocontainers/mugsy", "aliases": {"delta-dups.sh": "/usr/local/bin/delta-dups.sh", "fixMAFnames.pl": "/usr/local/bin/fixMAFnames.pl", "maf2fasta.pl": "/usr/local/bin/maf2fasta.pl", "mugsy": "/usr/local/bin/mugsy", "mugsyWGA": "/usr/local/bin/mugsyWGA", "mugsyenv.sh": "/usr/local/bin/mugsyenv.sh", "plot.pl": "/usr/local/bin/plot.pl", "splitmaf.pl": "/usr/local/bin/splitmaf.pl", "synchain-mugsy": "/usr/local/bin/synchain-mugsy", "xmfa2maf.pl": "/usr/local/bin/xmfa2maf.pl", "perl5.32.0": "/usr/local/bin/perl5.32.0", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mugsy.
shpc-registry automated BioContainers addition for mugsy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mugsy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mugsy:1.2.3--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mugsy/1.2.3--hdfd78af_4
$ module help quay.io/biocontainers/mugsy/1.2.3--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mugsy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mugsy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mugsy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mugsy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mugsy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mugsy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delta-dups.sh

```bash
$ singularity exec <container> /usr/local/bin/delta-dups.sh
$ podman run --it --rm --entrypoint /usr/local/bin/delta-dups.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-dups.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fixMAFnames.pl

```bash
$ singularity exec <container> /usr/local/bin/fixMAFnames.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fixMAFnames.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fixMAFnames.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf2fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/maf2fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/maf2fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mugsy

```bash
$ singularity exec <container> /usr/local/bin/mugsy
$ podman run --it --rm --entrypoint /usr/local/bin/mugsy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mugsy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mugsyWGA

```bash
$ singularity exec <container> /usr/local/bin/mugsyWGA
$ podman run --it --rm --entrypoint /usr/local/bin/mugsyWGA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mugsyWGA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mugsyenv.sh

```bash
$ singularity exec <container> /usr/local/bin/mugsyenv.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mugsyenv.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mugsyenv.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot.pl

```bash
$ singularity exec <container> /usr/local/bin/plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitmaf.pl

```bash
$ singularity exec <container> /usr/local/bin/splitmaf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/splitmaf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitmaf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### synchain-mugsy

```bash
$ singularity exec <container> /usr/local/bin/synchain-mugsy
$ podman run --it --rm --entrypoint /usr/local/bin/synchain-mugsy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/synchain-mugsy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmfa2maf.pl

```bash
$ singularity exec <container> /usr/local/bin/xmfa2maf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xmfa2maf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmfa2maf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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