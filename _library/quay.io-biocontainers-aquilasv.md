---
layout: container
name:  "quay.io/biocontainers/aquilasv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aquilasv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/aquilasv/container.yaml"
updated_at: "2022-10-29 05:34:23.228386"
latest: "1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/aquilasv"
aliases:
 - "AquilaSV_step1"
 - "AquilaSV_step2"
 - "AquilaSV_step3"
 - "2to3-3.9"
 - "ace2sam"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "export2sam.pl"
 - "f2py3.9"
 - "fasta-sanitize.pl"
versions:
 - "1.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for aquilasv"
config: {"url": "https://biocontainers.pro/tools/aquilasv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aquilasv", "latest": {"1.5--pyhdfd78af_0": "sha256:1170144f456ef04dc429ba3ff3daacf3e079050a6c8c71a6470bb50690140876"}, "tags": {"1.5--pyhdfd78af_0": "sha256:1170144f456ef04dc429ba3ff3daacf3e079050a6c8c71a6470bb50690140876"}, "docker": "quay.io/biocontainers/aquilasv", "aliases": {"AquilaSV_step1": "/usr/local/bin/AquilaSV_step1", "AquilaSV_step2": "/usr/local/bin/AquilaSV_step2", "AquilaSV_step3": "/usr/local/bin/AquilaSV_step3", "2to3-3.9": "/usr/local/bin/2to3-3.9", "ace2sam": "/usr/local/bin/ace2sam", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "export2sam.pl": "/usr/local/bin/export2sam.pl", "f2py3.9": "/usr/local/bin/f2py3.9", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aquilasv.
shpc-registry automated BioContainers addition for aquilasv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aquilasv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aquilasv:1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aquilasv/1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/aquilasv/1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aquilasv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aquilasv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aquilasv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aquilasv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aquilasv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aquilasv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AquilaSV_step1

```bash
$ singularity exec <container> /usr/local/bin/AquilaSV_step1
$ podman run --it --rm --entrypoint /usr/local/bin/AquilaSV_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AquilaSV_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AquilaSV_step2

```bash
$ singularity exec <container> /usr/local/bin/AquilaSV_step2
$ podman run --it --rm --entrypoint /usr/local/bin/AquilaSV_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AquilaSV_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AquilaSV_step3

```bash
$ singularity exec <container> /usr/local/bin/AquilaSV_step3
$ podman run --it --rm --entrypoint /usr/local/bin/AquilaSV_step3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AquilaSV_step3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cds-mapping-stats

```bash
$ singularity exec <container> /usr/local/bin/cds-mapping-stats
$ podman run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-subgraphs

```bash
$ singularity exec <container> /usr/local/bin/cds-subgraphs
$ podman run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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