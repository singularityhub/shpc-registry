---
layout: container
name:  "quay.io/biocontainers/bsmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bsmap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bsmap/container.yaml"
updated_at: "2022-10-29 05:54:10.950616"
latest: "2.90--h5b5514e_4"
container_url: "https://biocontainers.pro/tools/bsmap"
aliases:
 - "bsmap"
 - "bsp2sam.py"
 - "methdiff.py"
 - "methratio.py"
 - "sam2bam.sh"
 - "ace2sam"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "build_env_setup.sh"
 - "conda_build.sh"
 - "export2sam.pl"
 - "fasta-sanitize.pl"
 - "htsfile"
 - "idle"
versions:
 - "2.90--h5b5514e_4"
description: "shpc-registry automated BioContainers addition for bsmap"
config: {"url": "https://biocontainers.pro/tools/bsmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bsmap", "latest": {"2.90--h5b5514e_4": "sha256:03e1c7931c26dd818f2ba3ed0a8cb2d2769e04e10b233825a16b9bc0a924a3f2"}, "tags": {"2.90--h5b5514e_4": "sha256:03e1c7931c26dd818f2ba3ed0a8cb2d2769e04e10b233825a16b9bc0a924a3f2"}, "docker": "quay.io/biocontainers/bsmap", "aliases": {"bsmap": "/usr/local/bin/bsmap", "bsp2sam.py": "/usr/local/bin/bsp2sam.py", "methdiff.py": "/usr/local/bin/methdiff.py", "methratio.py": "/usr/local/bin/methratio.py", "sam2bam.sh": "/usr/local/bin/sam2bam.sh", "ace2sam": "/usr/local/bin/ace2sam", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "conda_build.sh": "/usr/local/bin/conda_build.sh", "export2sam.pl": "/usr/local/bin/export2sam.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "htsfile": "/usr/local/bin/htsfile", "idle": "/usr/local/bin/idle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bsmap.
shpc-registry automated BioContainers addition for bsmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bsmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bsmap:2.90--h5b5514e_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bsmap/2.90--h5b5514e_4
$ module help quay.io/biocontainers/bsmap/2.90--h5b5514e_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bsmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bsmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bsmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bsmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bsmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bsmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bsmap

```bash
$ singularity exec <container> /usr/local/bin/bsmap
$ podman run --it --rm --entrypoint /usr/local/bin/bsmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsp2sam.py

```bash
$ singularity exec <container> /usr/local/bin/bsp2sam.py
$ podman run --it --rm --entrypoint /usr/local/bin/bsp2sam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsp2sam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### methdiff.py

```bash
$ singularity exec <container> /usr/local/bin/methdiff.py
$ podman run --it --rm --entrypoint /usr/local/bin/methdiff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methdiff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### methratio.py

```bash
$ singularity exec <container> /usr/local/bin/methratio.py
$ podman run --it --rm --entrypoint /usr/local/bin/methratio.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methratio.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2bam.sh

```bash
$ singularity exec <container> /usr/local/bin/sam2bam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sam2bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
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