---
layout: container
name:  "quay.io/biocontainers/hivtrace"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hivtrace/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hivtrace/container.yaml"
updated_at: "2022-10-27 01:07:40.229978"
latest: "1.5.0--py_0"
container_url: "https://biocontainers.pro/tools/hivtrace"
aliases:
 - "TNS"
 - "bam2fna"
 - "bam2msa"
 - "bamclip"
 - "bealign"
 - "clipedge"
 - "consensus"
 - "hivnetworkannotate"
 - "hivnetworkcsv"
 - "hivtrace"
 - "hivtrace_strip_drams"
 - "hivtrace_viz"
 - "msa2bam"
 - "seqmerge"
versions:
 - "1.5.0--py_0"
description: "shpc-registry automated BioContainers addition for hivtrace"
config: {"url": "https://biocontainers.pro/tools/hivtrace", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hivtrace", "latest": {"1.5.0--py_0": "sha256:24d874c0c474ab22bd1ce90dea2ca29fe212e006325493970f55a034719d220a"}, "tags": {"1.5.0--py_0": "sha256:24d874c0c474ab22bd1ce90dea2ca29fe212e006325493970f55a034719d220a"}, "docker": "quay.io/biocontainers/hivtrace", "aliases": {"TNS": "/usr/local/bin/TNS", "bam2fna": "/usr/local/bin/bam2fna", "bam2msa": "/usr/local/bin/bam2msa", "bamclip": "/usr/local/bin/bamclip", "bealign": "/usr/local/bin/bealign", "clipedge": "/usr/local/bin/clipedge", "consensus": "/usr/local/bin/consensus", "hivnetworkannotate": "/usr/local/bin/hivnetworkannotate", "hivnetworkcsv": "/usr/local/bin/hivnetworkcsv", "hivtrace": "/usr/local/bin/hivtrace", "hivtrace_strip_drams": "/usr/local/bin/hivtrace_strip_drams", "hivtrace_viz": "/usr/local/bin/hivtrace_viz", "msa2bam": "/usr/local/bin/msa2bam", "seqmerge": "/usr/local/bin/seqmerge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hivtrace.
shpc-registry automated BioContainers addition for hivtrace
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hivtrace
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hivtrace:1.5.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hivtrace/1.5.0--py_0
$ module help quay.io/biocontainers/hivtrace/1.5.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hivtrace-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hivtrace-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hivtrace-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hivtrace-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hivtrace-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hivtrace-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TNS

```bash
$ singularity exec <container> /usr/local/bin/TNS
$ podman run --it --rm --entrypoint /usr/local/bin/TNS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TNS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2fna

```bash
$ singularity exec <container> /usr/local/bin/bam2fna
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2msa

```bash
$ singularity exec <container> /usr/local/bin/bam2msa
$ podman run --it --rm --entrypoint /usr/local/bin/bam2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamclip

```bash
$ singularity exec <container> /usr/local/bin/bamclip
$ podman run --it --rm --entrypoint /usr/local/bin/bamclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bealign

```bash
$ singularity exec <container> /usr/local/bin/bealign
$ podman run --it --rm --entrypoint /usr/local/bin/bealign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bealign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clipedge

```bash
$ singularity exec <container> /usr/local/bin/clipedge
$ podman run --it --rm --entrypoint /usr/local/bin/clipedge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clipedge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus

```bash
$ singularity exec <container> /usr/local/bin/consensus
$ podman run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hivnetworkannotate

```bash
$ singularity exec <container> /usr/local/bin/hivnetworkannotate
$ podman run --it --rm --entrypoint /usr/local/bin/hivnetworkannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hivnetworkannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hivnetworkcsv

```bash
$ singularity exec <container> /usr/local/bin/hivnetworkcsv
$ podman run --it --rm --entrypoint /usr/local/bin/hivnetworkcsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hivnetworkcsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hivtrace

```bash
$ singularity exec <container> /usr/local/bin/hivtrace
$ podman run --it --rm --entrypoint /usr/local/bin/hivtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hivtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hivtrace_strip_drams

```bash
$ singularity exec <container> /usr/local/bin/hivtrace_strip_drams
$ podman run --it --rm --entrypoint /usr/local/bin/hivtrace_strip_drams   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hivtrace_strip_drams   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hivtrace_viz

```bash
$ singularity exec <container> /usr/local/bin/hivtrace_viz
$ podman run --it --rm --entrypoint /usr/local/bin/hivtrace_viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hivtrace_viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msa2bam

```bash
$ singularity exec <container> /usr/local/bin/msa2bam
$ podman run --it --rm --entrypoint /usr/local/bin/msa2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqmerge

```bash
$ singularity exec <container> /usr/local/bin/seqmerge
$ podman run --it --rm --entrypoint /usr/local/bin/seqmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
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