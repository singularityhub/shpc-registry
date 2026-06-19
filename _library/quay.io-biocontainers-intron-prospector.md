---
layout: container
name:  "quay.io/biocontainers/intron-prospector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/intron-prospector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/intron-prospector/container.yaml"
updated_at: "2026-06-19 08:00:56.912392"
latest: "1.5.1--hd6466ae_0"
container_url: "https://biocontainers.pro/tools/intron-prospector"
aliases:
 - "intron-prospector"
 - "intron-prospector-merge"
 - "intronProspector"
 - "intronProspectorMerge"
 - "ref-cache"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.5.0--hd6466ae_0"
 - "1.5.1--hd6466ae_0"
description: "singularity registry hpc automated addition for intron-prospector"
config: {"url": "https://biocontainers.pro/tools/intron-prospector", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for intron-prospector", "latest": {"1.5.1--hd6466ae_0": "sha256:77f98e90dbad051cd09afe563cb75334428845aec43ef45842f19b1fe3719194"}, "tags": {"1.5.0--hd6466ae_0": "sha256:12285033e4cbac3c7f3b8995d5f561bad3d79f1b106284c1f9d7601c81712c89", "1.5.1--hd6466ae_0": "sha256:77f98e90dbad051cd09afe563cb75334428845aec43ef45842f19b1fe3719194"}, "docker": "quay.io/biocontainers/intron-prospector", "aliases": {"intron-prospector": "/usr/local/bin/intron-prospector", "intron-prospector-merge": "/usr/local/bin/intron-prospector-merge", "intronProspector": "/usr/local/bin/intronProspector", "intronProspectorMerge": "/usr/local/bin/intronProspectorMerge", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/intron-prospector.
singularity registry hpc automated addition for intron-prospector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/intron-prospector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/intron-prospector:1.5.1--hd6466ae_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/intron-prospector/1.5.1--hd6466ae_0
$ module help quay.io/biocontainers/intron-prospector/1.5.1--hd6466ae_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### intron-prospector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### intron-prospector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### intron-prospector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### intron-prospector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### intron-prospector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### intron-prospector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### intron-prospector

```bash
$ singularity exec <container> /usr/local/bin/intron-prospector
$ podman run --it --rm --entrypoint /usr/local/bin/intron-prospector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron-prospector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron-prospector-merge

```bash
$ singularity exec <container> /usr/local/bin/intron-prospector-merge
$ podman run --it --rm --entrypoint /usr/local/bin/intron-prospector-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron-prospector-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intronProspector

```bash
$ singularity exec <container> /usr/local/bin/intronProspector
$ podman run --it --rm --entrypoint /usr/local/bin/intronProspector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intronProspector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intronProspectorMerge

```bash
$ singularity exec <container> /usr/local/bin/intronProspectorMerge
$ podman run --it --rm --entrypoint /usr/local/bin/intronProspectorMerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intronProspectorMerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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