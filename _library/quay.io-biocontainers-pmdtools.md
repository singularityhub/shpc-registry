---
layout: container
name:  "quay.io/biocontainers/pmdtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pmdtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pmdtools/container.yaml"
updated_at: "2022-10-29 05:42:54.073644"
latest: "0.60--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/pmdtools"
aliases:
 - "plotPMD"
 - "pmdtools"
 - "2to3-3.9"
 - "ace2sam"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "fasta-sanitize.pl"
 - "htsfile"
 - "idle3.9"
 - "interpolate_sam.pl"
versions:
 - "0.60--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for pmdtools"
config: {"url": "https://biocontainers.pro/tools/pmdtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pmdtools", "latest": {"0.60--hdfd78af_5": "sha256:6f9ead275bcd212e37545897faee6f8040311585910930c46d5dd6c0e5885bfa"}, "tags": {"0.60--hdfd78af_5": "sha256:6f9ead275bcd212e37545897faee6f8040311585910930c46d5dd6c0e5885bfa"}, "docker": "quay.io/biocontainers/pmdtools", "aliases": {"plotPMD": "/usr/local/bin/plotPMD", "pmdtools": "/usr/local/bin/pmdtools", "2to3-3.9": "/usr/local/bin/2to3-3.9", "ace2sam": "/usr/local/bin/ace2sam", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "htsfile": "/usr/local/bin/htsfile", "idle3.9": "/usr/local/bin/idle3.9", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pmdtools.
shpc-registry automated BioContainers addition for pmdtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pmdtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pmdtools:0.60--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pmdtools/0.60--hdfd78af_5
$ module help quay.io/biocontainers/pmdtools/0.60--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pmdtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pmdtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pmdtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pmdtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pmdtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pmdtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plotPMD

```bash
$ singularity exec <container> /usr/local/bin/plotPMD
$ podman run --it --rm --entrypoint /usr/local/bin/plotPMD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotPMD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmdtools

```bash
$ singularity exec <container> /usr/local/bin/pmdtools
$ podman run --it --rm --entrypoint /usr/local/bin/pmdtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmdtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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