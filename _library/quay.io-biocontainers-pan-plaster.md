---
layout: container
name:  "quay.io/biocontainers/pan-plaster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pan-plaster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pan-plaster/container.yaml"
updated_at: "2025-10-20 03:30:30.044784"
latest: "1.2.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pan-plaster"
aliases:
 - "delta2vcf"
 - "plaster"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
 - "mummerplot"
 - "nucmer"
 - "promer"
 - "repeat-match"
 - "show-aligns"
versions:
 - "1.2.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pan-plaster"
config: {"url": "https://biocontainers.pro/tools/pan-plaster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pan-plaster", "latest": {"1.2.1--hdfd78af_0": "sha256:fed6778ea62c415a6d01fff696f3f30485fbb4ff1af0e07d70af15b73b47a375"}, "tags": {"1.2.1--hdfd78af_0": "sha256:fed6778ea62c415a6d01fff696f3f30485fbb4ff1af0e07d70af15b73b47a375"}, "docker": "quay.io/biocontainers/pan-plaster", "aliases": {"delta2vcf": "/usr/local/bin/delta2vcf", "plaster": "/usr/local/bin/plaster", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot", "nucmer": "/usr/local/bin/nucmer", "promer": "/usr/local/bin/promer", "repeat-match": "/usr/local/bin/repeat-match", "show-aligns": "/usr/local/bin/show-aligns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pan-plaster.
shpc-registry automated BioContainers addition for pan-plaster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pan-plaster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pan-plaster:1.2.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pan-plaster/1.2.1--hdfd78af_0
$ module help quay.io/biocontainers/pan-plaster/1.2.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pan-plaster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pan-plaster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pan-plaster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pan-plaster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pan-plaster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pan-plaster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delta2vcf

```bash
$ singularity exec <container> /usr/local/bin/delta2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plaster

```bash
$ singularity exec <container> /usr/local/bin/plaster
$ podman run --it --rm --entrypoint /usr/local/bin/plaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /usr/local/bin/mummerplot
$ podman run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucmer

```bash
$ singularity exec <container> /usr/local/bin/nucmer
$ podman run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promer

```bash
$ singularity exec <container> /usr/local/bin/promer
$ podman run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repeat-match

```bash
$ singularity exec <container> /usr/local/bin/repeat-match
$ podman run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-aligns

```bash
$ singularity exec <container> /usr/local/bin/show-aligns
$ podman run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
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